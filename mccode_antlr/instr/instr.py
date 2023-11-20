"""Data structures required for representing the contents of a McCode instr file"""
from io import StringIO
from dataclasses import dataclass, field
from typing import Union
from ..common import InstrumentParameter, MetaData, parameter_name_present, RawC, blocks_to_raw_c
from ..reader import Registry
from .instance import Instance
from .group import Group
from zenlog import log


@dataclass
class Instr:
    """Intermediate representation of a McCode instrument

    Read from a .instr file -- possibly including more .comp and .instr file sources
    For output to a runtime source file
    """
    name: str = None  # Instrument name, e.g. {name}.instr (typically)
    source: str = None  # Instrument *file* name
    parameters: tuple[InstrumentParameter] = field(default_factory=tuple)  # runtime-set instrument parameters
    metadata: tuple[MetaData] = field(default_factory=tuple)  # metadata for use by simulation consumers
    components: tuple[Instance] = field(default_factory=tuple)  #
    included: tuple[str] = field(default_factory=tuple)  # names of included instr definition(s)
    user: tuple[RawC] = field(default_factory=tuple)  # struct members for _particle
    declare: tuple[RawC] = field(default_factory=tuple)  # global parameters used in component trace
    initialize: tuple[RawC] = field(default_factory=tuple)  # initialization of global declare parameters
    save: tuple[RawC] = field(default_factory=tuple)  # statements executed after TRACE to save results
    final: tuple[RawC] = field(default_factory=tuple)  # clean-up memory for global declare parameters
    groups: dict[str, Group] = field(default_factory=dict)
    flags: tuple[str] = field(default_factory=tuple)  # (C) flags needed for compilation of the (translated) instrument
    registries: tuple[Registry] = field(default_factory=tuple)  # the registries used by the reader to populate this

    def to_file(self, output=None, wrapper=None):
        if output is None:
            output = StringIO()
        if wrapper is None:
            from mccode_antlr.common import TextWrapper
            wrapper = TextWrapper(width=120)
        print(wrapper.start_block_comment(f'Instrument {self.name}'), file=output)
        print(wrapper.line('Instrument:', [self.name or 'None']), file=output)
        print(wrapper.line('Source:', [self.source or 'None']), file=output)
        print(wrapper.line('Contains:', [f'"%include {include}"' for include in self.included]), file=output)
        print(wrapper.line('Registries:', [registry.name for registry in self.registries]), file=output)
        for registry in self.registries:
            registry.to_file(output=output, wrapper=wrapper)
        print(wrapper.end_block_comment(), file=output)

        instr_parameters = wrapper.hide(', '.join(p.to_string(wrapper=wrapper) for p in self.parameters))
        first_line = wrapper.line('DEFINE INSTRUMENT', [f'{self.name}({instr_parameters})'])
        print(first_line, file=output)

        for metadata in self.metadata:
            metadata.to_file(output=output, wrapper=wrapper)
        if self.flags:
            print(wrapper.quoted_line('DEPENDENCY ', list(self.flags)), file=output)

        if self.declare:
            print(wrapper.block('DECLARE', _join_rawc_tuple(self.declare)), file=output)
        if self.user:
            print(wrapper.block('USERVARS', _join_rawc_tuple(self.user)), file=output)
        if self.initialize:
            print(wrapper.block('INITIALIZE', _join_rawc_tuple(self.initialize)), file=output)

        print(wrapper.start_list('TRACE'), file=output)
        for instance in self.components:
            print(wrapper.start_list_item(), file=output)
            instance.to_file(output, wrapper)
            print(wrapper.end_list_item(), file=output)
        if self.save:
            print(wrapper.block('SAVE', _join_rawc_tuple(self.save)), file=output)
        if self.final:
            print(wrapper.block('FINALLY', _join_rawc_tuple(self.final)), file=output)
        print(wrapper.end_list('END'), file=output)

    def to_string(self, wrapper):
        from io import StringIO
        output = StringIO()
        self.to_file(output, wrapper)
        return output.getvalue()

    def __str__(self):
        from mccode_antlr.common import TextWrapper
        return self.to_string(TextWrapper())

    def _my_repr_html_(self):
        from mccode_antlr.common import HTMLWrapper
        wrapper = HTMLWrapper(hider='hider', hidden='hidden')
        output = StringIO()
        self.to_file(output=output, wrapper=wrapper)
        body = output.getvalue()
        style = """
        <style> 
        .hider {cursor: pointer; user-select: none;}
        .hider::before {content: "...";}
        .hidden-before::before {display: none;}
        .hidden {display: none;}
        .active {display: block;}
        </style>
        """
        script = """
        <script>
        var toggler = document.getElementsByClassName("hider");
        var i;
        for (i = 0; i < toggler.length; i++) {
            toggler[i].addEventListener("click", function() {
                var id = this.getAttribute('data-id');
                this.parentElement.querySelector(`.hidden[id=${id}]`).classList.toggle("active");
                this.classList.toggle("hidden-before");
            });
        }
        </script>
        """
        html = f'<html><head><title>{self.name}</title>{style}</head><body>{body}{script}</body></html>'
        return html

    def add_component(self, a: Instance):
        if any(x.name == a.name for x in self.components):
            raise RuntimeError(f"A component instance named {a.name} is already present in the instrument")
        self.components += (a,)

    def add_parameter(self, a: InstrumentParameter, ignore_repeated=False):
        if not parameter_name_present(self.parameters, a.name):
            self.parameters += (a,)
        elif not ignore_repeated:
            raise RuntimeError(f"An instrument parameter named {a.name} is already present in the instrument")

    def get_parameter(self, name, default=None):
        if parameter_name_present(self.parameters, name):
            for parameter in self.parameters:
                if name == parameter.name:
                    return parameter
        return default

    def has_parameter(self, name):
        return parameter_name_present(self.parameters, name)

    def last_component(self, count: int = 1, removable_ok: bool = True):
        if len(self.components) < count:
            raise RuntimeError(f"Only {len(self.components)} components defined -- can not go back {count}.")
        if removable_ok:
            return self.components[-count]
        fixed = [comp for comp in self.components if not comp.removable]
        if len(fixed) < count:
            for comp in self.components:
                log.info(f'{comp.name}')
            raise RuntimeError(f"Only {len(fixed)} fixed components defined -- can not go back {count}.")
        return fixed[-count]

    def get_component(self, name: str):
        if name == 'PREVIOUS':
            return self.components[-1]
        for comp in self.components:
            if comp.name == name:
                return comp
        raise RuntimeError(f"No component instance named {name} defined.")

    def has_component_named(self, name: str):
        return any(comp.name == name for comp in self.components)

    def get_component_names_by_category(self, category: str):
        """Find all component instance names for a given category.

        Note:
            The category of an instance is determined by its type, and is either
            - set inside the .comp file by a 'CATEGORY <category>' directive, or
            - *guessed* by the reader based on the path to the .comp file.
            The second behaviour is to match McStasScript/McCode-3, which does not work for user-defined components.
        """
        return [inst.name for inst in self.components if category in inst.type.category]

    def add_included(self, name: str):
        self.included += (name,)

    def DEPENDENCY(self, *strings):
        self.flags += strings

    def USERVARS(self, *blocks):
        self.user += blocks_to_raw_c(*blocks)

    def DECLARE(self, *blocks):
        self.declare += blocks_to_raw_c(*blocks)

    def INITIALIZE(self, *blocks):
        self.initialize += blocks_to_raw_c(*blocks)

    def SAVE(self, *blocks):
        self.save += blocks_to_raw_c(*blocks)

    def FINALLY(self, *blocks):
        self.final += blocks_to_raw_c(*blocks)

    def add_metadata(self, m: MetaData):
        if any([x.name == m.name for x in self.metadata]):
            self.metadata = tuple([x for x in self.metadata if x.name != m.name])
        self.metadata += (m,)

    def determine_groups(self):
        for id, inst in enumerate(self.components):
            if inst.group:
                if inst.group not in self.groups:
                    self.groups[inst.group] = Group(inst.group, len(self.groups))
                self.groups[inst.group].add(id, inst)

    def component_types(self):
        # # If component order is unimportant, we can use a set:
        # return set(inst.type for inst in self.components)
        # For comparison with the C code generator, we must keep the order of component definitions
        return list(dict.fromkeys([inst.type for inst in self.components]))

    def collect_metadata(self):
        """Component definitions and instances can define metadata too, collect it all together here"""
        # Metadata defined in an instance overrides that defined in a component.
        # Metadata defined for an instrument is added to the collected list
        return tuple(m for inst in self.components for m in inst.collect_metadata()) + self.metadata

    def _getpath(self, filename: str):
        from pathlib import Path
        for registry in self.registries:
            if registry.known(filename):
                return registry.path(filename).absolute().resolve()
        return Path()

    # def _replace_env_getpath_cmd(self, flags: Union[str, bytes]):
    #     """Replace CMD, ENV, and GETPATH directives from a flag string or byte-array"""
    #     # Mimics McCode-3/tools/Python/mccodelib/cflags.py:evaluate_dependency_str
    #     #
    #     is_bytes = isinstance(flags, bytes)
    #     to_str = (lambda b: b.decode()) if is_bytes else (lambda b: b)
    #     from_str = (lambda b: b.encode()) if is_bytes else (lambda b: b)
    #
    #     def getpath(chars):
    #         return from_str(str(self._getpath(to_str(chars)).as_posix()))
    #
    #     def eval_cmd(chars):
    #         from subprocess import run, CalledProcessError
    #         try:
    #             proc = run(to_str(chars), check=True, shell=True, capture_output=True)
    #             output = proc.stdout
    #         except CalledProcessError as error:
    #             raise RuntimeError(f"Calling {to_str(chars)} resulted in error {error}")
    #         output = [line.strip() for line in to_str(output).splitlines() if line.strip()]
    #         if len(output) > 1:
    #             raise RuntimeError(f"Calling {to_str(chars)} produced more than one line of output")
    #         return from_str(output[0] if output else '')
    #
    #     def eval_env(chars):
    #         from os import environ
    #         return from_str(environ.get(to_str(chars), ''))
    #
    #     def replace(chars, start, replacer):
    #         if start not in chars:
    #             return chars
    #         before, after = chars.split(start, 1)
    #         if from_str('(') != after[0]:
    #             raise ValueError(f'Missing opening parenthesis in dependency string after {to_str(start)}')
    #         if from_str(')') not in after:
    #             raise ValueError(f'Missing closing parenthesis in dependency string after {to_str(start)}')
    #         dep, after = after[1:].split(from_str(')'), 1)
    #         if start in dep:
    #             raise ValueError(f'Nested {to_str(start)} in dependency string')
    #         print(f'{type(before)} -- {before}')
    #         print(f'{type(replacer(dep))}')
    #         return before + replacer(dep) + replace(after, start, replacer)
    #
    #     keys = [b'ENV', b'GETPATH', b'CMD'] if is_bytes else ['ENV', 'GETPATH', 'CMD']
    #
    #     print(f'The input {flags} is a {type(flags)} object, so {is_bytes = }')
    #     for key, worker in zip(keys, [eval_env, getpath, eval_cmd]):
    #         flags = replace(flags, key, worker)
    #
    #     return flags

    def _replace_env_getpath_cmd(self, flags: str):
        """Replace CMD, ENV, and GETPATH directives from a flag string"""

        # Mimics McCode-3/tools/Python/mccodelib/cflags.py:evaluate_dependency_str
        #
        def getpath(chars):
            return self._getpath(chars).as_posix()

        def eval_cmd(chars):
            from subprocess import run, CalledProcessError
            try:
                proc = run(chars, check=True, shell=True, capture_output=True, text=True)
                output = proc.stdout
            except CalledProcessError as error:
                raise RuntimeError(f"Calling {chars} resulted in error {error}")
            output = [line.strip() for line in output.splitlines() if line.strip()]
            if len(output) > 1:
                raise RuntimeError(f"Calling {chars} produced more than one line of output")
            return output[0] if output else ''

        def eval_env(chars):
            from os import environ
            return environ.get(chars, '')

        def replace(chars, start, replacer):
            if start not in chars:
                return chars
            before, after = chars.split(start, 1)
            if '(' != after[0]:
                raise ValueError(f'Missing opening parenthesis in dependency string after {start}')
            if ')' not in after:
                raise ValueError(f'Missing closing parenthesis in dependency string after {start}')
            dep, after = after[1:].split(')', 1)
            if start in dep:
                raise ValueError(f'Nested {start} in dependency string')
            return before + replacer(dep) + replace(after, start, replacer)

        for key, worker in zip(['ENV', 'GETPATH', 'CMD'], [eval_env, getpath, eval_cmd]):
            flags = replace(flags, key, worker)

        return flags

    def _replace_keywords(self, flag):
        from mccode_antlr.config import config
        from re import sub
        if '@NEXUSFLAGS@' in flag:
            flag = sub(r'@NEXUSFLAGS@', config['flags']['nexus'].as_str_expanded(), flag)
        if '@MCCODE_LIB@' in flag:
            print(f'The instrument {self.name} uses @MCCODE_LIB@ dependencies which no longer work.')
            print('Expect problems at compilation.')
            flag = sub('@MCCODE_LIB@', '.', flag)
        return flag

    def decoded_flags(self) -> list[str]:
        # Each 'flag' in self.flags is from a single instrument component DEPENDENCY, and might contain duplicates:
        # If we accept that white space differences matter, we can deduplicate the strings 'easily'
        unique_flags = set(self.flags)
        # log.debug(f'{unique_flags = }')
        # The dependency strings are allowed to contain any of
        #       '@NEXUSFLAGS@', @MCCODE_LIB@, CMD(...), ENV(...), GETPATH(...)
        # each of which should be replaced by ... something. Start by replacing the 'static' (old-style) keywords
        replaced_flags = [self._replace_keywords(flag) for flag in unique_flags]
        # Then use the above decoder method to replace any instances of CMD, ENV, or GETPATH
        return [self._replace_env_getpath_cmd(flag) for flag in replaced_flags]

    def copy(self, first=0, last=-1):
        """Return a copy of this instrument, optionally with only a subset of components"""
        from copy import deepcopy
        copy = Instr(self.name, self.source)
        copy.parameters = tuple(x for x in self.parameters)
        copy.metadata = tuple(x.copy() for x in self.metadata)
        if last < 0:
            last += 1 + len(self.components)
        copy.components = tuple(x.copy() for x in self.components[first:last])
        copy.included = tuple(x for x in self.included)
        copy.user = tuple(x.copy() for x in self.user)
        copy.declare = tuple(x.copy() for x in self.declare)
        copy.initialize = tuple(x.copy() for x in self.initialize)
        copy.save = tuple(x.copy() for x in self.save)
        copy.final = tuple(x.copy() for x in self.final)
        copy.groups = {k: v.copy() for k, v in self.groups.items()}
        copy.flags = tuple(x for x in self.flags)
        copy.registries = tuple(x for x in self.registries)
        return copy

    def split(self, after, remove_unused_parameters=False):
        if isinstance(after, Instance):
            index = self.components.index(after)
        elif isinstance(after, str):
            index = [i for i, x in enumerate(self.components) if x.name == after]
            if len(index) != 1:
                raise RuntimeError(f'Can only split an instrument after a single component, "{after}" matches {index}')
            index = index[0]
        else:
            raise RuntimeError('Can only split an instrument after a component or component name')
        first = self.copy(last=index + 1)
        first.name = self.name + '_first'
        if first.check_instrument_parameters(remove=remove_unused_parameters) and not remove_unused_parameters:
            log.warn(f'Instrument {first.name} has unused instrument parameters')
        second = self.copy(first=index + 1)
        second.name = self.name + '_second'
        if second.check_instrument_parameters(remove=remove_unused_parameters) and not remove_unused_parameters:
            log.warn(f'Instrument {second.name} has unused instrument parameters')
        return first, second

    def make_instance(self, name, component, at_relative=None, rotate_relative=None, orientation=None,
                      parameters=None, group=None, removable=False):
        if parameters is None:
            parameters = tuple()
        if any(x.name == name for x in self.components):
            raise RuntimeError(f"An instance named {name} is already present in the instrument")
        if isinstance(component, str):
            from ..reader import Reader
            reader = Reader(registries=list(self.registries))
            component = reader.get_component(component)
            self.flags += tuple(reader.c_flags)
        self.components += (Instance(name, component, at_relative, rotate_relative, orientation,
                                     parameters, group, removable),)

    def mcpl_split(self, after, filename=None, output_parameters=None, input_parameters=None, remove_unused_parameters=False):
        from ..common import ComponentParameter
        from ..common import Expr, Value, ObjectType
        from .orientation import Vector, Angles
        if filename is None:
            filename = self.name + '.mcpl'
        if filename[0] != '"' or filename[-1] != '"':
            filename = '"' + filename + '"'

        filename_parameter = ComponentParameter('filename', Expr(Value('mcpl_filename', object_type=ObjectType.parameter)))
        first, second = self.split(after, remove_unused_parameters=remove_unused_parameters)
        mcpl_filename = InstrumentParameter.parse(f'string mcpl_filename = {filename}')
        first.add_parameter(mcpl_filename)
        second.add_parameter(mcpl_filename)

        fc = first.components[-1]
        if fc.type.name != 'Arm':
            log.warn(f'Component {after} is a {fc.type.name} instead of an Arm -- using MCPL file may cause problems')

        if output_parameters is None:
            output_parameters = (filename_parameter,)
        elif not any(p.name == 'filename' for p in output_parameters):
            output_parameters = (filename_parameter,) + output_parameters
        # remove the last component, since we're going to re-use its name:
        first.components = first.components[:-1]
        # automatically adds the component at the end of the list:
        first.make_instance(fc.name, 'MCPL_output', fc.at_relative, fc.rotate_relative, fc.orientation,
                            output_parameters)

        if input_parameters is None:
            input_parameters = (filename_parameter,)
        elif not any(p.name == 'filename' for p in input_parameters):
            input_parameters = (filename_parameter,) + input_parameters
        if not any(p.name == 'verbose' for p in input_parameters):
            input_parameters = (ComponentParameter('verbose', Expr.float(0)),) + input_parameters
        # the MCPL input component _is_ the origin of its simulation
        second.make_instance(fc.name, 'MCPL_input', (Vector(), None), (Angles(), None),
                             parameters=input_parameters)
        # move the newly added component to the front of the list:
        second.components = (second.components[-1],) + second.components[:-1]

        return first, second

    def parameter_used(self, name: str):
        """Check that an instrument parameter is used in the instrument"""
        for instance in self.components:
            if instance.parameter_used(name):
                return True
        for section in (self.declare, self.initialize, self.save, self.final):
            for block in section:
                # A more complex check would see if the use itself leads to a parameter being used, but
                # that would be language dependent and probably not worth the effort.
                if name in block:
                    return True
        return False

    def check_instrument_parameters(self, remove=False):
        """Check that all instrument parameters are used in the instrument, and optionally remove any that are not

        Returns
        -------
        int
            The number of unused instrument parameters
        """
        names = [p.name for p in self.parameters]
        used = [self.parameter_used(p.name) for p in self.parameters]
        if not all(used):
            log.warn(f'The following instrument parameters are not used in the instrument: '
                     f'{", ".join([n for n, u in zip(names, used) if not u])}')
            if remove:
                self.parameters = tuple(p for i, p in enumerate(self.parameters) if used[i])
                log.warn(f'Removed unused instrument parameters; {len(self.parameters)} remain')
        return len(used) - sum(used)

    def verify_instance_parameters(self):
        """Check that all instance parameters are of the expected type, and that identifiers which match
        instrument parameter names are flagged as such"""
        for instance in self.components:
            instance.verify_parameters(self.parameters)



def _join_rawc_tuple(rawc_tuple: tuple[RawC]):
    return '\n'.join([str(rc) for rc in rawc_tuple])
