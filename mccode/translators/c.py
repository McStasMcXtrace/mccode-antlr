"""Translates a McComp instrument from its intermediate form to a C runtime source file."""
import os
from io import StringIO
from pathlib import Path
from ..instr import Instr, Instance
from .target import TargetVisitor
from .c_listener import extract_c_declared_variables
from ..common.utilities import escape_str_for_c


class CTargetVisitor(TargetVisitor):
    target_language = 'c'

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

        # Use an ANTLR4 lexer/parser/listener to extract all validly-declared variables
        # If there are user-declared types, they will not be identified at this point ...
        # FIXME?
        def extract_declares(name, raw_c_obj):
            decs = extract_c_declared_variables(raw_c_obj.source)
            n = sum(init is not None for c, init in decs.values())
            if n:
                print(f'Warning USERVARS block from {name} contains {n} assignments (= sign).')
                print('        Move them to an EXTEND section. May fail at compile')
            return decs

        declares = dict()  # will be {variable_name: (variable_type, [init_value|None])}
        for raw_user_vars_c_block in self.source.user:
            declares.update(extract_declares(self.source.name, raw_user_vars_c_block))
        # Look for USERVAR section(s) in the set of component definitions too:
        for component in self.source.component_types():
            for raw_user_vars_c_block in component.user:
                declares.update(extract_declares(component.name, raw_user_vars_c_block))

        # translate the dictionary to a new one, which indicates if a named variable is an array
        strip_array = str.maketrans('', '', '*[]')
        stripped = {n.translate(strip_array).strip(): (c_type, '*[]' in n) for n, (c_type, _) in declares.items()}

        if len(declares):
            self.out('  // user variables and comp-injections:')
        for name, (c_type, val) in declares.items():
            self.out(f'  {c_type} {name};')
        self.out('};')
        self.out("typedef struct _struct_particle _class_particle;\n")

        self.out("_class_particle _particle_global_randnbuse_var;")
        self.out("_class_particle* _particle = &_particle_global_randnbuse_var;\n")
        
        # Below lines relating to mcgenstate / setstate are in principle McStas - centric, we ought to generate
        # this function based on "project"
        self.out("#pragma acc routine")
        self.out("_class_particle mcgenstate(void);")
        self.out("#pragma acc routine")
        self.out("_class_particle mcsetstate(double x, double y, double z, double vx, double vy, double vz,")
        self.out("			   double t, double sx, double sy, double sz, double p, int mcgravitation, void *mcMagnet, int mcallowbackprop);")
        self.out("")
        self.out("extern int mcgravitation;      /* flag to enable gravitation */")
        self.out("#pragma acc declare create ( mcgravitation )")
        self.out("int mcallowbackprop;        ")
        self.out("#pragma acc declare create ( mcallowbackprop )")

        self.out("")
        self.out("_class_particle mcgenstate(void) {")
        self.out("  _class_particle particle = mcsetstate(0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, mcgravitation, NULL, mcallowbackprop);")
        self.out("  return(particle);")
        self.out("}")

        # generate uservar return functions
        self.out("/*Generated user variable handlers:*/\n")
        self.out("#pragma acc routine")
        self.out("double particle_getvar(_class_particle *p, char *name, int *suc);\n")
        self.out("#ifdef OPENACC")
        self.out("#pragma acc routine")
        self.out("int str_comp(char *str1, char *str2);")
        self.out("#endif\n")
        self.out("double particle_getvar(_class_particle *p, char *name, int *suc){")
        self.out("#ifndef OPENACC")
        self.out("#define str_comp strcmp")
        self.out("#endif")
        self.out("  int s=1;")
        self.out("  double rval=0;")
        self.out('  if(!str_comp("x",name)){rval=p->x;s=0;}')
        self.out('  if(!str_comp("y",name)){rval=p->y;s=0;}')
        self.out('  if(!str_comp("z",name)){rval=p->z;s=0;}')
        self.out('  if(!str_comp("vx",name)){rval=p->vx;s=0;}')
        self.out('  if(!str_comp("vy",name)){rval=p->vy;s=0;}')
        self.out('  if(!str_comp("vz",name)){rval=p->vz;s=0;}')
        self.out('  if(!str_comp("sx",name)){rval=p->sx;s=0;}')
        self.out('  if(!str_comp("sy",name)){rval=p->sy;s=0;}')
        self.out('  if(!str_comp("sz",name)){rval=p->sz;s=0;}')
        self.out('  if(!str_comp("t",name)){rval=p->t;s=0;}')
        self.out('  if(!str_comp("p",name)){rval=p->p;s=0;}')
        for name in stripped:
            # Shouldn't we exclude array-valued names here?
            self.out(f'  if(!str_comp("{name}",name)){{rval=*( (double *)(&(p->{name})) );s=0;}}')
        self.out("  if (suc!=0x0) {*suc=s;}")
        self.out("  return rval;")
        self.out("}\n")

        self.out("#pragma acc routine")
        self.out("void* particle_getvar_void(_class_particle *p, char *name, int *suc);\n")
        self.out("#ifdef OPENACC")
        self.out("#pragma acc routine")
        self.out("int str_comp(char *str1, char *str2);")
        self.out("#endif\n")
        self.out("void* particle_getvar_void(_class_particle *p, char *name, int *suc){")
        self.out("#ifndef OPENACC")
        self.out("#define str_comp strcmp")
        self.out("#endif")
        self.out("  int s=1;")
        self.out("  void* rval=0;")
        self.out("  if(!str_comp(\"x\",name)) {rval=(void*)&(p->x); s=0;}")
        self.out("  if(!str_comp(\"y\",name)) {rval=(void*)&(p->y); s=0;}")
        self.out("  if(!str_comp(\"z\",name)) {rval=(void*)&(p->z); s=0;}")
        self.out("  if(!str_comp(\"vx\",name)){rval=(void*)&(p->vx);s=0;}")
        self.out("  if(!str_comp(\"vy\",name)){rval=(void*)&(p->vy);s=0;}")
        self.out("  if(!str_comp(\"vz\",name)){rval=(void*)&(p->vz);s=0;}")
        self.out("  if(!str_comp(\"sx\",name)){rval=(void*)&(p->sx);s=0;}")
        self.out("  if(!str_comp(\"sy\",name)){rval=(void*)&(p->sy);s=0;}")
        self.out("  if(!str_comp(\"sz\",name)){rval=(void*)&(p->sz);s=0;}")
        self.out("  if(!str_comp(\"t\",name)) {rval=(void*)&(p->t); s=0;}")
        self.out("  if(!str_comp(\"p\",name)) {rval=(void*)&(p->p); s=0;}")
        for name in stripped:
            # Array valued names seem OK here, since a user can type-cast correctly
            self.out(f'  if(!str_comp("{name}",name)){{rval=(void*)&(p->{name});s=0;}}')
        self.out("  if (suc!=0x0) {*suc=s;}")
        self.out("  return rval;")
        self.out("}\n")

        self.out("#pragma acc routine")
        self.out("int particle_setvar_void(_class_particle *, char *, void*);\n")
        self.out("int particle_setvar_void(_class_particle *p, char *name, void* value){")
        self.out("#ifndef OPENACC")
        self.out("#define str_comp strcmp")
        self.out("#endif")
        self.out("  int rval=1;")
        self.out("  if(!str_comp(\"x\",name)) {memcpy(&(p->x),  value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"y\",name)) {memcpy(&(p->y),  value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"z\",name)) {memcpy(&(p->z),  value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"vx\",name)){memcpy(&(p->vx), value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"vy\",name)){memcpy(&(p->vy), value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"vz\",name)){memcpy(&(p->vz), value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"sx\",name)){memcpy(&(p->sx), value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"sy\",name)){memcpy(&(p->sy), value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"sz\",name)){memcpy(&(p->sz), value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"p\",name)) {memcpy(&(p->p),  value, sizeof(double)); rval=0;}")
        self.out("  if(!str_comp(\"t\",name)) {memcpy(&(p->t),  value, sizeof(double)); rval=0;}")
        for name, (c_type, is_array) in stripped.items():
            if not is_array:
                # Not an array -- we should be able ot use memcopy freely
                self.out(f'  if(!str_comp("{name}",name)){{memcpy(&(p->{name}), value, sizeof({c_type})); rval=0;}}')
        self.out("  return rval;")
        self.out("}\n")

        self.out("#pragma acc routine")
        self.out("int particle_setvar_void_array(_class_particle *, char *, void*, int);")
        self.out("")
        self.out("int particle_setvar_void_array(_class_particle *p, char *name, void* value, int elements){")
        self.out("#ifndef OPENACC")
        self.out("#define str_comp strcmp")
        self.out("#endif")
        self.out("  int rval=1;")
        for name, (c_type, is_array) in stripped.items():
            if is_array:
                # an array -- need to know how many elements we're copying
                self.out(f'  if(!str_comp("{name}",name)){{memcpy(&(p->{name}), value, elements * sizeof({c_type})); rval=0;}}')
        self.out("  return rval;")
        self.out("}\n")
        
        # Function to handle a particle restore of physical particle params
        # FIXME Why not define this in a static C file?
        self.out("#pragma acc routine")
        self.out("void particle_restore(_class_particle *p, _class_particle *p0);\n")
        self.out("void particle_restore(_class_particle *p, _class_particle *p0) {")
        self.out("  p->x  = p0->x;  p->y  = p0->y;  p->z  = p0->z;")
        self.out("  p->vx = p0->vx; p->vy = p0->vy; p->vz = p0->vz;")
        self.out("  p->sx = p0->sx; p->sy = p0->sy; p->sz = p0->sz;")
        self.out("  p->t = p0->t;  p->p  = p0->p;")
        self.out("  p->_absorbed=0; p->_restore=0;")
        self.out("}\n")

        self.out("#pragma acc routine")
        self.out("double particle_getuservar_byid(_class_particle *p, int id, int *suc){")
        self.out("  int s=1;")
        self.out("  double rval=0;")
        self.out("  switch(id){")
        for i, name in enumerate(stripped):
            self.out(f"  case {i}: {{rval=*( (double *)(&(p->{name})) ); s=0; break;}}")
        self.out("  }")
        self.out("  if (suc!=0x0) {*suc=s;}")
        self.out("  return rval;")
        self.out("}")
        self.out("")

        self.out("#pragma acc routine")
        self.out("void particle_uservar_init(_class_particle *p){")
        for name, (c_type, init_value) in declares.items():
            if stripped[name][1] or (c_type not in ("double", "MCNUM", "int") and init_value is None):
                print(f'\nWARNING:\n  --> USERVAR {name} is of type {c_type}{" array" if stripped[name][1] else ""}')
                print('  --> and may need specific per-particle initialization through an EXTEND block!\n')
            else:
                self.out(f'  p->{name}={0 if init_value is None else init_value};')
        self.out('}\n')

        if self.config.get('include_runtime'):
            self.out('#define MC_EMBEDDED_RUNTIME')
            self.embed_file("mccode-r.h")
            if self.runtime.get('project') == 1:
                self.embed_file('mcstas-r.h')
            elif self.runtime.get('project') == 2:
                self.embed_file('mcxtrace-r.h')
            if self.verbose:
                print(f"Compile '{self.sink} -DUSE_NEXUS -lNeXus' to enable NeXus support")
            self.embed_file("mccode-r.c")
            if self.runtime.get('project') == 1:
                self.embed_file('mcstas-r.c')
            elif self.runtime.get('project') == 2:
                self.embed_file('mcxtrace-r.c')
        else:
            # This only works if the module is *not* a compressed archive
            # If it is, we would need to do some trickery to ... write out the
            self.out(f'#include "{self.include_path("mcode-r.h")}"')
            print('Dependency: mccode-r.o')
            runtime_name = 'mcstas-r' if self.runtime.get('project') != 2 else 'mcxtrace-r.h'
            self.out(f'# include "{self.include_path(runtime_name+".h")}"')
            print(f'Dependency: {runtime_name}.o')

        self.out('\n/* *****************************************************************************')
        self.out(f' * Start of instrument {self.source.name} generated code')
        self.out('***************************************************************************** */\n')

        self.out("#ifdef MC_TRACE_ENABLED")
        self.out("int traceenabled = 1;")
        self.out("#else")
        self.out("int traceenabled = 0;")
        self.out("#endif")
        self.out(f'#define {self.runtime.get("name","none").upper()} "{self.include_path()}"')

        self.out(f'int   defaultmain         = {1 if self.config.get("default_main") else 0};')
        self.out(f'char  instrument_name[]   = "{self.source.name}";')
        self.out(f'char  instrument_source[] = "{escape_str_for_c(self.source.source)}";')
        self.out(f'char *instrument_exe      = NULL; /* will be set to argv[0] in main */')

        f = Path(self.source.source)
        if self.config.get('embed_instrument_file') and f.exists() and os.access(f, os.R_OK) :
            with f.open('r') as file:
                self.out(f'char instrument_code[] = "{escape_str_for_c(file.read())}";\n')
        else:
            self.out(f'char instrument_code[] = '
                     f'"Instrument {self.source.name} source code from {escape_str_for_c(self.source.source)}'
                     f' is not embedded in this executable.\n'
                     f' Use --source option when running {self.config.get("fancy", "none")}.";')

        if self.config.get('use_default_main'):
            self.out('int main(int argc, char *argv[]){return mccode_main(argc, argv);}')



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



