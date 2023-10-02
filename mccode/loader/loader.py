from pathlib import Path
from typing import Union
from mccode.instr import Instr
from mccode.reader import Registry


def load_mccode_instr(filename: Union[str, Path], registry: Registry) -> Instr:
    from antlr4 import CommonTokenStream, InputStream
    from mccode.grammar import McInstrParser, McInstrLexer
    from mccode.instr import InstrVisitor
    from mccode.reader import Reader
    instr_source = Path(filename).read_text()
    parser = McInstrParser(CommonTokenStream(McInstrLexer(InputStream(instr_source))))
    visitor = InstrVisitor(Reader(registries=[registry]), str(filename))
    return visitor.visitProg(parser.prog())


def load_mcstas_instr(filename: Union[str, Path]) -> Instr:
    from mccode.reader import MCSTAS_REGISTRY
    return load_mccode_instr(filename, MCSTAS_REGISTRY)


def load_mcxtrace_instr(filename: Union[str, Path]) -> Instr:
    from mccode.reader import MCXTRACE_REGISTRY
    return load_mccode_instr(filename, MCXTRACE_REGISTRY)
