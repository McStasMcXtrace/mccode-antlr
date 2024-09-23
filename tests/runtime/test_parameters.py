from .compiled import compiled, compile_and_run

@compiled
def test_parameters():
    """Ensure that instrument parameters are available for 'when' statements, e.g., in the raytrace section"""
    from mccode_antlr.loader.loader import parse_mcstas_instr
    from textwrap import dedent
    instr = parse_mcstas_instr(dedent("""\
        define instrument test_parameters(int boolean_value=1)
        declare %{int count;%}
        initialize %{count = -1;%}
        trace
        component o = Arm() at (0,0,0) absolute extend %{++count;%}
        component a = Arm() when (count%4==0) at (0,0,0) absolute 
                      extend %{printf("a=%d\\n", count); SCATTER; %}
        component b = Arm() when (count%2==0) at (0,0,0) absolute 
                      extend %{printf("b=%d\\n", count);%}
        component c = Arm() when (boolean_value && count%2) at (0,0,0) absolute
                      extend %{printf("c=%d\\n", count);%}
        end 
    """))
    n_max = 5
    results, data = compile_and_run(instr, f"-n {n_max} boolean_value=0")
    lines = results.decode('utf-8').splitlines()
    print(lines)
    expected = []
    for i in range(n_max):
        if i % 4 == 0:
            expected.append(f'a={i}')
        if i % 2 == 0:
            expected.append(f'b={i}')

    for ex, ln in zip(expected, lines):
        assert ex == ln

    results, data = compile_and_run(instr, f"-n {n_max} boolean_value=1")
    lines = results.decode('utf-8').splitlines()
    print(lines)
    expected = []
    for i in range(n_max):
        if i % 4 == 0:
            expected.append(f'a={i}')
        if i % 2 == 0:
            expected.append(f'b={i}')
        if i % 2:
            expected.append(f'c={i}')

    for ex, ln in zip(expected, lines):
        assert ex == ln
