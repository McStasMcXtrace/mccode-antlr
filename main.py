

def walk_stream(lexer, parser_class, parser_root, listener):
    from antlr4 import CommonTokenStream, ParseTreeWalker
    tokens = CommonTokenStream(lexer)
    parser = parser_class(tokens)
    tree = getattr(parser, parser_root)()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


def walk_comp(stream):
    from mccode_antlr.grammar import McCompLexer, McCompParser, McCompListener, McCompVisitor

    class Listener(McCompListener):
        def enterProg(self, ctx: McCompParser.ProgContext):
            print("Start the program!")

        def exitProg(self, ctx: McCompParser.ProgContext):
            print("Exit the program!")

    lexer = McCompLexer(stream)
    listener = Listener()  # this needs to be replaced by something that *does* something
    walk_stream(lexer, McCompParser, 'prog', listener)


def walk_instr(stream):
    from mccode_antlr.grammar import McInstrLexer, McInstrParser, McInstrListener, McInstrVisitor

    class Listener(McInstrListener):
        def enterProg(self, ctx: McInstrParser.ProgContext):
            print("Start the program!")

        def exitProg(self, ctx: McInstrParser.ProgContext):
            print("Exit the program!")

    lexer = McInstrLexer(stream)
    listener = Listener()  # this needs to be replaced by something that *does* something
    walk_stream(lexer, McInstrParser, 'prog', listener)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys
    from pathlib import Path
    from argparse import ArgumentParser
    from antlr4 import InputStream, FileStream
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', help='file to handle', type=str, default=None)
    parser.add_argument('-t', '--type', help='file type', type=str, default=None)

    args = parser.parse_args()

    file_ext = None if args.type is None else args.type
    file = None if args.file is None else Path(args.file)
    if file is not None and file_ext is None:
        file_ext = file.suffix
    if file is not None and file_ext != file.suffix:
        raise RuntimeError(f"Expected file type {file_ext} does not match provided file extension {file.suffix}!")

    if file is None:
        istream = InputStream(sys.stdin.readline())
    else:
        istream = FileStream(str(file.resolve()), encoding='utf8')

    if 'comp' in file_ext:
        walk_comp(istream)
    elif 'instr' in file_ext:
        walk_instr(istream)
    else:
        raise RuntimeError(f'Unknown file extension type {file_ext}')

