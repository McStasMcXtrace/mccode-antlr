def _runtime_parameters(is_mcstas):
    pars = ['x', 'y', 'z']
    if is_mcstas:
        pars.extend(['vx', 'vy', 'vz', 't', 'sx', 'sy', 'sz', 'p', 'mcgravitation', 'mcMagnet', 'allow_backprop'])
    else:
        pars.extend(['kx', 'ky', 'kz', 'phi', 't', 'Ex', 'Ey', 'Ez', 'p'])
    return pars


def _runtime_kv_parameters(is_mcstas):
    pars = ['p', 't']
    pars.extend(['vx', 'vy', 'vz'] if is_mcstas else ['kx', 'ky', 'kz'])
    pars.extend(['x', 'y', 'z'])
    return pars


def def_trace_section(is_mcstas):
    lines = [
        "/*******************************************************************************",
        "* components TRACE",
        "*******************************************************************************/"
    ]
    lines.extend([f'#define {x} (_particle->{x})' for x in _runtime_parameters(is_mcstas)])
    lines.extend([
        "/* if on GPU, globally nullify sprintf,fprintf,printfs   */",
        "/* (Similar defines are available in each comp trace but */",
        "/*  those are not enough to handle external libs etc. )  */",
        "#ifdef OPENACC",
        "#ifndef MULTICORE",
        "#define fprintf(stderr,...) printf(__VA_ARGS__)",
        "#define sprintf(string,...) printf(__VA_ARGS__)",
        "#define exit(...) noprintf()",
        "#define strcmp(a,b) str_comp(a,b)",
        "#define strlen(a) str_len(a)",
        "#endif",
        "#endif",
        # /* define SCATTERED, ABSORB and RESTORE macros for all TRACE */"
        "#define SCATTERED (_particle->_scattered)",
        "#define RESTORE (_particle->_restore)",
        "#define ABSORBED (_particle->_absorbed)",
        "#define RESTORE_NEUTRON(_index, ...) _particle->_restore = _index;",
        # /* define mcget_run_num within trace scope to refer to the particle */
        "#define mcget_run_num() _particle->_uid",
        "#define ABSORB0 do { DEBUG_STATE(); DEBUG_ABSORB(); MAGNET_OFF; ABSORBED++; return(_comp); } while(0)",
        "#define ABSORB ABSORB0"
    ])
    return '\n'.join(lines)


def undef_trace_section(is_mcstas):
    lines = [f'#undef {x}' for x in _runtime_parameters(is_mcstas)]
    lines.extend([
        "#ifdef OPENACC",
        "#ifndef MULTICORE",
        "#undef strlen",
        "#undef strcmp",
        "#undef exit",
        "#undef printf",
        "#undef sprintf",
        "#undef fprintf",
        "#endif",
        "#endif",
        "#undef SCATTERED",
        "#undef RESTORE",
        "#undef RESTORE_NEUTRON",
        "#undef STORE_NEUTRON",
        "#undef ABSORBED",
        "#undef ABSORB",
        "#undef ABSORB0",
    ])
    return '\n'.join(lines)


def cogen_trace_section(is_mcstas, source, declared_parameters, instrument_uservars, component_uservars):
    return '\n'.join([
        cogen_comp_trace_class(is_mcstas, c, source, declared_parameters[c.name],
                               instrument_uservars, component_uservars[c.name]) for c in source.component_types()
    ])


def cogen_comp_trace_class(is_mcstas, comp, source, declared_parameters, instr_uservars, comp_uservars):
    from .c_defines import cogen_parameter_define, cogen_parameter_undef
    # count matching component type instances which define an EXTEND block:
    extended = [(n, i) for n, i in enumerate(source.components) if i.type.name == comp.name and len(i.extend)]

    if len(extended) == 0 and all(x.is_empty for x in comp.trace):
        return ''

    lines = [
        '#pragma acc routine',
        f'_class_{comp.name} *class_{comp.name}_trace(_class_{comp.name} *_comp, _class_particle *_particle) {{',
        'ABSORBED=SCATTERED=RESTORE=0;',
        cogen_parameter_define(comp, declared_parameters),
    ]
    f, n = comp.trace[0].fn if len(comp.trace) else (comp.name, 0)
    lines.append(f'SIG_MESSAGE("[_{comp.name}_trace] component NULL={comp.name}() [{f}:{n}]");')

    # FIXME This should be checking *only* for file.comp *formal* parameters specified with `symbol` as the typename
    #       which is not yet supported in this translator. Only the formal parameters can have `instr_type_symbol`
    #       and only in two specific situations: symbol {name}, symbol {name} = {expr}

    # Check if there are any user-defined parameter types ... (something which wasn't set previously?)
    # This is the 'symbol' type
    declared_types = [x.type for x in declared_parameters]
    # there must be a better way than this
    is_symbol = [t == 'symbol' for t in declared_types]
    # TODO FIXME This should be looping through setting parameters. It is probably wrong.
    if any(is_symbol):
        for i, inst in [(i, inst) for i, inst in enumerate(source.components) if inst.type.name == comp.name]:
            lines.extend([
                f'  /* check if this is component {inst.name} */',
                f'  if(_comp->_index == {1+i}) {{ '
            ])
            # loop through the symbol types and set the component-instance values from ... somewhere
            for c_dec in declared_parameters:
                # Use the user-defined instance parameter if it exists, or attempt to use a default otherwise?
                inst_param = [p for p in inst.parameters if p.name == c_dec.name]
                v = inst_param[0].value if len(inst_param) else c_dec.init
                if v is not None:
                    lines.append(f'    {c_dec.name} = {v};')
            lines.append('  }')

    # output the actual TRACE block(s)
    for block in comp.trace:
        lines.append(block.to_c())

    # instr files do not produce a code block to output here.
    pars = _runtime_kv_parameters(is_mcstas)
    lines.extend(["#ifndef NOABSORB_INF_NAN", "  /* Check for nan or inf particle parms */ "])
    lines.extend([f"  if(isnan({x}) || isinf({x})) ABSORB;" for x in pars])
    lines.append("#else")

    def long(x):
        return f'printf("NAN or INF found in {x}, %s (particle %lld)\\n",_comp->_name,_particle->_uid)'

    lines.extend([f'  if(isnan({x}) || isinf({x})) {long(x)};' for x in pars])
    lines.append('#endif')

    if len(extended):
        # combine the USERVARS from the instrument and this component type blocks:
        # uvs = set().union(instr_uservars).union(comp_uservars)
        uvs = list(dict.fromkeys([*instr_uservars, *comp_uservars]))
        # So that the EXTEND block(s) can access them
        lines.extend([f'  #define {x.name} (_particle->{x.name})' for x in uvs])
        # `index` was defined above to be the component index into the full instrument list
        for index, inst in extended:
            lines.append(f'if (_comp->_index == {1+index}) {{ // EXTEND {inst.name}')
            for ext in inst.extend:
                lines.append(ext.to_c())
            lines.append("}")
        lines.extend(f'  #undef {x.name}' for x in uvs)

    # return the component
    lines.extend([
        cogen_parameter_undef(comp, declared_parameters),
        '  return(_comp);',
        f'}} /* class_{comp.name}_trace */',
        ''
    ])

    return '\n'.join(lines)
