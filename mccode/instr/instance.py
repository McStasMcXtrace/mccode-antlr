from dataclasses import dataclass, field
from typing import Self
from ..comp import Comp
from ..common import ComponentParameter, Value, MetaData, parameter_name_present, RawC, blocks_to_raw_c
from .orientation import Orientation, from_at_relative_rotated_relative
from .jump import Jump

@dataclass
class Instance:
    name: str
    type: Comp
    at_relative: tuple[tuple[Value, Value, Value], Self]
    rotate_relative: tuple[tuple[Value, Value, Value], Self]
    orientation: Orientation = None
    parameters: tuple[ComponentParameter] = field(default_factory=tuple)
    removable: bool = False
    cpu: bool = False
    split: Value = None
    when: Value = None
    group: str = None
    extend: tuple[RawC] = field(default_factory=tuple)
    jump: tuple[Jump] = field(default_factory=tuple)
    metadata: tuple[MetaData] = field(default_factory=tuple)

    def __post_init__(self):
        if self.orientation is None:
            self.orientation = from_at_relative_rotated_relative(*self.at_relative, *self.rotate_relative)

    def set_parameter(self, name: str, value):
        if not parameter_name_present(self.type.parameters, name):
            raise RuntimeError(f"Unknown parameter {name} for component type {self.type.name}")
        if parameter_name_present(self.parameters, name):
            raise RuntimeError(f"Multiple definitions of {name} in component instance {self.name}")
        p = self.type.get_parameter(name)
        if not p.compatible_value(value):
            raise RuntimeError(f"Provided value for parameter {name} is not compatible with {self.type.name}")
        v = Value(p.value.data_type, value.value if isinstance(value, Value) else value)
        self.parameters += (ComponentParameter(p.name, v), )

    def REMOVABLE(self):
        self.removable = True

    def CPU(self):
        self.cpu = True

    def SPLIT(self, count):
        self.split = count

    def WHEN(self, expr):
        if not expr.is_a(Value.Type.str):
            raise RuntimeError(f'Evaluated WHEN statement {expr.value} would be constant at runtime!')
        self.when = expr

    def GROUP(self, name: str):
        self.group = name

    def EXTEND(self, *blocks):
        self.group += blocks_to_raw_c(blocks)

    def JUMP(self, *jumps):
        self.jump += jumps

    def add_metadata(self, m: MetaData):
        if any([x.name == m.name for x in self.metadata]):
            self.metadata = tuple([x for x in self.metadata if x.name != m.name])
        self.metadata += (m, )
