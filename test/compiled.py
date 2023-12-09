from __future__ import annotations
from functools import cache
from unittest import TestCase


@cache
def check_for_mccode_antlr_compiler(which: str) -> bool:
    import subprocess
    from zenlog import log
    from mccode_antlr.config import config
    cc = config
    for key in which.split('/'):
        cc = cc[key]
    cc = cc.get(str)

    try:
        subprocess.run([cc, '--version'], check=True)
        return True
    except FileNotFoundError:
        log.info(f'Expected compiler {cc} not found.')
        log.info('Provide alternate C compiler via MCCODE_ANTLR_CC environment variable')
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


def compile_and_run(instr, parameters, run=True, dump_source=True,
                    target: dict | None = None, config: dict | None = None):
    from mccode_antlr.compiler.c import compile_instrument, CBinaryTarget, run_compiled_instrument
    from mccode_antlr.translators.target import MCSTAS_GENERATOR
    from mccode_antlr.loader import read_mccode_dat
    from mccode_antlr.config import config as module_config
    from tempfile import TemporaryDirectory
    from os import R_OK, access
    from pathlib import Path
    from zenlog import log

    def_target = CBinaryTarget(mpi=False, acc=False, count=1, nexus=False)
    def_config = dict(default_main=True, enable_trace=False, portable=False, include_runtime=True,
                      embed_instrument_file=False, verbose=False)
    def_config.update(config or {})
    def_target.update(target or {})

    with TemporaryDirectory() as directory:
        try:
            compile_instrument(instr, def_target, directory,
                               generator=MCSTAS_GENERATOR, config=def_config, dump_source=dump_source)
        except RuntimeError as e:
            log.error(f'Failed to compile instrument: {e}')
            raise e
        binary = Path(directory).joinpath(f'{instr.name}{module_config["ext"].get(str)}')

        if not binary.exists() or not binary.is_file() or not access(binary, R_OK):
            raise FileNotFoundError(f"No executable binary, {binary}, produced")

        if run:
            result = run_compiled_instrument(binary, def_target, f"--dir {directory}/instr {parameters}",
                                             capture=True)
            sim_files = list(Path(directory).glob('**/*.dat'))
            dats = {file.stem: read_mccode_dat(file) for file in sim_files}
            return result, dats
        return None, None
