from ..grammar import McCompParser as Parser, McCompVisitor
from .comp import Comp
from ..common import ComponentParameter, Value, MetaData


def context_expr_to_value(a: Parser.ExprContext, memory: dict = None):
    if memory is None:
        memory = dict()
    if isinstance(a, Parser.ExpressionIdentifierContext):
        ident = str(a.Identifier())
        if ident in memory:
            return memory[ident]
        return ident
    if isinstance(a, Parser.ExpressionFloatContext):
        return float(str(a.FloatingLiteral()))
    if isinstance(a, Parser.ExpressionIntegerContext):
        return int(str(a.IntegerLitera()))
    if isinstance(a, Parser.ExpressionGroupingContext):
        value = context_expr_to_value(a.expr(), memory)
        if isinstance(value, str):
            if any(x in value for x in ('+', '-', ' ', '^')):
                return '(' + value + ')'
        return value
    if isinstance(a, Parser.ExpressionBinaryPMContext):
        left, right = [context_expr_to_value(x, memory) for x in a.expr()]
        op = '+' if a.Plus() is not None else '-'
        if isinstance(left, str) or isinstance(right, str):
            return f'{left} {op} {right}'
        return left + right if op == '+' else left - right
    if isinstance(a, Parser.ExpressionBinaryMDContext):
        left, right = [context_expr_to_value(x, memory) for x in a.expr()]
        op = '*' if a.Star() is not None else '/'
        if isinstance(left, str) or isinstance(right, str):
            return f'{left} {op} {right}'
        return left * right if op == '*' else left / right
    if isinstance(a, Parser.ExpressionExponentiationContext):
        left, right = [context_expr_to_value(x, memory) for x in a.expr()]
        if isinstance(left, str) or isinstance(right, str):
            return f'powf({left}, {right})'
        return left ** right
    if isinstance(a, Parser.ExpressionUnaryPMContext):
        right = context_expr_to_value(a.expr(), memory)
        if isinstance(right, str):
            return '-' + right if a.Plus() is None else right
        return -right if a.Plus() is None else right
    if isinstance(a, Parser.ExpressionFunctionCallContext):
        argument = context_expr_to_value(a.expr(), memory)
        if a.Identifer() not in memory:
            return f'{a.Identifer()}({argument})'
        return memory[a.Identifer()](argument)
    if isinstance(a, Parser.EpressionArrayAccessContext):
        argument = context_expr_to_value(a.expr(), memory)
        if a.Identifer() not in memory:
            return f'{a.Identifer()}[{argument}]'
        return memory[a.Identifier()][argument]


def context_initializer_list_to_tuple(a: Parser.InitializerlistContext):
    return tuple(context_expr_to_value(x) for x in a.expr())


class CompVisitor(McCompVisitor):
    def __init__(self, parent):
        self.parent = parent  # the instrument (handler?) that wanted to read this component
        self.state = Comp()

    def visitComponentDefineNew(self, ctx: Parser.ComponentDefineNewContext):
        self.state.name = str(ctx.Identifer())
        if ctx.NoAcc() is not None:
            self.state.no_acc()
        self.visitChildren(ctx)  # Use the visitor methods to fill in details of the state
        return self.state

    def visitComponentDefineCopy(self, ctx: Parser.ComponentDefinecopyContext):
        from copy import deepcopy
        new_name, copy_from = [str(x) for x in ctx.Identifer()]
        if self.parent is None:
            raise RuntimeError("Can not copy a component definition without a parent instrument")
        copy_from_comp = self.parent.get_named_component(copy_from)
        # pull from that component ... deepcopy _just_ in case
        self.state = deepcopy(copy_from_comp)
        # update the name to match what we're going to call this component
        self.state.name = new_name
        # add parameters, overwrite all provided details
        if ctx.NoAcc() is not None:
            self.state.no_acc()
        self.visitChildren(ctx)  # Use the visitor methods to overwrite details of the state
        return self.state

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
        self.parent.add_cflags(self.visit(ctx.StringLiteral()))

    def visitDeclareBlock(self, ctx: Parser.DeclareBlockContext):
        self.state.DECLARE(self.visit(ctx.unparsed_block()))

    def visitDeclareBlockCopy(self, ctx: Parser.DeclareBlockCopyContext):
        copy_from = self.parent.get_named_component(str(ctx.Identifier()))
        self.state.DECLARE(copy_from.declare + '\n' + self.visit(ctx.unparsed_block()))

    def visitShareBlock(self, ctx: Parser.ShareBlockContext):
        self.state.SHARE(self.visit(ctx.unparsed_block()))

    def visitShareBlockCopy(self, ctx: Parser.ShareBlockCopyContext):
        copy_from = self.parent.get_named_component(str(ctx.Identifier()))
        self.state.SHARE(copy_from.share + '\n' + self.visit(ctx.unparsed_block()))

    def visitInitialzieBlock(self, ctx: Parser.InitializeBlockContext):
        self.state.INITIALIZE(self.visit(ctx.unparsed_block()))

    def visitInitializeBlockCopy(self, ctx: Parser.InitializeBlockCopyContext):
        copy_from = self.parent.get_named_component(str(ctx.Identifier()))
        self.state.INITIALIZE(copy_from.initialize + '\n' + self.visit(ctx.unparsed_block()))

    def visitUservars(self, ctx: Parser.UservarsContext):
        self.state.USERVARS(self.visit(ctx.unparsed_block()))

    def visitSaveBlock(self, ctx: Parser.SaveBlockContext):
        self.state.SAVE(self.visit(ctx.unparsed_block()))

    def visitSaveBlockCopy(self, ctx: Parser.SaveBlockCopyContext):
        copy_from = self.parent.get_named_component(str(ctx.Identifier()))
        self.state.SAVE(copy_from.save + '\n' + self.visit(ctx.unparsed_block()))

    def visitFinallyBlock(self, ctx: Parser.FinallyBlockContext):
        self.state.FINALLY(self.visit(ctx.unparsed_block()))

    def visitFinallyBlockCopy(self, ctx: Parser.FinallyBlockCopyContext):
        copy_from = self.parent.get_named_component(str(ctx.Identifier()))
        self.state.FINALLY(copy_from.final + '\n' + self.visit(ctx.unparsed_block()))

    def visitDisplayBlock(self, ctx: Parser.DisplayBlockContext):
        self.state.DISPLAY(self.visit(ctx.unparsed_block()))

    def visitDisplayBlockCopy(self, ctx: Parser.DisplayBlockCopyContext):
        copy_from = self.parent.get_named_component(str(ctx.Identifier()))
        self.state.DISPLAY(copy_from.display + '\n' + self.visit(ctx.unparsed_block()))

    def visitMetadata(self, ctx: Parser.MetadataContext):
        metadata = self.visit(ctx.unparsed_block())
        self.state.add_metadata(MetaData.from_component_tokens(self.state.name, str(ctx.mime), str(ctx.name), metadata))

    def visitUnparsed_block(self, ctx: Parser.Unparsed_blockContext):
        return "" if ctx.content is None else str(ctx.content)

# TODO Implement all of these visitors
    def visitExpressionUnaryPM(self, ctx: Parser.ExpressionUnaryPMContext):
        return self.visitChildren(ctx)

    def visitExpressionGrouping(self, ctx: Parser.ExpressionGroupingContext):
        return self.visitChildren(ctx)

    def visitExpressionFloat(self, ctx: Parser.ExpressionFloatContext):
        return self.visitChildren(ctx)

    def visitExpressionArrayAccess(self, ctx: Parser.ExpressionArrayAccessContext):
        return self.visitChildren(ctx)

    def visitExpressionIdentifier(self, ctx: Parser.ExpressionIdentifierContext):
        return self.visitChildren(ctx)

    def visitExpressionInteger(self, ctx: Parser.ExpressionIntegerContext):
        return self.visitChildren(ctx)

    def visitExpressionExponentiation(self, ctx: Parser.ExpressionExponentiationContext):
        return self.visitChildren(ctx)

    def visitExpressionBinaryPM(self, ctx: Parser.ExpressionBinaryPMContext):
        return self.visitChildren(ctx)

    def visitExpressionFunctionCall(self, ctx: Parser.ExpressionFunctionCallContext):
        return self.visitChildren(ctx)

    def visitExpressionBinaryMD(self, ctx: Parser.ExpressionBinaryMDContext):
        return self.visitChildren(ctx)

    def visitInitializerlist(self, ctx: Parser.InitializerlistContext):
        return self.visitChildren(ctx)