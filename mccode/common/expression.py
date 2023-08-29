import ast
from dataclasses import dataclass
from typing import Union
from enum import Enum
from zenlog import log

# class NameReplacer(ast.NodeTransformer):
#     def __init__(self, **values):
#         self.values = values
#
#     def visit_Name(self, node):
#         if node.id in self.values:
#             return ast.Constant(self.values[node.id])
#         return node
#
#
# @dataclass
# class Expr:
#     expr: str = ""
#
#     @property
#     def ids(self):
#         from ast import walk, parse, Name
#         tree = parse(self.expr)
#         return list(set(x.id for x in walk(tree) if isinstance(x, Name)))
#
#     def eval(self, **values):
#         from ast import parse, fix_missing_locations, dump, literal_eval
#         if any(name not in values for name in self.ids):
#             raise RuntimeError(f"Not all of {self.ids} provided as keyword=value arguments")
#         tree = NameReplacer(**values).visit(parse(self.expr))
#         fixed = fix_missing_locations(tree)
#         print(eval(fixed))
#         print(dump(fixed))
#         obj = compile(fixed, '', 'exec')
#         eval(obj)


class ObjectType(Enum):
    value = 1
    initializer_list = 2
    identifier = 3
    function = 4
    parameter = 5

    @property
    def is_id(self):
        return self == ObjectType.identifier

    @property
    def is_parameter(self):
        return self == ObjectType.parameter

    @property
    def is_function(self):
        return self == ObjectType.function


class ShapeType(Enum):
    scalar = 1
    vector = 2

    @property
    def mccode_c_type(self):
        return '' if self == ShapeType.scalar else '*'

    def compatible(self, other):
        return self == other

    @property
    def is_scalar(self):
        return self == ShapeType.scalar

    @property
    def is_vector(self):
        return self == ShapeType.vector


class DataType(Enum):
    undefined = 0
    float = 1
    int = 2
    str = 3

    def compatible(self, other):
        if self == DataType.undefined or other == DataType.undefined or self == other:
            return True
        if (self == DataType.float and other == DataType.int) or (self == DataType.int and other == DataType.float):
            return True
        return False

    # promotion rules:
    def __add__(self, other):
        if self == DataType.undefined:
            return other
        if other == DataType.undefined:
            return self
        if self == other:
            return self
        if (self == DataType.float and other == DataType.int) or (self == DataType.int and other == DataType.float):
            return DataType.int
        return DataType.str

    __sub__ = __add__
    __mul__ = __add__
    __truediv__ = __add__

    @property
    def is_str(self):
        return self == DataType.str

    @property
    def mccode_c_type(self):
        if self == DataType.float:
            return "double"
        if self == DataType.int:
            return "int"
        if self == DataType.str:
            return "char *"
        raise RuntimeError(f"No known conversion from non-enumerated data type {self}")


def _comb(f, s: list):
    return ','.join(f(x) for x in s)


class Op:
    def __init__(self):
        self.data_type = DataType.undefined
        self.style = 'C'  # there should be a better way to do this

    def __hash__(self):
        return hash(str(self))

    @property
    def is_op(self):
        return True

    @property
    def is_zero(self):
        return False

    @property
    def is_id(self):
        return False

    @property
    def is_parameter(self):
        return False

    @property
    def is_str(self):
        return self.data_type.is_str

    def is_value(self, other):
        return self == other

    @property
    def is_scalar(self):
        return False

    @property
    def is_vector(self):
        return False

    @property
    def vector_known(self):
        return False

    def __add__(self, other):
        if other.is_zero:
            return self
        return BinaryOp('+', self, other)

    def __sub__(self, other):
        if other.is_zero:
            return self
        return BinaryOp('-', self, other)

    def __mul__(self, other):
        if other.is_zero:
            return other
        if other.is_value(1):
            return self
        if other.is_value(-1):
            return -self
        return BinaryOp('*', self, other)

    def __truediv__(self, other):
        if other.is_zero:
            raise RuntimeError('Division by zero')
        if other.is_value(1):
            return self
        if other.is_value(-1):
            return -self
        return BinaryOp('/', self, other)

    def __neg__(self):
        return UnaryOp('-', self)

    def __pos__(self):
        return self

    def __abs__(self):
        return UnaryOp('abs', self)


class TrinaryOp(Op):
    def __init__(self, op, first, second, third):
        super().__init__()
        self.op = op
        first, second, third = [x.expr if isinstance(x, Expr) else x for x in (first, second, third)]
        first, second, third = [[x] if not isinstance(x, list) else x for x in (first, second, third)]
        self.first = first
        self.second = second
        self.third = third
        # In C the data types for `if_true` and `if_false` in
        #   `(logical test) ? if_true : if_false;`
        # _must_ be the same. Python is more flexible, but we need to at least have a promotable common type
        # for compatibility with C.
        left_data_types = list(dict.fromkeys(x.data_type for x in second))
        right_data_types = list(dict.fromkeys(x.data_type for x in third))
        if len(left_data_types) != 1 or len(right_data_types) != 1:
            raise RuntimeError('Multiple data types in one value not supported')
        self.data_type = left_data_types[0] + right_data_types[0]

    def _str_repr_(self, first, second, third):
        if '__trinary__' == self.op:
            if self.style == 'C':
                return f'{first} ? {second} : {third}'
            return f'{second} if {first} else {third}'

    def __str__(self):
        return self._str_repr_(_comb(str, self.first), _comb(str, self.second), _comb(str, self.third))

    def __repr__(self):
        return self._str_repr_(_comb(repr, self.first), _comb(repr, self.second), _comb(repr, self.third))

    def __eq__(self, other):
        if not isinstance(other, TrinaryOp):
            return False
        return self.op == other.op and self.first == other.first and self.second == other.second and self.third == other.third

    @property
    def is_scalar(self):
        return len(self.first) == 1 and len(self.second) == 1 and len(self.third) == 1\
            and self.first[0].is_scalar and self.second[0].is_scalar and self.third[0].is_scalar

    @property
    def is_vector(self):
        return len(self.first) == 1 and len(self.second) == 1 and len(self.third) == 1 \
            and self.first[0].is_vector and self.second[0].is_vector and self.third[0].is_vector

    @property
    def vector_known(self):
        return len(self.first) == 1 and len(self.second) == 1 and len(self.third) == 1 \
            and self.first[0].vector_known and self.second[0].vector_known and self.third[0].vector_known


class BinaryOp(Op):
    def __init__(self, op, left, right):
        super().__init__()
        if isinstance(left, Expr):
            left = left.expr
        if isinstance(right, Expr):
            right = right.expr
        if not isinstance(left, list):
            left = [left]
        if not isinstance(right, list):
            right = [right]
        self.op = op
        self.left = left
        self.right = right
        if op in ('__call__', '__struct_access__', '__pointer_access__', '__getitem__'):
            data_type = DataType.undefined
        else:
            left_data_types = list(dict.fromkeys(x.data_type for x in left))
            right_data_types = list(dict.fromkeys(x.data_type for x in right))
            if len(left_data_types) != 1 or len(right_data_types) != 1:
                raise RuntimeError('Multiple data types in one value not supported')
            data_type = left_data_types[0] + right_data_types[0]
        self.data_type = data_type
        self.style = 'C'  # there should be a better way to do this

    def _str_repr_(self, lstr, rstr):
        if '__call__' == self.op:
            return f'{lstr}({rstr})'
        if '__struct_access__' == self.op:
            return f'{lstr}.{rstr}' if 'C' == self.style else f'getattr({lstr}, {rstr})'
        if '__pointer_access__' == self.op:
            return f'{lstr}->{rstr}' if 'C' == self.style else f'getattr({lstr}, {rstr})'
        if '__getitem__' == self.op:
            return f'{lstr}[{rstr}]'
        if '__pow__' == self.op:
            return f'{lstr}^{rstr}' if 'C' == self.style else f'{lstr}**{rstr}'
        if '__lt__' == self.op:
            return f'{lstr}<{rstr}'
        if '__gt__' == self.op:
            return f'{lstr}>{rstr}'
        if '__le__' == self.op:
            return f'{lstr}<={rstr}'
        if '__ge__' == self.op:
            return f'{lstr}>={rstr}'
        if '__eq__' == self.op:
            return f'{lstr}=={rstr}'
        if '__or__' == self.op:
            return f'{lstr} || {rstr}' if 'C' == self.style else f'{lstr} or {rstr}'
        if '__and__' == self.op:
            return f'{lstr} && {rstr}' if 'C' == self.style else f'{lstr} and {rstr}'
        if any(x in self.op for x in '+-'):
            return f'({lstr} {self.op} {rstr})'
        if any(x in self.op for x in '*/'):
            return f'{lstr} {self.op} {rstr}'
        return f'{self.op}({lstr}, {rstr})'

    def __str__(self):
        return self._str_repr_(_comb(str, self.left), _comb(str, self.right))

    def __repr__(self):
        return self._str_repr_(_comb(repr, self.left), _comb(repr, self.right))

    def __eq__(self, other):
        if not isinstance(other, BinaryOp):
            return False
        return self.op == other.op and self.left == other.left and self.right == other.right

    @property
    def is_scalar(self):
        return len(self.left) == 1 and len(self.right) == 1 and self.left[0].is_scalar and self.right[0].is_scalar

    @property
    def is_vector(self):
        return len(self.left) == 1 and len(self.right) == 1 and self.left[0].is_vector or self.right[0].is_vector

    @property
    def vector_known(self):
        return len(self.left) == 1 and len(self.right) == 1 and self.left[0].vector_known and self.right[0].vector_known
    #
    # def __len__(self):
    #     return max(len(self.left), len(self.right))


class UnaryOp(Op):
    def __init__(self, op, value):
        super().__init__()
        if isinstance(value, Expr):
            value = value.expr
        if not isinstance(value, list):
            value = [value]
        self.op = op
        self.value = value
        data_types = list(dict.fromkeys(x.data_type for x in value))
        if len(data_types) != 1:
            raise RuntimeError('Multiple data types in one value not supported')
        self.data_type = data_types[0]
        self.style = 'C'  # there should be a better way to do this

    def _str_repr_(self, vstr):
        if '__group__' == self.op:
            return f'({vstr})'
        if '__not__' == self.op:
            return f'!{vstr}' if 'C' == self.style else f'not {vstr}'
        if any(x in self.op for x in '+-'):
            return f'{self.op}{vstr}'
        return f'{self.op}({vstr})'

    def __str__(self):
        return self._str_repr_(_comb(str, self.value))

    def __repr__(self):
        return self._str_repr_(_comb(repr, self.value))

    def __neg__(self):
        if self.op == '-':
            return self.value
        return UnaryOp('-', self)

    def __abs__(self):
        if self.op == 'abs':
            # abs(abs(x)) is abs(x)
            return self
        return UnaryOp('abs', self)

    def __eq__(self, other):
        if not isinstance(other, UnaryOp):
            return False
        return self.op == other.op and self.value == other.value

    @property
    def is_scalar(self):
        return len(self.value) == 1 and self.value[0].is_scalar

    @property
    def is_vector(self):
        return len(self.value) == 1 and self.value[0].is_vector

    @property
    def vector_known(self):
        return len(self.value) == 1 and self.value[0].vector_known

    # def __len__(self):
    #     return len(self.value)

    def __gt__(self, other):
        log.debug(f'{self} > {other} has been called (but probably should not have been!)')
        return False


class Value:
    def __init__(self, value, data_type=None, object_type=None, shape_type=None):
        self._value = value
        if data_type is None or not isinstance(data_type, DataType):
            data_type = DataType.undefined
        if object_type is None or not isinstance(object_type, ObjectType):
            object_type = ObjectType.identifier if data_type != DataType.str and isinstance(value, str) else ObjectType.value
        if shape_type is None or not isinstance(shape_type, ShapeType):
            shape_type = ShapeType.vector if not isinstance(value, str) and hasattr(value, '__len__') else ShapeType.scalar
        self._object = object_type
        self._data = data_type
        self._shape = shape_type

    @property
    def value(self):
        return self._value

    @property
    def object_type(self):
        return self._object

    @property
    def data_type(self):
        return self._data

    @property
    def shape_type(self):
        return self._shape

    @value.setter
    def value(self, value):
        log.debug(f'Updating Value from {self._value} to {value}')
        self._object = self.data_type != DataType.str and isinstance(value, str)
        self._value = value

    @data_type.setter
    def data_type(self, dt):
        self._data = dt

    @property
    def has_value(self):
        return self.value is not None

    @property
    def vector_known(self):
        return self.is_vector and self.has_value and not isinstance(self.value, str)

    def _str_repr_(self):
        return f'_instrument_var._parameters.{self.value}' if self.is_parameter else f'{self.value}'

    def __str__(self):
        return self._str_repr_()

    def __repr__(self):
        return f'{self.shape_type} {self.data_type} {self._str_repr_()}'

    def __hash__(self):
        return hash(str(self))

    def compatible(self, other, id_ok=False):
        if isinstance(other, (UnaryOp, BinaryOp)):
            return id_ok
        value = other if isinstance(other, Value) else Value.best(other)
        return (id_ok and value.is_str) or (self.data_type.compatible(value.data_type) and self.shape_type.compatible(value.shape_type))

    @classmethod
    def float(cls, value):
        try:
            v = float(value) if value is not None else None
        except ValueError:
            v = value
        return cls(v, DataType.float)

    @classmethod
    def int(cls, value):
        try:
            v = int(value) if value is not None else None
        except ValueError:
            v = value
        return cls(v, DataType.int)

    @classmethod
    def str(cls, value):
        return cls(value, DataType.str)

    @classmethod
    def id(cls, value):
        return cls(value, DataType.str)

    @classmethod
    def array(cls, value, dt=None):
        return cls(value, data_type=dt, object_type=None, shape_type=ShapeType.vector)

    @classmethod
    def function(cls, value, dt=None):
        return cls(value, object_type=ObjectType.function)

    @classmethod
    def best(cls, value):
        if isinstance(value, str):
            return cls(value, DataType.str)
        if isinstance(value, int) or (isinstance(value, float) and value.is_integer()):
            return cls(value, DataType.int)
        return cls(value, DataType.float)

    @property
    def is_id(self):
        return self.data_type != DataType.str and isinstance(self.value, str)

    @property
    def is_parameter(self):
        return self.object_type.is_parameter

    @property
    def is_str(self):
        return self.data_type.is_str

    @property
    def is_op(self):
        return False

    @property
    def is_zero(self):
        return not self.is_id and self.value == 0

    def is_value(self, v):
        return not self.is_id and v.is_value(self.value) if hasattr(v, 'is_value') else self.value == v

    @property
    def is_scalar(self):
        return self.shape_type.is_scalar

    @property
    def is_vector(self):
        return self.shape_type.is_vector

    # def __len__(self):
    #     return len(self.value) if self.is_vector else 1

    @property
    def vector_len(self):
        return len(self.value) if self.is_vector else 1

    def __add__(self, other):
        other = other if isinstance(other, (Value, Op)) else Value.best(other)
        if self.is_zero:
            return other
        if other.is_zero:
            return self
        if other.is_op and isinstance(other, UnaryOp) and other.op == '-':
            return self - other.value
        if self.is_id and (isinstance(other, Value) and not isinstance(other.value, str) and other < 0):
            return self - (-other.value)
        if other.is_op or self.is_id or other.is_id:
            return BinaryOp('+', self, other)
        pdt = self.data_type + other.data_type
        return BinaryOp('+', self, other) if pdt.is_str else Value(self.value + other.value, pdt)

    def __sub__(self, other):
        other = other if isinstance(other, (Value, Op)) else Value.best(other)
        if self.is_zero:
            return -other
        if other.is_zero:
            return self
        if other.is_op and isinstance(other, UnaryOp) and other.op == '-':
            return self + other.value
        if self.is_id and (isinstance(other, Value) and not isinstance(other.value, str) and other < 0):
            return self + (-other.value)
        if other.is_op or self.is_id or other.is_id:
            return BinaryOp('-', self, other)
        pdt = self.data_type - other.data_type
        return BinaryOp('-', self, other) if pdt.is_str else Value(self.value - other.value, pdt)

    def __mul__(self, other):
        other = other if isinstance(other, (Value, Op)) else Value.best(other)
        pdt = self.data_type * other.data_type
        if self.is_zero or other.is_zero:
            return Value(0, DataType.int if pdt.is_str else pdt)
        if self.is_value(1):
            return other
        if self.is_value(-1):
            return -other
        if other.is_op or self.is_id or other.is_id:
            return BinaryOp('*', self, other)
        return BinaryOp('*', self, other) if pdt.is_str else Value(self.value * other.value, pdt)

    def __truediv__(self, other):
        other = other if isinstance(other, (Value, Op)) else Value.best(other)
        pdt = self.data_type / other.data_type
        if self.is_zero:
            return Value(0, DataType.int if pdt.is_str else pdt)
        if other.is_value(1):
            return self
        if other.is_value(-1):
            return -self
        if other.is_zero:
            raise RuntimeError('Division by zero!')
        if other.is_op or self.is_id or other.is_id:
            return BinaryOp('/', self, other)
        return BinaryOp('/', self, other) if pdt.is_str else Value(self.value / other.value, pdt)

    def __neg__(self):
        return UnaryOp('-', self) if self.is_id or self.data_type.is_str else Value(-self.value, self.data_type)

    def __pos__(self):
        return Value(self.value, self.data_type)

    def __abs__(self):
        return UnaryOp('abs', self) if self.is_id or self.data_type.is_str else Value(abs(self.value), self.data_type)

    def __eq__(self, other):
        other = other if isinstance(other, (Value, Op)) else Value.best(other)
        if other.is_op:
            return False
        return self.value == other.value

    def __lt__(self, other):
        other = other if isinstance(other, (Value, Op)) else Value.best(other)
        if self.is_id or other.is_op or other.is_id:
            return BinaryOp('__lt__', self, other)
        return self.value < other.value

    def __gt__(self, other):
        other = other if isinstance(other, (Value, Op)) else Value.best(other)
        if self.is_id or other.is_op or other.is_id:
            return BinaryOp('__gt__', self, other)
        return self.value > other.value

    def __pow__(self, power):
        if not isinstance(power, (Value, Op)):
            power = Value.best(power)
        if self.is_zero or self.is_value(1):
            return self
        if power.is_zero:
            return Value(1, data_type=self.data_type)
        return BinaryOp('__pow__', self, power)

    @property
    def mccode_c_type(self):
        return self.data_type.mccode_c_type + self.shape_type.mccode_c_type

    @property
    def mccode_c_type_name(self):
        if self.data_type == DataType.float and self.shape_type == ShapeType.scalar:
            return "instr_type_double"
        if self.data_type == DataType.int and self.shape_type == ShapeType.scalar:
            return "instr_type_int"
        if self.data_type == DataType.str and self.shape_type == ShapeType.scalar:
            return "instr_type_string"
        if self.data_type == DataType.float and self.shape_type == ShapeType.vector:
            return "instr_type_vector"
        if self.data_type == DataType.int and self.shape_type == ShapeType.vector:
            return "instr_type_vector"
        raise RuntimeError(f"No known conversion from non-enumerated data type {self.data_type} + {self.shape_type}")


class Expr:
    def __init__(self, expr: Union[Value, UnaryOp, BinaryOp, list[Union[Value, UnaryOp, BinaryOp]]]):
        self.expr = expr if isinstance(expr, list) else [expr]

    def __str__(self):
        return ','.join(str(x) for x in self.expr)

    def __repr__(self):
        return ','.join(repr(x) for x in self.expr)

    def __hash__(self):
        return hash(str(self))

    @classmethod
    def float(cls, value):
        if isinstance(value, cls):
            # Make sure the held expression *thinks* it's a float:
            for expr in value.expr:
                if expr.data_type != DataType.float:
                    expr.data_type = DataType.float
            return value
        return cls(Value.float(value))

    @classmethod
    def int(cls, value):
        if isinstance(value, cls):
            # Make sure the held expression *thinks* it's a float:
            for expr in value.expr:
                if expr.data_type != DataType.int:
                    expr.data_type = DataType.int
            return value
        return cls(Value.int(value))

    @classmethod
    def str(cls, value):
        if isinstance(value, cls):
            # Make sure the held expression *thinks* it's a float:
            for expr in value.expr:
                if expr.data_type != DataType.str:
                    expr.data_type = DataType.str
            return value
        return cls(Value.str(value))

    @classmethod
    def id(cls, value):
        if isinstance(value, cls):
            return value
        return cls(Value.id(value))

    @classmethod
    def array(cls, value):
        return cls(Value.array(value))

    @classmethod
    def function(cls, value):
        return cls(Value.function(value))

    @classmethod
    def best(cls, value):
        return cls(Value.best(value))

    @property
    def is_op(self):
        return len(self.expr) == 1 and self.expr[0].is_op

    @property
    def is_zero(self):
        return len(self.expr) == 1 and self.expr[0].is_zero

    @property
    def is_id(self):
        return len(self.expr) == 1 and self.expr[0].is_id

    @property
    def is_parameter(self):
        return len(self.expr) == 1 and self.expr[0].is_parameter

    @property
    def is_str(self):
        return len(self.expr) == 1 and self.expr[0].is_str

    @property
    def is_scalar(self):
        return len(self.expr) == 1 and self.expr[0].is_scalar

    def is_value(self, value):
        return len(self.expr) == 1 and self.expr[0].is_value(value)

    @property
    def is_vector(self):
        return len(self.expr) == 1 and self.expr[0].is_vector
    #
    # def __len__(self):
    #     return len(self.expr)
    @property
    def vector_len(self):
        if len(self.expr) != 1:
            raise RuntimeError('No vector_len for array Expr objects')
        return self.expr[0].vector_len

    @property
    def is_constant(self):
        return len(self.expr) == 1 and isinstance(self.expr[0], Value) and not self.expr[0].is_id

    @property
    def has_value(self):
        return self.is_constant and self.expr[0].has_value

    @property
    def vector_known(self):
        return self.is_constant and self.expr[0].vector_known

    @property
    def value(self):
        if not self.is_constant:
            raise NotImplementedError("No conversion from expressions to constants ... yet")
        return self.expr[0].value

    def compatible(self, other, id_ok=False):
        other_expr = other.expr[0] if (isinstance(other, Expr) and len(other.expr) == 1) else other
        return len(self.expr) == 1 and self.expr[0].compatible(other_expr, id_ok)

    def __add__(self, other):
        if len(self.expr) != 1:
            raise RuntimeError('Can not add to array Expr')
        other_expr = other.expr[0] if (isinstance(other, Expr) and len(other.expr) == 1) else other
        return Expr(self.expr[0] + other_expr)

    def __sub__(self, other):
        if len(self.expr) != 1:
            raise RuntimeError('Can not subtract array Expr')
        other_expr = other.expr[0] if (isinstance(other, Expr) and len(other.expr) == 1) else other
        return Expr(self.expr[0] - other_expr)

    def __mul__(self, other):
        if len(self.expr) != 1:
            raise RuntimeError('Can not multiply array Expr')
        other_expr = other.expr[0] if (isinstance(other, Expr) and len(other.expr) == 1) else other
        return Expr(self.expr[0] * other_expr)

    def __truediv__(self, other):
        if len(self.expr) != 1:
            raise RuntimeError('Can not divide array Expr')
        other_expr = other.expr[0] if (isinstance(other, Expr) and len(other.expr) == 1) else other
        return Expr(self.expr[0] / other_expr)

    def __neg__(self):
        return Expr([-x for x in self.expr])

    def __pos__(self):
        return self

    def __abs__(self):
        return Expr([abs(x) for x in self.expr])

    def __eq__(self, other):
        if isinstance(other, Expr):
            if len(other.expr) != len(self.expr):
                return False
            for o_expr, s_expr in zip(other.expr, self.expr):
                if o_expr != s_expr:
                    return False
            return True
        return len(self.expr) == 1 and self.expr[0] == other

    def __lt__(self, other):
        if isinstance(other, Expr):
            if len(other.expr) != len(self.expr):
                raise RuntimeError('Can not compare unequal-sized-array Expr objects')
            for o_expr, s_expr in zip(other.expr, self.expr):
                if o_expr <= s_expr:
                    return False
            return True
        return len(self.expr) == 1 and self.expr[0] < other

    def __gt__(self, other):
        if isinstance(other, Expr):
            if len(other.expr) != len(self.expr):
                raise RuntimeError('Can not compare unequal-sized-array Expr objects')
            for o_expr, s_expr in zip(other.expr, self.expr):
                if o_expr >= s_expr:
                    return False
            return True
        return len(self.expr) == 1 and self.expr[0] > other

    @property
    def mccode_c_type(self):
        if len(self.expr) != 1:
            raise RuntimeError('No McCode C type for array Expr objects')
        return self.expr[0].mccode_c_type

    @property
    def mccode_c_type_name(self):
        if len(self.expr) != 1:
            raise RuntimeError('No McCode C type name for array Expr objects')
        return self.expr[0].mccode_c_type_name

    @property
    def data_type(self):
        if len(self.expr) != 1:
            raise RuntimeError('No data type for array Expr objects')
        return self.expr[0].data_type

    @data_type.setter
    def data_type(self, dt):
        if len(self.expr) != 1:
            raise RuntimeError('No data type for array Expr objects')
        self.expr[0].data_type = dt


def unary_expr(func, name, v):
    ops = {'cos': 'acos', 'sin': 'asin', 'tan': 'atan'}
    if isinstance(v, Expr):
        v = v.expr
    if isinstance(v, UnaryOp) and ((name in ops and v.op == ops[name]) or (v.op in ops and name == ops[v.op])):
        return Expr(v.value)
    if isinstance(v, Value) and not v.is_id:
        if v.is_str or isinstance(v.value, str):
            raise RuntimeError(f'How is a _string_ valued parameter, {v} not an identifier?')
        return Expr(Value.best(func(v.value)))
    return Expr(UnaryOp(name, v))


def binary_expr(func, name, left, right):
    ops = {'atan2': ('sin', 'cos')}
    if isinstance(left, Expr):
        left = left.expr
    if isinstance(right, Expr):
        right = right.expr
    if isinstance(left, UnaryOp) and isinstance(right, UnaryOp) and name in ops:
        left_func, right_func = ops[name]
        if left.op == left_func and right.op == right_func and left.value == right.value:
            return Expr(left.value)
    if isinstance(left, Value) and isinstance(right, Value) and not left.is_id and not right.is_id:
        return Expr(Value.best(func(left.value, right.value)))
    return Expr(BinaryOp(name, left, right))
