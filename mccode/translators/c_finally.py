def cogen_finally(source, declared_parameters):
    lines = ["/* *****************************************************************************",
             f"* instrument {source.name} and components FINALLY",
             "***************************************************************************** */",
             ]

    for comp in source.component_types():
        lines.extend(cogen_comp_finally_class(comp, declared_parameters[comp.name]))

    # write the instrument main code, which calls component ones
    lines.append(f'int save(void) /* called by mccode_main for {source.name}:FINALLY */')
    lines.extend([f"#pragma acc update host(_{comp.name}_var)" for comp in source.components])
    lines.extend([
        '#pragma acc update host(_instrument_var);',
        '',
        ' siminfo_init(NULL);'
        ' save(siminfo_file); /* save data when simulation ends */'
    ])

    # insert user code from instrument definition
    if len(source.final):
        f, n = source.final[0].fn
        lines.extend([
            f'  /* Instrument {source.name} FINALLY */',
            f'  SIG_MESSAGE("[{source.name} FINALLY [{f}:{n}]");'
        ])
        for par in source.parameters:
            # ensure there's no conflict of names
            lines.append(f'  #define {par.name} (instrument->_parameters.{par.name}')
        for block in source.final:
            lines.append(block.to_c())
        for par in source.parameters:
            lines.append(f'  #undef {par.name}')

    lines.append('/* call iteratively all components FINALLY */')
    for comp in source.components:
        if len(comp.type.final):
            lines.append(f'  class_{comp.type.name}_finally(&_{comp.name}_var);')

    lines.extend([
        '  siminfo_close();'
        '',
        '  return(0);',
        '} /* finally */',
        ''
    ])
    return '\n'.join(lines)


def cogen_comp_finally_class(comp, declared_parameters):
    from .c_defines import cogen_parameter_define, cogen_parameter_undef
    if not len(comp.final):
        return []

    lines = [
        f'_class_{comp.name} *class_{comp.name}_finally(_class_{comp.name} *_comp) {{',
        cogen_parameter_define(comp)
    ]
    f, n = comp.final[0].fn if len(comp.final) else (comp.name, 0)
    lines.append(f'  SIG_MESSAGE("[_{comp.name}_finally] component NULL={comp.name}() [{f}:{n}]");')

    for block in comp.final:
        lines.append(block.to_c())

    lines.extend([
        cogen_parameter_undef(comp),
        '  return(_comp);',
        f'}} /* class_{comp.name}_finally */',
        ''
    ])
    return lines