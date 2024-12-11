from __future__ import annotations
from functools import cache
from unittest import TestCase
from mccode_antlr.compiler.check import simple_instr_compiles, compiled, gpu_only, mpi_only

@cache
def mcpl_config_available():
    try:
        import subprocess
        subprocess.run(['mcpl-config', '--version'], check=True)
    except FileNotFoundError:
        return False
    return True


def mcpl_compiled(method):
    def wrapper(*args, **kwargs):
        if mcpl_config_available() and simple_instr_compiles('cc'):
            method(*args, **kwargs)
        elif isinstance(args[0], TestCase):
            msg = "working compiler" if mcpl_config_available() else "mcpl interface"
            args[0].skipTest(f'Skipping due to missing {msg}')

    return wrapper


def compile_and_run(instr, parameters, run=True, dump_source=True, target: dict | None = None, config: dict | None = None):
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from mccode_antlr.translators.target import MCSTAS_GENERATOR
    from mccode_antlr.run import mccode_compile, mccode_run_compiled

    kwargs = dict(generator=MCSTAS_GENERATOR, target=target, config=config, dump_source=dump_source)

    with TemporaryDirectory() as directory:
        binary, target = mccode_compile(instr, directory, **kwargs)
        # The runtime output directory used *can not* exist for McStas/McXtrace to work properly.
        # So find a name inside this directory that doesn't exist (any name should work)
        return mccode_run_compiled(binary, target, Path(directory).joinpath('t'), parameters) if run else (None, None)
