# Generated from /home/gst/PycharmProjects/mccode4/mccode/grammar/McComp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .McCompParser import McCompParser
else:
    from McCompParser import McCompParser

# This class defines a complete generic visitor for a parse tree produced by McCompParser.

class McCompVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by McCompParser#prog.
    def visitProg(self, ctx:McCompParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ComponentDefineNew.
    def visitComponentDefineNew(self, ctx:McCompParser.ComponentDefineNewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ComponentDefineCopy.
    def visitComponentDefineCopy(self, ctx:McCompParser.ComponentDefineCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#component_trace.
    def visitComponent_trace(self, ctx:McCompParser.Component_traceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#component_parameter_set.
    def visitComponent_parameter_set(self, ctx:McCompParser.Component_parameter_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#component_define_parameters.
    def visitComponent_define_parameters(self, ctx:McCompParser.Component_define_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#component_set_parameters.
    def visitComponent_set_parameters(self, ctx:McCompParser.Component_set_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#component_out_parameters.
    def visitComponent_out_parameters(self, ctx:McCompParser.Component_out_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#component_parameters.
    def visitComponent_parameters(self, ctx:McCompParser.Component_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ComponentParameterDouble.
    def visitComponentParameterDouble(self, ctx:McCompParser.ComponentParameterDoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ComponentParameterInteger.
    def visitComponentParameterInteger(self, ctx:McCompParser.ComponentParameterIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ComponentParameterString.
    def visitComponentParameterString(self, ctx:McCompParser.ComponentParameterStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ComponentParameterVector.
    def visitComponentParameterVector(self, ctx:McCompParser.ComponentParameterVectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ComponentParameterDoubleArray.
    def visitComponentParameterDoubleArray(self, ctx:McCompParser.ComponentParameterDoubleArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ComponentParameterIntegerArray.
    def visitComponentParameterIntegerArray(self, ctx:McCompParser.ComponentParameterIntegerArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#component_ref.
    def visitComponent_ref(self, ctx:McCompParser.Component_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#coords.
    def visitCoords(self, ctx:McCompParser.CoordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#reference.
    def visitReference(self, ctx:McCompParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#dependency.
    def visitDependency(self, ctx:McCompParser.DependencyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#DeclareBlock.
    def visitDeclareBlock(self, ctx:McCompParser.DeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#DeclareBlockCopy.
    def visitDeclareBlockCopy(self, ctx:McCompParser.DeclareBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ShareBlock.
    def visitShareBlock(self, ctx:McCompParser.ShareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#ShareBlockCopy.
    def visitShareBlockCopy(self, ctx:McCompParser.ShareBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#uservars.
    def visitUservars(self, ctx:McCompParser.UservarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#InitializeBlock.
    def visitInitializeBlock(self, ctx:McCompParser.InitializeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#InitializeBlockCopy.
    def visitInitializeBlockCopy(self, ctx:McCompParser.InitializeBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SaveBlock.
    def visitSaveBlock(self, ctx:McCompParser.SaveBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SaveBlockCopy.
    def visitSaveBlockCopy(self, ctx:McCompParser.SaveBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#FinallyBlock.
    def visitFinallyBlock(self, ctx:McCompParser.FinallyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#FinallyBlockCopy.
    def visitFinallyBlockCopy(self, ctx:McCompParser.FinallyBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#DisplayBlock.
    def visitDisplayBlock(self, ctx:McCompParser.DisplayBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#DisplayBlockCopy.
    def visitDisplayBlockCopy(self, ctx:McCompParser.DisplayBlockCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#split.
    def visitSplit(self, ctx:McCompParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#when.
    def visitWhen(self, ctx:McCompParser.WhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#place.
    def visitPlace(self, ctx:McCompParser.PlaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#orientation.
    def visitOrientation(self, ctx:McCompParser.OrientationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#groupref.
    def visitGroupref(self, ctx:McCompParser.GrouprefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#extend.
    def visitExtend(self, ctx:McCompParser.ExtendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#jump.
    def visitJump(self, ctx:McCompParser.JumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#jumpname.
    def visitJumpname(self, ctx:McCompParser.JumpnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#MetadataSimpleName.
    def visitMetadataSimpleName(self, ctx:McCompParser.MetadataSimpleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#MetadataStringName.
    def visitMetadataStringName(self, ctx:McCompParser.MetadataStringNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#initializerlist.
    def visitInitializerlist(self, ctx:McCompParser.InitializerlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SimpleExpressionUnaryPM.
    def visitSimpleExpressionUnaryPM(self, ctx:McCompParser.SimpleExpressionUnaryPMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SimpleExpressionGrouping.
    def visitSimpleExpressionGrouping(self, ctx:McCompParser.SimpleExpressionGroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SimpleExpressionBinaryMD.
    def visitSimpleExpressionBinaryMD(self, ctx:McCompParser.SimpleExpressionBinaryMDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SimpleExpressionBinaryPM.
    def visitSimpleExpressionBinaryPM(self, ctx:McCompParser.SimpleExpressionBinaryPMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SimpleExpressionArrayAccess.
    def visitSimpleExpressionArrayAccess(self, ctx:McCompParser.SimpleExpressionArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SimpleExpressionInteger.
    def visitSimpleExpressionInteger(self, ctx:McCompParser.SimpleExpressionIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SimpleExpressionFunctionCall.
    def visitSimpleExpressionFunctionCall(self, ctx:McCompParser.SimpleExpressionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SimpleExpressionIdentifier.
    def visitSimpleExpressionIdentifier(self, ctx:McCompParser.SimpleExpressionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SimpleExpressionFloat.
    def visitSimpleExpressionFloat(self, ctx:McCompParser.SimpleExpressionFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#shell.
    def visitShell(self, ctx:McCompParser.ShellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SearchPath.
    def visitSearchPath(self, ctx:McCompParser.SearchPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by McCompParser#SearchShell.
    def visitSearchShell(self, ctx:McCompParser.SearchShellContext):
        return self.visitChildren(ctx)



del McCompParser