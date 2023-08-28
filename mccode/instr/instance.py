from zenlog import log
from dataclasses import dataclass, field
from typing import Self
from ..comp import Comp
from ..common import Expr
from ..common import ComponentParameter, MetaData, parameter_name_present, RawC, blocks_to_raw_c
from .orientation import DependentOrientation
from .jump import Jump

@dataclass
class Instance:
    """Intermediate representation of a McCode component instance

    Read from a .instr file TRACE section, using one or more .comp sources
    For output to a runtime source file
    """
    name: str
    type: Comp
    at_relative: tuple[tuple[Expr, Expr, Expr], Self]
    rotate_relative: tuple[tuple[Expr, Expr, Expr], Self]
    orientation: DependentOrientation = None
    parameters: tuple[ComponentParameter] = field(default_factory=tuple)
    removable: bool = False
    cpu: bool = False
    split: Expr = None
    when: Expr = None
    group: str = None
    extend: tuple[RawC] = field(default_factory=tuple)
    jump: tuple[Jump] = field(default_factory=tuple)
    metadata: tuple[MetaData] = field(default_factory=tuple)

    def __post_init__(self):
        if self.orientation is None:
            at, at_rel = self.at_relative[0], None if self.at_relative[1] is None else self.at_relative[1].orientation
            rt, rt_rel = self.rotate_relative[0], None if self.rotate_relative[1] is None else self.rotate_relative[1].orientation
            self.orientation = DependentOrientation.from_dependent_orientations(at_rel, at, rt_rel, rt)

    def set_parameter(self, name: str, value):
        if not parameter_name_present(self.type.define, name) and not parameter_name_present(self.type.setting, name):
            raise RuntimeError(f"Unknown parameter {name} for component type {self.type.name}")
        if parameter_name_present(self.parameters, name):
            raise RuntimeError(f"Multiple definitions of {name} in component instance {self.name}")
        p = self.type.get_parameter(name)
        if not p.compatible_value(value):
            log.debug(f'{p=}, {name=}, {value=}')
            raise RuntimeError(f"Provided value for parameter {name} is not compatible with {self.type.name}")
        v = value if isinstance(value, Expr) else Expr.best(value)

        # is this parameter value *actually* an instrument parameter *name*
        if v.is_id:  # or v.is_str:
            pass
        self.parameters += (ComponentParameter(p.name, v), )

    def get_parameter(self, name: str):
        for par in self.parameters:
            if par.name == name:
                return par
        return self.type.get_parameter(name)

    def set_parameters(self, **kwargs):
        for name, value in kwargs.items():
            self.set_parameter(name, value)

    def REMOVABLE(self):
        self.removable = True

    def CPU(self):
        self.cpu = True

    def SPLIT(self, count):
        self.split = count

    def WHEN(self, expr):
        if expr.is_constant:
            # if not expr.is_a(Value.Type.str):
            raise RuntimeError(f'Evaluated WHEN statement {expr} would be constant at runtime!')
        self.when = expr

    def GROUP(self, name: str):
        self.group = name

    def EXTEND(self, *blocks):
        self.extend += blocks_to_raw_c(*blocks)

    def JUMP(self, *jumps):
        self.jump += jumps

    def add_metadata(self, m: MetaData):
        if any([x.name == m.name for x in self.metadata]):
            self.metadata = tuple([x for x in self.metadata if x.name != m.name])
        self.metadata += (m, )

    def collect_metadata(self):
        # A component declaration and instance can define metadata with the same name
        # When they do, the metadata from *the instance* should take precedence
        md = {m.name: m for m in self.type.collect_metadata()}
        md.update({m.name: m for m in self.metadata})
        return tuple(md.values())
