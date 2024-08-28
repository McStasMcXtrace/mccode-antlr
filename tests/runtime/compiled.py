from __future__ import annotations
from functools import cache
from unittest import TestCase


@cache
def check_for_mccode_antlr_compiler(which: str) -> bool:
    import subprocess
    from loguru import logger
    from mccode_antlr.config import config
    cc = config
    for key in which.split('/'):
        cc = cc[key]
    cc = cc.get(str)

    try:
        subprocess.run([cc, '--version'], check=True)
        return True
    except FileNotFoundError:
        logger.info(f'Expected compiler {cc} not found.')
        logger.info('Provide alternate C compiler via MCCODE_ANTLR_CC environment variable')
    return False


@cache
def simple_instr_compiles(which: str) -> bool:
    if check_for_mccode_antlr_compiler(which):
        try:
            from mccode_antlr.loader import parse_mcstas_instr
            instr = parse_mcstas_instr("define instrument check() trace component a = Arm() at (0,0,0) absolute end")
            compile_and_run(instr, "-n 1", run=False, target={'acc': which == 'acc'})
        except RuntimeError:
            return False
        except FileNotFoundError:
            return False
    return True


def compiled(method, compiler: str | None = None):
    if compiler is None:
        # Basic compiled instruments only need the 'cc' compiler specified in the config file
        compiler = 'cc'

    def wrapper(*args, **kwargs):
        if simple_instr_compiles(compiler):
            method(*args, **kwargs)
        elif isinstance(args[0], TestCase):
            args[0].skipTest(f'Skipping due to lack of working ${compiler}')

    return wrapper


def gpu_only(method):
    # GPU compiled instruments need the specific OpenACC compiler
    # **PLUS** they need to _actually_ have the openACC header (macOS and Windows don't use different compilers)
    return compiled(method, 'acc')


def mpi_only(method):
    # MPI compiled instruments need the specified compiler
    return compiled(method, 'mpi/cc')


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
