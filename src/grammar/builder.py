from __future__ import annotations
from loguru import logger
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


def rebuild_language(grammar_file,
                     target: Target,
                     features: list[Feature],
                     verbose=False,
                     ):
    from pathlib import Path
    from subprocess import Popen, PIPE
    from antlr4_tool_runner import initialize_paths, install_jre_and_antlr
    from antlr4_tool_runner import process_args

    def antlr4_version():
        return process_args()[1]

    if not isinstance(grammar_file, Path):
        grammar_file = Path(grammar_file)

    args =[
        f'-Dlanguage={target}',
        '-visitor' if Feature.visitor in features else '-no-visitor',
        '-listener' if Feature.listener in features else '-no-listener',
        '-o', str(grammar_file.parent / str(target)),
        str(grammar_file)
    ]

    if verbose:
        logger.info(f'Building language files for {grammar_file}')

    # The following copies the implementation of antlr4_tool_runner.tool, which pulls `args` from the system argv list
    # Setup:
    initialize_paths()
    version = antlr4_version()
    jar, java = install_jre_and_antlr(version)
    # Call antlr4
    p = Popen([java, '-cp', jar, 'org.antlr.v4.Tool'] + args, stdout=PIPE, stderr=PIPE)
    out, err = [x.decode('UTF-8') for x in p.communicate()]
    if err:
        print(err, end='')
    if out:
        print(out, end='')


def language_present_and_up_to_date(grammar_file, newest, verbose=False):
    from pathlib import Path
    if not isinstance(grammar_file, Path):
        grammar_file = Path(grammar_file)

    if not grammar_file.exists():
        raise RuntimeError(f"The grammar file {grammar_file} does not exist.")

    root = grammar_file.parent
    lexer_file = root.joinpath(f'{grammar_file.stem}Lexer.py')
    parser_file = root.joinpath(f'{grammar_file.stem}Parser.py')
    listener_file = root.joinpath(f'{grammar_file.stem}Listener.py')
    visitor_file = root.joinpath(f'{grammar_file.stem}Visitor.py')

    generated_files = lexer_file, parser_file, listener_file, visitor_file

    if not all(x.exists() for x in generated_files):
        if verbose:
            logger.info(f'Not all language files exist for {grammar_file}')
        return False

    if any(x.stat().st_mtime < newest for x in generated_files):
        if verbose:
            logger.info(f'Not all language files up-to-date for {grammar_file}')
        return False

    if verbose:
        logger.info(f'Language files for {grammar_file} are up-to-date')
    return True


def rebuild_speedy_language(grammar_file, features: list[Feature], verbose=False):
    from speedy_antlr_tool import generate

    rebuild_language(grammar_file, Target.cpp, features, verbose=verbose)
    rebuild_language(grammar_file, Target.python, [], verbose=verbose)

    py_parser_path = grammar_file.parent / str(Target.python) / f'{grammar_file.stem}Parser.py'
    cpp_output_dir = grammar_file.parent / str(Target.cpp)
    generate(py_parser_path, cpp_output_dir)


def ensure_language_up_to_date(
        grammar: str,
        *,
        target: Target,
        features: list[Feature],
        deps=None,
        verbose=False,
        speed=False,
):
    """Ensure the ANTLR parsed language files are up-to-date."""
    from pathlib import Path
    grammar_file = Path(__file__).parent.joinpath(f'{grammar}.g4')

    newest = grammar_file.stat().st_mtime
    if deps:
        for dep in deps:
            newest = max(newest, Path(__file__).parent.joinpath(f'{dep}.g4').stat().st_mtime)

    if not language_present_and_up_to_date(grammar_file, newest, verbose=verbose):
        if speed:
            rebuild_speedy_language(grammar_file, features, verbose=verbose)
        else:
            rebuild_language(grammar_file, target, features, verbose=verbose)


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser(prog="mccode-antlr-build", description='Ensure ANTLR files are up-to-date')
    parser.add_argument('-v ', '--verbose', action='store_true', help='Print out more information')
    args = parser.parse_args()
    verbose = args.verbose

    ensure_language_up_to_date('McComp', target=Target.python, features=[Feature.visitor], deps=('McCommon', 'cpp'), verbose=verbose, speed=True)
    ensure_language_up_to_date('McInstr', target=Target.python, features=[Feature.visitor], deps=('McCommon', 'cpp'), verbose=verbose, speed=True)
    ensure_language_up_to_date('C', target=Target.python, features=[Feature.visitor, Feature.listener], verbose=verbose)

if __name__ == '__main__':
    main()
