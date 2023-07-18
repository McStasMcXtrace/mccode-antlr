from ..grammar import McCompLexer, McCompParser as Parser, McCompVisitor
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


def context_to_component_parameter(a: Parser.Component_parameterContext):
    name = str(a.Identifer(0))
    default = None
    if isinstance(a, Parser.ComponentParameterDoubleContext):
        if a.Assign() is not None:
            default = context_expr_to_value(a.expr())
        value = Value(Value.Type.float, default)
    elif isinstance(a, Parser.ComponentParameterIntegerContext):
        if a.Assign() is not None:
            default = context_expr_to_value(a.expr())
        value = Value(Value.Type.int, default)
    elif isinstance(a, Parser.ComponentParameterStringContext):
        if a.Assign() is not None:
            default = 'NULL' if a.StringLiteral() is None else a.StringLiteral()
        value = Value(Value.Type.str, default)
    elif isinstance(a, (Parser.ComponentParameterVectorContext, Parser.ComponentParameterDoubleArrayContext)):
        if a.Assign() is not None:
            if a.Identifier() is not None:
                default = a.Identifer()
            elif a.initializerlist() is not None:
                default = context_initializer_list_to_tuple(a.initializerlist())
            else:
                default = "NULL"
        value = Value(Value.Type.float_array, default)
    elif isinstance(a, Parser.ComponentParameterIntArrayContext):
        if a.Assign() is not None:
            if a.Identifer() is not None:
                default = a.Identifer()
            elif a.initializerlist() is not None:
                default = context_initializer_list_to_tuple(a.initializerlist())
            else:
                default = "NULL"
        value = Value(Value.Type.int_array, default)
    else:
        raise RuntimeError(f"Unhandled context type {type(a)}")
    return ComponentParameter(name=name, value=value)


def context_to_component_parameters(a: Parser.Component_parametersContext):
    return [context_to_component_parameter(x) for x in a.component_parameter()]


def context_to_component_metadata(component_name: str, a: Parser.MetadataContext):
    mimetype, name = None, None
    if isinstance(a, Parser.MetadataIdIdContext):
        mimetype, name = [str(x) for x in a.Identifier()]
    elif isinstance(a, Parser.MetadataIdStrContext):
        mimetype = str(a.Identifer())
        name = str(a.StringLiteral())
    elif isinstance(a, Parser.MetadataStrIdContext):
        mimetype = str(a.StringLiteral())
        name = str(a.StringLiteral())
    elif isinstance(a, Parser.MetaDataStrStrContext):
        mimetype, name = [str(x) for x in a.StringLiteral()]
    else:
        raise RuntimeError(f"Unsupported Metadata context type {type(a)}")
    return MetaData.from_component_tokens(component_name, mimetype, name, str(a.UnparsedBlock()))


class CompVisitor(McCompVisitor):
    def __init__(self, parent):
        self.parent = parent  # the instrument (handler?) that wanted to read this component
        self.state = Comp()

    def visitComponentDefineNew(self, ctx: Parser.ComponentDefineNewContext):
        self.state.name = str(ctx.Identifer())
        self._fillComponentDefineState(ctx)
        return self.state

    def visitComponentDefineCopy(self, ctx: Parser.ComponentDefinecopyContext):
        from copy import deepcopy
        new_name, copy_from = [str(x) for x in ctx.Identifer()]
        # ... find and parse the component named in copy_from ... TODO Implement this in instr.visitor(?)
        if self.parent is None:
            raise RuntimeError("Can not copy a component definition without a parent instrument")
        copy_from_comp = self.parent.get_named_component_from_definition(copy_from)
        # pull from that component ... deepcopy _just_ in case
        self.state = deepcopy(copy_from_comp)
        # update the name to match what we're going to call this component
        self.state.name = new_name
        # add parameters, overwrite unparsed blocks
        self._fillComponentDefineState(ctx)
        return self.state

    def _fillComponentDefineState(self, ctx):

        sets = ctx.component_parameter_set()
        # DEFINE PARAMETER
        for par in context_to_component_parameters(sets.define_parameters().component_parameters()):
            self.state.add_parameter(par)
        # DEFINE SETTING
        for par in context_to_component_parameters(sets.set_parameters().component_parameters()):
            self.state.add_setting(par)
        # DEFINE OUTPUT
        for par in context_to_component_parameters(sets.out_parameters().component_parameters()):
            self.state.add_output(par)

        if ctx.metadata() is not None:
            self.state.metadata = tuple(context_to_component_metadata(self.state.name, x) for x in ctx.metadata())

        if ctx.shell() is not None:
            print(f"Implement executing shell scripts like\n\t{str(ctx.shell().StringLiteral())}")

        if ctx.dependency() is not None:
            self.state.dependency = ctx.dependency().StringLiteral()

        if ctx.NoAcc() is not None:
            self.state.no_acc()

        if ctx.share() is not None:
            self.state.SHARE(ctx.share().UnparsedBlock())

        if ctx.uservars() is not None:
            self.state.USERVARS(ctx.uservars().UnparsedBlock())

        if ctx.declare() is not None:
            self.state.DECLARE(ctx.declare().UnparsedBlock())

        if ctx.initialize() is not None:
            self.state.INITIALIZE(ctx.initialize().UnparsedBlock())

        if ctx.component_trace() is not None:
            self.state.TRACE(ctx.component_trace().UnparsedBlock())

        if ctx.save() is not None:
            self.state.SAVE(ctx.save().UnparsedBlock())

        if ctx.finally_() is not None:
            self.state.FINALLY(ctx.finally_().UnparsedBlock())

        if ctx.display() is not None:
            self.state.DISPLAY(ctx.display().UnparsedBlock())





