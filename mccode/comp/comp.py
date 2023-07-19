"""Data structures required for representing the contents of a McCode comp file"""
from dataclasses import dataclass, field
from ..common import ComponentParameter, MetaData, parameter_name_present


@dataclass
class RawC:
    filename: str
    line: int
    source: str

    @staticmethod
    def from_tuple(p: tuple):
        if isinstance(p, tuple) and len(p) == 3 and \
                isinstance(p[0], str) and isinstance(p[1], int) and isinstance(p[2], str):
            return RawC(*p)
        if isinstance(p, tuple) and len(p) == 2 and isinstance(p[0], int) and isinstance(p[1], str):
            return RawC("", *p)
        if isinstance(p, str):
            return RawC("", -1, p)
        raise RuntimeError(f"No conversion to RawC from\n{p}")

    def to_c(self):
        """Use the preprocessor #line directive to aid in debugging produced C source code."""
        return f'#line {self.line} "{self.filename}"\n{self.source}'


def blocks_to_rawc(*args):
    return tuple(x if isinstance(x, RawC) else RawC.from_tuple(x) for x in args)


# Could this be replaced by a subclassed 'name' class? E.g., Slit.comp <=> class McCompSlit(McComp)?
@dataclass
class Comp:
    name: str = None           # Component *type* name, e.g. {name}.comp
    parameters: tuple[ComponentParameter] = field(default_factory=tuple)  # instance-set component parameters
    settings: tuple[ComponentParameter] = field(default_factory=tuple)    # ??? 'setting' parameters
    output: tuple[ComponentParameter] = field(default_factory=tuple)      # 'output' parameters
    metadata: tuple[MetaData] = field(default_factory=tuple)              # metadata for use by simulation consumers
    dependency: str = None     # compile-time dependency
    acc: bool = True           # False if this component *can not* work under OpenACC
    # literal strings writen into C source files
    share: tuple[RawC] = field(default_factory=tuple)       # function(s) for all instances of this class 
    user: tuple[RawC] = field(default_factory=tuple)        # struct members for _particle
    declare: tuple[RawC] = field(default_factory=tuple)     # global parameters used in component trace
    initialize: tuple[RawC] = field(default_factory=tuple)  # initialization of global declare parameters
    trace: tuple[RawC] = field(default_factory=tuple)       # per-particle interaction executed at TRACE time
    save: tuple[RawC] = field(default_factory=tuple)        # statements executed after TRACE to save results
    final: tuple[RawC] = field(default_factory=tuple)       # clean-up memory for global declare parameters
    display: tuple[RawC] = field(default_factory=tuple)     # draw this component

    def has_parameter(self, a: ComponentParameter):
        return parameter_name_present(self.parameters, a)

    def parameter_name_used(self, parameter_type: str, a: ComponentParameter):
        """Verify that a new parameter name is not already in use."""
        if parameter_name_present(self.parameters, a):
            raise RuntimeError(f"{parameter_type} parameter {a.name} is already an instance parameter!")
        if parameter_name_present(self.settings, a):
            raise RuntimeError(f"{parameter_type} parameter {a.name} is already a setting parameter!")
        if parameter_name_present(self.output, a):
            raise RuntimeError(f"{parameter_type} parameter {a.name} is already an output parameter!")

    def add_parameter(self, a: ComponentParameter):
        self.parameter_name_used('Instance', a)
        self.parameters = (*self.parameters, a) if len(self.parameters) else (a, )

    def add_setting(self, a: ComponentParameter):
        self.parameter_name_used('Setting', a)
        self.settings = (*self.settings, a) if len(self.settings) else (a,)

    def add_output(self, a: ComponentParameter):
        self.parameter_name_used('Output', a)
        self.output = (*self.output, a) if len(self.output) else (a,)

    def no_acc(self):
        self.acc = False

    # Meta programming these block setting methods is more pain than its worth:
    def SHARE(self, *blocks):
        self.share += blocks_to_rawc(blocks)

    def USERVARS(self, *blocks):
        self.user += blocks_to_rawc(blocks)

    def DECLARE(self, *blocks):
        self.declare += blocks_to_rawc(blocks)

    def INITIALIZE(self, *blocks):
        self.initialize += blocks_to_rawc(blocks)

    def TRACE(self, *blocks):
        self.trace += blocks_to_rawc(blocks)

    def SAVE(self, *blocks):
        self.save += blocks_to_rawc(blocks)

    def FINALLY(self, *blocks):
        self.final += blocks_to_rawc(blocks)

    def DISPLAY(self, *blocks):
        self.display += blocks_to_rawc(blocks)

    def add_metadata(self, m: MetaData):
        if any([x.name == m.name for x in self.metadata]):
            self.metadata = tuple([x for x in self.metadata if x.name != m.name])
        self.metadata += (m, )
