from textwrap import dedent
from mccode_antlr.loader import parse_mcstas_instr
from .compiled import compiled_test, gpu_compiled_test, compile_and_run
from mccode_antlr.config import config
from mccode_antlr.reader.registry import InMemoryRegistry

# config['flags']['acc'] = "-lm -fast -Minfo=accel -acc=host -DOPENACC -x c -D_POSIX_C_SOURCE=2"

FAKE_COMPONENTS = dict(
    with_noacc=dedent("""DEFINE COMPONENT with_noacc
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
    without_noacc=dedent("""DEFINE COMPONENT without_noacc
    SETTING PARAMETERS (int n)
    TRACE
    %{
      for (int i= 0; i < n; i++) {
        printf("%d\\n", i);
      }
    %}
    END
    """),
)

in_memory = InMemoryRegistry("test_components")
for comp, repr in FAKE_COMPONENTS.items():
    in_memory.add_comp(comp, repr)


@gpu_compiled_test
def test_simple_acc():
    instr = parse_mcstas_instr(dedent("""
    define instrument test_simple_acc(dummy=0.)
    trace
    component origin = without_noacc() at (0, 0, 0) absolute
    end
    """), registries=[in_memory])
    compile_and_run(instr, '-n 1 dummy=2', target={'acc': True})


@gpu_compiled_test
def test_cpu_only_instance():
    instr = parse_mcstas_instr(dedent("""
    define instrument test_cpu_only_instance(dummy=0.)
    trace
    component origin = without_noacc() at (0, 0, 0) absolute
    cpu component ordered = without_noacc() at (0, 0, 1) absolute
    component disordered = without_noacc() at (0, 0, 2) absolute
    end
    """), registries=[in_memory])
    compile_and_run(instr, '-n 1 dummy=2', target={'acc': True})



@gpu_compiled_test
def test_noacc_component():
    instr = parse_mcstas_instr(dedent("""
    define instrument test_noacc_instance(dummy=0.)
    trace
    component origin = without_noacc() at (0, 0, 0) absolute
    component ordered = with_noacc() at (0, 0, 1) absolute
    end
    """), registries=[in_memory])
    compile_and_run(instr, '-n 1 dummy=2', target={'acc': True})


@gpu_compiled_test
def test_cpu_and_noacc_component():
    instr = parse_mcstas_instr(dedent("""
    define instrument test_cpu_and_noacc_component(dummy=0.)
    trace
    component origin = without_noacc() at (0, 0, 0) absolute
    cpu component ordered = with_noacc() at (0, 0, 1) absolute
    end
    """), registries=[in_memory])
    compile_and_run(instr, '-n 1 dummy=2', target={'acc': True})


