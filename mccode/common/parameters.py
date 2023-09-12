from dataclasses import dataclass
from typing import Union
from .expression import Expr


@dataclass
class InstrumentParameter:
    name: str
    unit: str
    value: Expr

    def __str__(self):
        from .expression import DataType
        mctype = ''
        if self.value.is_str:
            mctype = 'string '
        elif self.value.is_vector and self.value.data_type == DataType.float:
            mctype = 'vector '
        elif self.value.data_type == DataType.int:
            mctype = 'int '
        name = self.name if self.unit is None else f'{self.name}/{self.unit}'
        default = f' = {self.value}' if self.value.has_value else ''
        return f'{mctype}{name}{default}'

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

    def compatible_value(self, value):
        return self.value.compatible(value, id_ok=True)

    def __eq__(self, other):
        if isinstance(other, ComponentParameter):
            return self.name == other.name and self.value == other.value
        return self.value == other


def parameter_name_present(parameters: tuple[Union[InstrumentParameter, ComponentParameter]],
                           name: str) -> bool:
    return any(name == x.name for x in parameters)
