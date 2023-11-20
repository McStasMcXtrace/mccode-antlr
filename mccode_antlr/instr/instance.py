from zenlog import log
from dataclasses import dataclass, field
from typing import TypeVar, Union
from ..comp import Comp
from ..common import Expr, Value, DataType
from ..common import InstrumentParameter, ComponentParameter, MetaData, parameter_name_present, RawC, blocks_to_raw_c
from .orientation import Orient, Vector, Angles
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
    orientation: Orient = None
    parameters: tuple[ComponentParameter] = field(default_factory=tuple)
    removable: bool = False
    cpu: bool = False
    split: Expr = None
    when: Expr = None
    group: str = None
    extend: tuple[RawC] = field(default_factory=tuple)
    jump: tuple[Jump] = field(default_factory=tuple)
    metadata: tuple[MetaData] = field(default_factory=tuple)

    def __repr__(self):
        return f'Instance({self.name}, {self.type.name})'

    def to_file(self, output, wrapper=None):
        if self.cpu:
            print(wrapper.line('CPU', []), file=output)

        instance_parameters = wrapper.hide(', '.join(p.to_string(wrapper=wrapper) for p in self.parameters))
        line = wrapper.bold('COMPONENT') + f' {self.name} = {self.type.name}({instance_parameters}) '

        if self.when is not None:
            line += wrapper.bold('WHEN') + ' ' + wrapper.escape(str(self.when)) + ' '

        def rf(which, x, required=False):
            absolute = wrapper.bold('ABSOLUTE')
            relative = wrapper.bold('RELATIVE')
            return _triplet_ref_str(wrapper.bold(which), x, absolute, relative, required)

        # The "AT ..." statement is required even when it is "AT (0, 0, 0) ABSOLUTE"
        line += rf('AT', self.at_relative, required=True) + ' '
        line += rf('ROTATED', self.rotate_relative) + wrapper.br()
        print(line, file=output)

        if self.group is not None:
            print(wrapper.line('GROUP', [self.group]), file=output)
        if self.extend:
            extends = '\n'.join(str(ext) for ext in self.extend)
            print(wrapper.block('EXTEND', extends), file=output)
        for jump in self.jump:
            jump.to_file(output, wrapper)
        for metadata in self.metadata:
            metadata.to_file(output, wrapper)

    def to_string(self, wrapper):
        from io import StringIO
        output = StringIO()
        self.to_file(output, wrapper)
        return output.getvalue()

    def __str__(self):
        from mccode_antlr.common import TextWrapper
        return self.to_string(TextWrapper())

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
        if self.orientation is None:
            ar, rr = self.at_relative, self.rotate_relative
            if not isinstance(ar[0], Vector) or not isinstance(rr[0], Angles):
                log.warn(f'Expected {ar=} and {rr=} to be Vector and Angles respectively')
            if rr[1] is None and ar[1] is not None:
                log.warn(f'Expected rotation reference to be specified when at reference is specified')
            at = ar[0] if isinstance(ar[0], Vector) else Vector(*ar[0])
            an, ar = (ar[1].name, ar[1].orientation) if ar[1] else ("ABSOLUTE", None)
            rt = rr[0] if isinstance(rr[0], Angles) else Angles(*rr[0])
            rn, rr = (rr[1].name, rr[1].orientation) if rr[1] else (an, ar)
            self.orientation = Orient.from_dependent_orientations(ar, at, rr, rt)

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
        # # If a parameter is set to an instrument parameter name, we need to keep track of that here:
        # TODO: Either add a reference to the containing instrument (and carry that around always)
        #       Or perform this check when it comes time to translate the whole instrument :/

        self.parameters += (ComponentParameter(p.name, value), )

    def verify_parameters(self, instrument_parameters: tuple[InstrumentParameter]):
        """Check for instance parameters which are identifiers that match instrument parameter names,
        and flag them as parameter objects"""
        instrument_parameter_names = [x.name for x in instrument_parameters]
        for par in self.parameters:
            par.value.verify_parameters(instrument_parameter_names)

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

    def copy(self):
        return Instance(self.name, self.type, self.at_relative, self.rotate_relative,
                        orientation=self.orientation, parameters=self.parameters,
                        removable=self.removable, cpu=self.cpu, split=self.split, when=self.when,
                        group=self.group, extend=self.extend, jump=self.jump, metadata=self.metadata)

    def parameter_used(self, name: str):
        if any([name in par.value for par in self.parameters]):
            return True
        if name in self.at_relative[0] or name in self.rotate_relative[0] or name in self.orientation:
            return True
        if name in (self.split or []) or name in (self.when or []):
            return True
        for block in self.extend:
            if name in block:
                return True
        for jump in self.jump:
            if name in jump:
                return True
        return False


def _triplet_ref_str(which, tr: Union[VectorReference, AnglesReference], absolute, relative, required=False):
    pos, ref = tr
    if isinstance(pos, tuple):
        pos = Vector(*pos)
    if pos.is_null() and ref is None and not required:
        return ''
    return f'{which} {pos} {absolute if ref is None else f"{relative} {ref.name}"}'
