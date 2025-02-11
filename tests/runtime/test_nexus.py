from textwrap import dedent
from mccode_antlr.loader import parse_mcstas_instr
from .compiled import compiled_test, compile_and_run
from mccode_antlr.config import config
from mccode_antlr.reader.registry import InMemoryRegistry


# config['flags']['acc'] = "-lm -fast -Minfo=accel -acc=host -DOPENACC -x c -D_POSIX_C_SOURCE=2"

FAKE_COMPONENTS = dict(
    check_for_define=dedent(r"""DEFINE COMPONENT check_for_define
    SETTING PARAMETERS (int n)
    TRACE
    %{
    #ifdef UNUSUAL_MACRO_CONTROL
    printf("UNUSUAL_MACRO_CONTROL set\n");
    #else
    printf("UNUSUAL_MACRO_CONTROL not set\n");
    #endif
    %}
    END
    """),
    check_for_nexus=dedent(r"""DEFINE COMPONENT check_for_nexus
    SETTING PARAMETERS (int n)
    TRACE
    %{
    %}
    END
    """)
)


in_memory = InMemoryRegistry("test_components")
for comp, repr in FAKE_COMPONENTS.items():
    in_memory.add_comp(comp, repr)


@compiled_test
def test_instr_dependency():
    instr = parse_mcstas_instr(dedent("""
    define instrument test_instr_dependency(dummy=0.)
    DEPENDENCY "-DUNUSUAL_MACRO_CONTROL"
    trace
    component origin = check_for_define() at (0, 0, 0) absolute
    end
    """), registries=[in_memory])
    assert any('-DUNUSUAL_MACRO_CONTROL' == x for x in instr.flags)
    results, data = compile_and_run(instr, '-n 1 dummy=2')
    lines = results.decode('utf-8').splitlines()
    assert sum('UNUSUAL_MACRO_CONTROL set' == x for x in lines) == 1
    assert sum('UNUSUAL_MACRO_CONTROL not set' == x for x in lines) == 0


@compiled_test
def test_instr_no_dependency():
    instr = parse_mcstas_instr(dedent("""
    define instrument test_instr_no_dependency(dummy=0.)
    trace
    component origin = check_for_define() at (0, 0, 0) absolute
    end
    """), registries=[in_memory])
    assert not any('-DUNUSUAL_MACRO_CONTROL' == x for x in instr.flags)
    results, data = compile_and_run(instr, '-n 1 dummy=2')
    lines = results.decode('utf-8').splitlines()
    assert sum('UNUSUAL_MACRO_CONTROL set' == x for x in lines) == 0
    assert sum('UNUSUAL_MACRO_CONTROL not set' == x for x in lines) == 1


def test_nexus_key_is_expanded():
    from mccode_antlr.config import config
    instr = parse_mcstas_instr(dedent("""
       define instrument test_nexus_key_is_expanded(dummy=0.)
       DEPENDENCY "@NEXUSFLAGS@"
       trace
       component origin = check_for_nexus() at (0, 0, 0) absolute
       end
       """), registries=[in_memory])
    assert any('@NEXUSFLAGS@' == x for x in instr.flags)
    assert not any('@NEXUSFLAGS@' == x for x in instr.decoded_flags())
    nexus_flags = config['flags']['nexus'].get()
    assert any(nexus_flags == x for x in instr.decoded_flags())
