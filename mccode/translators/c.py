"""Translates a McComp instrument from its intermediate form to a C runtime source file."""
from ..instr import Instr, Instance
from .target import TargetVisitor
from .c_listener import extract_c_declared_variables
from ..common.utilities import escape_str_for_c

class CTargetVisitor(TargetVisitor):
    target_language = 'c'

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
        self.typedefs = list(typedefs)

    def __post_init__(self):
        """Before doing *anything* else. We need to search through all raw C code for %include statements.
        This could not be done earlier if the goal is to have a clear separation between the parsing and target
        languages. (A different target language would not include the same libraries in its raw blocks)
        """
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


    def visit_header(self):
        from .c_header import header_pre_runtime, header_post_runtime
        print('cogen_header(instr, output_name)')

        is_mcstas = self.runtime.get('project') == 1
        if not is_mcstas and self.runtime.get('project') != 2:
            print(f'Unknown runtime for project index {self.runtime.get("project")}')

        self.out(header_pre_runtime(is_mcstas, self.source, self.runtime, self.config, self.typedefs))
        # runtime part
        if self.config.get('include_runtime'):
            self.out('#define MC_EMBEDDED_RUNTIME')
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
        print('warnings += cogen_decls(instr)')
        contents, warnings = declarations_pre_libraries(self.source, self.typedefs)
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
        self.out('#undef compcurname\n#undef compcurtype\n#undef compcurindex')
        self.out(f"/* end of instrument '{self.source.name}' and components DECLARE */")

        self.warnings += warnings

    def visit_initialize(self):
        print('warnings += cogen_section(instr, "INITIALISE", "init", instr->inits)')

    def enter_instance(self, instance: Instance):
        # replacing: warnings += cogen_trace_functions(instr)
        pass

    def leave_instance(self, instance: Instance):
        # replacing: undef_trace_section(instr)
        pass

    def visit_component(self, instance: Instance):
        pass

    def enter_uservars(self):
        print('def_uservars(instr)')

    def leave_uservars(self):
        print('undef_uservars(instr)')

    def visit_raytrace(self):
        print('warnings += cogen_raytrace(instr)')

    def visit_raytrace_funnel(self):
        print('warnings += cogen_rt_funnel(instr)')

    def visit_save(self):
        print('warnings += cogen_section(instr, "SAVE", "save", instr->saves)')

    def visit_finally(self):
        print('warnings += cogen_section(instr, "FINALLY", "finally", instr->finals)')

    def visit_display(self):
        print('warnings += cogen_section(instr, "DISPLAY", "display", NULL)')

    def visit_macros(self):
        print('cogen_getvarpars_fct(instr)')
        print('cogen_getparticlevar_fct(instr)')
        print('cogen_getcompindex_fct(instr)')
        print('embed_file("literals-r.c")')  # used to query and display instrument/component-defined literal strings
        print('embed_file("mccode_main.c")')



