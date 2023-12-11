def make_assembler(name: str):
    from mccode_antlr.assembler import Assembler
    from mccode_antlr.reader import MCSTAS_REGISTRY
    return Assembler(name, registries=[MCSTAS_REGISTRY])


def parse_instr_string(instr_source: str):
    from mccode_antlr.loader import parse_mcstas_instr
    return parse_mcstas_instr(instr_source)