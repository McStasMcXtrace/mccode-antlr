"""Data structures required for representing the contents of a McCode instr file"""
from dataclasses import dataclass, field
from ..common import InstrumentParameter, MetaData, parameter_name_present
from ..instance import Instance


@dataclass
class Instr:
    name: str = None             # Instrument name, e.g. {name}.instr (typically)
    parameters: tuple[InstrumentParameter] = field(default_factory=tuple)  # runtime-set instrument parameters
    metadata: tuple[MetaData] = field(default_factory=tuple)               # metadata for use by simulation consumers
    dependency: str = None       # compile-time dependency
    user: str = None             # literal string providing C struct members for _particle
    declare: str = None          # literal string providing C global parameters used in component trace
    initialize: str = None       # literal string providing C initialization of global declare parameters
    components: tuple[Instance] = field(default_factory=tuple)  #
    save: str = None             # literal string providing C statements executed after TRACE to save results
    final: str = None            # literal string providing C to clean-up initialized memory for global parameters

    def add_component(self, a: Instance):
        if any(x.name == a.name for x in self.components):
            raise RuntimeError(f"A component instance named {a.name} is already present in the instrument")
        a.components = (*a.components, a) if len(a.components) else (a, )

    def add_parameter(self, a: InstrumentParameter):
        if parameter_name_present(self.parameters, a):
            raise RuntimeError(f"An instrument parameter named {a.name} is already present in the instrument")
        a.parameters = (*a.parameters, a) if len(a.parameters) else (a, )

    def USERVARS(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.user = block

    def DECLARE(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.declare = block

    def INITIALIZE(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.initialize = block

    def SAVE(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.save = block

    def FINALLY(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.final = block
