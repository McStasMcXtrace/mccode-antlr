"""Data structures required for representing the contents of a McCode instr file"""
from dataclasses import dataclass, field
from ..common import InstrumentParameter, MetaData, parameter_name_present, RawC, blocks_to_raw_c
from .instance import Instance
from .group import Group


@dataclass
class Instr:
    name: str = None             # Instrument name, e.g. {name}.instr (typically)
    parameters: tuple[InstrumentParameter] = field(default_factory=tuple)  # runtime-set instrument parameters
    metadata: tuple[MetaData] = field(default_factory=tuple)               # metadata for use by simulation consumers
    dependency: str = None       # compile-time dependency
    components: tuple[Instance] = field(default_factory=tuple)  #
    included: tuple[str] = field(default_factory=tuple)  # names of included instr definition(s)
    user: tuple[RawC] = field(default_factory=tuple)  # struct members for _particle
    declare: tuple[RawC] = field(default_factory=tuple)  # global parameters used in component trace
    initialize: tuple[RawC] = field(default_factory=tuple)  # initialization of global declare parameters
    save: tuple[RawC] = field(default_factory=tuple)  # statements executed after TRACE to save results
    final: tuple[RawC] = field(default_factory=tuple)  # clean-up memory for global declare parameters
    groups: dict[str, Group] = field(default_factory=dict)

    def add_component(self, a: Instance):
        if any(x.name == a.name for x in self.components):
            raise RuntimeError(f"A component instance named {a.name} is already present in the instrument")
        a.components = (*a.components, a) if len(a.components) else (a, )

    def add_parameter(self, a: InstrumentParameter):
        if parameter_name_present(self.parameters, a.name):
            raise RuntimeError(f"An instrument parameter named {a.name} is already present in the instrument")
        a.parameters = (*a.parameters, a) if len(a.parameters) else (a, )

    def last_component(self, count: int = 1, removable_ok: bool = True):
        if len(self.components) <= count:
            raise RuntimeError(f"Only {len(self.components)} components defined -- can not go back {count}.")
        if removable_ok:
            return self.components[-count]
        fixed = [comp for comp in self.components if not comp.removable]
        if len(fixed) <= count:
            raise RuntimeError(f"Only {len(fixed)} fixed components defined -- can not go back {count}.")
        return fixed[-count]

    def get_component(self, name: str):
        for comp in self.components:
            if comp.name == name:
                return comp
        raise RuntimeError(f"No component instance named {name} defined.")

    def add_included(self, name: str):
        self.included += (name, )

    def USERVARS(self, *blocks):
        self.user += blocks_to_raw_c(blocks)

    def DECLARE(self, *blocks):
        self.declare += blocks_to_raw_c(blocks)

    def INITIALIZE(self, *blocks):
        self.initialize += blocks_to_raw_c(blocks)

    def SAVE(self, *blocks):
        self.save += blocks_to_raw_c(blocks)

    def FINALLY(self, *blocks):
        self.final += blocks_to_raw_c(blocks)

    def add_metadata(self, m: MetaData):
        if any([x.name == m.name for x in self.metadata]):
            self.metadata = tuple([x for x in self.metadata if x.name != m.name])
        self.metadata += (m, )

    def determine_groups(self):
        for id, inst in enumerate(self.components):
            if inst.group:
                if inst.group not in self.groups:
                    self.groups[inst.group] = Group(inst.group, len(self.groups))
                self.groups[inst.group].add(id, inst)