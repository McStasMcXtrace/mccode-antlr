from pathlib import Path
from typing import Union


def read_mcstas_instr(filename: Union[str, Path]):
    from antlr4 import CommonTokenStream, InputStream
    from mccode.grammar import McInstrParser, McInstrLexer
    from mccode.instr import InstrVisitor
    from mccode.reader import MCSTAS_REGISTRY, Reader
    instr_source = Path(filename).read_text()
    parser = McInstrParser(CommonTokenStream(McInstrLexer(InputStream(instr_source))))
    visitor = InstrVisitor(Reader(registries=[MCSTAS_REGISTRY]), str(filename))
    return visitor.visitProg(parser.prog())
