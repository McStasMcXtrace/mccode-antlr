"""Translates a McComp instrument from its intermediate form to a C runtime source file."""
from collections import namedtuple
from ..reader import LIBC_REGISTRY
from ..instr import Instr, Instance
from .target import TargetVisitor
from .c_listener import extract_c_declared_variables

# For use in keeping track of 'USERVAR' particle struct injections
CDeclaration = namedtuple("CDeclaration", "name type init is_pointer is_array orig")

class CTargetVisitor(TargetVisitor, target_language='c'):
    def _file_contents(self, filename):
        # First try the McCode C runtime libraries:
        path = self.include_path(filename)
        # Then any registries used in reading the file(s)
        if not path.is_file() and self.known(filename):
            path = self.locate(filename)
        if not path.is_file():
            raise RuntimeError(f"Can not include the file {filename} because it is not locatable")
        with path.open('r') as file:
            contents = file.read()
        return contents

    def _handle_raw_c_include(self, raw_c: str):
        import regex as re
        re_lib = re.compile(r'^\s*%include\s*"(?P<libname>[^"\n\.]+)"\s*$', re.MULTILINE)
        re_inc = re.compile(r'^\s*%include\s*"(?P<filename>[^"\n]+)"\s*$', re.MULTILINE)
        # Include statements without an extension are library includes (.h, plus .c if embedding the runtime)
        # McCode3 would insert the library immediately on first-encounter, but we want to collect all libraries
        # and ensure they're included before all components.

        # Get any library names in this block:
        libraries = set(match.group('libname') for match in re_lib.finditer(raw_c))
        # *erase* the library includes from the block:
        raw_c = re.sub(re_lib, '', raw_c)

        # If there are any non-library includes remaining, we should insert them immediately:
        matches = list(re_inc.finditer(raw_c))
        while len(matches):
            # Try and find this matched filename
            filename = matches[0].group('filename')
            this_re = re.compile(rf'^\s*%include\s*"{filename}"\s*$', re.MULTILINE)
            raw_c = re.sub(this_re, self._file_contents(filename), raw_c)
            # re-match since we modified raw_c
            matches = list(re_inc.finditer(raw_c))

        return libraries, raw_c

    def _parse_libraries_for_typedefs(self):
        from .c_listener import extract_c_declared_variables_and_defined_types as parse
        typedefs = set()
        for library in self.libraries:
            declares, defined_types = parse(self._file_contents(f'{library}.h'), user_types=list(typedefs))
            typedefs = typedefs.union(set(defined_types))
        # types can also be defined in component 'SHARE' blocks:
        for block in [share for comp in self.source.component_types() if len(comp.share) for share in comp.share]:
            declares, defined_types = parse(block.source, user_types=list(typedefs))
            typedefs = typedefs.union(set(defined_types))
        self.typedefs = list(typedefs)

    def _determine_uservars(self):
        """An instrument can define 'USERVARS' which thus far has been treated as an unparsed block of code.
        We now must extract parameter declarations from this block (there should be *only* declarations, no
        initialization is supported in McCode-3).
        Each declaration *should* of the form
            {type} {name};
            {type} * {name};
            {type} {name}[N];
        Where {type} is a valid C typename _or_ a typename defined in any included libraries or 'SHARE' blocks.
        A possible future extension could allow for valid instantiation in the USERVAR blocks.
        This function extracts the parameter {name}, {type}, (scalar|pointer|array)-ness, and initializer if present
        for the unique set of all variables added to the _particle struct by the user -- it checks for name clashes
        between definitions as well (identical definitions are allowed but not equal named non-matching definitions)

        Extracted values are stored in namedtuple `CDeclaration` objects for easier interaction.
        """
        def extract_declares(name, raw_c_obj):
            from .c_listener import extract_c_declared_variables as parse
            # decs is a dictionary {'variable_name': ('variable_type', ['initializer'|None])}
            decs = parse(raw_c_obj.source, user_types=self.typedefs)
            n = sum(init is not None for c, init in decs.values())
            if n:
                print(f'Warning USERVARS block from {name} contains {n} assignments (= sign).')
                print('        Move them to an EXTEND section. May fail at compile')
            # check if the variable name includes a pointer specification or is literal array
            sc = str.maketrans('', '', '*[] ')  # for '* name' or '***** name' or 'name[]' -> 'name'
            name_pointer_array = [(x.translate(sc), '*' in x, '[' in x and ']' in x) for x in decs]
            return [CDeclaration(n, t, i, p, a, o) for (n, p, a), (o, (t, i)) in zip(name_pointer_array, decs.items())]

        declares = set()  # will be (CDeclaration(name, type, init, is_pointer, is_array, orig), )
        for raw_user_vars_c_block in self.source.user:
            declares.union(extract_declares(self.source.name, raw_user_vars_c_block))

        # Check for differing repeated declarations -- these are set elements with the same name:
        if len(set([d.name for d in declares])) != len(declares):
            raise RuntimeError(f"One or more instrument USERVARS repeated in {self.source.name}")

        # Look for USERVAR section(s) in the set of component definitions too:
        comp_declares = dict()
        for component in self.source.component_types():
            comp_declares[component.name] = set()
            for raw_user_vars_c_block in component.user:
                comp_declares[component.name].union(extract_declares(component.name, raw_user_vars_c_block))
            # Check for differing repeated declarations in this component:
            if len(set([d.name for d in comp_declares[component.name]])) != len(comp_declares[component.name]):
                raise RuntimeError(f"One or more component USERVARS repeated in {component.name}")

        # Check for name clashes *between* components
        nd = set([x for dec in comp_declares.values() for x in dec])
        if len(set([x.name for x in nd])) != len(nd):
            culprits = [x.name for x in self.source.component_types() if len(comp_declares[x.name])]
            raise RuntimeError(f'One or more component USERVARS repeated between components {culprits}')
        # And between all components and the instrument
        nd.union(declares)
        if len(set([x.name for x in nd])) != len(nd):
            culprits = [x.name for x in self.source.component_types() if len(comp_declares[x.name])]
            raise RuntimeError(f'Conflicting USERVAR declarations between instrument {self.source.name} and {culprits}')

        self.instrument_uservars = declares
        self.component_uservars = comp_declares

    def __post_init__(self):
        """Before doing *anything* else. We need to search through all raw C code for %include statements.
        This could not be done earlier if the goal is to have a clear separation between the parsing and target
        languages. (A different target language would not include the same libraries in its raw blocks)
        """
        # Make sure the registry list contains the C library registry, so that we can find and include files
        if not any(reg == LIBC_REGISTRY for reg in self.registries):
            self.registries.append(LIBC_REGISTRY)

        libraries = set()
        inst = self.source
        for grp in (inst.user, inst.declare, inst.initialize, inst.save, inst.final):
            for block in grp:
                libs, block.source = self._handle_raw_c_include(block.source)
                libraries = libraries.union(libs)
        for typ in inst.component_types():
            for grp in (typ.share, typ.user, typ.declare, typ.initialize, typ.trace, typ.save, typ.final, typ.display):
                for block in grp:
                    libs, block.source = self._handle_raw_c_include(block.source)
                    libraries = libraries.union(libs)
        for instance in inst.components:
            for block in instance.extend:
                libs, block.source = self._handle_raw_c_include(block.source)
                libraries = libraries.union(libs)
        self.libraries = list(libraries)

        # search the library headers for type definitions:
        self._parse_libraries_for_typedefs()

        # pull together the per-component-type defined parameters into a dictionary... since this is required
        # in multiple places :/
        # TODO Update component_declared parameters to use CDeclaration as well.
        for typ in inst.component_types():
            declared_parameters = dict()
            for block in typ.declare:
                declared_parameters.update(extract_c_declared_variables(block.source, user_types=self.typedefs))
            self.component_declared_parameters[typ.name] = declared_parameters

        self._determine_uservars()

    def visit_header(self):
        from .c_header import header_pre_runtime, header_post_runtime
        # Get the unique list of USERVAR declarations:
        uuv = set().union(self.instrument_uservars)
        for x in self.component_uservars:
            uuv.union(x)

        is_mcstas = self.is_mcstas
        self.out(header_pre_runtime(is_mcstas, self.source, self.runtime, self.config, self.typedefs, uuv))
        # runtime part
        if self.config.get('include_runtime'):
            self.out('#define MC_EMBEDDED_RUNTIME')
            self.embed_file('mcstas-d.h' if is_mcstas else 'mcxtrace-d.h')
            self.embed_file("mccode-r.h")
            self.embed_file('mcstas-r.h' if is_mcstas else 'mcxtrace-r.h')
            self.embed_file("mccode-r.c")
            self.embed_file('mcstas-r.c' if is_mcstas else 'mcxtrace-r.c')
            if self.verbose:
                print(f"Compile '{self.sink} -DUSE_NEXUS -lNeXus' to enable NeXus support")
        else:
            # This only works if the module is *not* a compressed archive
            # If it is, we would need to do some trickery to ... write out the
            self.out(f'#include "{self.include_path("mcode-r.h")}"')
            self.out(f'#include "{self.include_path("mcstas-r.h" if is_mcstas else "mcxtrace-r.h")}"')
            print(f"Dependency: mccode-r.o\nDependency: {'mcstas-r.o' if is_mcstas else 'mcxtrace-r.o'}")

        self.out(header_post_runtime(self.source, self.runtime, self.config, self.include_path()))

    def visit_declare(self):
        from .c_decls import declarations_pre_libraries
        if self.verbose:
            print(f"Writing instrument '{self.source.name}' and components DECLARE")
        contents, warnings = declarations_pre_libraries(self.source, self.typedefs, self.component_declared_parameters)
        self.out(contents)

        if len(self.libraries):
            self.out("/* %include libraries from instrument and component definitions */")
        for library in self.libraries:
            self.out(f'/* Contents of {library}.h */')
            self.out(self._file_contents(f'{library}.h'))
        if self.config.get('include_runtime'):
            for library in self.libraries:
                self.out(f'/* Contents of {library}.c */')
                self.out(self._file_contents(f'{library}.c'))
        else:
            for library in self.libraries:
                print(f'Dependency: {library}.o')

        self.out("/* User declarations from instrument definition. Can define functions. */")
        self.out('\n'.join([dec.to_c() for dec in self.source.declare]))
        # FIXME I _think_ these macro undefines are not used (that is, they're never defined in the first place)
        self.out('#undef compcurname\n#undef compcurtype\n#undef compcurindex')
        self.out(f"/* end of instrument '{self.source.name}' and components DECLARE */")

        self.warnings += warnings

    def visit_initialize(self):
        from .c_initialise import cogen_initialize
        self.out(cogen_initialize(self.source, self.component_declared_parameters, self.ok_to_skip))

    def enter_trace(self):
        from .c_trace import def_trace_section, cogen_trace_section
        self.out(def_trace_section(self.is_mcstas))
        self.out(cogen_trace_section(self.is_mcstas, self.source, self.component_declared_parameters,
                                     self.instrument_uservars, self.component_uservars))

    def leave_trace(self):
        from .c_trace import undef_trace_section
        self.out(undef_trace_section(self.is_mcstas))

    def enter_uservars(self):
        # After cogen_trace_section, the USERVAR particle struct members need to be defined for raytrace
        uuv = set().union(self.instrument_uservars)
        for x in self.component_uservars:
            uuv.union(x)
        self.out('\n'.join([f'#define {x.name} (_particle->{x.name})' for x in uuv]))

    def leave_uservars(self):
        # following TRACE before undef_trace_section, the USERVAR particle struct members need to be undef'd
        uuv = set().union(self.instrument_uservars)
        for x in self.component_uservars:
            uuv.union(x)
        self.out('\n'.join([f'#undef {x.name}' for x in uuv]))

    def visit_raytrace(self):
        from .c_raytrace import cogen_raytrace
        self.out(cogen_raytrace(self.source, self.ok_to_skip))

    def visit_raytrace_funnel(self):
        from .c_raytrace import cogen_funnel
        self.out(cogen_funnel(self.source, self.ok_to_skip))

    def visit_save(self):
        from .c_save import cogen_save
        self.out(cogen_save(self.source, self.component_declared_parameters))

    def visit_finally(self):
        from .c_finally import cogen_finally
        self.out(cogen_finally(self.source, self.component_declared_parameters))

    def visit_display(self):
        from .c_display import cogen_display
        self.out(cogen_display(self.source, self.component_declared_parameters))

    def visit_macros(self):
        from .c_macros import cogen_getvarpars_fct, cogen_getcompindex_fct, cogen_getparticlevar_fct
        self.out(cogen_getvarpars_fct(self.source))
        uuv = set().union(self.instrument_uservars)
        for x in self.component_uservars:
            uuv.union(x)
        self.out(cogen_getparticlevar_fct(uuv))
        self.out(cogen_getcompindex_fct(self.source))
        self.embed_file('metadata-r.c')
        self.embed_file('mccode_main.c')
        self.out(f'/* end of generated C code {self.sink} */')
