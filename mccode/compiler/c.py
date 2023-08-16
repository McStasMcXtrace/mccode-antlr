"""Handles compilation of C translated instruments into usable binaries"""
from dataclasses import dataclass
from enum import Enum, Flag, auto
from typing import Union
from pathlib import Path
from mccode.instr import Instr
from mccode.translators.c import CTargetVisitor


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


    @property
    def compiler(self) -> str:
        from mccode.config import config
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
        from mccode.config import config
        if self.type & CBinaryTarget.Type.acc:
            # acc *or* acc + mpi uses the OpenACC compiler *and* flags
            return config['flags']['acc'].as_str_expanded().split()
        # otherwise use the standard compiler flags
        return config['flags']['cc'].as_str_expanded().split()

    @property
    def extra_flags(self) -> list[str]:
        """Only a little confusing ..."""
        from mccode.config import config
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


def compile_instrument(instrument: Instr, target: CBinaryTarget, output: Union[str, Path] = None,
                       recompile: bool = False, **kwargs):
    from os import R_OK, access
    from subprocess import run, CalledProcessError
    from mccode.config import config
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

    if output.exists() and not recompile:
        raise RuntimeError(f"Output {output} exists but recompile is not requested.")

    # the type of binary requested determines (some of) the required flags:
    flags = target.flags + target.extra_flags
    # the flags in an instrument *might* contain ENV, CMD, GETPATH directives which need to be expanded via decode:
    flags.extend([word for flag in instrument.decoded_flags() for word in flag.split()])

    # Why is this addition necessary?
    if any('OPENACC' in word for word in flags) and any('NeXus' in word for word in flags):
        flags.append('-D__GNUC__')

    command = [target.compiler, *target.flags, *flags, '-o', str(output), '-']
    try:
        run(command, input=instrument_source(instrument, **kwargs), text=True, check=True)
    except CalledProcessError as error:
        raise RuntimeError(f'Compilation failed, raising error {error}')

    if not output.exists():
        raise RuntimeError(f"Compilation should have produced {output}, but it does not appear to exist")
    if not access(output, R_OK):
        raise RuntimeError(f"{output} exists but is not an executable")

    return output


def run_compiled_instrument(binary: Path, target: CBinaryTarget, options: str, capture=False):
    from subprocess import run, CalledProcessError
    from platform import system
    from mccode.config import config

    # If NeXus output is requested and the InstrumentDescriptionFile is needed, run a different script entirely...
    #   TODO think about actually doing this?
    # if target.flags & CBinaryTarget.Type.nexus and idf_required:
    #     run([config['idfgen'].get(str), str(binary), *options])

    command = []
    if target.flags & CBinaryTarget.Type.mpi:
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
        if target.flags & CBinaryTarget.Type.acc and 'Windows' != system():
            # Each worker should have the environment variable CUDA_VISIBLE_DEVICES defined as the value of
            # OMPI_COMM_WORLD_LOCAL_RANK, which gets sent by MPI to the worker. This assigment must take place
            # *on* the worker, which requires hijacking the executable that MPI runs
            command.append('acc_gpu_bind')
            raise NotImplementedError('CUDA GPU binding not yet implemented')

    # In normal operation, the binary is provided with options
    command.extend([str(binary), *options.split()])
    # which we then execute:
    try:
        proc = run(command, check=True, capture_output=capture)
    except CalledProcessError as error:
        raise RuntimeError(f'Execution of {command} failed with error {error}')

    return proc.stdout if capture else ""