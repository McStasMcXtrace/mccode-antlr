from dataclasses import dataclass
from typing import Union
from .expression import Expr


@dataclass
class InstrumentParameter:
    name: str
    unit: str
    value: Expr

    def __str__(self):
        from io import StringIO
        from mccode.common import TextWrapper
        output = StringIO()
        self.to_file(output, TextWrapper())
        return output.getvalue()

    def to_file(self, output, wrapper):
        from .expression import DataType
        line = ''
        if self.value.is_str:
            line = 'string '
        elif self.value.is_vector and self.value.data_type == DataType.float:
            line = 'vector '
        elif self.value.data_type == DataType.int:
            line = 'int '
        if len(line):
            if not self.value.has_value and self.unit is None:
                line = wrapper.type_parameter(line, self.name)
            elif not self.value.has_value:
                line = wrapper.type_parmeter_unit(line, self.name, self.unit)
            elif self.unit is None:
                line = wrapper.type_parameter_value(line, self.name, self.value)
            else:
                line = wrapper.type_parmeter_unit_value(line, self.name, self.unit, self.value)
        else:
            if not self.value.has_value and self.unit is None:
                line = wrapper.parameter(self.name)
            elif not self.value.has_value:
                line = wrapper.parmeter_unit(self.name, self.unit)
            elif self.unit is None:
                line = wrapper.parameter_value(self.name, self.value)
            else:
                line = wrapper.parmeter_unit_value(self.name, self.unit, self.value)
        print(line, file=output)

    @staticmethod
    def parse(s: str):
        from antlr4 import CommonTokenStream, InputStream
        from ..grammar import McInstrParser, McInstrLexer
        from ..instr import InstrVisitor
        stream = InputStream(s)
        lexer = McInstrLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = McInstrParser(tokens)
        visitor = InstrVisitor(None, None)
        return visitor.getInstrument_parameter(parser.instrument_parameter())


@dataclass
class ComponentParameter:
    name: str
    value: Expr

    def __str__(self):
        return f"{self.name}={self.value}"

    def to_file(self, output, wrapper):
        print(wrapper.parameter_value(self.name, self.value), file=output)

    def compatible_value(self, value):
        return self.value.compatible(value, id_ok=True)

    def __eq__(self, other):
        if isinstance(other, ComponentParameter):
            return self.name == other.name and self.value == other.value
        return self.value == other


def parameter_name_present(parameters: tuple[Union[InstrumentParameter, ComponentParameter]],
                           name: str) -> bool:
    return any(name == x.name for x in parameters)
