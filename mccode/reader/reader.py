from typing import Union
from pathlib import Path
from dataclasses import dataclass, field
from .registry import Registry, MCSTAS_REGISTRY, registries_match, registry_from_specification
from ..comp import Comp


@dataclass
class Reader:
    registries: list[Registry] = field(default_factory=list)
    components: dict[str, Comp] = field(default_factory=dict)
    c_flags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if len(self.registries) == 0:
            self.registries = [MCSTAS_REGISTRY, ]

    def prepend_registry(self, reg: Registry):
        self.registries[:0] = [reg, ]

    def append_registry(self, reg: Registry):
        self.registries.append(reg)

    def handle_search_keyword(self, spec: str):
        if not any(registries_match(reg, spec) for reg in self.registries):
            reg = registry_from_specification(spec)
            if reg is not None:
                self.prepend_registry(reg)
            else:
                raise RuntimeError(f"Registry specification {spec} did not specify a valid registry!")

    def add_c_flags(self, flags):
        self.c_flags.append(flags)

    def locate(self, name: str, which: str = None, ext: str = None):
        registries = self.registries if which is None else [x for x in self.registries if x.name in which]
        for reg in registries:
            if reg.known(name, ext):
                return reg.path(name, ext)
        names = [reg.name for reg in registries]
        msg = "registry " + names[0] if len(names) == 1 else 'registries: ' + ','.join(names)
        raise RuntimeError(f'{name} not found in {msg}')

    def known(self, name: str, which: str = None):
        registries = self.registries if which is None else [x for x in self.registries if x.name in which]
        return any([reg.known(name) for reg in registries])

    def unique(self, name: str, which: str = None):
        registries = self.registries if which is None else [x for x in self.registries if x.name in which]
        return sum([1 for reg in registries if reg.unique(name)]) == 1

    def contain(self, name: str, which: str = None):
        registries = self.registries if which is None else [x for x in self.registries if x.name in which]
        return [reg.name for reg in registries if reg.known(name)]

    def stream(self, name: str, which: str = None):
        from antlr4 import FileStream
        return FileStream(str(self.locate(name, which=which).resolve()))

    def add_component(self, name: str):
        if name in self.components:
            raise RuntimeError("The named component is already known.")
        from antlr4 import CommonTokenStream, FileStream
        from ..grammar import McCompLexer, McCompParser
        from ..comp import CompVisitor
        filename = str(self.locate(name, ext='.comp').resolve())
        lexer = McCompLexer(FileStream(filename))
        tokens = CommonTokenStream(lexer)
        parser = McCompParser(tokens)
        visitor = CompVisitor(self, filename)  # The visitor needs to be able to call *this* method
        res = visitor.visitProg(parser.prog())
        if not isinstance(res, Comp):
            raise RuntimeError(f'Parsing component file {filename} did not produce a component object!')
        self.components[name] = res

    def get_component(self, name: str):
        if name not in self.components:
            self.add_component(name)
        return self.components[name]

    def get_instrument(self, name: Union[str, Path]):
        """Load and parse an instr Instrument definition file

        In McCode3 fashion, the instrument file *should* be in the current working directory.
        In new-fashion, the registry/registries will be checked if it is not.
        """
        from antlr4 import CommonTokenStream, FileStream
        from ..grammar import McInstrParser, McInstrLexer
        from ..instr import InstrVisitor, Instr
        path = name if isinstance(name, Path) else Path(name)
        if path.suffix != '.instr':
            path = path.with_suffix(f'{path.suffix}.instr')
        if not path.exists() and not path.is_file():
            path = self.locate(path.name)  # include the .instr for the search
        if not path.exists() and not path.is_file():
            raise RuntimeError(f'Can not locate instr file for {name}.')
        filename = str(path.resolve())
        lexer = McInstrLexer(FileStream(filename))
        tokens = CommonTokenStream(lexer)
        parser = McInstrParser(tokens)
        visitor = InstrVisitor(self, filename)
        res = visitor.visitProg(parser.prog())
        if not isinstance(res, Instr):
            raise RuntimeError(f'Parsing instrument file {filename} did not produce an Instr object')
        res.source = filename
        res.flags = tuple(self.c_flags)
        res.registries = tuple(self.registries)
        return res

