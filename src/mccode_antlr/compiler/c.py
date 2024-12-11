"""Handles compilation of C translated instruments into usable binaries"""
from enum import Flag, auto
from typing import Union
from pathlib import Path
from mccode_antlr.instr import Instr
from mccode_antlr.translators.c import CTargetVisitor
from loguru import logger
from .check import compiled, gpu_only, mpi_only


class CBinaryTarget:
    class Type(Flag):
        single = auto()
        acc = auto()
        mpi = auto()
        nexus = auto()

    def __init__(self, mpi: bool = False, acc: bool = False, count: int = 1, nexus: bool = False):
        self.count = count
        if mpi and acc:
            self.type = CBinaryTarget.Type.acc | CBinaryTarget.Type.mpi
        elif mpi:
            self.type = CBinaryTarget.Type.mpi
        elif acc:
            self.type = CBinaryTarget.Type.acc
        else:
            self.type = CBinaryTarget.Type.single
        # completely orthogonal, probably a bad idea to include here at all:
        if nexus:
            self.type |= CBinaryTarget.Type.nexus

    def update(self, d: dict):
        self.count = d.get('count', self.count)
        d_mpi = d.get('mpi', self.type & CBinaryTarget.Type.mpi)
        d_acc = d.get('acc', self.type & CBinaryTarget.Type.acc)
        if d_mpi and d_acc:
            self.type = CBinaryTarget.Type.acc | CBinaryTarget.Type.mpi
        elif d_mpi:
            self.type = CBinaryTarget.Type.mpi
        elif d_acc:
            self.type = CBinaryTarget.Type.acc
        else:
            self.type = CBinaryTarget.Type.single
        if d.get('nexus', self.type & CBinaryTarget.Type.nexus):
            self.type |= CBinaryTarget.Type.nexus

    @property
    def compiler(self) -> str:
        from mccode_antlr.config import config
        if self.type & CBinaryTarget.Type.acc:
            # acc *or* acc + mpi uses the OpenACC compiler
            return config['acc'].as_str_expanded()
        elif self.type & CBinaryTarget.Type.mpi:
            # mpi (no-acc) uses the OpenMPI compiler
            return config['mpi']['cc'].as_str_expanded()
        # otherwise use the standard C compiler
        return config['cc'].as_str_expanded()

    @property
    def flags(self) -> list[str]:
        from mccode_antlr.config import config
        if self.type & CBinaryTarget.Type.acc:
            # acc *or* acc + mpi uses the OpenACC compiler *and* flags
            return config['flags']['acc'].as_str_expanded().split()
        # otherwise use the standard compiler flags
        return config['flags']['cc'].as_str_expanded().split()

    @property
    def linker_flags(self) -> list[str]:
        from mccode_antlr.config import config
        return config['flags']['ld'].as_str_expanded().split()

    @property
    def extra_flags(self) -> list[str]:
        """Only a little confusing ..."""
        from mccode_antlr.config import config
        extras = []
        if self.type & CBinaryTarget.Type.mpi:
            extras.extend(config['flags']['mpi'].as_str_expanded().split())
        if self.type & CBinaryTarget.Type.nexus:
            extras.extend(config['flags']['nexus'].as_str_expanded().split())
        return extras


def instrument_source(instrument: Instr, generator: dict, config: dict, verbose: bool = None):
    if verbose is None:
        verbose = config.get('verbose', False)
    # TargetVisitor to uses instrument.registries (and the CTargetVisitor *appends* its LIBC_REGISTRY if necessary)
    visitor = CTargetVisitor(instrument, generate=generator, config=config, verbose=verbose)
    # Does the conversion by 'visiting' the instrument, then returns the full string of the generated source code
    return visitor.contents()


def get_compiler_linker_flags(instrument: Instr, target: CBinaryTarget):
    # the type of binary requested determines (some of) the required flags:
    compiler_flags = target.flags + target.extra_flags
    linker_flags = target.linker_flags
    # the instrument-defined flags are always(?) linker flags:
    # the flags in an instrument *might* contain ENV, CMD, GETPATH directives which need to be expanded via decode:
    linker_flags.extend(
        [word for flag in instrument.decoded_flags() for word in flag.split()])

    # Why is this addition necessary?
    if any('OPENACC' in word for word in compiler_flags) and any(
            'NeXus' in word for word in compiler_flags):
        compiler_flags.append('-D__GNUC__')
    return compiler_flags, linker_flags


def _compile_instrument(
        instrument: Instr,
        target: CBinaryTarget,
        output: Union[str, Path] = None,
        replace: bool = False,
        dump_source: bool = False,
        **kwargs
):
    """Do the actual compilation -- should not be called directly by users

    Note
    ----
    If you are a user of the mccode-antlr module, call the `compile_instrument`
    gateway method instead to enable a cached check that your system compiler is
    configured correctly.
    """
    from os import R_OK, access
    from subprocess import run, CalledProcessError
    from mccode_antlr.config import config
    logger.info(f'Compile {instrument.name}')
    # determine a name and location for the binary file
    if output is None:
        # use the current working directory if nothing provided
        output = Path()
    if not isinstance(output, Path):
        # allow for a string input to be interpreted as a path
        output = Path(output)
    if output.is_dir():
        # allow for the user to specify only the output *directory*
        output = output.joinpath(instrument.name).with_suffix(config['ext'].get(str))

    if output.exists() and not replace:
        return output

    compiler_flags, linker_flags = get_compiler_linker_flags(instrument, target)

    # The solitary '-' specifies *where* the stdin source should be processed, which is critical for getting
    # linking flags right on (some) Linux systems
    command = [target.compiler, *compiler_flags, '-o', str(output), '-', *linker_flags]
    source = instrument_source(instrument, **kwargs)
    if dump_source:
        source_file = Path().joinpath(output.parts[-1]).with_suffix('.c')
        logger.info(f'Source written in {source_file}')
        with open(source_file, 'w') as cfile:
            cfile.write(source)
    result = run(command, input=source, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f"Compilation\n{command}\nfailed with output\n{result.stdout}\nand error\n{result.stderr}")
    if not output.exists():
        raise RuntimeError(f"Compilation should have produced {output}, but it does not appear to exist")
    if not access(output, R_OK):
        raise RuntimeError(f"{output} exists but is not an executable")
    return output


@gpu_only
def compile_acc_instrument(*args, **kwargs):
    return _compile_instrument(*args, **kwargs)


@mpi_only
def compile_mpi_instrument(*args, **kwargs):
    return _compile_instrument(*args, **kwargs)


@compiled
def compile_c_instrument(*args, **kwargs):
    return _compile_instrument(*args, **kwargs)


def compile_instrument(
        instrument: Instr,
        target: CBinaryTarget,
        output: Union[str, Path] = None,
        replace: bool = False,
        dump_source: bool = False,
        **kwargs
):
    """Compile an Instr object to one of the possible C targets

    Parameters
    ----------
    instrument: Instr
        The Instr to turn into a compiled binary
    target: CBinaryTarget
        The type of binary to produce: C99, OpenACC, MPI, etc.
    output:
        The path (and optionally name) where to store the produced binary
    replace:
        If true compilation will proceed even if a same-named path exists already
    dump_source:
        A diagnostic mode that outputs the generated C code into the current working
        directory
    """
    if target.type & CBinaryTarget.Type.acc:
        return compile_acc_instrument(instrument, target, output, replace, dump_source, **kwargs)
    if target.type & CBinaryTarget.Type.mpi:
        return compile_mpi_instrument(instrument, target, output, replace, dump_source, **kwargs)
    return compile_c_instrument(instrument, target, output, replace, dump_source, **kwargs)


def run_compiled_instrument(binary: Path, target: CBinaryTarget, options: str, capture=False, dry_run: bool = False):
    from subprocess import run, CalledProcessError
    from platform import system
    from mccode_antlr.config import config

    # If NeXus output is requested and the InstrumentDescriptionFile is needed, run a different script entirely...
    #   TODO think about actually doing this?
    # if target.flags & CBinaryTarget.Type.nexus and idf_required:
    #     run([config['idfgen'].get(str), str(binary), *options])

    command = []
    if target.type & CBinaryTarget.Type.mpi:
        # we execute mpirun
        command.append(config['mpi']['run'].as_str_expanded())
        # which takes optional flags
        if target.count == 0:
            print("Using system default number of mpirun processes")
        else:
            command.extend(['-np', str(target.count)])
        if config['machinefile'].exists():
            command.extend(['-machinefile', config['machinefile'].as_str_expanded()])
        # and requires trickery if we want to restrict the GPU used
        if target.type & CBinaryTarget.Type.acc and 'Windows' != system():
            # Each worker should have the environment variable CUDA_VISIBLE_DEVICES defined as the value of
            # OMPI_COMM_WORLD_LOCAL_RANK, which gets sent by MPI to the worker. This assigment must take place
            # *on* the worker, which requires hijacking the executable that MPI runs
            command.append('acc_gpu_bind')
            raise NotImplementedError('CUDA GPU binding not yet implemented')

    binary = binary.resolve()
    if not binary.exists():
        raise RuntimeError(f'Can not execute {binary} since it does not exist.')

    # In normal operation, the binary is provided with options
    command.extend([str(binary), *options.split()])
    # which we then execute:
    if dry_run:
        logger.info(f'Would execute {command}')
        return ""
    result = run(command, capture_output=capture)
    if result.returncode and capture:
        raise RuntimeError(f'Execution of {command} failed with output\n{result.stdout}\n and error\n{result.stderr}')
    elif result.returncode:
        raise RuntimeError(f'Execution of {command} failed, see above for error message(s)')

    return (result.stdout + result.stderr) if capture else ""
