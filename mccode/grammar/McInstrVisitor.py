# Generated from /home/gst/PycharmProjects/mccode4/mccode/grammar/McInstr.g4 by ANTLR 4.13.0
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


    # Visit a parse tree produced by McInstrParser#instrument_trace_include.
    def visitInstrument_trace_include(self, ctx:McInstrParser.Instrument_trace_includeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#component_instance.
    def visitComponent_instance(self, ctx:McInstrParser.Component_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InstanceNameCopyIdentifier.
    def visitInstanceNameCopyIdentifier(self, ctx:McInstrParser.InstanceNameCopyIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#InstanceNameMyself.
    def visitInstanceNameMyself(self, ctx:McInstrParser.InstanceNameMyselfContext):
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


    # Visit a parse tree produced by McInstrParser#ShareBlock.
    def visitShareBlock(self, ctx:McInstrParser.ShareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#ShareBlockCopy.
    def visitShareBlockCopy(self, ctx:McInstrParser.ShareBlockCopyContext):
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


    # Visit a parse tree produced by McInstrParser#DisplayBlock.
    def visitDisplayBlock(self, ctx:McInstrParser.DisplayBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#DisplayBlockCopy.
    def visitDisplayBlockCopy(self, ctx:McInstrParser.DisplayBlockCopyContext):
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


    # Visit a parse tree produced by McInstrParser#extend.
    def visitExtend(self, ctx:McInstrParser.ExtendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#jump.
    def visitJump(self, ctx:McInstrParser.JumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#jumpname.
    def visitJumpname(self, ctx:McInstrParser.JumpnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#MetadataSimpleName.
    def visitMetadataSimpleName(self, ctx:McInstrParser.MetadataSimpleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#MetadataStringName.
    def visitMetadataStringName(self, ctx:McInstrParser.MetadataStringNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#initializerlist.
    def visitInitializerlist(self, ctx:McInstrParser.InitializerlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SimpleExpressionUnaryPM.
    def visitSimpleExpressionUnaryPM(self, ctx:McInstrParser.SimpleExpressionUnaryPMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SimpleExpressionGrouping.
    def visitSimpleExpressionGrouping(self, ctx:McInstrParser.SimpleExpressionGroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SimpleExpressionBinaryMD.
    def visitSimpleExpressionBinaryMD(self, ctx:McInstrParser.SimpleExpressionBinaryMDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SimpleExpressionBinaryPM.
    def visitSimpleExpressionBinaryPM(self, ctx:McInstrParser.SimpleExpressionBinaryPMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SimpleExpressionArrayAccess.
    def visitSimpleExpressionArrayAccess(self, ctx:McInstrParser.SimpleExpressionArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SimpleExpressionInteger.
    def visitSimpleExpressionInteger(self, ctx:McInstrParser.SimpleExpressionIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SimpleExpressionFunctionCall.
    def visitSimpleExpressionFunctionCall(self, ctx:McInstrParser.SimpleExpressionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SimpleExpressionIdentifier.
    def visitSimpleExpressionIdentifier(self, ctx:McInstrParser.SimpleExpressionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McInstrParser#SimpleExpressionFloat.
    def visitSimpleExpressionFloat(self, ctx:McInstrParser.SimpleExpressionFloatContext):
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



del McInstrParser