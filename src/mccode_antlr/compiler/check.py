from __future__ import annotations
from functools import cache

def subprocess_fails(args: list[str]):
    import subprocess
    try:
        subprocess.run(args, check=True)
        return False
    except FileNotFoundError:
        pass
    except RuntimeError:
        pass
    return True


@cache
def check_for_mccode_antlr_compiler(which: str) -> bool:
    from loguru import logger
    from ..config import config
    cc = config
    for key in which.split('/'):
        cc = cc[key]
    cc = cc.get(str)

    # different compilers support different 'version' or 'help' command line options
    options = '--version', '/?', '--help'
    if all(subprocess_fails([cc, opt]) for opt in options):
        logger.info(f"Compiler '{cc}' not found.")
        which = which.replace('/','_')
        logger.info(f'Provide alternate via MCCODE_ANTLR_{which} environment variable')
        return False
    return True


def compiles(compiler: str, instr):
    from os import access, R_OK
    from loguru import logger
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from subprocess import run
    from mccode_antlr.translators.target import MCSTAS_GENERATOR
    from .c import CBinaryTarget, get_compiler_linker_flags, instrument_source
    from ..config import config as module_config

    target = CBinaryTarget(mpi='mpi' in compiler, acc=compiler == 'acc', count=1, nexus=False)

    compile_config = dict(default_main=True, enable_trace=False, portable=False,
                  include_runtime=True, embed_instrument_file=False, verbose=False)

    compiler_flags, linker_flags = get_compiler_linker_flags(instr, target)

    with TemporaryDirectory() as directory:
        binary = Path(directory) / f"output{module_config['ext'].get(str)}"
        command = [target.compiler, *compiler_flags, '-o', str(binary), '-', *linker_flags]
        source = instrument_source(instr, generator=MCSTAS_GENERATOR, config=compile_config)
        result = run(command, input=source, text=True, capture_output=True)

        if result.returncode:
            logger.info(f'Failed compiling simple instrument with error: {result.stderr}')
            logger.info(f"Verify compiler {target.compiler} accepts {compiler_flags} and linker accepts {linker_flags}")
            return False
        if not binary.exists() or not binary.is_file() or not access(binary, R_OK):
            logger.info(f"Compilation did not produce an executable output file, check that {target.compiler} works")
            return False

    return True


@cache
def simple_instr_compiles(which: str) -> bool:
    from subprocess import CalledProcessError
    if not check_for_mccode_antlr_compiler(which):
        return False
    try:
        from mccode_antlr.loader import parse_mcstas_instr
        instr = parse_mcstas_instr("define instrument check() trace component a = Arm() at (0,0,0) absolute end")
        return compiles(which, instr)
    except RuntimeError:
        return False
    except FileNotFoundError:
        return False
    except CalledProcessError:
        return False


def compiled(method, compiler: str | None = None):
    from unittest import TestCase
    if compiler is None:
        # Basic compiled instruments only need the 'cc' compiler specified in the config file
        compiler = 'cc'

    def wrapper(*args, **kwargs):
        if simple_instr_compiles(compiler):
            return method(*args, **kwargs)
        elif isinstance(args[0], TestCase):
            args[0].skipTest(f'Skipping due to lack of working ${compiler}')
        else:
            raise RuntimeError(f'A working compiler is required to use function {method.__name__}')

    return wrapper


def gpu_only(method):
    from loguru import logger
    # GPU compiled instruments need the specific OpenACC compiler
    # **PLUS** they need to _actually_ have the openACC header (macOS and Windows don't use different compilers)
    return compiled(method, 'acc')


def mpi_only(method):
    # MPI compiled instruments need the specified compiler
    return compiled(method, 'mpi/cc')
