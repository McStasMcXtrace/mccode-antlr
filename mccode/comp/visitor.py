from ..grammar import McCompParser as Parser, McCompVisitor
from .comp import Comp
from ..common import ComponentParameter, Value, MetaData


class CompVisitor(McCompVisitor):
    def __init__(self, parent, filename):
        self.parent = parent  # the instrument (handler?) that wanted to read this component
        self.filename = filename
        self.state = Comp()

    def visitProg(self, ctx: Parser.ProgContext):
        self.state = Comp()
        self.visit(ctx.component_definition())
        return self.state

    def visitComponentDefineNew(self, ctx: Parser.ComponentDefineNewContext):
        self.state.name = str(ctx.Identifer())
        if ctx.NoAcc() is not None:
            self.state.no_acc()
        self.visitChildren(ctx)  # Use the visitor methods to fill in details of the state

    def visitComponentDefineCopy(self, ctx: Parser.ComponentDefineCopyContext):
        from copy import deepcopy
        new_name, copy_from = [str(x) for x in ctx.Identifer()]
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

    def visitComponent_trace(self, ctx: Parser.Component_traceContext):
        self.state.TRACE(self.visit(ctx.unparsed_block()))

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
        value = Value(Value.Type.float, None if ctx.Assign() is None else self.visit(ctx.expr()))
        return ComponentParameter(name=name, value=value)

    def visitComponentParameterInteger(self, ctx: Parser.ComponentParameterIntegerContext):
        name = str(ctx.Identifier())
        value = Value(Value.Type.int, None if ctx.Assign() is None else self.visit(ctx.expr()))
        return ComponentParameter(name=name, value=value)

    def visitComponentParameterString(self, ctx: Parser.ComponentParameterStringContext):
        name = str(ctx.Identifier())
        default = None
        if ctx.Assign() is not None:
            default = 'NULL' if ctx.StringLiteral() is None else self.visit(ctx.StringLiteral())
        return ComponentParameter(name=name, value=Value(Value.Type.str, default))

    def visitComponentParameterVector(self, ctx: Parser.ComponentParameterVectorContext):
        name = str(ctx.Identifier(0))
        default = None
        if ctx.assign() is not None:
            default = "NULL"
            if ctx.Identifier(1) is not None:
                default = str(ctx.Identifier(1))
            elif ctx.initializerlist() is not None:
                default = self.visit(ctx.initializerlist())
        return ComponentParameter(name=name, value=Value(Value.Type.float_array, default))

    def visitComponentParameterSymbol(self, ctx: Parser.ComponentParameterSymbolContext):
        raise RuntimeError("McCode symbol parameter type not supported yet")

    def visitComponentParameterDoubleArray(self, ctx: Parser.ComponentParameterDoubleArrayContext):
        # 'vector' is really just an alias for 'double *', right?
        return self.visitComponentParameterVector(ctx)

    def visitComponentParameterIntegerArray(self, ctx: Parser.ComponentParameterIntegerArrayContext):
        name = str(ctx.Identifier(0))
        default = None
        if ctx.assign() is not None:
            default = "NULL"
            if ctx.Identifier(1) is not None:
                default = str(ctx.Identifier(1))
            elif ctx.initializerlist() is not None:
                default = self.visit(ctx.initializerlist())
        return ComponentParameter(name=name, value=Value(Value.Type.int_array, default))

    def visitDependency(self, ctx: Parser.DependencyContext):
        self.parent.add_c_flags(self.visit(ctx.StringLiteral()))

    def visitDeclareBlock(self, ctx: Parser.DeclareBlockContext):
        self.state.DECLARE(self.visit(ctx.unparsed_block()))

    def visitDeclareBlockCopy(self, ctx: Parser.DeclareBlockCopyContext):
        copy_from = self.parent.get_component(str(ctx.Identifier()))
        self.state.DECLARE(copy_from.declare, self.visit(ctx.unparsed_block()))

    def visitShareBlock(self, ctx: Parser.ShareBlockContext):
        self.state.SHARE(self.visit(ctx.unparsed_block()))

    def visitShareBlockCopy(self, ctx: Parser.ShareBlockCopyContext):
        copy_from = self.parent.get_component(str(ctx.Identifier()))
        self.state.SHARE(copy_from.share, self.visit(ctx.unparsed_block()))

    def visitInitialzieBlock(self, ctx: Parser.InitializeBlockContext):
        self.state.INITIALIZE(self.visit(ctx.unparsed_block()))

    def visitInitializeBlockCopy(self, ctx: Parser.InitializeBlockCopyContext):
        copy_from = self.parent.get_component(str(ctx.Identifier()))
        self.state.INITIALIZE(copy_from.initialize, self.visit(ctx.unparsed_block()))

    def visitUservars(self, ctx: Parser.UservarsContext):
        self.state.USERVARS(self.visit(ctx.unparsed_block()))

    def visitSaveBlock(self, ctx: Parser.SaveBlockContext):
        self.state.SAVE(self.visit(ctx.unparsed_block()))

    def visitSaveBlockCopy(self, ctx: Parser.SaveBlockCopyContext):
        copy_from = self.parent.get_component(str(ctx.Identifier()))
        self.state.SAVE(copy_from.save, self.visit(ctx.unparsed_block()))

    def visitFinallyBlock(self, ctx: Parser.FinallyBlockContext):
        self.state.FINALLY(self.visit(ctx.unparsed_block()))

    def visitFinallyBlockCopy(self, ctx: Parser.FinallyBlockCopyContext):
        copy_from = self.parent.get_component(str(ctx.Identifier()))
        self.state.FINALLY(copy_from.final, self.visit(ctx.unparsed_block()))

    def visitDisplayBlock(self, ctx: Parser.DisplayBlockContext):
        self.state.DISPLAY(self.visit(ctx.unparsed_block()))

    def visitDisplayBlockCopy(self, ctx: Parser.DisplayBlockCopyContext):
        copy_from = self.parent.get_component(str(ctx.Identifier()))
        self.state.DISPLAY(copy_from.display, self.visit(ctx.unparsed_block()))

    def visitMetadata(self, ctx: Parser.MetadataContext):
        filename, line_number, metadata = self.visit(ctx.unparsed_block())
        self.state.add_metadata(MetaData.from_component_tokens(self.state.name, str(ctx.mime), str(ctx.name), metadata))

    def visitUnparsed_block(self, ctx: Parser.Unparsed_blockContext):
        # We want to extract the source-file line number (and filename) for use in the C-preprocessor
        # via `#file {number} "{filename}"` directives, for more expressive error handling
        line_number = None if ctx.start is None else ctx.start.line
        return self.filename, line_number, "" if ctx.content is None else str(ctx.content)

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
        return self.visit(ctx.expr())

    def visitExpressionFloat(self, ctx: Parser.ExpressionFloatContext):
        return float(str(ctx.FloatingLiteral()))

    def visitExpressionArrayAccess(self, ctx: Parser.ExpressionArrayAccessContext):
        return f'{ctx.Identifier()}[{self.visit(ctx.expr())}]'

    def visitExpressionIdentifier(self, ctx: Parser.ExpressionIdentifierContext):
        return str(ctx.Identifier())

    def visitExpressionInteger(self, ctx: Parser.ExpressionIntegerContext):
        return int(str(ctx.Identifier()))

    def visitExpressionExponentiation(self, ctx: Parser.ExpressionExponentiationContext):
        base = self.visit(ctx.base)
        exponent = self.visit(ctx.exponent)
        if isinstance(base, str) or isinstance(exponent, str):
            return f'powf({base}, {exponent})'
        return base ** exponent

    def visitExpressionBinaryPM(self, ctx: Parser.ExpressionBinaryPMContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if isinstance(left, str) or isinstance(right, str):
            return f"{left} {'+' if ctx.Minus() is None else '-'} {right}"
        return left + right if ctx.Minus() is None else left - right

    def visitExpressionFunctionCall(self, ctx: Parser.ExpressionFunctionCallContext):
        return f'{ctx.Identifier()}({self.visit(ctx.expr())}'

    def visitExpressionBinaryMD(self, ctx: Parser.ExpressionBinaryMDContext):
        left, right = self.visit(ctx.left), self.visit(ctx.right)
        if isinstance(left, str) or isinstance(right, str):
            return f"{left} {'*' if ctx.Div() is None else '/'} {right}"
        return left * right if ctx.Div() is None else left / right

    def visitInitializerlist(self, ctx: Parser.InitializerlistContext):
        values = [self.visit(x) for x in ctx.values()]
        if any(isinstance(x, str) for x in values):
            return '{' + ','.join([str(x) for x in values]) + '}'
        return tuple(values)
