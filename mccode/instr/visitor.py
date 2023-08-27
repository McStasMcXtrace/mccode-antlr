from ..grammar import McInstrParser, McInstrVisitor
from ..common import InstrumentParameter, MetaData, Expr
from .instr import Instr
from .instance import Instance
from .jump import Jump


class InstrVisitor(McInstrVisitor):
    def __init__(self, parent, filename):
        self.parent = parent
        self.filename = filename
        self.state = Instr()

    def visitProg(self, ctx: McInstrParser.ProgContext):
        self.state = Instr()
        self.visit(ctx.instrument_definition())
        return self.state

    def visitInstrument_definition(self, ctx: McInstrParser.Instrument_definitionContext):
        self.state.name = str(ctx.Identifier())
        self.visitChildren(ctx)
        self.state.determine_groups()

    def visitInstrument_parameters(self, ctx: McInstrParser.Instrument_parametersContext):
        for param in ctx.params:
            self.state.add_parameter(self.visit(param))

    def getInstrument_parameter(self, ctx: McInstrParser.Instrument_parameterContext):
        return self.visit(ctx)

    def visitInstrument_metadata(self, ctx: McInstrParser.Instrument_metadataContext):
        for metadata_context in ctx.metadata():
            mime, name, metadata = self.visit(metadata_context)
            self.state.add_metadata(MetaData.from_instrument_tokens(self.state.name, mime, name, metadata))

    def visitInstrumentParameterDouble(self, ctx: McInstrParser.InstrumentParameterDoubleContext):
        name = str(ctx.Identifier())
        unit = None if ctx.instrument_parameter_unit() is None else self.visit(ctx.instrument_parameter_unit())
        value = None if ctx.Assign() is None else self.visit(ctx.expr())
        return InstrumentParameter(name, unit, Expr.float(value))

    def visitInstrumentParameterInteger(self, ctx: McInstrParser.InstrumentParameterIntegerContext):
        name = str(ctx.Identifier())
        unit = None if ctx.instrument_parameter_unit() is None else self.visit(ctx.instrument_parameter_unit())
        value = None if ctx.Assign() is None else self.visit(ctx.expr())
        return InstrumentParameter(name, unit, Expr.int(value))

    def visitInstrumentParameterString(self, ctx: McInstrParser.InstrumentParameterStringContext):
        name = str(ctx.Identifier())
        unit = None if ctx.instrument_parameter_unit() is None else self.visit(ctx.instrument_parameter_unit())
        value = None if ctx.Assign() is None else str(ctx.StringLiteral())
        return InstrumentParameter(name, unit, Expr.str(value))

    def visitInstrument_parameter_unit(self, ctx: McInstrParser.Instrument_parameter_unitContext):
        return str(ctx.StringLiteral())

    def visitInstrument_trace(self, ctx: McInstrParser.Instrument_traceContext):
        return self.visitChildren(ctx)

    def visitInstrument_trace_include(self, ctx: McInstrParser.Instrument_trace_includeContext):
        instr = self.parent.get_instrument(str(ctx.StringLiteral()))
        # TODO work out how/what to copy from the other instrument into this one
        self.state.add_included(instr.name)
        for par in instr.parameters:
            self.state.add_parameter(par)
        for meta in instr.metadata:
            self.state.add_metadata(meta)
        if len(instr.declare):
            self.state.declare += instr.declare
        if len(instr.user):
            self.state.user += instr.user
        if len(instr.initialize):
            self.state.initialize += instr.initialize
        if len(instr.save):
            self.state.save += instr.save
        if len(instr.final):
            self.state.final += instr.final
        # McCode3 parsed everything in one memory space, so used some trickery to include
        # component instances from one instrument into another. Here we can be a bit more straightforward
        for instance in instr.components:
            if not instance.removable:
                self.state.add_component(instance)
        # Group membership is determined after all parsing, so nothing to do here

    def visitComponent_instance(self, ctx: McInstrParser.Component_instanceContext):
        name = self.visit(ctx.instance_name())
        comp = self.visit(ctx.component_type())
        at = self.visit(ctx.place())
        if ctx.orientation() is not None:
            rotate = self.visit(ctx.orientation())
        else:
            # In the case of "AT (x, y, z) ABSOLUTE" or "AT (x, y, z) RELATIVE identifier"
            # We must use *the same* relative information for the rotation -- at[1] is None or a valid instance:
            rotate = ((Expr.int(0), Expr.int(0), Expr.int(0)), at[1])
        instance = Instance(name, comp, at, rotate)
        if ctx.instance_parameters() is not None:
            for param_name, param_value in self.visit(ctx.instance_parameters()):
                instance.set_parameter(param_name, param_value)
        if ctx.Removable() is not None:
            instance.REMOVABLE()
        if ctx.Cpu() is not None:
            instance.CPU()
        if ctx.split() is not None:
            instance.SPLIT(self.visit(ctx.split()))
        if ctx.when() is not None:
            instance.WHEN(self.visit(ctx.when()))
        if ctx.groupref() is not None:
            instance.GROUP(self.visit(ctx.groupref()))
        if ctx.extend() is not None:
            instance.EXTEND(self.visit(ctx.extend()))
        if ctx.jumps() is not None:
            instance.JUMP(*self.visit(ctx.jumps()))
        if ctx.metadata() is not None:
            # deal with definition vs instance metadata here?
            for metadata_context in ctx.metadata():
                mime, name, metadata = self.visit(metadata_context)
                instance.add_metadata(MetaData.from_component_tokens(name, str(ctx.mime), str(ctx.name), metadata))
        # Include this instantiated component instance in the instrument components list
        self.state.add_component(instance)

    def visitInstanceNameCopyIdentifier(self, ctx: McInstrParser.InstanceNameCopyIdentifierContext):
        return f'{ctx.Identifier()}_{len(self.state.components)+1}'

    def visitInstanceNameCopy(self, ctx: McInstrParser.InstanceNameCopyContext):
        return f'Comp_{len(self.state.components) + 1}'

    def visitInstanceNameIdentifier(self, ctx: McInstrParser.InstanceNameIdentifierContext):
        return str(ctx.Identifier())

    def visitComponentTypeCopy(self, ctx: McInstrParser.ComponentTypeCopyContext):
        return self.visit(ctx.component_ref())

    def visitComponentTypeIdentifier(self, ctx: McInstrParser.ComponentTypeIdentifierContext):
        return self.parent.get_component(str(ctx.Identifier()))

    def visitInstance_parameters(self, ctx: McInstrParser.Instance_parametersContext):
        return [self.visit(p) for p in ctx.params]

    def visitInstanceParameterExpr(self, ctx: McInstrParser.InstanceParameterExprContext):
        return str(ctx.Identifier()), self.visit(ctx.expr())

    def visitInstanceParameterString(self, ctx: McInstrParser.InstanceParameterStringContext):
        # A string-literal instance parameter is never an identifier
        return str(ctx.Identifier()), Expr.str(str(ctx.StringLiteral()))

    def visitSplit(self, ctx: McInstrParser.SplitContext):
        return Expr.int(10) if ctx.expr() is None else self.visit(ctx.expr())

    def visitWhen(self, ctx: McInstrParser.WhenContext):
        return self.visit(ctx.expr())

    def visitPlace(self, ctx: McInstrParser.PlaceContext):
        vector = self.visit(ctx.coords())
        relative = self.visit(ctx.reference())
        return vector, relative

    def visitOrientation(self, ctx: McInstrParser.OrientationContext):
        angles = self.visit(ctx.coords())
        relative = self.visit(ctx.reference())
        return angles, relative

    def visitGroupref(self, ctx: McInstrParser.GrouprefContext):
        return str(ctx.Identifier())

    def visitJumps(self, ctx: McInstrParser.JumpsContext):
        return [self.visit(j) for j in ctx.jump()]

    def visitJump(self, ctx: McInstrParser.JumpContext):
        name, index = self.visit(ctx.jumpname())
        iterate = ctx.Iterate() is not None  # and ctx.When() is None
        condition = self.visit(ctx.expr())
        return Jump(name, index, iterate, condition)

    def visitJumpPrevious(self, ctx: McInstrParser.JumpPreviousContext):
        i = ctx.IntegerLiteral()
        return ("PREVIOUS", -1) if i is None else (f"PREVIOUS_{i}", -int(i))

    def visitJumpMyself(self, ctx: McInstrParser.JumpMyselfContext):
        return "MYSELF", 0

    def visitJumpNext(self, ctx: McInstrParser.JumpNextContext):
        i = ctx.IntegerLiteral()
        return ("NEXT", 1) if i is None else (f"NEXT_{i}", int(i))

    def visitJumpIdentifier(self, ctx: McInstrParser.JumpIdentifierContext):
        return str(ctx.Identifier()), 0

    def visitComponent_ref(self, ctx: McInstrParser.Component_refContext):
        if ctx.Previous() is not None:
            count = 1 if ctx.IntegerLiteral() is None else int(str(ctx.IntegerLiteral()))
            return self.state.last_component(count, removable_ok=False)
        return self.state.get_component(str(ctx.Identifier()))

    def visitCoords(self, ctx: McInstrParser.CoordsContext):
        # A coordinate is _always_ a float, even when represented by an expression or identifier
        # Actually implement the visitExpr variants correctly?
        return tuple([Expr.float(self.visit(x)) for x in ctx.expr()])

    def visitReference(self, ctx: McInstrParser.ReferenceContext):
        # ABSOLUTE or RELATIVE ABSOLUTE -> None
        return self.visit(ctx.component_ref()) if ctx.Absolute() is None else None

    def visitDependency(self, ctx: McInstrParser.DependencyContext):
        return str(ctx.StringLiteral())

    def visitDeclareBlock(self, ctx: McInstrParser.DeclareBlockContext):
        self.state.DECLARE(self.visit(ctx.unparsed_block()))

    def visitUservars(self, ctx: McInstrParser.UservarsContext):
        self.state.USERVARS(self.visit(ctx.unparsed_block()))

    def visitInitializeBlock(self, ctx: McInstrParser.InitializeBlockContext):
        self.state.INITIALIZE(self.visit(ctx.unparsed_block()))

    def visitSaveBlock(self, ctx: McInstrParser.SaveBlockContext):
        self.state.SAVE(self.visit(ctx.unparsed_block()))

    def visitFinallyBlock(self, ctx: McInstrParser.FinallyBlockContext):
        self.state.FINALLY(self.visit(ctx.unparsed_block()))

    def visitDeclareBlockCopy(self, ctx: McInstrParser.DeclareBlockCopyContext):
        line_number = None if ctx.start is None else ctx.start.line
        raise RuntimeError(f"{self.filename}: {line_number} -- DECLARE COPY only valid in comp files")
        # copy_from = self.parent.get_instrument(str(ctx.Identifier()))
        # self.state.DECLARE(copy_from.declare, self.visit(ctx.unparsed_block()))

    def visitInitializeBlockCopy(self, ctx: McInstrParser.InitializeBlockCopyContext):
        line_number = None if ctx.start is None else ctx.start.line
        raise RuntimeError(f"{self.filename}: {line_number} -- INITIALIZE COPY only valid in comp files")
        # copy_from = self.parent.get_instrument(str(ctx.Identifier()))
        # self.state.INITIALIZE(copy_from.initialize, self.visit(ctx.unparsed_block()))

    def visitSaveBlockCopy(self, ctx: McInstrParser.SaveBlockCopyContext):
        line_number = None if ctx.start is None else ctx.start.line
        raise RuntimeError(f"{self.filename}: {line_number} -- SAVE COPY only valid in comp files")
        # copy_from = self.parent.get_instrument(str(ctx.Identifier()))
        # self.state.SAVE(copy_from.save, self.visit(ctx.unparsed_block()))

    def visitFinallyBlockCopy(self, ctx: McInstrParser.FinallyBlockCopyContext):
        line_number = None if ctx.start is None else ctx.start.line
        raise RuntimeError(f"{self.filename}: {line_number} -- FINALLY COPY only valid in comp files")
        # copy_from = self.parent.get_instrument(str(ctx.Identifier()))
        # self.state.FINALLY(copy_from.final, self.visit(ctx.unparsed_block()))

    def visitExtend(self, ctx: McInstrParser.ExtendContext):
        return self.visit(ctx.unparsed_block())

    def visitMetadata(self, ctx: McInstrParser.MetadataContext):
        filename, line_number, metadata = self.visit(ctx.unparsed_block())
        return str(ctx.mime), str(ctx.name), metadata

    def visitUnparsed_block(self, ctx: McInstrParser.Unparsed_blockContext):
        # We want to extract the source-file line number (and filename) for use in the C-preprocessor
        # via `#line {number} "{filename}"` directives, for more expressive error handling
        line_number = None if ctx.start is None else ctx.start.line
        if line_number is None:
            print(f'Why is line none for {self.filename} {ctx.UnparsedBlock()}')
        return self.filename, line_number,  str(ctx.UnparsedBlock())[2:-2]

    def visitShell(self, ctx: McInstrParser.ShellContext):
        from subprocess import run
        args = str(ctx.StringLiteral()).split(' ')
        run(args, shell=True, check=True)

    def visitSearchPath(self, ctx: McInstrParser.SearchPathContext):
        self.parent.handle_search_keyword(str(ctx.StringLiteral()))

    def visitSearchShell(self, ctx: McInstrParser.SearchShellContext):
        from subprocess import run
        args = str(ctx.StringLiteral()).split()
        res = run(args, shell=True, capture_output=True, check=True)
        for specs in res.stdout.decode().split('\n'):
            self.parent.handle_search_keyword(specs)

    # TODO Make this and the identical list of visitors in comp/visitor.py a single definition ... somehow
    # FIXME There *are* no statements in McCode, so all identifiers always produce un-parsable values.
    def visitAssignment(self, ctx: McInstrParser.AssignmentContext):
        line_number = None if ctx.start is None else ctx.start.line
        raise RuntimeError(f"{self.filename}: {line_number} -- assignment statements are not (yet) supported")

    # TODO (maybe) Add control and statements into McCode, requiring some form of global stack.
    def visitExpressionUnaryPM(self, ctx: McInstrParser.ExpressionUnaryPMContext):
        right = self.visit(ctx.expr())
        if isinstance(right, str):
            return '-' + right if ctx.Plus() is None else right
        return -right if ctx.Plus() is None else right

    def visitExpressionGrouping(self, ctx: McInstrParser.ExpressionGroupingContext):
        from ..common import UnaryOp
        return Expr(UnaryOp('__group__', self.visit(ctx.expr())))

    def visitExpressionFloat(self, ctx: McInstrParser.ExpressionFloatContext):
        return Expr.float(str(ctx.FloatingLiteral()))

    def visitExpressionArrayAccess(self, ctx: McInstrParser.ExpressionArrayAccessContext):
        from ..common import BinaryOp, Value, ShapeType, ObjectType
        array = Expr(Value(str(ctx.Identifer()), object_type=ObjectType.identifier, shape_type=ShapeType.vector))
        return Expr(BinaryOp('__getitem__', array, self.visit(ctx.expr())))

    def visitExpressionIdentifier(self, ctx: McInstrParser.ExpressionIdentifierContext):
        from ..common import Value, ObjectType, parameter_name_present
        # check if this identifier is an InstrumentParameter name:
        name = str(ctx.Identifier())
        obj = ObjectType.parameter if parameter_name_present(self.state.parameters, name) else ObjectType.identifier
        return Expr(Value(name, object_type=obj))

    def visitExpressionInteger(self, ctx: McInstrParser.ExpressionIntegerContext):
        return Expr.int(str(ctx.IntegerLiteral()))

    def visitExpressionZero(self, ctx: McInstrParser.ExpressionZeroContext):
        return Expr.int(0)

    def visitExpressionExponentiation(self, ctx: McInstrParser.ExpressionExponentiationContext):
        base = self.visit(ctx.base)
        exponent = self.visit(ctx.exponent)
        return base ** exponent

    def visitExpressionBinaryPM(self, ctx: McInstrParser.ExpressionBinaryPMContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + right if ctx.Minus() is None else left - right

    def visitExpressionFunctionCall(self, ctx: McInstrParser.ExpressionFunctionCallContext):
        from ..common import BinaryOp, Value, ObjectType
        function = Value(str(ctx.Identifier()), object_type=ObjectType.function)
        return Expr(BinaryOp('__call__', function, self.visit(ctx.expr())))

    def visitExpressionBinaryMD(self, ctx: McInstrParser.ExpressionBinaryMDContext):
        left, right = self.visit(ctx.left), self.visit(ctx.right)
        return left * right if ctx.Div() is None else left / right

    def visitInitializerlist(self, ctx: McInstrParser.InitializerlistContext):
        from ..common import Value, ObjectType, ShapeType
        values = [self.visit(x).expr.value for x in ctx.values()]
        return Expr(Value(values, object_type=ObjectType.initializer_list, shape_type=ShapeType.vector))

    def visitExpressionBinaryAnd(self, ctx: McInstrParser.ExpressionBinaryAndContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return BinaryOp('__and__', left, right)

    def visitExpressionBinaryOr(self, ctx: McInstrParser.ExpressionBinaryOrContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return BinaryOp('__or__', left, right)

    def visitExpressionBinaryEqual(self, ctx: McInstrParser.ExpressionBinaryEqualContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return BinaryOp('__eq__', left, right)

    def visitExpressionBinaryLessEqual(self, ctx: McInstrParser.ExpressionBinaryLessEqualContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return BinaryOp('__le__', left, right)

    def visitExpressionBinaryGreaterEqual(self, ctx: McInstrParser.ExpressionBinaryGreaterEqualContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return BinaryOp('__ge__', left, right)

    def visitExpressionBinaryLess(self, ctx: McInstrParser.ExpressionBinaryLessContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return BinaryOp('__lt__', left, right)

    def visitExpressionBinaryGreater(self, ctx: McInstrParser.ExpressionBinaryGreaterContext):
        from ..common import BinaryOp
        left, right = [self.visit(x) for x in (ctx.left, ctx.right)]
        return BinaryOp('__gt__', left, right)