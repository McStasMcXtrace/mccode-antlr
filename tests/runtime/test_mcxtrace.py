from textwrap import dedent
from mccode_antlr.loader import parse_mcstas_instr
from .compiled import compiled_test, compile_and_run, Flavor
from mccode_antlr.reader.registry import InMemoryRegistry

in_memory = InMemoryRegistry(
    "test_components",
    trace_counter=dedent("""DEFINE COMPONENT trace_counter
    SETTING PARAMETERS (int n)
    NOACC
    TRACE
    %{
      for (int i= 0; i < n; i++) {
        printf("%d\\n", i);
      }
    %}
    END
    """),
    useless=dedent("""DEFINE COMPONENT useless
    SETTING PARAMETERS (int n)
    TRACE 
    %{
    %}
    END
    """),
)


@compiled_test
def test_simplest_mcstas():
    instr = parse_mcstas_instr(dedent("""
    define instrument test_simplest_mcstas(dummy=0.)
    trace component origin = useless() at (0, 0, 0) absolute end
    """), registries=[in_memory])
    compile_and_run(instr, '-n 1 dummy=2', flavor=Flavor.MCSTAS)


@compiled_test
def test_simplest_mcxtrace():
    instr = parse_mcstas_instr(dedent("""
    define instrument test_simplest_mcxtrace(dummy=0.)
    trace component origin = useless() at (0, 0, 0) absolute end
    """), registries=[in_memory])
    compile_and_run(instr, '-n 1 dummy=2', flavor=Flavor.MCXTRACE)

