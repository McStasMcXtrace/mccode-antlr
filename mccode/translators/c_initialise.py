
_GETDISTANCE_FCT = """
  double index_getdistance(int first_index, int second_index)
  /* Calculate the distance two components from their indexes*/
  {
    return coords_len(coords_sub(POS_A_COMP_INDEX(first_index), POS_A_COMP_INDEX(second_index)));
  }

  double getdistance(char* first_component, char* second_component)
  /* Calculate the distance between two named components */
  {
    int first_index = _getcomp_index(first_component);
    int second_index = _getcomp_index(second_component);
    return index_getdistance(first_index, second_index);
  }
  
  double checked_setpos_getdistance(int current_index, char* first_component, char* second_component)
  /* Calculate the distance between two named components at *_setpos() time, with component index checking */
  {
    int first_index = _getcomp_index(first_component);
    int second_index = _getcomp_index(second_component);
    if (first_index >= current_index || second_index >= current_index) {
      printf(\"setpos_getdistance can only be used with the names of components before the current one!\\n\");
      return 0;
    }
    return index_getdistance(first_index, second_index);
  }
  #define setpos_getdistance(first, second) checked_setpos_getdistance(current_setpos_index, first, second)
"""


def cogen_comp_init_position(index, comp, last, instr):
    ref = None if index == 0 else instr.components[last]
    lines = [
        f'  /* component {comp.name}={comp.type.name}() AT ROTATED */',
        '  {',
        '    Coords tc1, tc2;',
        '    tc1 = coords_set(0,0,0);',
        '    tc2 = coords_set(0,0,0);',
        '    Rotation tr1;',
        '    rot_set_rotation(tr1,0,0,0);'
    ]
    # Rotation first
    x, y, z = comp.rotate_relative[0]
    rel = comp.rotate_relative[1]
    if rel is None:
        lines.append(
            f'    rot_set_rotation(_{comp.name}_var._rotation_absolute, ({x})*DEG2RAD, ({y})*DEG2RAD, ({z})*DEG2RAD);'
        )
    else:
        lines.extend([
            f'    rot_set_rotation(tr1, ({x})*DEG2RAD, ({y})*DEG2RAD, ({z})*DEG2RAD);',
            f'    rot_mul(tr1, _{rel.name}_var._rotation_absolute, _{comp.name}_var._rotation_absolute);'
        ])
    # Sort out relative orientation
    if index == 0:
        lines.append(f'    rot_copy(_{comp.name}_var._rotation_relative, _{comp.name}_var._rotation_absolute);')
    else:
        lines.extend([
            f'    rot_transpose(_{ref.name}, tr1);',
            f'    rot_mul(_{comp.name}_var._rotation_absolute, tr1, _{comp.name}_var._rotation_relative);'
        ])
    lines.append(f'    _{comp.name}._rotation_is_identity = rot_test_identity(_{comp.name}._rotation_relative);')

    # Then translation
    x, y, z = comp.at_relative[0]
    rel = comp.at_relative[1]
    if rel is None:
        lines.append(f'    _{comp.name}_var._position_absolute = coords_set({x}, {y}, {z});')
    else:
        lines.extend([
            f'    tc1 = coords_set({x}, {y}, {z});',
            f'    rot_transpose(_{rel.name}_var._rotation_absolute, tr1);',
            '    tc2 = rot_apply(tr1, tc1);'
            f'    _{comp.name}_var._position_absolute = coords_add(_{rel.name}_var._position_absolute, tc2);'
        ])
    if index == 0:
        lines.append('    tc1 = coords_neg(_{comp.name}_var.position_absolute);')
    else:
        lines.append(f'    tc1 = coords_sub(_{ref.name}_var._position_absolute, _{comp.name}_var._position_absolute);')
    lines.extend([
        f'    _{comp.name}_var._position_relative = rot_apply(_{comp.name}_var._rotation_absolute, tc1);',
        f'  }} /* {comp.name}={comp.type.name}() AT ROTATED */',
        f'  DEBUG_COMPONENT("{comp.name}", _{comp.name}_var._position_absolute, _{comp.name}_var._rotation_absolute);',
        f'  instrument->_position_absolute[{index}] = _{comp.name}_var._position_absolute;',
        f'  instrument->_position_relative[{index}] = _{comp.name}_var._position_relative;',
        f'  _{comp.name}_var._position_relative_is_zero = coords_test_zero(_{comp.name}_var._position_relative);'
    ])
    return '\n'.join(lines)


def cogen_comp_setpos(index, comp, last, instr, component_declared_parameters):
    from ..common import Value

    def parameter_line(p):
        pl = []
        if p.value.is_a(Value.Type.str):
            if p.value.has_value and p.value.value != '0' and p.value.value != 'NULL':
                pl.extend([
                    f'  if ({p.value} && strlen({p.value}))',
                    f'    stracpy(_{comp.name}_var.parameters.{p.name}, {p.value} ? {p.value} : "", 16384);',
                    '  else'
                ])
            pl.append(f"  _{comp.name}_var.parameters.{p.name}[0]='\\0';")
        elif p.value.is_a(Value.Type.float_array) or p.value.is_a(Value.Type.int_array):
            if p.value.has_value and p.value.holds_array:
                for i, v in enumerate(p.value.value):
                    pl.append(f'  _{comp.name}_var.parameters.{p.name}[{i}] = {v};')
            else:
                # it's a string (if not None), and should be an identifier that is a pointer to the data
                pl.append(f'  _{comp.name}_var.parameters.{p.name} = {p.value if p.value.has_value else "NULL"};')
        # elif p.value.is_a(Value.Type.symbol):
        #   symbol is not handled (yet) but should be initialized to zero
        else:
            pl.append(f'  _{comp.name}_var.parameters.{p.name} = {p.value if p.value.has_value else 0};')
        return '\n'.join(pl)

    f, n = comp.type.initialize[0].fn if len(comp.type.initialize) else (comp.name, 0)

    lines = [
        f'/* component {comp.name}={comp.type.name}() SETTING, POSITION/ROTATION */',
        f'int _{comp.name}_setpos(void)"',
        "{ /* sets initial component parameters, position and rotation */",
        # init parameters. These can then be used in position/rotation syntax
        # all these parameters have a #define pointing to the real name space in structure
        f'  SIG_MESSAGE("[_{comp.name}_setpos] component {comp.name}={comp.type.name}() SETTING [{f}:{n}]',
        f'  stracpy(_{comp.name}_var._name, "{comp.name}", {len(comp.name)+1});',
        f'  stracpy(_{comp.name}_var._type, "{comp.type.name}", {len(comp.type.name)+1});',
        f'  _{comp.name}_var._index={index};',
        f'  int current_setpos_index = {index};'
    ]
    # setting parameters
    set_parameter_names = [x.name for x in comp.parameters]
    # TODO figure this out?! 'SETTING' parameters can be over-ridden by same-named instrument parameters??
    for par in comp.type.settings:
        tp = [x for x in comp.parameters if x.name == par.name][0] if par.name in set_parameter_names else par
        lines.append(parameter_line(tp))

    set_parameter_names = [x.name for x in comp.parameters]
    for par in comp.type.parameters:
        # select the instance parameter or default:
        tp = [x for x in comp.parameters if x.name == par.name][0] if par.name in set_parameter_names else par
        lines.append(parameter_line(tp))

    # private parameters
    declared_parameters = component_declared_parameters[comp.type.name]
    for name, (declared_type, initialized_value) in declared_parameters.items():
        init_to = 'NULL' if any(x in declared_type for x in '*[]') and initialized_value is None else initialized_value
        if init_to is not None:
            lines.append(f"  _{comp.name}_var.parameters.{name} = {init_to};")

    # position/rotation
    lines.append(cogen_comp_init_position(index, comp, last, instr))

    lines.extend([
        f'  instrument->counter_N[{index}] = instrument->counter_P[{index}] = instrument->counter_P2[{index}] = 0;',
        f'  instrument->counter_AbsorbProp[{index}] = 0;',
        f'  return(0);'
        f'}} /* _{comp.name}_setpos */'
    ])
    return lines


def cogen_initialize(source, component_declared_parameters, ok_to_skip):
    lines = ["/* *****************************************************************************",
             f"* instrument {source.name} and components INITIALIZE"
             "***************************************************************************** */",
             _GETDISTANCE_FCT, ""]

    last = 0
    for idx, comp in enumerate(source.components):
        lines.extend(cogen_comp_setpos(idx, comp, last, source, component_declared_parameters))
        if ok_to_skip is not None and not ok_to_skip[idx]:
            last = idx

    # generate class functions
    for comp in source.component_types():
        lines.extend(cogen_comp_initialize_class(comp, component_declared_parameters[comp.name]))

    # write the instrument main code, which calls component ones
    lines.extend([
        f'int initialize(void) /* called by mccode_main for {source.name}:INITIALIZE */',
        '  DEBUG_INSTR()',
        '',
        '  /* code_main/parseoptions/readparams sets instrument parameters value */',
        f'  stracpy(instrument->_name, "{source.name}", {len(source.name)+1});',
    ])

    # insert user code from instrument definition
    if len(source.initialize):
        f, n = source.initialize[0].fn
        lines.extend([
            f'  /* Instrument {source.name} INITIALIZE */',
            f'  SIG_MESSAGE("[{source.name} INITIALIZE [{f}:{n}]");'
        ])
        for par in source.parameters:
            # ensure there's no conflict of names
            lines.append(f'  #define {par.name} (instrument->_parameters.{par.name}')
        for block in source.initialize:
            lines.append(block.to_c())
        for par in source.parameters:
            lines.append(f'  #undef {par.name}')

    for comp in source.components:
        lines.append(f'  _{comp.name}_setpos(); /* type {comp.type.name} */')

    lines.append('/* call iteratively all components INITIALIZE */')
    for comp in source.components:
        if len(comp.type.initialize):
            lines.append(f'  class_{comp.type.name}_initialize(&_{comp.name}_var);')

    lines.extend([
        '  if (mcdotrace) display();',
        '  DEBUG_INSTR_END();',
        '',
        # call acc_attach for OpenACC (last thing to do in init)
        '#ifdef OPENACC',
        '#include <openacc.h>',
        # update component instances on device (e.g. push managed ata structures)
        *[f'#pragma acc update device(_{comp.name}_var)' for comp in source.components],
        # update instrument
        '#pragma acc update device(_instrument_var)',
        '#endif',
        '',
        '  return(0);',
        '} /* initialize */',
        ''
    ])

    return '\n'.join(lines)


def cogen_comp_initialize_class(comp, declared_parameters):
    if not len(comp.initialize):
        return []

    lines = [f'_class_{comp.name} *class_{comp.name}_initialize(_class_{comp.name} *_comp) {{']
    for par in comp.parameters:
        lines.append(f'  #define {par.name} (_comp->_parameters.{par.name})')
    for par in declared_parameters:
        lines.append(f'  #define {par} (_comp->_parameters.{par})')

    f, n = comp.initialize[0].fn if len(comp.initialize) else (comp.name, 0)
    lines.append(f'  SIG_MESSAGE("[_{comp.name}_initialize] component NULL={comp.name}() [{f}:{n}]");')

    for block in comp.initialize:
        lines.append(block.to_c())

    for par in comp.parameters:
        lines.append(f'  #undef {par.name}')
    for par in declared_parameters:
        lines.append(f'  #undef {par}')
    lines.extend([
        '  return(_comp);',
        f'}} /* class_{comp.name}_initialize */',
        ''
    ])
    return lines
