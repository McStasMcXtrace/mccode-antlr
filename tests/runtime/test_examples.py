from mccode_antlr.loader.loader import parse_mcstas_instr
from textwrap import dedent

from .compiled import compiled, compile_and_run

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