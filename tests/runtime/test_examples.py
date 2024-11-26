from mccode_antlr.loader.loader import parse_mcstas_instr
from textwrap import dedent

from .compiled import compiled, compile_and_run


@compiled
def test_without_components():
    instr = parse_mcstas_instr(dedent("""\
    DEFINE INSTRUMENT without_components(int dummy=0)
    DECLARE %{
    int i_declare;
    %}
    INITIALIZE %{
    i_declare = 1;
    printf("Ran without components!\\ndummy=%d\\n", dummy);
    %}
    TRACE
    FINALLY %{ %}
    END
    """))
    results, files = compile_and_run(instr, '-n 1 dummy=101')
    lines = results.decode('utf-8').splitlines()
    assert len(lines) == 3
    assert lines[0] == "Ran without components!"
    assert lines[1] == "dummy=101"



@compiled
def test_template_instr():
    """
    This test failed previously because its name is a reserved word in C++ (template)
    """
    instr = parse_mcstas_instr(dedent("""\
    DEFINE INSTRUMENT template(Par1=1)
    DECLARE %{ %}
    INITIALIZE %{ %}
    TRACE
    COMPONENT Origin = Progress_bar() AT (0,0,0) ABSOLUTE

    FINALLY %{ %}
    END
    """))
    compile_and_run(instr, "-n 1 Par1=2")


@compiled
def test_component_declare_variable_initialised():
    instr = parse_mcstas_instr(dedent("""\
    DEFINE INSTRUMENT namedsomething(dummy=0)
    DECLARE %{
    int initialized;
    %}
    INITIALIZE %{
    initialized = -1;
    %}
    TRACE
    component Origin = Progress_bar() at (0, 0, 0) absolute
    component mirror = SupermirrorFlat() at (0, 0, 0) absolute
    FINALLY %{ %}
    END
    """))
    compile_and_run(instr, '-n 1 dummy=1')


@compiled
def test_function_pointer_declare_parameter():
    instr = parse_mcstas_instr(dedent("""\
    DEFINE INSTRUMENT with_function_pointers(int which=0)
    DECLARE %{
    int add(int a, int b){ return a + b; }
    int subtract(int a, int b){ return a - b; }
    int multiply(int a, int b){ return a * b; }
    
    int (*fun_ptr)(int, int);
    int (*fun_ptr_arr[])(int, int) = {add, subtract, multiply};
    %}
    INITIALIZE %{
    switch (which){
    case 0: fun_ptr = add; break;
    case 1: fun_ptr = subtract; break;
    case 2: fun_ptr = multiply; break;
    default:
        printf("Valid settings for 'which' are {0, 1, 2}. 'which=%d' is invalid.\\n", which);
        exit(-1);
    }
    %}
    TRACE
    COMPONENT first = Arm() AT (0, 0, 0) ABSOLUTE EXTEND %{
        printf("first=%d\\n", fun_ptr(2, 1));
    %}
    COMPONENT second = Arm() AT (0, 0, 0) ABSOLUTE EXTEND %{
        int choice = instrument->_parameters.which; // _should_ this be necessary?
        printf("second=%d\\n", fun_ptr_arr[choice](2, 1));
    %} 
    FINALLY %{ %}
    END
    """))
    for which in (0, 1, 2):
        results, files = compile_and_run(instr, f'-n 1 which={which}')
        lines = results.decode('utf-8').splitlines()
        res = None
        if which == 0:
            res = 2 + 1
        elif which == 1:
            res = 2 - 1
        elif which == 2:
            res = 2 * 1
        assert lines[0] == f"first={res}"
        assert lines[1] == f"second={res}"


@compiled
def test_function_pointer_component_declare_parameter():
    from mccode_antlr.reader.registry import InMemoryRegistry
    in_memory_registry = InMemoryRegistry('test_components')
    comp_name = 'declares_function_pointer'
    in_memory_registry.add_comp(comp_name, dedent(rf"""
    DEFINE COMPONENT {comp_name} DEFINITION PARAMETERS ()
    SETTING PARAMETERS (int selector=0, int A=0, int B=0)
    OUTPUT PARAMETERS ()
    SHARE %{{
        int add(int a, int b){{return a + b;}}
        int sub(int a, int b){{return a - b;}}
        int mul(int a, int b){{return a * b;}}
    %}}
    DECLARE %{{
        int (*fun_ptr)(int, int);
        int (*fun_ptr_arr[])(int, int) = {{add, sub, mul}};
    %}}
    INITIALIZE %{{
        switch (selector) {{
        case 0: fun_ptr = add; break;
        case 1: fun_ptr = sub; break;
        case 2: fun_ptr = mul; break;
        default:
        printf("%s: Invalid selector=%d, valid settings are {{0, 1, 2}}\n", NAME_CURRENT_COMP, selector);
        exit(-1);
        }}
    %}}
    TRACE %{{
        printf("%s=%d\n", NAME_CURRENT_COMP, fun_ptr(A, B));
        printf("%s=%d\n", NAME_CURRENT_COMP, fun_ptr_arr[selector](A, B));
    %}}
    SAVE %{{
    %}}
    FINALLY %{{
    %}}
    END
    """))

    instr = parse_mcstas_instr(dedent(rf"""
    DEFINE INSTRUMENT with_component_function_pointers(int which=0)
    DECLARE %{{ %}}
    INITIALIZE %{{ %}}
    TRACE
    COMPONENT first = {comp_name}(selector=which, A=2, B=1) AT (0, 0, 0) ABSOLUTE
    COMPONENT second = {comp_name}(selector=which, A=1, B=3) AT (0, 0, 0) ABSOLUTE
    FINALLY %{{ %}}
    END
    """), registries=[in_memory_registry])
    for which in (0, 1, 2):
        results, files = compile_and_run(instr, f'-n 1 which={which}')
        lines = results.decode('utf-8').splitlines()
        print(lines)
        a, b = 0, 0
        if which == 0:
            a, b = 2 + 1, 1 + 3
        elif which == 1:
            a, b = 2 - 1, 1 - 3
        elif which == 2:
            a, b = 2 * 1, 1 * 3
        assert lines[0] == f"first={a}"
        assert lines[1] == f"first={a}"
        assert lines[2] == f"second={b}"
        assert lines[3] == f"second={b}"


@compiled
def test_struct_instance_parameter():
    instr = parse_mcstas_instr(dedent(r"""
    DEFINE INSTRUMENT templateTAS(DM=3.3539)
    DECLARE
    %{
      struct machine_hkl_struct {
        double dm;
        double refl;
        char refl_file[100];
      } machine_hkl;
    %}
    INITIALIZE
    %{
    machine_hkl.dm = DM; 
    machine_hkl.refl = 0.7;
    memset(machine_hkl.refl_file, '\0', sizeof(machine_hkl.refl_file));
    if (fabs(machine_hkl.dm - 3.355) < 0.2) {
      machine_hkl.refl = 1.0;
      strcpy(machine_hkl.refl_file, "HOPG.rfl");
    }
    %}
    TRACE
    COMPONENT Origin=Progress_bar()
    AT (0,0,0) ABSOLUTE
    
    COMPONENT PG1Xtal = Monochromator_curved(
      width  = 0.1, height = 0.1, NH=1, NV=1, RV=0, RH=0,
      DM = machine_hkl.dm, r0 = machine_hkl.refl, reflect = machine_hkl.refl_file)
    AT (0, 0, 0) RELATIVE Origin
    EXTEND
    %{
    printf("PG1Xtal.r0=%3.1f, PG1Xtal.reflect='%s'\n", r0, reflect);
    %}

    COMPONENT PG2Xtal = Monochromator_curved(
      width  = 0.1, height = 0.1, NH=1, NV=1, RV=0, RH=0,
      DM = machine_hkl.dm, 
      r0 = (fabs(machine_hkl.dm-3.355) < 0.2 ? 1: 0.7), 
      reflect=(fabs(machine_hkl.dm-3.355) < 0.2 ? "HOPG.rfl" : ""))
    AT (0, 0, 0) RELATIVE Origin
    EXTEND
    %{
    printf("PG2Xtal.r0=%3.1f, PG2Xtal.reflect='%s'\n", r0, reflect);
    %}

    END
    """))
    for dm, r0, filename in ((1.55, 0.7, ''), (3.355, 1.0, 'HOPG.rfl')):
        results, files = compile_and_run(instr, f'-n 1 DM={dm}')
        lines = results.decode('utf-8').splitlines()
        print('\n'.join(lines))
        assert lines[0] == '[templateTAS] Initialize'
        assert lines[1] == f"PG1Xtal.r0={r0:3.1f}, PG1Xtal.reflect='{filename}'"
        assert lines[2] == f"PG2Xtal.r0={r0:3.1f}, PG2Xtal.reflect='{filename}'"