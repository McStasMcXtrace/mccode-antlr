from zenlog import log
from ..grammar import CParser, CListener, McInstrParser
from ..instr import InstrVisitor
from ..common import Expr
from antlr4.error.ErrorListener import ErrorListener


def literal_string(ctx):
    start_token, stop_token = ctx.start, ctx.stop
    stream = start_token.getInputStream()
    return stream.getText(start_token.start, stop_token.stop)


class CErrorListener(ErrorListener):
    def __init__(self, source: str, pre=5, post=2):
        self.source = source
        self.pre = pre
        self.post = post

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        log.error(f'Syntax error in parsing {line},{column}')
        lines = self.source.split('\n')
        pre_lines = lines[line-self.pre:line]
        post_lines = lines[line:line+self.post]
        for line in pre_lines:
            log.info(line)
        log.error('~'*column + '^ ' + msg)
        for line in post_lines:
            log.info(line)


class DeclaresCListener(CListener):
    def __init__(self, typedefs: list = None, verbose=False):
        self.verbose = verbose
        self.typedefs = [] if typedefs is None else typedefs
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
            log.debug(message)

    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        self.debug('Enter declaration')
        self.is_declaration = True
        self.stored = False

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
        elif not self.stored and self.not_type_name is not None and self.last_type.endswith(self.not_type_name):
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
        self.debug('Exit declaration')

    def enterDeclarationSpecifiers(self, ctx: CParser.DeclarationSpecifiersContext):
        self.last_type = literal_string(ctx)
        self.debug(f'Enter Declaration Specifier {self.last_type=}')

    def enterStorageClassSpecifier(self, ctx: CParser.StorageClassSpecifierContext):
        self.is_typedef = 'typedef' in literal_string(ctx)
        self.debug(f'Enter storage class specifier {self.is_typedef=}')

    def enterTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        self.was_type = True
        self.debug(f'Enter type specifier')

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
            log.debug(message)

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
    from ..grammar import CLexer
    # self.debug('Load block into ANTLR4 stream')
    # self.debug(f'{block}')
    stream = InputStream(block)
    # self.debug('Run lexer')
    lexer = CLexer(stream)
    # self.debug('Tokenize stream')
    tokens = CommonTokenStream(lexer)
    # self.debug('Parse tokens')
    parser = CParser(tokens)
    parser.addErrorListener(CErrorListener(block))
    # self.debug('Extract compilation unit tree')
    tree = parser.compilationUnit()
    # self.debug('Initialize listener')
    listener = DeclaresCListener(user_types, verbose=verbose)
    # self.debug('Initialize walker')
    walker = ParseTreeWalker()
    # self.debug('Walk the tree')
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
    from antlr4 import InputStream, CommonTokenStream
    from ..grammar import McInstrLexer, McInstrParser
    from ..common import Expr, DataType
    lines = [f'{line};' for line in initialized_in.split(';') if len(line.strip())]
    found = {} if known is None else known
    for line in lines:
        parser = McInstrParser(CommonTokenStream(McInstrLexer(InputStream(line))))
        parser.addErrorListener((CErrorListener(line)))
        visitor = EvalCVisitor(found=found, verbose=verbose)
        visitor.visitAssignment(parser.assignment())
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
