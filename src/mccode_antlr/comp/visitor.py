from loguru import logger

from ..grammar import McCompParser as Parser, McCompVisitor
from .comp import Comp
from ..common import ComponentParameter, Expr, MetaData
from ..common.visitor import add_common_visitors


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
            logger.critical(f'The component {self.state.name} is a copied definition, complete with TRACE section')
            logger.critical(f'Now `TRACE COPY {ctx.Identifier()}` would add to the existing copied TRACE')
            logger.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
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
            logger.critical(f'The component {self.state.name} is a copied definition, complete with DECLARE section')
            logger.critical(f'Now `DECLARE COPY {ctx.Identifier()}` would add to the existing copied DECLARE')
            logger.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
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
            logger.critical(f'The component {self.state.name} is a copied definition, complete with INITIALIZE section')
            logger.critical(f'Now `INITIALIZE COPY {ctx.Identifier()}` would add to the existing copied INITIALIZE')
            logger.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
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
            logger.critical(f'The component {self.state.name} is a copied definition, complete with SAVE section')
            logger.critical(f'Now `SAVE COPY {ctx.Identifier()}` would add to the existing copied SAVE')
            logger.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
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
            logger.critical(f'The component {self.state.name} is a copied definition, complete with FINALLY section')
            logger.critical(f'Now `FINALLY COPY {ctx.Identifier()}` would add to the existing copied FINALLY')
            logger.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
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
            logger.critical(f'The component {self.state.name} is a copied definition, complete with DISPLAY section')
            logger.critical(f'Now `DISPLAY COPY {ctx.Identifier()}` would add to the existing copied DISPLAY')
            logger.critical(f'This is almost certainly not the intended behaviour, so you get only the new copy.')
            self.state.display = ()
        blocks = self.parent.get_component(str(ctx.Identifier())).display
        if ctx.Extend() is not None:
            blocks = [x for x in blocks]
            blocks.append(self.visit(ctx.unparsed_block()))
        self.state.DISPLAY(*blocks)

    def visitMetadata(self, ctx: Parser.MetadataContext):
        filename, line_number, metadata = self.visit(ctx.unparsed_block())
        mime = ctx.mime.text if ctx.mime.type == Parser.Identifier else ctx.mime.text[1:-1]
        name = ctx.name.text if ctx.name.type == Parser.Identifier else ctx.name.text[1:-1]
        metadata = MetaData.from_component_tokens(source=self.state.name, mimetype=mime, name=name, value=metadata)
        self.state.add_metadata(metadata)

    def visitUnparsed_block(self, ctx: Parser.Unparsed_blockContext):
        # We want to extract the source-file line number (and filename) for use in the C-preprocessor
        # via `#line {number} "{filename}"` directives, for more expressive error handling
        line_number = None if ctx.start is None else ctx.start.line
        content = str(ctx.UnparsedBlock())[2:-2]
        return self.filename, line_number, content

    # FIXME There *are* no statements in McCode, so all identifiers always produce un-parsable values.
    def visitAssignment(self, ctx: Parser.AssignmentContext):
        line_number = None if ctx.start is None else ctx.start.line
        raise RuntimeError(f"{self.filename}: {line_number} -- assignment statements are not (yet) supported")

    def visitExpressionPrevious(self, ctx: Parser.ExpressionPreviousContext):
        # The very-special no-good expression use of PREVIOUS where it is replaced by the last component's name
        raise RuntimeError('PREVIOUS is not a valid expression in Comp definitions')

    def visitExpressionMyself(self, ctx: Parser.ExpressionMyselfContext):
        # The even-worse expression use of MYSELF to refer to the current being-constructed component's name
        return Expr.str(self.instance.name)


add_common_visitors(CompVisitor)