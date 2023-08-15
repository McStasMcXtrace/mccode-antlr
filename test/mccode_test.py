from dataclasses import dataclass, field
from datetime import timedelta
from pathlib import Path
from typing import Self

from numpy import nan

from mccode.reader import Registry


@dataclass
class TestInstrExample:
    """Holds parameters for a single instr file %Example: test case"""
    sourcefile: Path
    testnb: int
    parvals: str = ""
    detector: str = ""
    targetval: float = nan
    testval: float = nan
    compiled: bool = False
    compiletime: timedelta = field(default_factory=timedelta)
    didrun: bool = False
    runtime: timedelta = field(default_factory=timedelta)
    errmsg: str = ""

    @classmethod
    def list_from_file(cls, filename: Path) -> list[Self]:
        import re
        rspec = re.compile(f'%Example:([^\n]*)Detector:([^\n]*)_I=([0-9.+-e]+)')
        with open(filename, 'r') as file:
            contents = file.read()
            matches = rspec.findall(contents)
        if len(matches):
            groups = [(m[0].strip(), m[1].strip(), float(m[2].strip())) for m in matches]
            return [cls(filename, i+1, p, d, t) for i, (p, d, t) in enumerate(groups)]
        return [cls(filename, 1)]

    def get_display_name(self):
        return f'{self.sourcefile.stem}_{self.testnb}' if self.testnb > 1 else self.sourcefile.stem

    def get_json_repr(self):
        jr = dict(displayname=self.get_display_name(),
                  sourcefile=self.sourcefile,
                  testnb=self.testnb,
                  parvals=self.parvals,
                  detector=self.detector,
                  targetval=self.targetval,
                  testval=self.testval,
                  compiled=self.compiled,
                  compiletime=self.compiletime,
                  didrun=self.didrun,
                  runtime=self.runtime,
                  errmsg=self.errmsg)
        return jr

    def save(self, path: Path):
        import json
        with open(path.joinpath(self.get_display_name() + '.json'), 'w') as file:
            json.dump(self.get_json_repr(), file)


@dataclass
class LineLogger:
    lines: list = field(default_factory=list)

    def logline(self, line: str):
        self.lines.append(line)

    def save(self, filename: Path):
        with open(filename, 'w') as file:
            file.write('\n'.join(self.lines))
            file.write('\n')

    def find(self, search: str):
        import re
        for line in self.lines:
            if re.search(search, line):
                return True
        return False


def get_cpu_name():
    from platform import system
    from subprocess import check_output
    if system() == "Windows":
        from platform import processor
        return processor()
    elif system() == "Darwin":
        from os import environ, pathsep
        environ['PATH'] = environ['PATH'] + pathsep + '/usr/sbin'
        command = "sysctl -n machdep.cpu.brand_string"
        return check_output(command).strip()
    elif system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                from re import sub
                return sub(".*model name.*:", "", line, 1).strip()
    return ""


def get_nvidia_gpu_name():
    """Identify GPU (Uses GPUtil which only knows about Nvidia GPUs)"""
    import GPUtil
    gpus = GPUtil.getGPUs()
    names = ','.join(gpu.name for gpu in gpus)
    return names if len(names) else "none"


def get_hostname():
    import socket
    return socket.gethostname()


def get_username():
    import os
    import pwd
    info = pwd.getpwuid(os.getuid())
    # Return the full name 'pw_gecos' if present, otherwise the username 'pw_name'
    return info[4] if len(info[4]) else info[0]


def _monitor_name_file_name_match(folder, monitor_name):
    import re
    look_for_filename = False
    with open(folder.joinpath('mccode.sim'), 'r') as file:
        lines = file.readlines()
    for line in lines:
        if re.match(rf"\s*component:\s*{monitor_name}$", line):
            look_for_filename = True
        if look_for_filename:
            m = re.match(r'\s*filename:\s+(.+)', line)
            if m:
                filename = folder.joinpath(m.group(1))
                if filename.is_file():
                    return filename
            if re.match('end data', line):
                # try the monitor named dat file
                zero_d_filename = folder.joinpath(monitor_name + '.dat')
                if zero_d_filename.is_file():
                    return zero_d_filename
                return None
    return None


def mccode_test_compiler(work_dir, file_path, c_compiler, c_flags, extension, registry, generator, config):
    from pathlib import Path
    from mccode.reader import Reader
    from mccode.compiler.c import compile_instrument
    # only the provided (remote) registry should be necessary for test instruments
    reader = Reader(registries=[registry])
    instrument = reader.get_instrument(file_path)
    options = {'compiler': c_compiler, 'flags': c_flags, 'output': Path(work_dir).joinpath(instrument.name + extension)}
    try:
        binary_path = compile_instrument(instrument, options, registry=registry, generator=generator, config=config)
    except RuntimeError:
        return False, Path()
    return True, binary_path


def mccode_c_settings():
    import platform
    system = platform.system()
    config = dict(default_main=True, enable_trace=False, portable=False, include_runtime=True,
                  embed_instrument_file=False, verbose=False)
    if system == "Linux":
        return "gcc", [], ".out", config
    elif system == "Darwin":
        return "clang", [], ".out", config
    elif system == "Windows":
        return "mingw", [], ".exe", config
    return platform.python_compiler().split()[0].lower(), [], "", config


def mcstas_test_compiler(work_dir, file_path):
    from mccode.reader import MCSTAS_REGISTRY
    from mccode.translators.target import MCSTAS_GENERATOR
    cc, flags, ext, config = mccode_c_settings()
    return mccode_test_compiler(work_dir, file_path, cc, flags, ext, MCSTAS_REGISTRY, MCSTAS_GENERATOR, config)


def mcxtrace_test_compiler(work_dir, file_path):
    from mccode.reader import MCXTRACE_REGISTRY
    from mccode.translators.target import MCXTRACE_GENERATOR
    cc, flags, ext, config = mccode_c_settings()
    return mccode_test_compiler(work_dir, file_path, cc, flags, ext, MCXTRACE_REGISTRY, MCXTRACE_GENERATOR, config)


def mccode_runner(binary_path, parameters: str):
    from tempfile import mkdtemp
    from subprocess import run, CalledProcessError
    output_path = mkdtemp(prefix=binary_path.stem, dir=binary_path.parent.resolve())
    command = [str(binary_path.resolve()), *(parameters.split()), '--dir', output_path]
    try:
        proc = run(command, check=True, capture_output=True)
    except CalledProcessError as error:
        return False, str(error), output_path
    return True, proc.stdout, output_path


def mccode_test(compiler, runner, registry: Registry, search_pattern=None, instr_count=None,
                skip_non_test: bool = False):
    """Run McCode instrument test(s) using the provided `compiler` and `runner` functions to handle those tasks.

    Each takes the expected working directory name (a string) and the path to the instr file as input.
    The compiler should return only a boolean success indication.
    The runner should return a boolean success indicator, the contents of the run standard output, and the directory
    (if any) used to store run output files -- these files are intended to reside below the working directory and will
    be automatically removed by this function.

    Parameters:
        compiler: a function taking a string and Path and producing the necessary runtime executable
        runner: a function taking a string and Path and running the executable, storing its output
        registry: a Registry object which knows where to find all 'examples/*' instr files
        search_pattern: an optional positive filter for the registered 'examples/*' instr files
        instr_count: an optional positive count of filtered instr files to include
        skip_non_test: a flag to control whether instr files which do not specify test cases should be compiled and run
    """
    import re
    import logging
    import tempfile
    from datetime import datetime
    logging.info(f"Finding test instruments in: {registry}")
    # we _require_ that all test instr files are in a folder called "examples" ...
    filenames = registry.match(re.compile('examples'))
    # allow the user to limit which test cases can be found via a regular expression search
    if search_pattern is not None:
        if not isinstance(search_pattern, re.Pattern):
            search_pattern = re.compile(search_pattern)
        filenames = [x for x in filenames if search_pattern.search(x) is not None]
    # optionally test case count limiter:
    if instr_count is not None and isinstance(instr_count, int) and instr_count > 0:
        filenames = filenames[:instr_count]

    # grab full paths to each file (in case this is a remote registry and they need to be fetched)
    filepaths = [registry.path(filename) for filename in filenames]

    longest_name = max(len(x.stem) for x in filepaths)

    # Build test objects from the '%Example:' line(s) in each file:
    tests = [x for filepath in filepaths for x in TestInstrExample.list_from_file(filepath)]

    binaries = dict()

    # Move into a temporary directory to ensure compilation/run times are from scratch
    with tempfile.TemporaryDirectory() as workdir:
        logging.info("Compiling instruments")
        for test in tests:
            if test.sourcefile not in binaries and (test.testnb != 0 or not skip_non_test):
                t1 = datetime.now()
                binaries[test.sourcefile] = compiler(workdir, test.sourcefile)
                test.compiletime = datetime.now() - t1

                if binaries[test.sourcefile][0]:
                    logging.info(f'%-{test.sourcefile.stem:>{longest_name}s}: {test.compiletime}')
                else:
                    logging.info(f'%-{test.sourcefile.stem:>{longest_name}s}: COMPILE ERROR')
            else:
                logging.info(f'%-{test.sourcefile.stem:>{longest_name}s}: COMPILE skipped')

        logging.info("Running tests")
        for test in tests:
            if not binaries.get(test.sourcefile, (False, None))[0]:
                logging.info(f'%-{test.sourcefile.stem:>{longest_name}s}: No compile')
                continue
            if test.testnb < 1:
                logging.info(f'%-{test.sourcefile.stem:>{longest_name}s}: No test')
                continue

            t1 = datetime.now()
            test.didrun, stdout, output_dir = runner(binaries[test.sourcefile][1], test.parvals)
            test.runtime = datetime.now() - t1

            if test.didrun:
                logging.info(f'%-{test.sourcefile.stem:>{longest_name}s}: {test.runtime}')
            else:
                logging.info(f'%-{test.sourcefile.stem:>{longest_name}s}: RUNTIME ERROR')
                continue

            detector_output = _monitor_name_file_name_match(output_dir, test.detector)
            test.testval = - 1
            if detector_output is None or not detector_output.is_file():
                rdet = re.compile(f'{test.detector}_I= ([0-9+-eE.]+)')
                matches = rdet.findall(stdout)
                if len(matches):
                    test.testval = float(matches[0][0])
            else:
                with open(detector_output, 'r') as detector_file:
                    detector_lines = detector_file.readlines()
                detector_pattern = re.compile('#values: ([0-9+-e.]+) ([0-9+-e.]+) ([0-9]+)')
                detector_matches = [detector_pattern.match(line) for line in detector_lines]
                detector_matches = [dm for dm in detector_matches if dm is not None]
                if len(detector_matches):
                    test.testval = float(detector_matches[0].group(1))

            test.testcomplete = True

    # Since we let the context manager control the output directories, save the test results ... here?
    for test in tests:
        test.save(Path())

    results = {t.get_display_name(): t.get_json_repr() for t in tests}
    # the 'ncount' and 'mpi' keys should be defined elsewhere
    results['_meta'] = {'date': datetime.now().isoformat(), 'hostname': get_hostname(),
                        'user': get_username(), 'cpu_type': get_cpu_name(), 'gpu_type': get_nvidia_gpu_name()}
    return results


def mcstas_test(search_pattern=None, instr_count=None, skip_non_test: bool = False):
    from mccode.reader import MCSTAS_REGISTRY as REGISTRY
    return mccode_test(mcstas_test_compiler, mccode_runner, REGISTRY, search_pattern, instr_count, skip_non_test)


def mcxtrace_test(search_pattern=None, instr_count=None, skip_non_test: bool = False):
    from mccode.reader import MCXTRACE_REGISTRY as REGISTRY
    return mccode_test(mcxtrace_test_compiler, mccode_runner, REGISTRY, search_pattern, instr_count, skip_non_test)
