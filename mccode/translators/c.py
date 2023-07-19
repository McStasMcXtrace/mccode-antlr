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

        print('cogen_header(instr, output_name)')
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

        if self.config.get('default_main'):
            self.out('#define MC_USE_DEFAULT_MAIN')
        if self.config.get('enable_trace'):
            self.out('#define MC_TRACE_ENABLED')
        if self.config.get('portable'):
            self.out('#define MC_PORTABLE')

        self.out('\n#include <string.h>\n')
        self.out("typedef double MCNUM;")
        self.out("typedef struct {MCNUM x, y, z;} Coords;")
        self.out("typedef MCNUM Rotation[3][3];")
        self.out("#define MCCODE_BASE_TYPES\n")
        self.out("#ifndef MC_NUSERVAR")
        self.out("#define MC_NUSERVAR 10")
        self.out("#endif\n")

        self.out('/* Particle JUMP control logic */')
        self.out('struct particle_logic_struct {')
        self.out('  int dummy;')
        for inst in self.source.components:
            for jump in inst.jump:
                if jump.iterate:
                    self.out(f'  long Jump_{inst.name}_{jump.target}; /* the JUMP connection <from>_<to> */')
        self.out('};\n')

        self.out("struct _struct_particle {")
        self.out("  double x,y,z; /* position [m] */")
        if self.runtime.get('project') == 1:
            # if MCCODE_PROJECT == 1   /* neutron */
            self.out("  double vx,vy,vz; /* velocity [m/s] */")
            self.out("  double sx,sy,sz; /* spin [0-1] */")
            self.out("  int mcgravitation; /* gravity-state */")
            self.out("  void *mcMagnet;    /* precession-state */")
            self.out("  int allow_backprop; /* allow backprop */")
        elif self.runtime.get('project') == 2:
            # elif MCCODE_PROJECT == 2 /* xray */
            self.out("  double kx,ky,kz; /* wave-vector */")
            self.out("  double phi, Ex,Ey,Ez; /* phase and electrical field */")
        # self.out("  randstate_t randstate[RANDSTATE_LEN]")
        self.out("  unsigned long randstate[7];")  # for the KISS generator
        self.out("  double t, p;    /* time, event weight */")
        self.out("  long long _uid;  /* event ID */")
        self.out("  long _index;     /* component index where to send this event */")
        # these are needed for SCATTERED, ABSORB and RESTORE macros
        self.out("  long _absorbed;  /* flag set to TRUE when this event is to be removed/ignored */")
        self.out(
            "  long _scattered; /* flag set to TRUE when this event has interacted with the last component instance */")
        self.out("  long _restore;   /* set to true if neutron event must be restored */")
        self.out("  long flag_nocoordschange;   /* set to true if particle is jumping */")

        # Include the struct defined earlier holding information on JUMP logic
        self.out("  struct particle_logic_struct _logic;")
        # Append variables from instr USERVARS block to particle struct
        # Also store these strings in the appropriate instrument list for later def/undef as state variables

        # TODO Pick up from cogenc line 2343, using the now-defined self.uservars instead of instr->user_vars
        # Figure out what `get_codeblock_vars` does.


    def visit_declare(self):
        self.warnings += 0
        print('warnings += cogen_decls(instr)')

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



