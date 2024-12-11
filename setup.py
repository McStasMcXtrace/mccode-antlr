from __future__ import annotations

from setuptools import Command, setup
import setuptools.command.build

from pathlib import Path
from enum import Enum

class Target(Enum):
    python = 0
    cpp = 1
    def __str__(self):
        if self == Target.python:
            return 'Python3'
        elif self == Target.cpp:
            return 'Cpp'
        raise ValueError(f'Unknown target {self}')


class Feature(Enum):
    listener = 0
    visitor = 1
    lexer = 2
    parser = 3
    def __str__(self):
        if self == Feature.listener:
            return 'Listener'
        if self == Feature.visitor:
            return 'Visitor'
        if self == Feature.lexer:
            return 'Lexer'
        if self == Feature.parser:
            return 'Parser'


def BuildANTLRCommand(source: Path, destination: str, grammars):

    def antlr4_runtime_version():
        """Retrieve the ANTLR4 version used by the available antlr4-python3-runtime"""
        from importlib import metadata
        try:
            return metadata.metadata('antlr4-python3-runtime').get('version')
        except metadata.PackageNotFoundError:
            raise RuntimeError("antlr4-python3-runtime is a build dependency!")

    def build_language(grammar_file: Path,
                       target: Target,
                       features: list[Feature],
                       output=None,
                       ):
        from subprocess import run
        from antlr4_tool_runner import initialize_paths, install_jre_and_antlr
        args = [
            f'-Dlanguage={target}',
            '-visitor' if Feature.visitor in features else '-no-visitor',
            '-listener' if Feature.listener in features else '-no-listener',
            '-o', output.resolve(),
            grammar_file.name
        ]
        print(f"Generating ANTLR {target} {' '.join(str(f) for f in features)} in {output} for {grammar_file}")
        # The following copies the implementation of antlr4_tool_runner.tool,
        # which pulls `args` from the system argv list
        initialize_paths()
        jar, java = install_jre_and_antlr(antlr4_runtime_version())
        run([java, '-cp', jar, 'org.antlr.v4.Tool'] + args, cwd=grammar_file.parent)

    class BuildANTLR(Command):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.build_lib = None
            self.editable_mode = False

        def initialize_options(self):
            """Initialize command state to defaults"""
            ...

        def finalize_options(self):
            """
            Populate the command state. This is where I traverse the directory
            tree to search for the *.ksc files to compile them later.
            The self.set_undefined_options is used to inherit the `build_lib`
            attribute from the `build_py` command.
            """
            self.set_undefined_options("build_py", ("build_lib", "build_lib"))

        def run(self):
            """
            Perform actions with side-effects, such as invoking a ksc to python compiler.
            The directory to which outputs are written depends on `editable_mode` attribute.
            When editable_mode == False, the outputs are written to directory pointed by build_lib.
            When editable_mode == True, the outputs are written in-place,
            i.e. into the directory containing the sources.
            The `run` method is not executed during sdist builds.
            """
            dest = Path(self.build_lib) / destination
            for grammar, options in grammars.items():
                build_language(source/f'{grammar}.g4',
                               target=options['target'],
                               features=options['features'],
                               output=dest)

        def get_output_mapping(self):
            """
            Return dict mapping output file paths to input file paths
            Example:
                dict = { "build/lib/output.py": "src/grammar/grammar.g4" }
            """
            files = {}
            dest = Path(self.build_lib) / destination
            for grammar, options in grammars.items():
                for feature in [Feature.lexer, Feature.parser] + options['features']:
                    files[dest / f"{grammar}{feature}.py"] = source / f"{grammar}.g4"
                    if deps := options.get("deps"):
                        for dep in deps:
                            files[dest / f"{dep}{feature}.py"] = source / f"{dep}.g4"
            return {str(k): str(v) for k, v in files.items()}

        def get_outputs(self):
            """Return list containing paths to output files (generated *.py files)"""
            files = []
            dest = Path(self.build_lib) / destination
            for grammar, options in grammars.items():
                for feature in [Feature.lexer, Feature.parser] + options['features']:
                    files.append(dest / f"{grammar}{feature}.py")
                    if deps := options.get("deps"):
                        files.extend(dest / f"{dep}{feature}.py" for dep in deps)
            return [str(file) for file in files]

        def get_source_files(self):
            """Returns list containing paths to input files (*.g4 ANTLR grammars)"""
            files = []
            for grammar, options in grammars.items():
                files.append(source / f"{grammar}.g4")
                if deps := options.get("deps"):
                    files.extend(source / f"{dep}.g4" for dep in deps)
            return [str(file) for file in files]

    return BuildANTLR


setuptools.command.build.build.sub_commands.append(("build_antlr", None))

setup(cmdclass={
    "build_antlr": BuildANTLRCommand(
        source=Path() / "src" / "grammar",  # grammar file loc relative to this file
        destination="mccode_antlr/grammar", # generated file loc in build dir
        grammars={
            'McComp': {
                'target': Target.python,
                'features': [Feature.visitor],
                'deps': ('McCommon', 'c99'),
            },
            'McInstr': {
                'target': Target.python,
                'features': [Feature.visitor],
                'deps': ('McCommon', 'c99'),
            },
            'C': {
                'target': Target.python,
                'features': [Feature.visitor, Feature.listener],
            },
        },
    )
})
