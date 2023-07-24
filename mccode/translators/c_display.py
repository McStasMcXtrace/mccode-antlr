def cogen_display(source, declared_parameters):
    lines = ["/* *****************************************************************************",
             f"* instrument {source.name} and components DISPLAY"
             "***************************************************************************** */",
             ]
    macros = dict(magnify='mcdis_magnify', line='mcdis_line', dashed_line='mcdis_dashed_line',
                  multiline='mcdis_multiline', rectangle='mcdis_rectangle', box='mcdis_box',
                  circle='mcdis_circle', cylinder='mcdis_cylinder', sphere='mcdis_sphere')

    for x, v in macros.items():
        lines.append(f'  #define {x} {v}')

    for comp in source.component_types:
        lines.extend(cogen_comp_display_class(comp, declared_parameters))

    for x in macros:
        lines.append(f'  #undef {x}')

    # write the instrument main code, which calls component ones
    lines.append(f'int display(void) /* called by mccode_main for {source.name}:DISPLAY */')
    lines.extend([f"#pragma acc update host(_{comp.name}_var)" for comp in source.components])
    lines.extend([
        '  printf("MCDISPLAY: start\n");',
        '',
    ])

    # Of course, there is no instrument level DISPLAY block directive
    # # insert user code from instrument definition
    # if len(source.display):
    #     f, n = source.display[0].fn
    #     lines.extend([
    #         f'  /* Instrument {source.name} DISPLAY */',
    #         f'  SIG_MESSAGE("[{source.name} DISPLAY [{f}:{n}]");'
    #     ])
    #     for par in source.parameters:
    #         # ensure there's no conflict of names
    #         lines.append(f'  #define {par.name} (instrument->_parameters.{par.name}')
    #     for block in source.display:
    #         lines.append(block.to_c())
    #     for par in source.parameters:
    #         lines.append(f'  #undef {par.name}')

    lines.append('/* call iteratively all components DISPLAY */')
    for comp in source.components:
        if len(comp.final):
            lines.append(f'  class_{comp.type.name}_display(&_{comp.name}_var);')

    lines.extend([
        '  printf("MCDISPLAY: end\n");'
        '',
        '  return(0);',
        '} /* display */',
        ''
    ])
    return '\n'.join(lines)


def cogen_comp_display_class(comp, declared_parameters):
    if not len(comp.display):
        return []

    lines = [f'_class_{comp.name} *class_{comp.name}_display(_class_{comp.name} *_comp) {{']
    for par in comp.parameters:
        lines.append(f'  #define {par.name} (_comp->_parameters.{par.name})')
    for par in declared_parameters:
        lines.append(f'  #define {par} (_comp->_parameters.{par})')

    f, n = comp.display[0].fn if len(comp.final) else comp.name, 0
    lines.append(f'  SIG_MESSAGE("[_{comp.name}_display] component NULL={comp.name}() [{f}:{n}]");')

    lines.append('  printf("MCDISPLAY: component %s\n", _comp->_name);')
    for block in comp.display:
        lines.append(block.to_c)

    for par in comp.parameters:
        lines.append(f'  #undef {par.name}')
    for par in declared_parameters:
        lines.append(f'  #undef {par}')
    lines.extend([
        '  return(_comp);',
        f'}} /* class_{comp.name}_display */',
        ''
    ])
    return lines
