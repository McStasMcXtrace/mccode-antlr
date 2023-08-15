"""Handles compilation of C translated instruments into usable binaries"""
from mccode.reader import Reader
from mccode.instr import Instr
from mccode.translators.c import CTargetVisitor


def instrument_source(instrument: Instr, generator: dict, config: dict, verbose: bool = None):
    if verbose is None:
        verbose = config.get('verbose', False)
    # TargetVisitor to uses instrument.registries (and the CTargetVisitor *appends* its LIBC_REGISTRY if necessary)
    visitor = CTargetVisitor(instrument, generate=generator, config=config, verbose=verbose)
    # Does the conversion by 'visiting' the instrument, then returns the full string of the generated source code
    return visitor.contents()


def compile_instrument(instrument: Instr, options: dict, **kwargs):
    from os import environ, R_OK, access
    from subprocess import run, CalledProcessError
    from pathlib import Path
    # determine a name for the binary file
    path = options.get('output', Path().joinpath(instrument.name))
    if not isinstance(path, Path):
        # if output was provided as a string:
        path = Path(path)
    if path.exists() and not options.get('recompile', False):
        raise RuntimeError(f"Output {path} exists but recompile is not requested.")

    # make the compiled version of the instrument:
    compiler = options.get('compiler', environ.get('CC'))
    if compiler is None:
        raise RuntimeError('Provide a compiler or specify the environment variable CC')
    # the flags '-x c -' probably only work for gcc/clang -- hopefully more:
    stdin_flags = options.get('stdin_flags', ['-x', 'c', '-'])

    command = [compiler, *instrument.flags, '-o', str(path)] + stdin_flags
    try:
        run(command, input=instrument_source(instrument, **kwargs), text=True, check=True)
    except CalledProcessError as error:
        raise RuntimeError(f'Compilation failed, raising error {error}')

    if not path.exists():
        raise RuntimeError(f"Compilation should have produced {path}, but it does not appear to exist")
    if not access(path, R_OK):
        raise RuntimeError(f"{path} exists but is not an executable")

    return path
