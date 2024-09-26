from loguru import logger
from ..grammar import CParser, McInstrParser, CVisitor
from ..instr import InstrVisitor
from ..common import Expr

def string_between_tokens(start_token, stop_token):
    stream = start_token.getInputStream()
    return stream.getText(start_token.start, stop_token.stop)


def literal_string(ctx, until=None):
    if until is None:
        until = ctx
    return string_between_tokens(ctx.start, until.stop)


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


class CDeclarator:
    def __init__(self, pointer, declare, extensions):
        self.pointer = pointer
        self.declare = declare
        self.extensions = extensions
        self.dtype = None

    def __str__(self):
        ext = " ".join(f'{x}' for x in self.extensions)
        dec = f'{self.declare} {ext}' if len(ext) else f'{self.declare}'
        if self.pointer:
            dec = f'{self.pointer} {dec}'
        if self.dtype:
            dec = f'{self.dtype} {dec}'
        return dec

    def variable_key(self):
        ext = " ".join(f'{x}' for x in self.extensions)
        dec = f'{self.declare} {ext}' if len(ext) else f'{self.declare}'
        if self.pointer:
            dec = f'{self.pointer} {dec}'
        return dec

    def __hash__(self):
        return hash(str(self))


class CFuncPointer:
    def __init__(self, declare: CDeclarator, modifiers):
        self.mods = modifiers
        self.declare = declare
        self.args = None

    def __str__(self):
        f = f'({self.mods} {self.declare})' if self.mods else f'({self.declare})'
        return f'{f}({self.args})' if self.args else f'{f}()'

    def __hash__(self):
        return hash(str(self))


class DeclaresCVisitor(CVisitor):
    def __init__(self, typedefs: list | None = None, verbose: bool = False):
        self.verbose = verbose
        self.typedefs = [x for x in typedefs] if typedefs else []
        self.declares = {}

    def debug(self, message):
        if self.verbose:
            logger.debug(message)

    def info(self, message):
        if self.verbose:
            logger.info(message)

    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        if ctx.staticAssertDeclaration() is not None:
            return
        #
        specs = [self.visit(x) for x in ctx.declarationSpecifiers().declarationSpecifier()]
        if ctx.initDeclaratorList() is not None:
            inits = [self.visit(x) for x in ctx.initDeclaratorList().initDeclarator()]
        else:
            inits = []

        if 'typedef' in specs:
            # this _is_ a typedef statement.
            # It (probably) is of the form
            #   typedef typeInformation aliasIdentifier;
            if specs[0] != 'typedef':
                self.debug(f"Expected typedef ... identifier; not\n{literal_string(ctx)}")
            if len(inits):
                self.debug(f'Expected no initializer with typedef, but found {inits}')
            alias = specs[-1]
            if alias in self.typedefs:
                self.info(f'Re-definition of typedef alias {alias}?')
            self.typedefs.append(alias)
        elif len(inits):
            for decl, init in inits:
                decl.dtype = ' '.join(specs)
                self.declares[decl] = init
        elif len(specs) > 1:
            decl = CDeclarator(pointer=None, declare=specs[-1], extensions=[])
            decl.dtype = ' '.join(specs[:-1])
            self.declares[decl] = None

    # Five declaration specifiers
    def visitStorageClassSpecifier(self, ctx:CParser.StorageClassSpecifierContext):
        self.debug(f'StorageClassSpecifier {literal_string(ctx)}')
        return literal_string(ctx)

    def visitTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        if (c := ctx.atomicTypeSpecifier()) is not None:
            return self.visit(c)
        if (c := ctx.structOrUnionSpecifier()) is not None:
            return self.visit(c)
        if (c := ctx.enumSpecifier()) is not None:
            return self.visit(c)
        if (c := ctx.typedefName()) is not None:
            return self.visit(c)
        if (c := ctx.constantExpression()) is not None:
            return f'__typeof__({self.visit(c)}'
        return literal_string(ctx)

    # Keep going from here
    def visitTypeQualifier(self, ctx:CParser.TypeQualifierContext):
        self.debug(f'typeQualifier {literal_string(ctx)}')
        return literal_string(ctx)

    def visitFunctionSpecifier(self, ctx:CParser.FunctionSpecifierContext):
        self.debug(f'functionSpecifier {literal_string(ctx)}')
        return literal_string(ctx)

    def visitAlignmentSpecifier(self, ctx:CParser.AlignmentSpecifierContext):
        self.debug(f'alignmentSpecifier {literal_string(ctx)}')
        return literal_string(ctx)

    # initDeclarator
    def visitInitDeclarator(self, ctx:CParser.InitDeclaratorContext):
        # declarator ( '=' initializer )?
        decl = self.visit(ctx.declarator())
        init = self.visit(ctx.initializer()) if ctx.initializer() else None
        return decl, init

    def visitAtomicTypeSpecifier(self, ctx:CParser.AtomicTypeSpecifierContext):
        self.debug(f'AtomicTypeSpecifier {literal_string(ctx)}')
        return literal_string(ctx)

    def visitStructOrUnionSpecifier(self, ctx:CParser.StructOrUnionContext):
        self.debug(f'StructOrUnion {literal_string(ctx)}')
        return literal_string(ctx)

    def visitEnumSpecifier(self, ctx:CParser.EnumSpecifierContext):
        self.debug(f'EnumSpecifier {literal_string(ctx)}')
        return literal_string(ctx)

    def visitTypedefName(self, ctx:CParser.TypedefNameContext):
        self.debug(f'TypedefName {literal_string(ctx)}')
        return literal_string(ctx)

    def visitConstantExpression(self, ctx:CParser.ConstantExpressionContext):
        a = ctx.conditionalExpression()
        self.debug(f'ConstantExpression {literal_string(ctx)}')
        return literal_string(a)

    def visitInitializer(self, ctx:CParser.InitializerContext):
        self.debug(f'Initializer {literal_string(ctx)}')
        return literal_string(ctx)

    def visitDeclarator(self, ctx:CParser.DeclaratorContext):
        ptr = self.visit(ctx.pointer()) if ctx.pointer() else None
        dec = self.visit(ctx.directDeclarator())
        extensions = [self.visit(x) for x in ctx.gccDeclaratorExtension()]
        return CDeclarator(pointer=ptr, declare=dec, extensions=extensions)

    def visitPointer(self, ctx:CParser.PointerContext):
        self.debug(f'pointer {literal_string(ctx)}')
        return literal_string(ctx)

    def visitDirectDeclarator(self, ctx:CParser.DirectDeclaratorContext):
        if ctx.declarator():
            # this _is_ a function pointer declarator, right?
            modifiers = literal_string(ctx.vcSpecificModifer()) if ctx.vcSpecificModifer() else None
            return CFuncPointer(self.visit(ctx.declarator()), modifiers=modifiers)
        if ctx.Identifier():
            return literal_string(ctx)

        dd = ctx.directDeclarator()
        after_dd_str = literal_string(ctx).replace(literal_string(dd), '')
        dec = self.visit(dd)
        if isinstance(dec, CFuncPointer):
            dec.args = after_dd_str.strip('()')
            return dec
        return dec + after_dd_str


def extract_c_declared_variables_and_defined_types(block: str, user_types: list = None, verbose=False):
    from antlr4 import InputStream, CommonTokenStream
    from antlr4.error.ErrorListener import ErrorListener
    from ..grammar import CLexer
    stream = InputStream(block)
    lexer = CLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = CParser(tokens)
    parser.addErrorListener(make_error_listener(ErrorListener, block))
    tree = parser.compilationUnit()
    visitor = DeclaresCVisitor(user_types, verbose=verbose)
    visitor.visitCompilationUnit(tree)
    # Consider _using_ the CDeclarator class instead of this conversion?
    variables = {dec.variable_key(): (dec.dtype, init) for dec, init in visitor.declares.items()}
    return variables, visitor.typedefs


def extract_c_declared_variables(block: str, user_types: list = None, verbose=False):
    variables, types = extract_c_declared_variables_and_defined_types(block, user_types, verbose=verbose)
    return variables


def extract_c_defined_then_declared_variables(defined_in_block: str, declared_in_block):
    _, defined_in_types = extract_c_declared_variables_and_defined_types(defined_in_block)
    return extract_c_declared_variables(declared_in_block, user_types=defined_in_types)


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
