def main():
    from argparse import ArgumentParser
    from .builder import _ensure_antlr_files_up_to_date_on_import

    parser = ArgumentParser(prog="mccode-antlr-build", description='Ensure ANTLR files are up-to-date')
    parser.add_argument('--verbose', action='store_true', help='Print out more information')
    args = parser.parse_args()
    verbose = args.verbose

    _ensure_antlr_files_up_to_date_on_import('McComp', deps=('McCommon', 'cpp'), verbose=verbose)
    _ensure_antlr_files_up_to_date_on_import('McInstr', deps=('McCommon', 'cpp'), verbose=verbose)
    _ensure_antlr_files_up_to_date_on_import('C', verbose=verbose)

if __name__ == '__main__':
    main()
