from .expression import (
    Expr, UnaryOp, BinaryOp, Value, ObjectType, ShapeType, DataType, TrinaryOp
)

def visitSomething(obj, ctx):
    pass

def getExpr(obj, ctx):
    return obj.visit(ctx)

# TODO (maybe) Add control and statements into McCode, requiring some form of global stack.
def visitExpressionUnaryPM(obj, ctx):
    right = obj.visit(ctx.expr())
    if isinstance(right, str):
        return '-' + right if ctx.Plus() is None else right
    return -right if ctx.Plus() is None else right

def visitExpressionGrouping(obj, ctx):
    return Expr(UnaryOp('__group__', obj.visit(ctx.expr())))

def visitExpressionFloat(obj, ctx):
    return Expr.float(str(ctx.FloatingLiteral()))

def visitExpressionPointerAccess(obj, ctx):
    pointer = Expr(Value(str(ctx.Identifier()), object_type=ObjectType.identifier))
    return Expr(BinaryOp('__pointer_access__', pointer, obj.visit(ctx.expr())))

def visitExpressionStructAccess(obj, ctx):
    struct = Expr(Value(str(ctx.Identifier()), object_type=ObjectType.identifier))
    return Expr(BinaryOp('__struct_access__', struct, obj.visit(ctx.expr())))

def visitExpressionArrayAccess(obj, ctx):
    array = Expr(Value(str(ctx.Identifier()), object_type=ObjectType.identifier, shape_type=ShapeType.vector))
    return Expr(BinaryOp('__getitem__', array, obj.visit(ctx.expr())))

def visitExpressionIdentifier(obj, ctx):
    # check if this identifier is an InstrumentParameter name:
    name = str(ctx.Identifier())
    inst_par = obj.state.get_parameter(name, None)
    obj = ObjectType.parameter if inst_par is not None else ObjectType.identifier
    dat = inst_par.value.data_type if inst_par is not None else DataType.undefined
    return Expr(Value(name, data_type=dat, object_type=obj))

def visitExpressionInteger(obj, ctx):
    return Expr.int(str(ctx.IntegerLiteral()))

def visitExpressionZero(obj, ctx):
    return Expr.int(0)

def visitExpressionExponentiation(obj, ctx):
    base, exponent = [obj.visit(ex) for ex in ctx.expr()]
    return base ** exponent

def visitExpressionBinaryPM(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return left + right if ctx.Minus() is None else left - right

def visitExpressionFunctionCall(obj, ctx):
    function = Value(str(ctx.Identifier()), object_type=ObjectType.function)
    # `ctx.args` isn't exposed by speedy-antlr-tool, but the function call is
    args = [obj.visit(arg).expr[0] for arg in ctx.expr()]  # each is a Value, UnaryOp, or BinaryOp?
    return Expr(BinaryOp('__call__', function, args))

def visitExpressionBinaryMD(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return left * right if ctx.Div() is None else left / right

def visitExpressionBinaryMod(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return Expr(BinaryOp('%', left, right))

def visitExpressionBinaryLeftShift(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return Expr(BinaryOp('<<', left, right))

def visitExpressionBinaryRightShift(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return Expr(BinaryOp('>>', left, right))

def visitInitializerlist(obj, ctx):
    # `ctx.values` is not exposed by speedy-antlr-tool
    values = [obj.visit(x).expr[0].value for x in ctx.expr()]
    return Expr(Value(values, object_type=ObjectType.initializer_list, shape_type=ShapeType.vector))

def visitExpressionUnaryLogic(obj, ctx):
    expr = obj.visit(ctx.expr())
    op = 'unknown'
    if ctx.Not() is not None:
        op = '__not__'
    return Expr(UnaryOp(op, expr))

def visitExpressionBinaryLogic(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    op = 'unknown'
    if ctx.AndAnd() is not None:
        op = '__and__'
    elif ctx.OrOr() is not None:
        op = '__or__'
    return Expr(BinaryOp(op, left, right))

def visitExpressionTrinaryLogic(obj, ctx):
    # `ctx.test`, `ctx.true_`, and `ctx._false` not exposed by speedy-antlr-tool
    test, true, false = [obj.visit(x) for x in ctx.expr()]
    return Expr(TrinaryOp('__trinary__', test, true, false))

def visitExpressionBinaryEqual(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return Expr(BinaryOp('__eq__', left, right))

def visitExpressionBinaryLessEqual(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return Expr(BinaryOp('__le__', left, right))

def visitExpressionBinaryGreaterEqual(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return Expr(BinaryOp('__ge__', left, right))

def visitExpressionBinaryLess(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return Expr(BinaryOp('__lt__', left, right))

def visitExpressionBinaryGreater(obj, ctx):
    # `ctx.left` and `ctx.right` are not exposed by speedy-antlr-tool
    left, right = [obj.visit(ex) for ex in ctx.expr()]
    return Expr(BinaryOp('__gt__', left, right))

def visitExpressionString(obj, ctx):
    strings = ''.join(str(sl).strip('"') for sl in ctx.StringLiteral())
    return Expr.str(f'"{strings}"')


common_visitors = (
    ('getExpr', getExpr),
    ('visitExpressionUnaryPM', visitExpressionUnaryPM),
    ('visitExpressionGrouping', visitExpressionGrouping),
    ('visitExpressionFloat', visitExpressionFloat),
    ('visitExpressionPointerAccess', visitExpressionPointerAccess),
    ('visitExpressionStructAccess', visitExpressionStructAccess),
    ('visitExpressionArrayAccess', visitExpressionArrayAccess),
    ('visitExpressionIdentifier', visitExpressionIdentifier),
    ('visitExpressionInteger', visitExpressionInteger),
    ('visitExpressionZero', visitExpressionZero),
    ('visitExpressionExponentiation', visitExpressionExponentiation),
    ('visitExpressionBinaryPM', visitExpressionBinaryPM),
    ('visitExpressionFunctionCall', visitExpressionFunctionCall),
    ('visitExpressionBinaryMD', visitExpressionBinaryMD),
    ('visitExpressionBinaryMod', visitExpressionBinaryMod),
    ('visitExpressionBinaryLeftShift', visitExpressionBinaryLeftShift),
    ('visitExpressionBinaryRightShift', visitExpressionBinaryRightShift),
    ('visitInitializerlist', visitInitializerlist),
    ('visitExpressionUnaryLogic', visitExpressionUnaryLogic),
    ('visitExpressionBinaryLogic', visitExpressionBinaryLogic),
    ('visitExpressionTrinaryLogic', visitExpressionTrinaryLogic),
    ('visitExpressionBinaryEqual', visitExpressionBinaryEqual),
    ('visitExpressionBinaryLessEqual', visitExpressionBinaryLessEqual),
    ('visitExpressionBinaryGreaterEqual', visitExpressionBinaryGreaterEqual),
    ('visitExpressionBinaryLess', visitExpressionBinaryLess),
    ('visitExpressionBinaryGreater', visitExpressionBinaryGreater),
    ('visitExpressionString', visitExpressionString),
)

def add_common_visitors(grammar_visitor):
    for name, func in common_visitors:
        setattr(grammar_visitor, name, func)
