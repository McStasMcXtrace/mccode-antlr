from typing import Union
from pathlib import Path
from zenlog import log
from dataclasses import dataclass, field
from antlr4.error.ErrorListener import ErrorListener
from .registry import Registry, MCSTAS_REGISTRY, registries_match, registry_from_specification
from ..comp import Comp


class ReaderErrorListener(ErrorListener):
    def __init__(self, filetype: str, name: str, source: str, pre=5, post=2):
        self.filetype = filetype
        self.name = name
        self.source = source
        self.pre = pre
        self.post = post

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        log.error(f'Syntax error in parsing {self.filetype} {self.name} at {line},{column}')
        lines = self.source.split('\n')
        pre_lines = lines[line-self.pre:line]
        post_lines = lines[line:line+self.post]
        for line in pre_lines:
            log.info(line)
        log.error('~'*column + '^ ' + msg)
        for line in post_lines:
            log.info(line)


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

    def fullname(self, name: str, which: str = None, ext: str=None):
        registries = self.registries if which is None else [x for x in self.registries if x.name in which]
        for reg in registries:
            if reg.known(name, ext):
                return reg.fullname(name, ext)
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
        return FileStream(str(self.locate(name, which=which).resolve()), encoding='utf8')

    def add_component(self, name: str, current_instance_name=None):
        if name in self.components:
            raise RuntimeError("The named component is already known.")
        from antlr4 import CommonTokenStream, FileStream
        from ..grammar import McCompLexer, McCompParser
        from ..comp import CompVisitor
        filename = str(self.locate(name, ext='.comp').resolve())
        with open(filename, 'r') as file:
            source = file.read()
        lexer = McCompLexer(FileStream(filename, encoding='utf8'))
        tokens = CommonTokenStream(lexer)
        parser = McCompParser(tokens)
        parser.addErrorListener(ReaderErrorListener('Component', name, source))
        visitor = CompVisitor(self, filename, instance_name=current_instance_name)  # The visitor needs to be able to call *this* method
        res = visitor.visitProg(parser.prog())
        if not isinstance(res, Comp):
            raise RuntimeError(f'Parsing component file {filename} did not produce a component object!')
        if res.category is None:
            # guess the component category from the registered filename (not fully resolved path)
            fullname = self.fullname(name, ext='.comp')
            fullname = fullname if isinstance(fullname, Path) else Path(fullname)
            # if fullname is an absolute path, it comes from a local repository -- so we don't know what to do
            res.category = 'UNKNOWN' if fullname.is_absolute() else fullname.parts[0]
        self.components[name] = res

    def get_component(self, name: str, current_instance_name=None):
        if name not in self.components:
            self.add_component(name, current_instance_name=current_instance_name)
        return self.components[name]

    def get_instrument(self, name: Union[str, Path], destination=None):
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
        with open(filename, 'r') as file:
            source = file.read()
        lexer = McInstrLexer(FileStream(filename, encoding='utf8'))
        tokens = CommonTokenStream(lexer)
        parser = McInstrParser(tokens)
        parser.addErrorListener(ReaderErrorListener('Instrument', name, source))
        visitor = InstrVisitor(self, filename, destination=destination)
        res = visitor.visitProg(parser.prog())
        if not isinstance(res, Instr):
            raise RuntimeError(f'Parsing instrument file {filename} did not produce an Instr object')
        res.source = filename
        res.flags = tuple(self.c_flags)
        res.registries = tuple(self.registries)
        return res
