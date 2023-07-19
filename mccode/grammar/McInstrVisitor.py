# Generated from /home/g/Code/mccode-antlr/mccode/grammar/McInstr.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .McInstrParser import McInstrParser
else:
    from McInstrParser import McInstrParser

# This class defines a complete generic visitor for a parse tree produced by McInstrParser.

class McInstrVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by McInstrParser#prog.
    def visitProg(self, ctx:McInstrParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#instrument_definition.
    def visitInstrument_definition(self, ctx:McInstrParser.Instrument_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#instrument_parameters.
    def visitInstrument_parameters(self, ctx:McInstrParser.Instrument_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InstrumentParameterDouble.
    def visitInstrumentParameterDouble(self, ctx:McInstrParser.InstrumentParameterDoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InstrumentParameterInteger.
    def visitInstrumentParameterInteger(self, ctx:McInstrParser.InstrumentParameterIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InstrumentParameterString.
    def visitInstrumentParameterString(self, ctx:McInstrParser.InstrumentParameterStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#instrument_trace.
    def visitInstrument_trace(self, ctx:McInstrParser.Instrument_traceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#instrument_metadata.
    def visitInstrument_metadata(self, ctx:McInstrParser.Instrument_metadataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#instrument_trace_include.
    def visitInstrument_trace_include(self, ctx:McInstrParser.Instrument_trace_includeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#component_instance.
    def visitComponent_instance(self, ctx:McInstrParser.Component_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InstanceNameCopyIdentifier.
    def visitInstanceNameCopyIdentifier(self, ctx:McInstrParser.InstanceNameCopyIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InstanceNameCopy.
    def visitInstanceNameCopy(self, ctx:McInstrParser.InstanceNameCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InstanceNameIdentifier.
    def visitInstanceNameIdentifier(self, ctx:McInstrParser.InstanceNameIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ComponentTypeCopy.
    def visitComponentTypeCopy(self, ctx:McInstrParser.ComponentTypeCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ComponentTypeIdentifier.
    def visitComponentTypeIdentifier(self, ctx:McInstrParser.ComponentTypeIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#instance_parameters.
    def visitInstance_parameters(self, ctx:McInstrParser.Instance_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#instance_parameter.
    def visitInstance_parameter(self, ctx:McInstrParser.Instance_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#split.
    def visitSplit(self, ctx:McInstrParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#when.
    def visitWhen(self, ctx:McInstrParser.WhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#place.
    def visitPlace(self, ctx:McInstrParser.PlaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#orientation.
    def visitOrientation(self, ctx:McInstrParser.OrientationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#groupref.
    def visitGroupref(self, ctx:McInstrParser.GrouprefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#jumps.
    def visitJumps(self, ctx:McInstrParser.JumpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#jump.
    def visitJump(self, ctx:McInstrParser.JumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#JumpPrevious.
    def visitJumpPrevious(self, ctx:McInstrParser.JumpPreviousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#JumpMyself.
    def visitJumpMyself(self, ctx:McInstrParser.JumpMyselfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#JumpNext.
    def visitJumpNext(self, ctx:McInstrParser.JumpNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#JumpIdentifier.
    def visitJumpIdentifier(self, ctx:McInstrParser.JumpIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#extend.
    def visitExtend(self, ctx:McInstrParser.ExtendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#component_ref.
    def visitComponent_ref(self, ctx:McInstrParser.Component_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#coords.
    def visitCoords(self, ctx:McInstrParser.CoordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#reference.
    def visitReference(self, ctx:McInstrParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#dependency.
    def visitDependency(self, ctx:McInstrParser.DependencyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#DeclareBlock.
    def visitDeclareBlock(self, ctx:McInstrParser.DeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#DeclareBlockCopy.
    def visitDeclareBlockCopy(self, ctx:McInstrParser.DeclareBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#uservars.
    def visitUservars(self, ctx:McInstrParser.UservarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InitializeBlock.
    def visitInitializeBlock(self, ctx:McInstrParser.InitializeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InitializeBlockCopy.
    def visitInitializeBlockCopy(self, ctx:McInstrParser.InitializeBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SaveBlock.
    def visitSaveBlock(self, ctx:McInstrParser.SaveBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SaveBlockCopy.
    def visitSaveBlockCopy(self, ctx:McInstrParser.SaveBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#FinallyBlock.
    def visitFinallyBlock(self, ctx:McInstrParser.FinallyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#FinallyBlockCopy.
    def visitFinallyBlockCopy(self, ctx:McInstrParser.FinallyBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#metadata.
    def visitMetadata(self, ctx:McInstrParser.MetadataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#initializerlist.
    def visitInitializerlist(self, ctx:McInstrParser.InitializerlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#assignment.
    def visitAssignment(self, ctx:McInstrParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionUnaryPM.
    def visitExpressionUnaryPM(self, ctx:McInstrParser.ExpressionUnaryPMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionGrouping.
    def visitExpressionGrouping(self, ctx:McInstrParser.ExpressionGroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionFloat.
    def visitExpressionFloat(self, ctx:McInstrParser.ExpressionFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionArrayAccess.
    def visitExpressionArrayAccess(self, ctx:McInstrParser.ExpressionArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionIdentifier.
    def visitExpressionIdentifier(self, ctx:McInstrParser.ExpressionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionInteger.
    def visitExpressionInteger(self, ctx:McInstrParser.ExpressionIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionExponentiation.
    def visitExpressionExponentiation(self, ctx:McInstrParser.ExpressionExponentiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionBinaryPM.
    def visitExpressionBinaryPM(self, ctx:McInstrParser.ExpressionBinaryPMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionFunctionCall.
    def visitExpressionFunctionCall(self, ctx:McInstrParser.ExpressionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ExpressionBinaryMD.
    def visitExpressionBinaryMD(self, ctx:McInstrParser.ExpressionBinaryMDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#shell.
    def visitShell(self, ctx:McInstrParser.ShellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SearchPath.
    def visitSearchPath(self, ctx:McInstrParser.SearchPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SearchShell.
    def visitSearchShell(self, ctx:McInstrParser.SearchShellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#unparsed_block.
    def visitUnparsed_block(self, ctx:McInstrParser.Unparsed_blockContext):
        return self.visitChildren(ctx)



del McInstrParser