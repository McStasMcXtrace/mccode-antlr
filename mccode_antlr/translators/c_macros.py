def cogen_getvarpars_fct(instr):
    lines = [
        "void* _getvar_parameters(char* compname)",
        "/* enables settings parameters based use of the GETPAR macro */",
        "{",
        "  #ifdef OPENACC",
        "    #define strcmp(a,b) str_comp(a,b)",
        "  #endif",
    ]
    for comp in instr.components:
        lines.append(f'  if (!strcmp(compname, "{comp.name}")) return (void *) &(_{comp.name}_var._parameters);')

    lines.extend([
        '  return 0;',
        '}',
        ''
    ])
    return '\n'.join(lines)


def cogen_getparticlevar_fct(uservars):
    lines = [
        "void* _get_particle_var(char *token, _class_particle *p)",
        "/* enables setpars based use of GET_PARTICLE_DVAR macro and similar */",
        "{",
    ]
    for var in uservars:
        lines.append(f'  if (!strcmp(token, "{var.name}")) return (void *) &(p->{var.name});')

    lines.extend([
        "  return 0;",
        "}",
        "",
    ])
    return '\n'.join(lines)


def cogen_getcompindex_fct(instr):
    lines = [
        "long _getcomp_index(char* compname)",
        "/* Enables retrieving the component position & rotation when the index is not known.",
        " * Component indexing into MACROS, e.g., POS_A_COMP_INDEX, are 1-based! */",
        "{",
    ]
    for index, comp in enumerate(instr.components):
        lines.append(f'  if (!strcmp(compname, "{comp.name}")) return {1+index};')

    lines.extend([
        "  return -1;",
        "}",
        "",
    ])
    return '\n'.join(lines)
