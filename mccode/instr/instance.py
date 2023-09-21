from zenlog import log
from dataclasses import dataclass, field
from typing import TypeVar, Union
from ..comp import Comp
from ..common import Expr, Value, DataType
from ..common import ComponentParameter, MetaData, parameter_name_present, RawC, blocks_to_raw_c
from .orientation import DependentOrientation, Vector, Angles
from .jump import Jump

InstanceReference = TypeVar('InstanceReference', bound='Instance')
VectorReference = tuple[Vector, InstanceReference]
AnglesReference = tuple[Angles, InstanceReference]

@dataclass
class Instance:
    """Intermediate representation of a McCode component instance

    Read from a .instr file TRACE section, using one or more .comp sources
    For output to a runtime source file
    """
    name: str
    type: Comp
    at_relative: VectorReference
    rotate_relative: AnglesReference
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

    def to_file(self, output, wrapper=None):
        if self.cpu:
            print(wrapper.line('CPU', []), file=output)

        instance_parameters = ', '.join(p.to_string(wrapper=wrapper) for p in self.parameters)
        first_line = wrapper.line('COMPONENT', [f'{self.name} = {self.type.name}({instance_parameters})'])
        print(first_line, file=output)

        if self.when is not None:
            print(wrapper.line('WHEN', [str(self.when)]), file=output)

        print(wrapper.line('AT', [_triplet_ref_str(self.at_relative)]), file=output)
        print(wrapper.line('ROTATED', [_triplet_ref_str(self.rotate_relative)]), file=output)

        if self.group is not None:
            print(wrapper.line('GROUP', [self.group]), file=output)
        if self.extend:
            extends = '\n'.join(str(ext) for ext in self.extend)
            print(wrapper.block('EXTEND', extends), file=output)
        for jump in self.jump:
            jump.to_file(output, wrapper)
        for metadata in self.metadata:
            metadata.to_file(output, wrapper)

    def __str__(self):
        from io import StringIO
        output = StringIO()
        self.to_file(output)
        return output.getvalue()

    @classmethod
    def from_instance(cls, name: str, ref: InstanceReference, at: VectorReference, rotate: AnglesReference):
        # from copy import deepcopy
        # copy each of: parameters, extend, group, jump, when, metadata
        return cls(name, ref.type, at, rotate,
                   parameters=tuple([par for par in ref.parameters]),
                   when=ref.when, group=ref.group,
                   extend=tuple([ext for ext in ref.extend]),
                   jump=tuple([jmp for jmp in ref.jump]),
                   metadata=tuple([md for md in ref.metadata]))

    def __post_init__(self):
        def tr(t: Union[VectorReference, AnglesReference]) -> tuple[Union[Vector, Angles], DependentOrientation]:
            va, rel = t
            return va, rel if rel is None else rel.orientation
        if self.orientation is None:
            at, at_rel = tr(self.at_relative)
            rt, rt_rel = tr(self.rotate_relative)
            self.orientation = DependentOrientation.from_dependent_orientations(at_rel, at, rt_rel, rt)

    def set_parameter(self, name: str, value, overwrite=False, allow_repeated=True):
        if not parameter_name_present(self.type.define, name) and not parameter_name_present(self.type.setting, name):
            raise RuntimeError(f"Unknown parameter {name} for component type {self.type.name}")
        if parameter_name_present(self.parameters, name):
            if overwrite:
                self.parameters = tuple(x for x in self.parameters if name != x.name)
            elif allow_repeated:
                par = [p for p in self.parameters if name == p.name][0]
                log.info(f'Multiple definitions of {name} in component instance {self.name}')
                if par.value != value:
                    log.info(f'  first-encountered value {par.value} retained')
                    log.info(f'  newly-encountered value {value} dropped')
            else:
                raise RuntimeError(f"Multiple definitions of {name} in component instance {self.name}")
        p = self.type.get_parameter(name)

        if not p.compatible_value(value):
            log.debug(f'{p=}, {name=}, {value=}')
            raise RuntimeError(f"Provided value for parameter {name} is not compatible with {self.type.name}")

        if isinstance(value, str):
            value = Expr.parse(value)
        elif not isinstance(value, Expr):
            # Copy the data_type of the component definition parameter
            # -- thus if value is a str but an int or float is expected, we will know it is an identifier
            value = Expr(Value(value, data_type=p.value.data_type))

        # 2023-09-14 This did nothing. Why was this here?
        # # is this parameter value *actually* an instrument parameter *name*
        # if value.is_id:
        #     pass
        self.parameters += (ComponentParameter(p.name, value), )

    def get_parameter(self, name: str):
        for par in self.parameters:
            if par.name == name:
                return par
        return self.type.get_parameter(name)

    def defines_parameter(self, name: str):
        """Check whether this instance has defined the named parameter"""
        return parameter_name_present(self.parameters, name)

    def set_parameters(self, **kwargs):
        for name, value in kwargs.items():
            self.set_parameter(name, value)

    def REMOVABLE(self):
        self.removable = True

    def CPU(self):
        self.cpu = True

    def SPLIT(self, count):
        if isinstance(count, str):
            count = Expr.parse(count)
        if not isinstance(count, Expr):
            raise ValueError(f'Expected provided SPLIT expression to be an Expr not a {type(count)}')
        self.split = count

    def WHEN(self, expr):
        if isinstance(expr, str):
            expr = Expr.parse(expr)
        if not isinstance(expr, Expr):
            raise ValueError(f'Expected provided WHEN expression to be an Expr not a {type(expr)}')
        if expr.is_constant:
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


def _triplet_ref_str(tr: Union[VectorReference, AnglesReference]):
    pos, ref = tr
    return f'({",".join(str(p) for p in pos)}) {"ABSOLUTE" if ref is None else f"RELATIVE {ref.name}"}'
