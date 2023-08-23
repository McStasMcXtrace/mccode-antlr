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


class IT(Enum):
    identifier = 1
    value = 2

    @property
    def is_id(self):
        return self == IT.identifier

class ST(Enum):
    scalar = 1
    vector = 2

    @property
    def mccode_c_type(self):
        return '' if self == ST.scalar else '*'

    def compatible(self, other):
        return self == other

    @property
    def is_scalar(self):
        return self == ST.scalar

    @property
    def is_vector(self):
        return self == ST.vector


class DT(Enum):
    float = 1
    int = 2
    str = 3

    def compatible(self, other):
        if self == other:
            return True
        if (self == DT.float and other == DT.int) or (self == DT.int and other == DT.float):
            return True
        return False

    # promotion rules:
    def __add__(self, other):
        if self == other:
            return self
        if (self == DT.float and other == DT.int) or (self == DT.int and other == DT.float):
            return DT.int
        return DT.str

    __sub__ = __add__
    __mul__ = __add__
    __truediv__ = __add__

    @property
    def is_str(self):
        return self == DT.str

    @property
    def mccode_c_type(self):
        if self == DT.float:
            return "double"
        if self == DT.int:
            return "int"
        if self == DT.str:
            return "char *"
        raise RuntimeError("No known conversion from non-enumerated data type")


class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
        self.dt = left.dt + right.dt

    def __str__(self):
        if any(x in self.op for x in '+-'):
            return f'({self.left} {self.op} {self.right})'
        if any(x in self.op for x in '*/'):
            return f'{self.left} {self.op} {self.right}'
        return f'{self.op}({self.left}, {self.right})'

    def __hash__(self):
        return hash(str(self))

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
        return BinaryOp('*', self, other)

    def __truediv__(self, other):
        if other.is_zero:
            raise RuntimeError('Division by zero')
        return BinaryOp('/', self, other)

    def __neg__(self):
        return UnaryOp('-', self)

    def __pos__(self):
        return self

    def __abs__(self):
        return UnaryOp('abs', self)


    @property
    def is_zero(self):
        return False

    @property
    def is_op(self):
        return True

    @property
    def is_id(self):
        return False

    def __eq__(self, other):
        if not isinstance(other, BinaryOp):
            return False
        return self.op == other.op and self.left == other.left and self.right == other.right

    @property
    def is_scalar(self):
        return self.left.is_scalar and self.right.is_scalar

    @property
    def is_vector(self):
        return self.left.is_vector or self.right.is_vector

    def __len__(self):
        return max(len(self.left), len(self.right))


class UnaryOp:
    def __init__(self, op, value):
        self.op = op
        self.value = value
        self.dt = value.dt

    def __str__(self):
        if any(x in self.op for x in '+-'):
            return f'{self.op}{self.value}'
        return f'{self.op}({self.value})'

    def __hash__(self):
        return hash(str(self))

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
        return BinaryOp('*', self, other)

    def __truediv__(self, other):
        if other.is_zero:
            raise RuntimeError('Division by zero')
        return BinaryOp('/', self, other)

    def __neg__(self):
        if self.op == '-':
            return self.value
        return UnaryOp('-', self)

    def __pos__(self):
        return self

    def __abs__(self):
        if self.op == 'abs':
            # abs(abs(x)) is abs(x)
            return self
        return UnaryOp('abs', self)

    @property
    def is_zero(self):
        return False

    @property
    def is_op(self):
        return True

    @property
    def is_id(self):
        return False

    def __eq__(self, other):
        if not isinstance(other, UnaryOp):
            return False
        return self.op == other.op and self.value == other.value

    @property
    def is_scalar(self):
        return self.value.is_scalar

    @property
    def is_vector(self):
        return self.value.is_vector

    def __len__(self):
        return len(self.value)

    def __gt__(self, other):
        log.debug(f'{self} > {other}')
        return False


class Value:
    def __init__(self, value, dt):
        self.value = value
        self.it = dt != DT.str and isinstance(value, str)
        self.dt = dt
        self.st = ST.vector if not isinstance(value, str) and hasattr(value, '__len__') else ST.scalar

    @property
    def has_value(self):
        return self.value is not None

    @property
    def holds_vector(self):
        return self.is_vector and self.has_value and not isinstance(self.value, str)

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.st} {self.dt} {self.value}'

    def __hash__(self):
        return hash(str(self))

    def compatible(self, other, id_ok=False):
        if isinstance(other, (UnaryOp, BinaryOp)):
            return False
        value = other if isinstance(other, Value) else Value.best(other)
        return (id_ok and value.is_str) or (self.dt.compatible(value.dt) and self.st.compatible(value.st))

    @classmethod
    def float(cls, value):
        try:
            v = float(value) if value is not None else None
        except ValueError:
            v = value
        return cls(v, DT.float)

    @classmethod
    def int(cls, value):
        try:
            v = int(value) if value is not None else None
        except ValueError:
            v = value
        return cls(v, DT.int)

    @classmethod
    def str(cls, value):
        return cls(value, DT.str)

    @classmethod
    def id(cls, value):
        return cls(value, DT.str)

    @classmethod
    def best(cls, value):
        if isinstance(value, str):
            return cls(value, DT.str)
        if isinstance(value, int) or (isinstance(value, float) and value.is_integer()):
            return cls(value, DT.int)
        return cls(value, DT.float)

    @property
    def is_id(self):
        return self.dt != DT.str and isinstance(self.value, str)
        # return self.it

    @property
    def is_str(self):
        return self.dt.is_str

    @property
    def is_op(self):
        return False

    @property
    def is_zero(self):
        return not self.is_id and self.value == 0

    @property
    def is_scalar(self):
        return self.st.is_scalar

    @property
    def is_vector(self):
        return self.st.is_vector

    def __len__(self):
        return len(self.value) if self.is_vector else 1

    def __add__(self, other):
        if self.is_zero:
            return other
        if other.is_zero:
            return self
        if other.is_op or self.is_id or other.is_id:
            return BinaryOp('+', self, other)
        pdt = self.dt + other.dt
        return BinaryOp('+', self, other) if pdt.is_str else Value(self.value + other.value, pdt)

    def __sub__(self, other):
        if self.is_zero:
            return other
        if other.is_zero:
            return self
        if other.is_op or self.is_id or other.is_id:
            return BinaryOp('-', self, other)
        pdt = self.dt - other.dt
        return BinaryOp('-', self, other) if pdt.is_str else Value(self.value - other.value, pdt)

    def __mul__(self, other):
        pdt = self.dt * other.dt
        if self.is_zero or other.is_zero:
            return Value(0, DT.int if pdt.is_str else pdt)
        if other.is_op or self.is_id or other.is_id:
            return BinaryOp('*', self, other)
        return BinaryOp('*', self, other) if pdt.is_str else Value(self.value * other.value, pdt)

    def __truediv__(self, other):
        pdt = self.dt / other.dt
        if self.is_zero:
            return Value(0, DT.int if pdt.is_str else pdt)
        if other.is_zero:
            raise RuntimeError('Division by zero!')
        if other.is_op or self.is_id or other.is_id:
            return BinaryOp('/', self, other)
        return BinaryOp('/', self, other) if pdt.is_str else Value(self.value / other.value, pdt)

    def __neg__(self):
        return UnaryOp('-', self) if self.is_id or self.dt.is_str else Value(-self.value, self.dt)

    def __pos__(self):
        return Value(self.value, self.dt)

    def __abs__(self):
        return UnaryOp('abs', self) if self.is_id or self.dt.is_str else Value(abs(self.value), self.dt)

    def __eq__(self, other):
        if other.is_op:
            return False
        return self.value == other.value

    def __lt__(self, other):
        if self.is_id or other.is_op or other.is_id:
            return BinaryOp('__lt__', self, other)
        return self.value < other.value

    def __gt__(self, other):
        if self.is_id or other.is_op or other.is_id:
            return BinaryOp('__gt__', self, other)
        return self.value > other.value

    @property
    def mccode_c_type(self):
        return self.dt.mccode_c_type + self.st.mccode_c_type

    @property
    def mccode_c_type_name(self):
        if self.dt == DT.float and self.st == ST.scalar:
            return "instr_type_double"
        if self.dt == DT.int and self.st == ST.scalar:
            return "instr_type_int"
        if self.dt == DT.str and self.st == ST.scalar:
            return "instr_type_string"
        if self.dt == DT.float and self.st == ST.vector:
            return "instr_type_vector"
        if self.dt == DT.int and self.st == ST.vector:
            return "instr_type_vector"
        raise RuntimeError("No known conversion from non-enumerated data type")


class Expr:
    def __init__(self, expr: Union[Value, UnaryOp, BinaryOp]):
        self.expr = expr

    def __str__(self):
        return str(self.expr)

    def __repr__(self):
        return repr(self.expr)

    def __hash__(self):
        return hash(self.expr)

    @classmethod
    def float(cls, value):
        return cls(Value.float(value))

    @classmethod
    def int(cls, value):
        return cls(Value.int(value))

    @classmethod
    def str(cls, value):
        return cls(Value.str(value))

    @classmethod
    def id(cls, value):
        return cls(Value.id(value))

    @classmethod
    def best(cls, value):
        return cls(Value.best(value))

    @property
    def is_op(self):
        return self.expr.is_op

    @property
    def is_zero(self):
        return self.expr.is_zero

    @property
    def is_id(self):
        return self.expr.is_id

    @property
    def is_str(self):
        return self.expr.is_str

    @property
    def is_scalar(self):
        return self.expr.is_scalar

    @property
    def is_vector(self):
        return self.expr.is_vector

    def __len__(self):
        return len(self.expr)

    @property
    def is_constant(self):
        return isinstance(self.expr, Value) and not self.expr.is_id

    @property
    def has_value(self):
        return self.is_constant and self.expr.has_value

    @property
    def holds_vector(self):
        return self.is_constant and self.expr.holds_vector

    @property
    def value(self):
        if not self.is_constant:
            raise NotImplementedError("No conversion from expressions to constants ... yet")
        return self.expr.value

    def compatible(self, other, id_ok=False):
        other_expr = other.expr if isinstance(other, Expr) else other
        return self.expr.compatible(other_expr, id_ok)

    def __add__(self, other):
        other_expr = other.expr if isinstance(other, Expr) else other
        return Expr(self.expr + other_expr)

    def __sub__(self, other):
        other_expr = other.expr if isinstance(other, Expr) else other
        return Expr(self.expr - other_expr)

    def __mul__(self, other):
        other_expr = other.expr if isinstance(other, Expr) else other
        return Expr(self.expr * other_expr)

    def __truediv__(self, other):
        other_expr = other.expr if isinstance(other, Expr) else other
        return Expr(self.expr / other_expr)

    def __neg__(self):
        return Expr(-self.expr)

    def __pos__(self):
        return self

    def __abs__(self):
        return Expr(abs(self.expr))

    def __eq__(self, other):
        other_expr = other.expr if isinstance(other, Expr) else other
        return self.expr == other_expr

    def __lt__(self, other):
        other_expr = other.expr if isinstance(other, Expr) else other
        return self.expr < other_expr

    def __gt__(self, other):
        other_expr = other.expr if isinstance(other, Expr) else other
        return self.expr > other_expr

    @property
    def mccode_c_type(self):
        return self.expr.mccode_c_type

    @property
    def mccode_c_type_name(self):
        return self.expr.mccode_c_type_name


def unary_expr(func, name, v):
    ops = {'cos': 'acos', 'sin': 'asin', 'tan': 'atan'}
    if isinstance(v, Expr):
        v = v.expr
    if isinstance(v, UnaryOp) and ((name in ops and v.op == ops[name]) or (v.op in ops and name == ops[v.op])):
        return Expr(v.value)
    if isinstance(v, Value) and not v.is_id:
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
