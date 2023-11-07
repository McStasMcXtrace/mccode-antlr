from zenlog import log

def rebuild_language(grammar_file, verbose=False):
    from pathlib import Path
    from subprocess import Popen, PIPE
    from antlr4_tool_runner import initialize_paths, get_version_arg, install_jre_and_antlr

    if not isinstance(grammar_file, Path):
        grammar_file = Path(grammar_file)

    # Do the McCode*.py files not exist? Or are they older than McCode.g4?
    # Then build them using ANTLR4:
    args = ['-Dlanguage=Python3', str(grammar_file), '-listener', '-visitor', '-o', str(grammar_file.parent)]

    # The following copies the implementation of antlr4_tool_runner.tool, which pulls `args` from the system argv list
    # Setup:
    initialize_paths()
    args, version = get_version_arg(args)
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
            log.info(f'Not all language files exist for {grammar_file}')
        return False

    if any(x.stat().st_mtime < newest for x in generated_files):
        if verbose:
            log.info(f'Not all language files up-to-date for {grammar_file}')
        return False

    if verbose:
        log.info(f'Language files for {grammar_file} are up-to-date')
    return True


def _ensure_antlr_files_up_to_date_on_import(grammar, deps=None, verbose=False):
    """Run on import of this (sub)module. Ensure the ANTLR parsed language files are up-to-date."""
    from pathlib import Path
    grammar_file = Path(__file__).parent.joinpath(f'{grammar}.g4')

    newest = grammar_file.stat().st_mtime
    if deps:
        for dep in deps:
            newest = max(newest, Path(__file__).parent.joinpath(f'{dep}.g4').stat().st_mtime)

    if not language_present_and_up_to_date(grammar_file, newest, verbose=verbose):
        rebuild_language(grammar_file, verbose=verbose)
