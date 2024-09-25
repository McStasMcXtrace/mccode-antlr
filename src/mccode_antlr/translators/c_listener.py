from loguru import logger
from ..grammar import CParser, CListener, McInstrParser
from ..instr import InstrVisitor
from ..common import Expr


def literal_string(ctx):
    start_token, stop_token = ctx.start, ctx.stop
    stream = start_token.getInputStream()
    return stream.getText(start_token.start, stop_token.stop)


def make_error_listener(super_class, source: str, pre=5, post=2):
    class ErrorListener(super_class):
        def __init__(self):
            self.source = source
            self.pre = pre
            self.post = post

        def syntaxError(self, recognizer, offendingSymbol, *args, **kwargs):
            if len(args) == 4 and isinstance(args[3], str):
                # The 'speedy-antlr' syntax
                char_index, line, column, msg = args
            else:
                # the antlr4 (4.13.0) syntax
                line, column, msg, e = args
            logger.error(f'Syntax error in parsing {line},{column}')
            lines = self.source.split('\n')
            pre_lines = lines[line-self.pre:line]
            post_lines = lines[line:line+self.post]
            for line in pre_lines:
                logger.info(line)
            logger.error('~'*column + '^ ' + str(msg))
            for line in post_lines:
                logger.info(line)

    return ErrorListener()

class TypedefCListener(CListener):
    def __init__(self, typedefs: list = None):
        self.typedefs = [] if typedefs is None else [x for x in typedefs]
        self.is_typedef = False
        self.typedef_name = None

    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        self.is_typedef = False
        self.typedef_name = None

    def exitDeclaration(self, ctx: CParser.DeclarationContext):
        if self.is_typedef and self.typedef_name is not None:
            typename = self.typedef_name.replace('*', '').strip()
            if typename not in self.typedefs:
                self.typedefs.append(typename)

    def enterStorageClassSpecifier(self, ctx: CParser.StorageClassSpecifierContext):
        self.is_typedef = 'typedef' in literal_string(ctx)

    def enterTypedefName(self, ctx: CParser.TypedefNameContext):
        self.typedef_name = literal_string(ctx)


class DeclaresCListener(CListener):
    def __init__(self, typedefs: list = None, verbose=False):
        self.verbose = verbose
        self.typedefs = [] if typedefs is None else [x for x in typedefs]
        self.variables = dict()  # self.variables['name'] = type, value set by listeners
        self.last_type = None
        self.last_name = None
        self.last_value = None
        self.is_declaration = False
        self.is_typedef = False
        self.not_type_name = None
        self.was_type = False
        self.stored = False
        
    def debug(self, message):
        if self.verbose:
            logger.debug(message)

    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        self.debug('Enter declaration')
        self.is_declaration = True
        self.stored = False

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx: CParser.DeclarationContext):
        if not self.stored and self.not_type_name is not None and self.last_type.endswith(self.not_type_name):
            # this can only happen for declaration lines? where no initialization is performed.
            new_type = self.last_type[:-len(self.not_type_name)].strip()
            self.debug(f'Storing declaration for {self.not_type_name} = ({new_type}, {self.last_value})')
            if len(new_type):
                self.variables[self.not_type_name] = (new_type, self.last_value)
                self.stored = True
        self.not_type_name = None
        self.last_type = None
        self.last_name = None
        self.last_value = None
        self.is_declaration = False
        self.is_typedef = False
        self.debug('Exit declaration')

    def enterDeclarationSpecifiers(self, ctx: CParser.DeclarationSpecifiersContext):
        self.last_type = literal_string(ctx)
        self.debug(f'Enter Declaration Specifier last_type=\n{self.last_type}')

    def enterTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        self.was_type = True
        self.debug(f'Enter type specifier ctx=\n{literal_string(ctx)}')

    def enterStorageClassSpecifier(self, ctx: CParser.StorageClassSpecifierContext):
        self.is_typedef = 'typedef' in literal_string(ctx)

    def enterTypedefName(self, ctx: CParser.TypedefNameContext):
        # Check here if this is a known typedef'd name or not :/
        self.was_type = literal_string(ctx) in self.typedefs
        if not self.was_type:
            # We erroneously ended up here thinking this is part of a type name.
            # It's not, but we need to save the string value _Somewhere_
            self.not_type_name = literal_string(ctx)
        self.debug(f'Enter typedef name {self.was_type=} {self.not_type_name=}')

    def exitInitDeclarator(self, ctx: CParser.InitDeclaratorContext):
        if not self.is_typedef:
            self.debug(f'Storing declaration for {self.last_name} = ({self.last_type}, {self.last_value})')
            self.variables[self.last_name] = (self.last_type, self.last_value)
            self.stored = True
            self.last_name = None
        self.last_value = None

    def enterDeclarator(self, ctx: CParser.DeclaratorContext):
        self.last_name = literal_string(ctx)
        self.debug(f'Enter declarator {self.last_name=}')

    def exitInitializer(self, ctx: CParser.InitializerContext):
        self.last_value = literal_string(ctx)
        self.debug(f'Exit initializer {self.last_value=}')


class EvalCVisitor(InstrVisitor):
    def __init__(self, found: dict = None, verbose=False):
        super().__init__(None, None)
        self.verbose = verbose
        self.assigned = {} if found is None else found
        self.prog = []

    def debug(self, message):
        if self.verbose:
            logger.debug(message)

    def visitAssignment(self, ctx: McInstrParser.AssignmentContext):
        name = str(ctx.Identifier())
        value = self.visit(ctx.expr())
        self.prog.append((name, value))
        self.assigned[name] = value
        self.debug(f'{literal_string(ctx)} -> {name} = {value}')

    def visitExpressionIdentifier(self, ctx: McInstrParser.ExpressionIdentifierContext):
        from ..common import Expr
        # check if we already have a value for this identifier and insert it if we do:
        name = str(ctx.Identifier())
        if name in self.assigned:
            return self.assigned[name]
        return Expr.id(name)



def extract_c_declared_variables_and_defined_types(block: str, user_types: list = None, verbose=False):
    from antlr4 import InputStream, CommonTokenStream
    from antlr4 import ParseTreeWalker
    from antlr4.error.ErrorListener import ErrorListener
    from ..grammar import CLexer
    stream = InputStream(block)
    lexer = CLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = CParser(tokens)
    parser.addErrorListener(make_error_listener(ErrorListener, block))
    tree = parser.compilationUnit()
    # Go through a first time to identify types -- this _could_ be problematic
    # if typedefs happen _after_ their name(s) are used. But we ignore that for now.
    typedef_listener = TypedefCListener(user_types)
    typedef_walker = ParseTreeWalker()
    typedef_walker.walk(typedef_listener, tree)
    # Go through again to get the declarations:
    listener = DeclaresCListener(typedef_listener.typedefs, verbose=verbose)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.variables, listener.typedefs


def extract_c_declared_variables(block: str, user_types: list = None, verbose=False):
    variables, types = extract_c_declared_variables_and_defined_types(block, user_types, verbose=verbose)
    return variables


def extract_c_defined_then_declared_variables(defined_in_block: str, declared_in_block):
    _, defined_in_types = extract_c_declared_variables_and_defined_types(defined_in_block)
    return extract_c_declared_variables(declared_in_block, user_types=defined_in_types)


def evaluate_c_defined_variables(variables: dict[str, str], initialized_in: str, known: dict[str, Expr] = None,
                                 verbose=False):
    """Evaluate individual statements from C-like source in an attempt to find values for the provided variables"""
    from antlr4 import InputStream
    from ..grammar import McInstr_parse, McInstr_ErrorListener
    from ..common import Expr, DataType
    lines = [f'{line};' for line in initialized_in.split(';') if len(line.strip())]
    found = {} if known is None else known
    for line in lines:
        tree = McInstr_parse(InputStream(line), 'assignment', make_error_listener(McInstr_ErrorListener, line))
        visitor = EvalCVisitor(found=found, verbose=verbose)
        visitor.visitAssignment(tree)
        found = visitor.assigned

    def get_found(name, data_type):
        expr = found.get(name, Expr.id(name)).simplify()
        if expr.is_singular:
            expr.data_type = DataType.from_name(data_type)
        return expr

    return {v: get_found(v, data_type) for v, data_type in variables.items()}


def _get_expr(type_name: str, initial_value: str) -> Expr:
    from ..common import DataType, Value
    expr = Expr(Value(None)) if initial_value is None else Expr.parse(initial_value)
    expr.data_type = DataType.from_name(type_name)
    return expr


def extract_c_declared_expressions(block: str, user_types: list = None, verbose=False) -> dict[str, Expr]:
    variables = extract_c_declared_variables(block, user_types, verbose=verbose)
    return {name: _get_expr(dt, val) for name, (dt, val) in variables.items()}


def evaluate_c_defined_expressions(variables: dict[str, Expr], initialized_in: str, verbose=False) -> dict[str, Expr]:
    """For defined identifiers, evaluate a (simple) block of C code to determine the end values of the identifiers"""
    names_types = {name: expr.data_type.name for name, expr in variables.items()}
    return evaluate_c_defined_variables(names_types, initialized_in, known=variables, verbose=verbose)
