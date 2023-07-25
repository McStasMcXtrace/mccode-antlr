"""
/*******************************************************************************
* cogen_decls: write the declaration part from the instrument description
*   that is the particle definition, the instrument parameters, the DECLARE part,
*   and all SHARE sections from components.
* input:  an instrument definition structure
* output: number of warnings/errors to fix.
*
* code is generated at root level of C file: only C definitions, no initialisers !
* calls: cogen_comp_declare
*******************************************************************************/
"""


def declarations_pre_libraries(source, typedefs: list, component_declared_parameters: dict):
    warnings = 0

    def instrument_parameters_struct():
        def _inner():
            if len(source.parameters) == 0:
                return f"char {source.name}_has_no_parameters;"
            return '\n'.join([f'  {p.value.mccode_c_type} {p.name};' for p in source.parameters])
        lines = ['struct _struct_instrument_parameters{', _inner(), '};',
                 'typedef struct _struct_instrument_parameters _class_instrument_parameters;']
        return '\n'.join(lines)

    count = len(source.groups) + sum(len(i.jump) + (0 if i.split is None else 1) for i in source.components)

    def control_statement_logic():
        #TODO FIXME Why do we care about jump counts here? The struct only contains GROUP and SPLIT counters
        # count number of groups, all jump lengths and splits
        if count == 0:
            return ""
        lines = "\n/* instrument SPLIT and GROUP control logic */\nstruct instrument_logic_struct{\n"
        comment = '/* equals index of scattering comp when in group */'
        lines += '\n'.join(f'  long Group_{name}; {comment}' for name in source.groups)
        c1 = '/* this is the SPLIT counter decremented down to 0 */'
        c2 = '/* this is the particle to duplicate */'
        lines += '\n'.join(f'  long Split_{i.name}; {c1}\n  _class_particle Split_{i.name}_particle; {c2}'
                           for i in source.components if i.split is not None)
        lines += '};\n'
        return lines

    def instrument_structure():
        n2 = len(source.components) + 2
        lines = ["struct _instrument_struct {",
                 f"  char   _name[256]; /* the name of this instrument e.g. '{source.name}' */",
                 "/* Counters per component instance */",
                 f"  double counter_AbsorbProp[{n2}]; /* absorbed events in PROP routines */",
                 f"  double counter_N[{n2}], counter_P[{n2}], counter_P2[{n2}]; /* event counters after each component instance */",
                 f"  _class_particle _trajectory[{n2}]; /* current trajectory for STORE/RESTORE */",
                 "/* Components position table (absolute and relative coords) */",
                 f"  Coords _position_relative[{n2}]; /* positions of all components */",
                 f"  Coords _position_absolute[{n2}];",
                 "  _class_instrument_parameters _parameters; /* instrument parameters */"]
        if count:
            lines.append("struct instrument_logic_struct logic; /* instrument logic */")
        lines.append("} _instrument_var;")
        lines.append("struct _instrument_struct *instrument = & _instrument_var;")
        lines.append("#pragma acc declare create ( _instrument_var )")
        lines.append("#pragma acc declare create ( instrument )")
        return '\n'.join(lines)

    def instrument_parameters_table():
        def one_line(name, typename, value, unit):
            return f'  "{name},  &(_instrument_var._parameters{name}) , {typename}, "{value}", "{unit}",'
        lines = [f'int numipar = {len(source.parameters)};', 'struct mcinputtable_struct mcinputtable[] = {']
        lines.extend([one_line(p.name, p.value.mccode_c_type_name, p.value, p.unit) for p in source.parameters])
        lines.extend(['  NULL, NULL, instr_type_double, "", ""'])
        lines.append("};")
        return '\n'.join(lines)

    def metadata_table():
        def one_line(defined_by, name, mimetype, value):
            from ..common.utilities import escape_str_for_c
            return f'"{defined_by}", "{name}", "{mimetype}", {escape_str_for_c(value)}, '

        metadata = source.collect_metadata()
        lines = ['struct metadata_table_struct metadtata_table[] = {']
        lines.extend([one_line(m.source.name, m.name, m.mimetype, m.value) for m in metadata])
        lines.extend(['"", "", "", ""', '};', f'int num_metadata = {len(metadata)};'])
        return '\n'.join(lines)

    def component_share_declarations():
        components = source.component_types()  # This is a set, so inclusion order is not preserved.
        sharers = [c for c in components if len(c.share)]
        if len(sharers) == 0:
            return ''
        lines = [
            "/* ************************************************************************** */",
            "/*             SHARE user declarations for all components                     */",
            "/* ************************************************************************** */"]
        for comp in sharers:
            lines.append(f"/* Shared user declarations for all components types '{comp.name}'. */")
            # TODO FIXME to_c includes the `#line` preprocessor directive -- which was removed from McCode3??
            lines.extend([share.to_c() for share in comp.share])
        lines.extend([
            "/* ************************************************************************** */",
            "/*             End of SHARE user declarations for all components              */",
            "/* ************************************************************************** */"])
        return '\n'.join(lines)

    def component_type_declarations():
        lines = ["/* ********************** component definition declarations. **************** */"]
        lines.extend([component_type_declaration(comp, typedefs, component_declared_parameters[comp.name])
                      for comp in source.component_types()])
        return '\n'.join(lines)

    def component_instance_declarations():
        lines = [component_instance_declaration(instance, index) for index, instance in enumerate(source.components)]
        lines.append(f'int mcNUMCOMP = {len(source.components)}')
        return '\n'.join(lines)

    contents = [
        '/* *****************************************************************************',
        f"* instrument '{source.name}' and components DECLARE",
        '***************************************************************************** */',
        '',
        '/* Instrument parameters: structure and a table for the initialisation',
        '   (Used in e.g. inputparse and I/O function (e.g. detector_out) */',
        '',
        instrument_parameters_struct(),
        control_statement_logic(),
        instrument_structure(),
        instrument_parameters_table(),
        metadata_table(),
        component_share_declarations(),
        component_type_declarations(),
        component_instance_declarations(),
    ]
    return '\n'.join(contents), warnings


def component_type_declaration(comp, typedefs: list, declared_parameters: dict):
    """Declare the *component type* structures needed for component instances.
    Includes the component parameters structure and positioning code.
    """
    from ..common import Value
    from .c_listener import extract_c_declared_variables
    warnings = 0
    lines = [
        f'/* Parameter definition for component type {comp.name} */',
        f'struct _struct_{comp.name}_parameters {{',
        f'  /* Component type {comp.name} setting parameters */'
    ]
    for par in comp.parameters:
        if par.value.is_a(Value.Type.float_array) or par.value.is_a(Value.Type.int_array):
            if par.value.holds_array:
                # this is only possible if the value is a tuple of numbers, so no str representations of calculations
                c_type = par.value.mccode_c_type.translate(str.maketrans('', '', ' *'))  # strip the trailing ' *'
                lines.append(f'  {c_type} {par.name}[{len(par.value.value)}];')
            elif par.value.has_value:
                print(f'The parameter {par.name} of {comp.name} appears to be default-initialized')
                print(f'with a non-numeric initializer list: {comp.value}')
                print(f'This will cause errors as initializer-lists can only contain literal numbers.')
                warnings += 1
                lines.append(f'  {par.value.mccode_c_type} {par.name};')
            else:
                lines.append(f'  {par.value.mccode_c_type} {par.name};')
        if par.value.is_a(Value.Type.str):
            # TODO FIXME The cogen implementation *ALSO* makes static arrays for `vector` parameters?

            # the mccode runtime does not want to allocate or deallocate the memory for this string.
            # So it expects a statically sized (16kB) char array
            c_type = par.value.mccode_c_type.translate(str.maketrans('', '', ' *'))
            lines.append(f'  {c_type} {par.name}[16384];')
        else:
            # basic integer or float
            lines.append(f'  {par.value.mccode_c_type} {par.name};')

    lines.append(f'/* Component type {comp.name} private parameters */')
    # declared_parameters = dict()
    # for declare_block in comp.declare:
    #     declared_parameters.update(extract_c_declared_variables(declare_block.source, user_types=typedefs))
    #
    for name, (declared_type, initialized) in declared_parameters.items():
        lines.append(f'  {declared_type} {name}; /* {"Not initialized" if initialized is None else initialized} */')

    if len(comp.parameters) + len(declared_parameters) == 0:
        lines.append(f'  char {comp.name}_has_no_parameters;')

    lines.extend([
        f'}}; /* _struct_{comp.name}_parameters */',
        f'typedef struct _struct_{comp.name}_parameters _class_{comp.name}_parameters;',
        '',
        f"/* Parameters for component type '{comp.name}' */",
        f"struct _struct_{comp.name} {{",
        f"  char     _name[256]; /* e.g. instance of {comp.name} name */",
        f"  char     _type[{len(comp.name)+1}]; /* {comp.name} */",
        f"  long     _index; /* index in TRACE list */",
        "  Coords   _position_absolute;",
        "  Coords   _position_relative; /* wrt PREVIOUS */",
        "  Rotation _rotation_absolute;",
        "  Rotation _rotation_relative; /* wrt PREVIOUS */",
        "  int      _rotation_is_identity;",
        "  int      _position_relative_is_zero;",
        f"  _class_{comp.name}_parameters _parameters;",
        "};",
        f"typedef struct _struct_{comp.name}, _class_{comp.name};"
    ])
    return '\n'.join(lines)


def component_instance_declaration(instance, index):
    """Declare the *instance* variable of the component-type structure"""
    lines = [
        f'/* component {instance.name} = {instance.type.name}() [{index}] DECLARE */',
        f'_class_{instance.type.name} _{instance.name}_var;',
        f'#pragma acc declare create ( _{instance.name}_var )'
    ]
    return '\n'.join(lines)
