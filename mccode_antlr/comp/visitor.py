from ..grammar import McCompParser as Parser, McCompVisitor
from .comp import Comp
from ..common import ComponentParameter, Expr, MetaData
from zenlog import log

class CompVisitor(McCompVisitor):
    def __init__(self, parent, filename, instance_name=None):
        self.parent = parent  # the instrument (handler?) that wanted to read this component
        self.filename = filename
        self.state = Comp()
        self.instance_name = instance_name

    def visitProg(self, ctx: Parser.ProgContext):
        self.state = Comp()
        self.visit(ctx.component_definition())
        return self.state

    def visitComponentDefineNew(self, ctx: Parser.ComponentDefineNewContext):
        self.state.name = str(ctx.Identifier())
        if ctx.NoAcc() is not None:
            self.state.no_acc()
        self.visitChildren(ctx)  # Use the visitor methods to fill in details of the state

    def visitComponentDefineCopy(self, ctx: Parser.ComponentDefineCopyContext):
        from copy import deepcopy
        new_name, copy_from = [str(x) for x in ctx.Identifier()]
        if self.parent is None:
            raise RuntimeError("Can not copy a component definition without a parent instrument")
        copy_from_comp = self.parent.get_component(copy_from)
        # pull from that component ... deepcopy _just_ in case
        self.state = deepcopy(copy_from_comp)
        # update the name to match what we're going to call this component
        self.state.name = new_name
        # add parameters, overwrite all provided details
        if ctx.NoAcc() is not None:
            self.state.no_acc()
        self.visitChildren(ctx)  # Use the visitor methods to overwrite details of the state

    def visitCategory(self, ctx: Parser.CategoryContext):
        # Return the provided identifier or string literal, minus quotes
        self.state.category = str(ctx.StringLiteral())[1:-1] if ctx.Identifier() is None else str(ctx.Identifer())

    def visitTraceBlock(self, ctx: Parser.TraceBlockContext):
        self.state.TRACE(self.visit(ctx.unparsed_block()))
        
    def visitTraceBlockCopy(self, ctx: Parser.TraceBlockCopyContext):
        if len(self.state.trace):
            log.critical(f'The component {self.state.name} is a copied definition, complete with TRACE section')
            log.critical(f'Now `TRACE COPY {ctx.Identifier()}` would add to the existing copied TRACE')
            log.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
            self.state.trace = ()
        blocks = self.parent.get_component(str(ctx.Identifier())).trace
        if ctx.Extend() is not None:
            blocks = [x for x in blocks]
            blocks.append(self.visit(ctx.unparsed_block()))
        self.state.TRACE(*blocks)

    def visitComponent_define_parameters(self, ctx: Parser.Component_define_parametersContext):
        for parameter in self.visit(ctx.component_parameters()):
            self.state.add_parameter(parameter)

    def visitComponent_set_parameters(self, ctx: Parser.Component_set_parametersContext):
        for parameter in self.visit(ctx.component_parameters()):
            self.state.add_setting(parameter)

    def visitComponent_out_parameters(self, ctx: Parser.Component_out_parametersContext):
        for parameter in self.visit(ctx.component_parameters()):
            self.state.add_output(parameter)

    def visitComponent_parameters(self, ctx: Parser.Component_parametersContext):
        return [self.visit(x) for x in ctx.component_parameter()]

    def visitComponentParameterDouble(self, ctx: Parser.ComponentParameterDoubleContext):
        name = str(ctx.Identifier())
        value = None
        if ctx.Assign() is not None:
            # protect against a literal '0' provided ... which doesn't match IntegerLiteral for some reason
            value = 0 if ctx.expr() is None else self.visit(ctx.expr())
        return ComponentParameter(name=name, value=Expr.float(value))

    def visitComponentParameterInteger(self, ctx: Parser.ComponentParameterIntegerContext):
        name = str(ctx.Identifier())
        value = None
        if ctx.Assign() is not None:
            # protect against a literal '0' provided ... which doesn't match IntegerLiteral for some reason
            value = 0 if ctx.expr() is None else self.visit(ctx.expr())
        return ComponentParameter(name=name, value=Expr.int(value))

    def visitComponentParameterString(self, ctx: Parser.ComponentParameterStringContext):
        name = str(ctx.Identifier())
        default = None
        if ctx.Assign() is not None:
            default = 'NULL' if ctx.StringLiteral() is None else str(ctx.StringLiteral())
        return ComponentParameter(name=name, value=Expr.str(default))

    def visitComponentParameterVector(self, ctx: Parser.ComponentParameterVectorContext):
        from ..common import Value, DataType, ShapeType
        name = str(ctx.Identifier(0))
        if ctx.Assign() is not None and ctx.initializerlist() is not None:
            value = self.visit(ctx.initializerlist())
            value.data_type = DataType.float
        else:
            default = None
            if ctx.Assign() is not None:
                default = "NULL"
                if ctx.Identifier(1) is not None:
                    default = str(ctx.Identifier(1))
            value = Expr(Value(default, data_type=DataType.float, shape_type=ShapeType.vector))
        return ComponentParameter(name=name, value=value)

    def visitComponentParameterSymbol(self, ctx: Parser.ComponentParameterSymbolContext):
        raise RuntimeError("McCode symbol parameter type not supported yet")

    def visitComponentParameterDoubleArray(self, ctx: Parser.ComponentParameterDoubleArrayContext):
        # 'vector' is really just an alias for 'double *', right?
        return self.visitComponentParameterVector(ctx)

    def visitComponentParameterIntegerArray(self, ctx: Parser.ComponentParameterIntegerArrayContext):
        from ..common import Value, DataType, ShapeType
        name = str(ctx.Identifier(0))
        if ctx.assign() is not None and ctx.initializerlist() is not None:
            value = self.visit(ctx.initializerlist())
            value.data_type = DataType.int
        else:
            default = None
            if ctx.assign() is not None:
                default = "NULL"
                if ctx.Identifier(1) is not None:
                    default = str(ctx.Identifier(1))
            value = Expr(Value(default, data_type=DataType.int, shape_type=ShapeType.vector))
        return ComponentParameter(name=name, value=value)

    def visitDependency(self, ctx: Parser.DependencyContext):
        if ctx.StringLiteral() is not None:
            # the flags are the literal string without its quotes:
            self.parent.add_c_flags(str(ctx.StringLiteral()).strip('"'))

    def visitDeclareBlock(self, ctx: Parser.DeclareBlockContext):
        self.state.DECLARE(self.visit(ctx.unparsed_block()))

    def visitDeclareBlockCopy(self, ctx: Parser.DeclareBlockCopyContext):
        if len(self.state.declare):
            log.critical(f'The component {self.state.name} is a copied definition, complete with DECLARE section')
            log.critical(f'Now `DECLARE COPY {ctx.Identifier()}` would add to the existing copied DECLARE')
            log.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
            self.state.declare = ()
        blocks = self.parent.get_component(str(ctx.Identifier())).declare
        if ctx.Extend() is not None:
            blocks = [x for x in blocks]
            blocks.append(self.visit(ctx.unparsed_block()))
        self.state.DECLARE(*blocks)

    def visitShareBlock(self, ctx: Parser.ShareBlockContext):
        self.state.SHARE(self.visit(ctx.unparsed_block()))

    def visitShareBlockCopy(self, ctx: Parser.ShareBlockCopyContext):
        blocks = self.parent.get_component(str(ctx.Identifier())).share
        if ctx.Extend() is not None:
            blocks = [x for x in blocks]
            blocks.append(self.visit(ctx.unparsed_block()))
        self.state.SHARE(*blocks)

    def visitInitializeBlock(self, ctx: Parser.InitializeBlockContext):
        self.state.INITIALIZE(self.visit(ctx.unparsed_block()))

    def visitInitializeBlockCopy(self, ctx: Parser.InitializeBlockCopyContext):
        if len(self.state.initialize):
            log.critical(f'The component {self.state.name} is a copied definition, complete with INITIALIZE section')
            log.critical(f'Now `INITIALIZE COPY {ctx.Identifier()}` would add to the existing copied INITIALIZE')
            log.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
            self.state.initialize = ()
        blocks = self.parent.get_component(str(ctx.Identifier())).initialize
        if ctx.Extend() is not None:
            blocks = [x for x in blocks]
            blocks.append(self.visit(ctx.unparsed_block()))
        self.state.INITIALIZE(*blocks)

    def visitUservars(self, ctx: Parser.UservarsContext):
        self.state.USERVARS(self.visit(ctx.unparsed_block()))

    def visitSaveBlock(self, ctx: Parser.SaveBlockContext):
        self.state.SAVE(self.visit(ctx.unparsed_block()))

    def visitSaveBlockCopy(self, ctx: Parser.SaveBlockCopyContext):
        if len(self.state.save):
            log.critical(f'The component {self.state.name} is a copied definition, complete with SAVE section')
            log.critical(f'Now `SAVE COPY {ctx.Identifier()}` would add to the existing copied SAVE')
            log.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
            self.state.save = ()
        blocks = self.parent.get_component(str(ctx.Identifier())).save
        if ctx.Extend() is not None:
            blocks = [x for x in blocks]
            blocks.append(self.visit(ctx.unparsed_block()))
        self.state.SAVE(*blocks)

    def visitFinallyBlock(self, ctx: Parser.FinallyBlockContext):
        self.state.FINALLY(self.visit(ctx.unparsed_block()))

    def visitFinallyBlockCopy(self, ctx: Parser.FinallyBlockCopyContext):
        if len(self.state.final):
            log.critical(f'The component {self.state.name} is a copied definition, complete with FINALLY section')
            log.critical(f'Now `FINALLY COPY {ctx.Identifier()}` would add to the existing copied FINALLY')
            log.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
            self.state.final = ()
        blocks = self.parent.get_component(str(ctx.Identifier())).final
        if ctx.Extend() is not None:
            blocks = [x for x in blocks]
            blocks.append(self.visit(ctx.unparsed_block()))
        self.state.FINALLY(*blocks)

    def visitDisplayBlock(self, ctx: Parser.DisplayBlockContext):
        self.state.DISPLAY(self.visit(ctx.unparsed_block()))

    def visitDisplayBlockCopy(self, ctx: Parser.DisplayBlockCopyContext):
        if len(self.state.display):
            log.critical(f'The component {self.state.name} is a copied definition, complete with DISPLAY section')
            log.critical(f'Now `DISPLAY COPY {ctx.Identifier()}` would add to the existing copied DISPLAY')
            log.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
            self.state.display = ()
        blocks = self.parent.get_component(str(ctx.Identifier())).display
        if ctx.Extend() is not None:
            blocks = [x for x in blocks]
            blocks.append(self.visit(ctx.unparsed_block()))
        self.state.DISPLAY(*blocks)

    def visitMetadata(self, ctx: Parser.MetadataContext):
        filename, line_number, metadata = self.visit(ctx.unparsed_block())
        self.state.add_metadata(MetaData.from_component_tokens(self.state.name, str(ctx.mime), str(ctx.name), metadata))

    def visitUnparsed_block(self, ctx: Parser.Unparsed_blockContext):
        # We want to extract the source-file line number (and filename) for use in the C-preprocessor
        # via `#line {number} "{filename}"` directives, for more expressive error handling
        line_number = None if ctx.start is None else ctx.start.line
        content = str(ctx.UnparsedBlock())[2:-2]
        return self.filename, line_number, content

    # TODO Make this and the identical list of visitors in instr/visitor.py a single definition ... somehow
    # FIXME There *are* no statements in McCode, so all identifiers always produce un-parsable values.
    def visitAssignment(self, ctx: Parser.AssignmentContext):
        line_number = None if ctx.start is None else ctx.start.line
        raise RuntimeError(f"{self.filename}: {line_number} -- assignment statements are not (yet) supported")

    # TODO (maybe) Add control and statements into McCode, requiring some form of global stack.
    def visitExpressionUnaryPM(self, ctx: Parser.ExpressionUnaryPMContext):
        right = self.visit(ctx.expr())
        if isinstance(right, str):
            return '-' + right if ctx.Plus() is None else right
        return -right if ctx.Plus() is None else right

    def visitExpressionGrouping(self, ctx: Parser.ExpressionGroupingContext):
        from ..common import UnaryOp
        return Expr(UnaryOp('__group__', self.visit(ctx.expr())))

    def visitExpressionFloat(self, ctx: Parser.ExpressionFloatContext):
        return Expr.float(str(ctx.FloatingLiteral()))

    def visitExpressionPointerAccess(self, ctx: Parser.ExpressionPointerAccessContext):
        from ..common import BinaryOp, Value, ObjectType
        pointer = Expr(Value(str(ctx.Identifier()), object_type=ObjectType.identifier))
        return Expr(BinaryOp('__pointer_access__', pointer, self.visit(ctx.expr())))

    def visitExpressionStructAccess(self, ctx: Parser.ExpressionStructAccessContext):
        from ..common import BinaryOp, Value, ObjectType
        struct = Expr(Value(str(ctx.Identifier()), object_type=ObjectType.identifier))
        return Expr(BinaryOp('__struct_access__', struct, self.visit(ctx.expr())))

    def visitExpressionArrayAccess(self, ctx: Parser.ExpressionArrayAccessContext):
        from ..common import BinaryOp, Value, ShapeType, ObjectType
        array = Expr(Value(str(ctx.Identifier()), object_type=ObjectType.identifier, shape_type=ShapeType.vector))
        return Expr(BinaryOp('__getitem__', array, self.visit(ctx.expr())))

    def visitExpressionIdentifier(self, ctx: Parser.ExpressionIdentifierContext):
        from ..common import Value, ObjectType
        return Expr(Value(str(ctx.Identifier()), object_type=ObjectType.identifier))

    def visitExpressionInteger(self, ctx: Parser.ExpressionIntegerContext):
        return Expr.int(str(ctx.IntegerLiteral()))

    def visitExpressionZero(self, ctx: Parser.ExpressionZeroContext):
        return Expr.int(0)

    def visitExpressionExponentiation(self, ctx: Parser.ExpressionExponentiationContext):
        base = self.visit(ctx.base)
        exponent = self.visit(ctx.exponent)
        return base ** exponent

    def visitExpressionBinaryPM(self, ctx: Parser.ExpressionBinaryPMContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + right if ctx.Minus() is None else left - right

    def visitExpressionFunctionCall(self, ctx: Parser.ExpressionFunctionCallContext):
        from ..common import BinaryOp, Value, ObjectType
        function = Value(str(ctx.Identifier()), object_type=ObjectType.function)
        args = [self.visit(arg).expr[0] for arg in ctx.args]  # each is a Value, UnaryOp, or BinaryOp?
        return Expr(BinaryOp('__call__', function, args))

    def visitExpressionBinaryMD(self, ctx: Parser.ExpressionBinaryMDContext):
        left, right = self.visit(ctx.left), self.visit(ctx.right)
        return left * right if ctx.Div() is None else left / right

    def visitInitializerlist(self, ctx: Parser.InitializerlistContext):
        from ..common import Value, ObjectType, ShapeType
        values = [self.visit(x).expr[0].value for x in ctx.values]
        return Expr(Value(values, object_type=ObjectType.initializer_list, shape_type=ShapeType.vector))

    def visitExpressionUnaryLogic(self, ctx: Parser.ExpressionUnaryLogicContext):
        from ..common import UnaryOp
        expr = self.visit(ctx.expr())
        op = 'unknown'
        if ctx.Not() is not None:
            op = '__not__'
        return Expr(UnaryOp(op, expr))

    def visitExpressionTrinaryLogic(self, ctx: Parser.ExpressionTrinaryLogicContext):
        from ..common import TrinaryOp
        test, true, false = [self.visit(x) for x in (ctx.test, ctx.true, ctx.false)]
        return Expr(TrinaryOp('__trinary__', test, true, false))

    def visitExpressionBinaryLogic(self, ctx: Parser.ExpressionBinaryLogicContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        op = 'unknown'
        if ctx.AndAnd() is not None:
            op = '__and__'
        elif ctx.OrOr() is not None:
            op = '__or__'
        return Expr(BinaryOp(op, left, right))

    def visitExpressionBinaryEqual(self, ctx: Parser.ExpressionBinaryEqualContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return Expr(BinaryOp('__eq__', left, right))

    def visitExpressionBinaryLessEqual(self, ctx: Parser.ExpressionBinaryLessEqualContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return Expr(BinaryOp('__le__', left, right))

    def visitExpressionBinaryGreaterEqual(self, ctx: Parser.ExpressionBinaryGreaterEqualContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return Expr(BinaryOp('__ge__', left, right))

    def visitExpressionBinaryLess(self, ctx: Parser.ExpressionBinaryLessContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return Expr(BinaryOp('__lt__', left, right))

    def visitExpressionBinaryGreater(self, ctx: Parser.ExpressionBinaryGreaterContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return Expr(BinaryOp('__gt__', left, right))

    def visitExpressionString(self, ctx: Parser.ExpressionStringContext):
        strings = ''.join(str(sl).strip('"') for sl in ctx.StringLiteral())
        return Expr.str(f'"{strings}"')

    def visitExpressionPrevious(self, ctx: Parser.ExpressionPreviousContext):
        # The very-special no-good expression use of PREVIOUS where it is replaced by the last component's name
        raise RuntimeError('PREVIOUS is not a valid expression in Comp definitions')

    def visitExpressionMyself(self, ctx: Parser.ExpressionMyselfContext):
        # The even-worse expression use of MYSELF to refer to the current being-constructed component's name
        return Expr.str(self.instance.name)
