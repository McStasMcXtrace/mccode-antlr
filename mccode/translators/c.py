"""Translates a McComp instrument from its intermediate form to a C runtime source file."""
from io import StringIO
from ..instr import Instr, Instance
from .target import TargetVisitor


class CTargetVisitor(TargetVisitor):
    def visit_header(self):
        """ McCode-3 Comment (cogen.c.in line 2213)
        Output code for the mcstas runtime system. Default is to copy the runtime
        code into the generated executable, to minimize problems with finding the
        right files during compilation and linking, but this may be changed using
        the --no-runtime compiler switch.
        """
        from datetime import datetime

        print('cogen_header(instr, output_name);')
        self.out('/* Automatically generated file. Do not edit. ')
        self.out(' * Format:     ANSI C source code')
        self.out(f' * Creator:    {self.runtime.get("fancy")} <{self.runtime.get("url")}>')
        self.out(f' * Instrument: {self.source.source} ({self.source.name})')
        self.out(f' * Date: {datetime.now()}')
        self.out(f' * File: {self.sink}')
        self.out(f' * CFLAGS={self.source.dependency}\n */\n')

        self.out(f'#define MCCODE_STRING "{self.runtime.get("fancy")}')
        self.out(f'#define FLAVOR "{self.runtime.get("name", "none")}"')
        self.out(f'#define FLAVOR_UPPER "{self.runtime.get("name", "none").upper()}"\n')



    def visit_declare(self):
        self.warnings += 0
        print('warnings += cogen_decls(instr);')

    def visit_initialize(self):
        print('warnings += cogen_section(instr, "INITIALISE", "init", instr->inits);')

    def enter_instance(self, instance: Instance):
        # replacing: warnings += cogen_trace_functions(instr);
        pass

    def leave_instance(self, instance: Instance):
        # replacing: undef_trace_section(instr);
        pass

    def visit_component(self, instance: Instance):
        pass

    def enter_uservars(self):
        print('def_uservars(instr);')

    def leave_uservars(self):
        print('undef_uservars(instr);')

    def visit_raytrace(self):
        print('warnings += cogen_raytrace(instr);')

    def visit_raytrace_funnel(self):
        print('warnings += cogen_rt_funnel(instr);')

    def visit_save(self):
        print('warnings += cogen_section(instr, "SAVE", "save", instr->saves);')

    def visit_finally(self):
        print('warnings += cogen_section(instr, "FINALLY", "finally", instr->finals);')

    def visit_display(self):
        print('warnings += cogen_section(instr, "DISPLAY", "display", NULL);')

    def visit_macros(self):
        print('cogen_getvarpars_fct(instr);')
        print('cogen_getparticlevar_fct(instr);')
        print('cogen_getcompindex_fct(instr);')
        print('embed_file("literals-r.c");')  # used to query and display instrument/component-defined literal strings
        print('embed_file("mccode_main.c");')



