def mcstas_script_parse():
    from argparse import ArgumentParser
    from pathlib import Path

    def resolvable(name: str):
        return Path(name).resolve()

    parser = ArgumentParser(prog='mcstas', description='Convert mccode-3 instr and comp files to mcstas runtime in C')
    parser.add_argument('filename', type=resolvable, help='.instr file name to be converted')

    args = parser.parse_args()

    return args.filename


def mcstas_script():
    from mccode.reader import Reader, MCSTAS_REGISTRY
    filename = mcstas_script_parse()

    reader = Reader(registries=[MCSTAS_REGISTRY])

    instrument = reader.get_instrument(filename)

    # Now write out the translated instrument in the McStas runtime
    print(instrument)


if __name__ == '__main__':
    mcstas_script()
