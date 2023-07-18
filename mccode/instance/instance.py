from dataclasses import dataclass, field
from ..comp import Comp
from ..common import ComponentParameter, MetaData, parameter_name_present
from .orientation import Orientation


@dataclass
class Instance:
    name: str
    type: Comp
    place: tuple
    orientation: Orientation
    parameters: tuple[ComponentParameter] = field(default_factory=tuple)
    removable: bool = False
    cpu: bool = False
    split: str = None
    when: str = None
    group: str = None
    extend: str = None
    jump: str = None
    metadata: tuple[MetaData] = field(default_factory=tuple)

    def set_parameter(self, a: ComponentParameter):
        if self.type.has_parameter(a) and not parameter_name_present(self.parameters, a):
            self.parameters = (*self.parameters, a) if len(self.parameters) else (a, )
        elif not self.type.has_parameter(a):
            raise RuntimeError(f"Unknown parameter {a.name} for component type {self.type.name}")
        else:
            raise RuntimeError(f"Multiple definitions of {a.name} in component instance {self.name}")

    def REMOVABLE(self):
        self.removable = True

    def CPU(self):
        self.cpu = True

    def SPLIT(self, line):
        self.split = line

    def WHEN(self, line):
        self.when = line

    def GROUP(self, line):
        self.group = line

    def EXTEND(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.group = block

    def JUMP(self, line):
        self.jump = line
