def header_pre_runtime(is_mcstas, source, runtime: dict, config: dict, typedefs: list, uservars: list):
    from datetime import datetime

    def jump_line(instance, jump):
        return f'long Jump_{instance.name}_{jump}; /* the JUMP connection <from>_<to> */'

    jump_string = '\n'.join([jump_line(i, j) for i in source.components for j in i.jump if j.iterate])

    if is_mcstas:
        particle_struct = '\n'.join([
            "  double vx,vy,vz; /* velocity [m/s] */",
            "  double sx,sy,sz; /* spin [0-1] */",
            "  int mcgravitation; /* gravity-state */",
            "  void *mcMagnet;    /* precession-state */",
            "  int allow_backprop; /* allow backprop */"])
    else:
        particle_struct = '\n'.join([
            "  double kx,ky,kz; /* wave-vector */",
            "  double phi, Ex,Ey,Ez; /* phase and electrical field */"])

    # Append variables from instr USERVARS block to particle struct
    # Also store these strings in the appropriate instrument list for later def/undef as state variables

    uservar_string = '//user variables and comp - injections:\n' if len(uservars) else ''
    uservar_string += '\n'.join([f'  {x.type} {x.name};' for x in uservars])

    # Shouldn't we exclude array-valued names here?
    getvar = '\n'.join([f'  if(!str_comp("{x.name}",name)){{rval=*((double*)(&(p->{x.name})));s=0;}}' for x in uservars])

    # Array valued names seem OK here, since a user can type-cast correctly
    getvar_void = '\n'.join(
        [f'  if (!str_comp("{x.name}", name)){{rval=(void * ) & (p->{x.name});s=0;}}' for x in uservars])

    # For non-array values we can safely use memcpy (probably)
    setvar_void = '\n'.join(
        [f'  if(!str_comp("{x.name}",name)){{memcpy(&(p->{x.name}), value, sizeof({x.type})); rval=0;}}'
         for x in uservars if not x.is_array and not x.is_pointer])

    # an array -- need to know how many elements we're copying
    setvar_void_array = '\n'.join(
        [f'  if(!str_comp("{x.name}",name)){{memcpy(&(p->{x.name}), value, elements * sizeof({x.type})); rval=0;}}'
         for x in uservars if x.is_array or x.is_pointer])

    getuservar_byid = '\n'.join(
        [f'  case {i}: {{rval=*( (double *)(&(p->{x.name})) ); s=0; break;}}' for i, x in enumerate(uservars)])

    uservar_init = ''
    for x in uservars:
        if (x.type not in ('double', 'MCNUM', 'int') and x.init is None) or x.is_pointer or x.is_array:
            array_str = ' array' if x.is_pointer or x.is_array else ''
            print(f'\nWARNING:\n --> USERVAR {x.name} is of type {x.type}{array_str}')
            print('  --> and may need specific per-particle initialization through an EXTEND block!\n')
        else:
            uservar_init += f'\np->{x.name}={0 if x.init is None else x.init};'

    contents = f"""/* Automatically generated file. Do not edit.
 * Format:     ANSI C source code
 * Creator:    {runtime.get("fancy")} <{runtime.get("url")}>
 * Instrument: {source.source} ({source.name})
 * Date: {datetime.now()}
 * File: {config.get('output')}
 * CFLAGS={' '.join(set(source.flags))}
 */
 
#define MCCODE_STRING "{runtime.get("fancy")}"
#define FLAVOR "{runtime.get("name", "none")}"
#define FLAVOR_UPPER "{runtime.get("name", "none").upper()}"
{'#define MC_USE_DEFAULT_MAIN' if config.get('default_main') else ''}
{'#define MC_TRACE_ENABLED' if config.get('enable_trace') else ''}
{'#define MC_PORTABLE' if config.get('portable') else ''}

#include <string.h>

typedef double MCNUM;
typedef struct {{MCNUM x, y, z;}} Coords;
typedef MCNUM Rotation[3][3];
#define MCCODE_BASE_TYPES

#ifndef MC_NUSERVAR
#define MC_NUSERVAR 10
#endif

/* Particle JUMP control logic */
struct particle_logic_struct {{
  int dummy;{jump_string}
}};
struct _struct_particle {{
  double x,y,z; /* position [m] */
{particle_struct}
  unsigned long randstate[7];
  double t, p;    /* time, event weight */
  long long _uid;  /* event ID */
  long _index;     /* component index where to send this event */
  long _absorbed;  /* flag set to TRUE when this event is to be removed/ignored */
  long _scattered; /* flag set to TRUE when this event has interacted with the last component instance */
  long _restore;   /* set to true if neutron event must be restored */
  long flag_nocoordschange;   /* set to true if particle is jumping */
  struct particle_logic_struct _logic;
  {uservar_string}
}};
typedef struct _struct_particle _class_particle;

_class_particle _particle_global_randnbuse_var;
_class_particle* _particle = &_particle_global_randnbuse_var;

// Below lines relating to mcgenstate / setstate are in principle McStas - centric, we ought to generate
//this function based on "project"
#pragma acc routine
_class_particle mcgenstate(void);
#pragma acc routine
_class_particle mcsetstate(double x, double y, double z, double vx, double vy, double vz,
    double t, double sx, double sy, double sz, double p, int mcgravitation, void *mcMagnet, int mcallowbackprop);

extern int mcgravitation;      /* flag to enable gravitation */
#pragma acc declare create ( mcgravitation )
int mcallowbackprop;        
#pragma acc declare create ( mcallowbackprop )

_class_particle mcgenstate(void) {{
  _class_particle particle = mcsetstate(0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, mcgravitation, NULL, mcallowbackprop);
  return(particle);
}}
/*Generated user variable handlers:*/

#pragma acc routine
double particle_getvar(_class_particle *p, char *name, int *suc);

#ifdef OPENACC
#pragma acc routine
int str_comp(char *str1, char *str2);
#endif

double particle_getvar(_class_particle *p, char *name, int *suc){{
#ifndef OPENACC
#define str_comp strcmp
#endif
  int s=1;
  double rval=0;
  if(!str_comp("x",name)){{rval=p->x;s=0;}}
  if(!str_comp("y",name)){{rval=p->y;s=0;}}
  if(!str_comp("z",name)){{rval=p->z;s=0;}}
  if(!str_comp("vx",name)){{rval=p->vx;s=0;}}
  if(!str_comp("vy",name)){{rval=p->vy;s=0;}}
  if(!str_comp("vz",name)){{rval=p->vz;s=0;}}
  if(!str_comp("sx",name)){{rval=p->sx;s=0;}}
  if(!str_comp("sy",name)){{rval=p->sy;s=0;}}
  if(!str_comp("sz",name)){{rval=p->sz;s=0;}}
  if(!str_comp("t",name)){{rval=p->t;s=0;}}
  if(!str_comp("p",name)){{rval=p->p;s=0;}}
{getvar}  
  if (suc!=0x0) {{*suc=s;}}
  return rval;
}}

#pragma acc routine
void* particle_getvar_void(_class_particle *p, char *name, int *suc);\n
#ifdef OPENACC
#pragma acc routine
int str_comp(char *str1, char *str2);
#endif

void* particle_getvar_void(_class_particle *p, char *name, int *suc){{
#ifndef OPENACC
#define str_comp strcmp
#endif
  int s=1;
  void* rval=0;
  if(!str_comp("x",name)) {{rval=(void*)&(p->x); s=0;}}
  if(!str_comp("y",name)) {{rval=(void*)&(p->y); s=0;}}
  if(!str_comp("z",name)) {{rval=(void*)&(p->z); s=0;}}
  if(!str_comp("vx",name)){{rval=(void*)&(p->vx);s=0;}}
  if(!str_comp("vy",name)){{rval=(void*)&(p->vy);s=0;}}
  if(!str_comp("vz",name)){{rval=(void*)&(p->vz);s=0;}}
  if(!str_comp("sx",name)){{rval=(void*)&(p->sx);s=0;}}
  if(!str_comp("sy",name)){{rval=(void*)&(p->sy);s=0;}}
  if(!str_comp("sz",name)){{rval=(void*)&(p->sz);s=0;}}
  if(!str_comp("t",name)) {{rval=(void*)&(p->t); s=0;}}
  if(!str_comp("p",name)) {{rval=(void*)&(p->p); s=0;}}
{getvar_void}
  if (suc!=0x0) {{*suc=s;}}
  return rval;
}}

#pragma acc routine
int particle_setvar_void(_class_particle *, char *, void*);\n
int particle_setvar_void(_class_particle *p, char *name, void* value){{
#ifndef OPENACC
#define str_comp strcmp
#endif
  int rval=1;
  if(!str_comp("x",name)) {{memcpy(&(p->x),  value, sizeof(double)); rval=0;}}
  if(!str_comp("y",name)) {{memcpy(&(p->y),  value, sizeof(double)); rval=0;}}
  if(!str_comp("z",name)) {{memcpy(&(p->z),  value, sizeof(double)); rval=0;}}
  if(!str_comp("vx",name)){{memcpy(&(p->vx), value, sizeof(double)); rval=0;}}
  if(!str_comp("vy",name)){{memcpy(&(p->vy), value, sizeof(double)); rval=0;}}
  if(!str_comp("vz",name)){{memcpy(&(p->vz), value, sizeof(double)); rval=0;}}
  if(!str_comp("sx",name)){{memcpy(&(p->sx), value, sizeof(double)); rval=0;}}
  if(!str_comp("sy",name)){{memcpy(&(p->sy), value, sizeof(double)); rval=0;}}
  if(!str_comp("sz",name)){{memcpy(&(p->sz), value, sizeof(double)); rval=0;}}
  if(!str_comp("p",name)) {{memcpy(&(p->p),  value, sizeof(double)); rval=0;}}
  if(!str_comp("t",name)) {{memcpy(&(p->t),  value, sizeof(double)); rval=0;}}
{setvar_void}  
  return rval;
}}

#pragma acc routine
int particle_setvar_void_array(_class_particle *, char *, void*, int);

int particle_setvar_void_array(_class_particle *p, char *name, void* value, int elements){{
#ifndef OPENACC
#define str_comp strcmp
#endif
  int rval=1;
{setvar_void_array}
  return rval;
}}

// Function to handle a particle restore of physical particle params
#pragma acc routine
void particle_restore(_class_particle *p, _class_particle *p0);
void particle_restore(_class_particle *p, _class_particle *p0) {{
  p->x  = p0->x;  p->y  = p0->y;  p->z  = p0->z;
  p->vx = p0->vx; p->vy = p0->vy; p->vz = p0->vz;
  p->sx = p0->sx; p->sy = p0->sy; p->sz = p0->sz;
  p->t = p0->t;  p->p  = p0->p;
  p->_absorbed=0; p->_restore=0;
}}

#pragma acc routine
double particle_getuservar_byid(_class_particle *p, int id, int *suc){{
  int s=1;
  double rval=0;
  switch(id){{
{getuservar_byid}
  }}
  if (suc!=0x0) {{*suc=s;}}
  return rval;
}}

#pragma acc routine
void particle_uservar_init(_class_particle *p){{
{uservar_init}
}}
"""
    return contents


def header_post_runtime(source, runtime: dict, config: dict, include_path):
    from ..common.utilities import escape_str_for_c

    def source_file_contents():
        from pathlib import Path
        from os import access, R_OK
        if source.source is None and config.get('embed_instrument_file'):
            raise RuntimeError('Requested source embedding, but no source file provided!')
        elif source.source is None:
            return 'Instrument source code is not embedded in this executable.'
        path = Path(source.source)
        if config.get('embed_instrument_file') and path.exists() and access(path, R_OK):
            with path.open('r') as file:
                return escape_str_for_c(file.read())
        message = f"Instrument {source.name} source code "
        message += f"from {escape_str_for_c(source.source)} is not embedded in this executable.\\n"
        message += f"Use --source option when running {config.get('flavor')}"
        return message

    main_file_string = 'int main(int argc, char *argv[]){return mccode_main(argc, argv);}'
    contents = f"""
/* *****************************************************************************
 * Start of instrument '{source.name}' generated code
***************************************************************************** */

#ifdef MC_TRACE_ENABLED
int traceenabled = 1;
#else
int traceenabled = 0;
#endif
#define {runtime.get("name", "none").upper()} "{escape_str_for_c(str(include_path))}"
int   defaultmain         = {1 if config.get("default_main") else 0};
char  instrument_name[]   = "{source.name}";
char  instrument_source[] = "{escape_str_for_c(source.source)}";
char *instrument_exe      = NULL; /* will be set to argv[0] in main */
char instrument_code[] = "{source_file_contents()}";
{main_file_string if config.get('default_main') else ''}
"""
    return contents
