from zenlog import log
from ..grammar import CParser, CListener


def literal_string(ctx):
    start_token, stop_token = ctx.start, ctx.stop
    stream = start_token.getInputStream()
    return stream.getText(start_token.start, stop_token.stop)


class DeclaresCListener(CListener):
    def __init__(self, typedefs: list = None):
        self.typedefs = [] if typedefs is None else typedefs
        self.variables = dict()  # self.variables['name'] = type, value set by listeners
        self.last_type = None
        self.last_name = None
        self.last_value = None
        self.is_declaration = False
        self.is_typedef = False
        self.not_type_name = None
        self.was_type = False

    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        self.is_declaration = True

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx: CParser.DeclarationContext):
        if self.is_typedef:
            typename = self.not_type_name if self.last_name is None else self.last_name
            if typename is None:
                print(literal_string(ctx))
                print(self.last_type)
                print(self.last_name)
                print(self.last_value)
                print(self.not_type_name)
                return
            self.typedefs.append(typename.replace('*', '').strip())
            self.is_typedef = False
        elif self.not_type_name is not None and self.last_type.endswith(self.not_type_name):
            # this can only happen for declaration lines? where no initialization is performed.
            new_type = self.last_type[:-len(self.not_type_name)].strip()
            self.variables[self.not_type_name] = (new_type, self.last_value)
        self.not_type_name = None
        self.last_type = None
        self.last_name = None
        self.last_value = None
        self.is_declaration = False

    def enterDeclarationSpecifiers(self, ctx: CParser.DeclarationSpecifiersContext):
        self.last_type = literal_string(ctx)

    def enterStorageClassSpecifier(self, ctx: CParser.StorageClassSpecifierContext):
        self.is_typedef = 'typedef' in literal_string(ctx)

    def enterTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        self.was_type = True

    def enterTypedefName(self, ctx: CParser.TypedefNameContext):
        # Check here if this is a known typedef'd name or not :/
        self.was_type = literal_string(ctx) in self.typedefs
        if not self.was_type:
            # We erroneously ended up here thinking this is part of a type name.
            # It's not, but we need to save the string value _Somewhere_
            self.not_type_name = literal_string(ctx)

    def exitInitDeclarator(self, ctx: CParser.InitDeclaratorContext):
        if not self.is_typedef:
            self.variables[self.last_name] = (self.last_type, self.last_value)
            self.last_name = None
        self.last_value = None

    def enterDeclarator(self, ctx: CParser.DeclaratorContext):
        self.last_name = literal_string(ctx)

    def exitInitializer(self, ctx: CParser.InitializerContext):
        self.last_value = literal_string(ctx)


def extract_c_declared_variables_and_defined_types(block: str, user_types: list = None):
    from antlr4 import InputStream, CommonTokenStream
    from antlr4 import ParseTreeWalker
    from ..grammar import CLexer
    # log.debug('Load block into ANTLR4 stream')
    # log.debug(f'{block}')
    stream = InputStream(block)
    # log.debug('Run lexer')
    lexer = CLexer(stream)
    # log.debug('Tokenize stream')
    tokens = CommonTokenStream(lexer)
    # log.debug('Parse tokens')
    parser = CParser(tokens)
    # log.debug('Extract compilation unit tree')
    tree = parser.compilationUnit()
    # log.debug('Initialize listener')
    listener = DeclaresCListener(user_types)
    # log.debug('Initialize walker')
    walker = ParseTreeWalker()
    # log.debug('Walk the tree')
    walker.walk(listener, tree)
    return listener.variables, listener.typedefs


def extract_c_declared_variables(block: str, user_types: list = None):
    variables, types = extract_c_declared_variables_and_defined_types(block, user_types)
    return variables


def extract_c_defined_then_declared_variables(defined_in_block: str, declared_in_block):
    _, defined_in_types = extract_c_declared_variables_and_defined_types(defined_in_block)
    return extract_c_declared_variables(declared_in_block, user_types=defined_in_types)
