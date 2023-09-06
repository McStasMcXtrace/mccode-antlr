from dataclasses import dataclass
from typing import Union
from .expression import Expr


@dataclass
class InstrumentParameter:
    name: str
    unit: str
    value: Expr

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


def parameter_name_present(parameters: tuple[Union[InstrumentParameter, ComponentParameter]],
                           name: str) -> bool:
    return any(name == x.name for x in parameters)
