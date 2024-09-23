from pathlib import Path
from typing import Union
from mccode_antlr.instr import Instr
from mccode_antlr.reader import Registry


def parse_mccode_instr_parameters(contents: str):
    from antlr4 import InputStream
    from mccode_antlr.grammar import McInstr_parse
    from mccode_antlr.instr import InstrParametersVisitor
    visitor = InstrParametersVisitor()
    return visitor.visitProg(McInstr_parse(InputStream(contents), 'prog'))


def parse_mccode_instr(contents: str, registry: Registry, source: str = None) -> Instr:
    from antlr4 import InputStream
    from mccode_antlr.grammar import McInstr_parse
    from mccode_antlr.instr import InstrVisitor
    from mccode_antlr.reader import Reader
    registries = [registry]
    reader = Reader(registries=registries)
    visitor = InstrVisitor(reader, source or '<string>')
    instr = visitor.visitProg(McInstr_parse(InputStream(contents), 'prog'))
    instr.flags = tuple(reader.c_flags)
    instr.registries = tuple(registries)
    return instr


def parse_mcstas_instr(contents: str) -> Instr:
    from mccode_antlr.reader import MCSTAS_REGISTRY
    return parse_mccode_instr(contents, MCSTAS_REGISTRY)


def parse_mcxtrace_instr(contents: str) -> Instr:
    from mccode_antlr.reader import MCXTRACE_REGISTRY
    return parse_mccode_instr(contents, MCXTRACE_REGISTRY)


def load_mccode_instr(filename: Union[str, Path], registry: Registry) -> Instr:
    return parse_mccode_instr(Path(filename).read_text(), registry, source=str(filename))


def load_mcstas_instr(filename: Union[str, Path]) -> Instr:
    from mccode_antlr.reader import MCSTAS_REGISTRY
    return load_mccode_instr(filename, MCSTAS_REGISTRY)


def load_mcxtrace_instr(filename: Union[str, Path]) -> Instr:
    from mccode_antlr.reader import MCXTRACE_REGISTRY
    return load_mccode_instr(filename, MCXTRACE_REGISTRY)
