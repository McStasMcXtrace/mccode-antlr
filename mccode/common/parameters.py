from dataclasses import dataclass
from enum import Enum
from typing import Union

_REMOVE_BRACES = str.maketrans('', '', '{}')


class Value:
    class Type(Enum):
        float = 1
        int = 2
        str = 3
        float_array = 4
        int_array = 5

    def __init__(self, data_type: Type, value):
        self.data_type = data_type
        self.value = value

    def is_a(self, data_type: Type):
        return self.data_type == data_type

    @property
    def has_value(self):
        return self.value is not None

    @staticmethod
    def float(value):
        if value is None:
            return Value(Value.Type.float, None)
        try:
            return Value(Value.Type.float, float(value))
        except ValueError:
            return Value(Value.Type.float, value)

    @staticmethod
    def int(value):
        if value is None:
            return Value(Value.Type.int, None)
        try:
            return Value(Value.Type.int, int(value))
        except ValueError:
            return Value(Value.Type.int, value)

    @staticmethod
    def str(value):
        if value is None:
            return Value(Value.Type.str, None)
        return Value(Value.Type.str, value)

    @property
    def holds_array(self):
        if self.data_type == Value.Type.float_array or self.data_type == Value.Type.int_array:
            return not (isinstance(self.value, str) or self.value is None)
        return False

    def __str__(self):
        if self.holds_array:
            return '{' + ','.join([str(x) for x in self.value]) + '}'
        return '' if self.value is None else str(self.value)

    @staticmethod
    def _handle_return_value(value):
        if isinstance(value, str):
            # check that this makes sense given the old data type?
            return Value(Value.Type.str, value)
        elif hasattr(value, '__len__'):
            if not isinstance(value, tuple):
                value = tuple(x for x in value)
            if all(isinstance(x, int) or (isinstance(x, float) and x.is_integer()) for x in value):
                return Value(Value.Type.int_array, tuple(int(x) for x in value))
            if all(isinstance(x, float) for x in value):
                return Value(Value.Type.float_array, value)
            # TODO Add str_array?
            raise RuntimeError(f"Return value is an array but not int_array or float_array")
        elif isinstance(value, int) or (isinstance(value, float) and value.is_integer()):
            return Value(Value.Type.int, int(value))
        elif isinstance(value, float):
            return Value(Value.Type.float, value)
        elif isinstance(value, str):
            return Value(Value.Type.str, value)
        raise RuntimeError(f"Unsupported scalar return value type {type(value)}")

    def apply_elementwise_function(self, f, fname: str):
        if self.value is None:
            raise RuntimeError(f"Can not apply function {fname} to an uninitialized Value")
        if isinstance(self.value, str):
            return Value(self.data_type, f'{fname}({self.value})')
        if self.holds_array:
            return Value._handle_return_value(tuple(f(x) for x in self.value))
        return Value._handle_return_value(f(self.value))

    def apply_vector_function(self, f, fname: str):
        if self.value is None:
            raise RuntimeError(f"Can not apply function {fname} to an uninitialized Value")
        if isinstance(self.value, str):
            return Value(self.data_type, f'{fname}({self.value})')
        return Value._handle_return_value(f(self.value))

    def _binary_op(self, v, fun, op):
        rv = self.apply_elementwise_function(fun, op)
        if rv.is_a(Value.Type.str):
            return Value(self.data_type, f'({self.value} {op} {v}')
        return rv

    def __mul__(self, other):
        if self.data_type == Value.Type.str and (isinstance(other, Value) and other.is_a(Value.Type.str)):
            return Value(Value.Type.str, f'{self.value} * {other.value}')
        v = other.value if isinstance(other, Value) else other
        return self._binary_op(v, lambda x: x * v, '*')

    def __truediv__(self, other):
        if self.data_type == Value.Type.str and (isinstance(other, Value) and other.is_a(Value.Type.str)):
            return Value(Value.Type.str, f'{self.value} / {other.value}')
        v = other.value if isinstance(other, Value) else other
        return self._binary_op(v, lambda x: x / v, '/')

    def __add__(self, other):
        if self.data_type == Value.Type.str and (isinstance(other, Value) and other.is_a(Value.Type.str)):
            return Value(Value.Type.str, f'{self.value} + {other.value}')
        v = other.value if isinstance(other, Value) else other
        return self._binary_op(v, lambda x: x + v, '+')

    def __sub__(self, other):
        if self.data_type == Value.Type.str and (isinstance(other, Value) and other.is_a(Value.Type.str)):
            return Value(Value.Type.str, f'{self.value} - {other.value}')
        v = other.value if isinstance(other, Value) else other
        return self._binary_op(v, lambda x: x - v, '-')

    def __neg__(self):
        if self.data_type == Value.Type.str:
            return Value(Value.Type.str, f'-{self.value}')
        return self.apply_elementwise_function(lambda x: -x, '__neg__')

    def __pos__(self):
        if self.data_type == Value.Type.str:
            return Value(Value.Type.str, f'+{self.value}')
        return self.apply_elementwise_function(lambda x: +x, '__pos__')

    def __abs__(self):
        if self.data_type == Value.Type.str:
            return Value(Value.Type.str, f'abs({self.value})')
        return self.apply_elementwise_function(lambda x: abs(x), 'abs')


@dataclass
class InstrumentParameter:
    name: str
    unit: str
    value: Value

    # @staticmethod
    # def from_tokens(data_type: str, name: str, unit: str = None, value: str = None):
    #     mv = Value.from_tokens(data_type, value)
    #     if mv.is_a(Value.Type.float_array) or mv.is_a(Value.Type.int_array):
    #         raise RuntimeError(f"Unsupported data type {data_type} for McInstrumentParameter")
    #     return InstrumentParameter(name, unit, mv)


@dataclass
class ComponentParameter:
    name: str
    value: Value

    #
    # @staticmethod
    # def from_tokens(data_type: str, name: str, value: str):
    #     return ComponentParameter(name, Value.from_tokens(data_type, value))


def parameter_name_present(parameters: tuple[Union[InstrumentParameter, ComponentParameter]],
                           parameter: Union[InstrumentParameter, ComponentParameter]) -> bool:
    return any(parameter.name == x.name for x in parameters)
