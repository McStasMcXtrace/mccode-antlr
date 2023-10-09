from pathlib import Path
from typing import Union
from mccode.instr import Instr
from mccode.reader import Registry


def parse_mccode_instr(contents: str, registry: Registry, source: str = None) -> Instr:
    from antlr4 import CommonTokenStream, InputStream
    from mccode.grammar import McInstrParser, McInstrLexer
    from mccode.instr import InstrVisitor
    from mccode.reader import Reader
    parser = McInstrParser(CommonTokenStream(McInstrLexer(InputStream(contents))))
    registries = [registry]
    reader = Reader(registries=registries)
    visitor = InstrVisitor(reader, source or '<string>')
    instr = visitor.visitProg(parser.prog())
    instr.flags = tuple(reader.c_flags)
    instr.registries = tuple(registries)
    return instr


def pseudo_parse_mccode_instr(contents: str, source: str = None) -> Instr:
    from mccode.reader import PseudoReader
    from mccode.instr import InstrVisitor
    from mccode.grammar import McInstrParser, McInstrLexer
    from antlr4 import CommonTokenStream, InputStream
    parser = McInstrParser(CommonTokenStream(McInstrLexer(InputStream(contents))))
    visitor = InstrVisitor(PseudoReader(), source or '<string>')
    return visitor.visitProg(parser.prog())


def parse_mcstas_instr(contents: str) -> Instr:
    from mccode.reader import MCSTAS_REGISTRY
    return parse_mccode_instr(contents, MCSTAS_REGISTRY)


def parse_mcxtrace_instr(contents: str) -> Instr:
    from mccode.reader import MCXTRACE_REGISTRY
    return parse_mccode_instr(contents, MCXTRACE_REGISTRY)


def load_mccode_instr(filename: Union[str, Path], registry: Registry) -> Instr:
    return parse_mccode_instr(Path(filename).read_text(), registry, source=str(filename))


def load_mcstas_instr(filename: Union[str, Path]) -> Instr:
    from mccode.reader import MCSTAS_REGISTRY
    return load_mccode_instr(filename, MCSTAS_REGISTRY)


def load_mcxtrace_instr(filename: Union[str, Path]) -> Instr:
    from mccode.reader import MCXTRACE_REGISTRY
    return load_mccode_instr(filename, MCXTRACE_REGISTRY)
