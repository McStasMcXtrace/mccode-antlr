def mcstas_script_parse():
    from argparse import ArgumentParser
    from pathlib import Path

    def resolvable(name: str):
        return Path(name).resolve()

    parser = ArgumentParser(prog='mcstas', description='Convert mccode-3 instr and comp files to mcstas runtime in C')
    parser.add_argument('filename', type=resolvable, help='.instr file name to be converted')

    parser.add_argument('-o', '--output-file', type=str, help='Output filename for C runtime file')
    parser.add_argument('-I', '--search-dir', type=resolvable, help='Extra component search directory')
    parser.add_argument('-t', '--trace', action='store', help="Enable 'trace' mode for instrument display")
    parser.add_argument('-p', '--portable', action='store', help='No idea. Your guess is better than mine.')
    parser.add_argument('-v', '--version', action='store', help='Print the McCode version')
    parser.add_argument('--source', action='store', help='Embed the instrument source code in the executable')
    parser.add_argument('--no-main', action='store', help='Do not create main(), for external embedding')
    parser.add_argument('--no-runtime', action='store', help='Do not embed run-time libraries')
    parser.add_argument('--verbose', action='store', help='Verbose output during conversion')

    args = parser.parse_args()

    if args.version:
        from sys import exit
        from mccode import __version__
        print(f'mccode code generator version {__version__}')
        print(' Copyright (c) European Spallation Source ERIC, 2023')
        print('Based on McStas/McXtrace version 3')
        print(' Copyright (c) DTU Physics and Risoe National Laboratory, 1997-2023')
        print(' Additions (c) Institut Laue Langevin, 2003-2019')
        print('All rights reserved\n\nComponents are (c) their authors, see component headers.')
        exit(1)

    return args


def mcstas_script():
    from mccode.reader import Reader, MCSTAS_REGISTRY
    from mccode.reader import LocalRegistry
    from mccode.translators.c import CTargetVisitor
    from mccode.translators.target import MCSTAS_GENERATOR

    args = mcstas_script_parse()

    config = dict(default_main=(not args.no_main) if args.no_main is not None else True,
                  enable_trace=args.trace if args.trace is not None else False,
                  portable=args.portable if args.portable is not None else False,
                  include_runtime=(not args.no_runtime) if args.no_runtime is not None else True,
                  embed_instrument_file=args.source if args.source is not None else False,
                  verbose=args.verbose if args.verbose is not None else False,
                  output=args.output_file if args.output_file is not None else args.filename.with_suffix('.c')
                  )

    # TODO somehow pull out extra search directories into LocalRegistries
    registries = [MCSTAS_REGISTRY]
    if args.search_dir is not None:
        registries.append(LocalRegistry(args.searchdir.stem, args.searchdir))

    reader = Reader(registries=registries)

    instrument = reader.get_instrument(args.filename)

    # Now write out the translated instrument in the McStas runtime
    print(instrument)

    visitor = CTargetVisitor(instrument, generate=MCSTAS_GENERATOR, config=config, verbose=config['verbose'],
                             registries=reader.registries)
    # Go through the instrument, finish by writing the output file:
    visitor.translate(filename=config['output'])


if __name__ == '__main__':
    mcstas_script()
