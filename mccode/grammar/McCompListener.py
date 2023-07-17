# Generated from /home/gst/PycharmProjects/mccode4/mccode/grammar/McComp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .McCompParser import McCompParser
else:
    from McCompParser import McCompParser

# This class defines a complete listener for a parse tree produced by McCompParser.
class McCompListener(ParseTreeListener):

    # Enter a parse tree produced by McCompParser#prog.
    def enterProg(self, ctx:McCompParser.ProgContext):
        pass

    # Exit a parse tree produced by McCompParser#prog.
    def exitProg(self, ctx:McCompParser.ProgContext):
        pass


    # Enter a parse tree produced by McCompParser#ComponentDefineNew.
    def enterComponentDefineNew(self, ctx:McCompParser.ComponentDefineNewContext):
        pass

    # Exit a parse tree produced by McCompParser#ComponentDefineNew.
    def exitComponentDefineNew(self, ctx:McCompParser.ComponentDefineNewContext):
        pass


    # Enter a parse tree produced by McCompParser#ComponentDefineCopy.
    def enterComponentDefineCopy(self, ctx:McCompParser.ComponentDefineCopyContext):
        pass

    # Exit a parse tree produced by McCompParser#ComponentDefineCopy.
    def exitComponentDefineCopy(self, ctx:McCompParser.ComponentDefineCopyContext):
        pass


    # Enter a parse tree produced by McCompParser#component_trace.
    def enterComponent_trace(self, ctx:McCompParser.Component_traceContext):
        pass

    # Exit a parse tree produced by McCompParser#component_trace.
    def exitComponent_trace(self, ctx:McCompParser.Component_traceContext):
        pass


    # Enter a parse tree produced by McCompParser#component_parameter_set.
    def enterComponent_parameter_set(self, ctx:McCompParser.Component_parameter_setContext):
        pass

    # Exit a parse tree produced by McCompParser#component_parameter_set.
    def exitComponent_parameter_set(self, ctx:McCompParser.Component_parameter_setContext):
        pass


    # Enter a parse tree produced by McCompParser#component_define_parameters.
    def enterComponent_define_parameters(self, ctx:McCompParser.Component_define_parametersContext):
        pass

    # Exit a parse tree produced by McCompParser#component_define_parameters.
    def exitComponent_define_parameters(self, ctx:McCompParser.Component_define_parametersContext):
        pass


    # Enter a parse tree produced by McCompParser#component_set_parameters.
    def enterComponent_set_parameters(self, ctx:McCompParser.Component_set_parametersContext):
        pass

    # Exit a parse tree produced by McCompParser#component_set_parameters.
    def exitComponent_set_parameters(self, ctx:McCompParser.Component_set_parametersContext):
        pass


    # Enter a parse tree produced by McCompParser#component_out_parameters.
    def enterComponent_out_parameters(self, ctx:McCompParser.Component_out_parametersContext):
        pass

    # Exit a parse tree produced by McCompParser#component_out_parameters.
    def exitComponent_out_parameters(self, ctx:McCompParser.Component_out_parametersContext):
        pass


    # Enter a parse tree produced by McCompParser#component_parameters.
    def enterComponent_parameters(self, ctx:McCompParser.Component_parametersContext):
        pass

    # Exit a parse tree produced by McCompParser#component_parameters.
    def exitComponent_parameters(self, ctx:McCompParser.Component_parametersContext):
        pass


    # Enter a parse tree produced by McCompParser#ComponentParameterDouble.
    def enterComponentParameterDouble(self, ctx:McCompParser.ComponentParameterDoubleContext):
        pass

    # Exit a parse tree produced by McCompParser#ComponentParameterDouble.
    def exitComponentParameterDouble(self, ctx:McCompParser.ComponentParameterDoubleContext):
        pass


    # Enter a parse tree produced by McCompParser#ComponentParameterInteger.
    def enterComponentParameterInteger(self, ctx:McCompParser.ComponentParameterIntegerContext):
        pass

    # Exit a parse tree produced by McCompParser#ComponentParameterInteger.
    def exitComponentParameterInteger(self, ctx:McCompParser.ComponentParameterIntegerContext):
        pass


    # Enter a parse tree produced by McCompParser#ComponentParameterString.
    def enterComponentParameterString(self, ctx:McCompParser.ComponentParameterStringContext):
        pass

    # Exit a parse tree produced by McCompParser#ComponentParameterString.
    def exitComponentParameterString(self, ctx:McCompParser.ComponentParameterStringContext):
        pass


    # Enter a parse tree produced by McCompParser#ComponentParameterVector.
    def enterComponentParameterVector(self, ctx:McCompParser.ComponentParameterVectorContext):
        pass

    # Exit a parse tree produced by McCompParser#ComponentParameterVector.
    def exitComponentParameterVector(self, ctx:McCompParser.ComponentParameterVectorContext):
        pass


    # Enter a parse tree produced by McCompParser#ComponentParameterDoubleArray.
    def enterComponentParameterDoubleArray(self, ctx:McCompParser.ComponentParameterDoubleArrayContext):
        pass

    # Exit a parse tree produced by McCompParser#ComponentParameterDoubleArray.
    def exitComponentParameterDoubleArray(self, ctx:McCompParser.ComponentParameterDoubleArrayContext):
        pass


    # Enter a parse tree produced by McCompParser#ComponentParameterIntegerArray.
    def enterComponentParameterIntegerArray(self, ctx:McCompParser.ComponentParameterIntegerArrayContext):
        pass

    # Exit a parse tree produced by McCompParser#ComponentParameterIntegerArray.
    def exitComponentParameterIntegerArray(self, ctx:McCompParser.ComponentParameterIntegerArrayContext):
        pass


    # Enter a parse tree produced by McCompParser#component_ref.
    def enterComponent_ref(self, ctx:McCompParser.Component_refContext):
        pass

    # Exit a parse tree produced by McCompParser#component_ref.
    def exitComponent_ref(self, ctx:McCompParser.Component_refContext):
        pass


    # Enter a parse tree produced by McCompParser#coords.
    def enterCoords(self, ctx:McCompParser.CoordsContext):
        pass

    # Exit a parse tree produced by McCompParser#coords.
    def exitCoords(self, ctx:McCompParser.CoordsContext):
        pass


    # Enter a parse tree produced by McCompParser#reference.
    def enterReference(self, ctx:McCompParser.ReferenceContext):
        pass

    # Exit a parse tree produced by McCompParser#reference.
    def exitReference(self, ctx:McCompParser.ReferenceContext):
        pass


    # Enter a parse tree produced by McCompParser#dependency.
    def enterDependency(self, ctx:McCompParser.DependencyContext):
        pass

    # Exit a parse tree produced by McCompParser#dependency.
    def exitDependency(self, ctx:McCompParser.DependencyContext):
        pass


    # Enter a parse tree produced by McCompParser#DeclareBlock.
    def enterDeclareBlock(self, ctx:McCompParser.DeclareBlockContext):
        pass

    # Exit a parse tree produced by McCompParser#DeclareBlock.
    def exitDeclareBlock(self, ctx:McCompParser.DeclareBlockContext):
        pass


    # Enter a parse tree produced by McCompParser#DeclareBlockCopy.
    def enterDeclareBlockCopy(self, ctx:McCompParser.DeclareBlockCopyContext):
        pass

    # Exit a parse tree produced by McCompParser#DeclareBlockCopy.
    def exitDeclareBlockCopy(self, ctx:McCompParser.DeclareBlockCopyContext):
        pass


    # Enter a parse tree produced by McCompParser#ShareBlock.
    def enterShareBlock(self, ctx:McCompParser.ShareBlockContext):
        pass

    # Exit a parse tree produced by McCompParser#ShareBlock.
    def exitShareBlock(self, ctx:McCompParser.ShareBlockContext):
        pass


    # Enter a parse tree produced by McCompParser#ShareBlockCopy.
    def enterShareBlockCopy(self, ctx:McCompParser.ShareBlockCopyContext):
        pass

    # Exit a parse tree produced by McCompParser#ShareBlockCopy.
    def exitShareBlockCopy(self, ctx:McCompParser.ShareBlockCopyContext):
        pass


    # Enter a parse tree produced by McCompParser#uservars.
    def enterUservars(self, ctx:McCompParser.UservarsContext):
        pass

    # Exit a parse tree produced by McCompParser#uservars.
    def exitUservars(self, ctx:McCompParser.UservarsContext):
        pass


    # Enter a parse tree produced by McCompParser#InitializeBlock.
    def enterInitializeBlock(self, ctx:McCompParser.InitializeBlockContext):
        pass

    # Exit a parse tree produced by McCompParser#InitializeBlock.
    def exitInitializeBlock(self, ctx:McCompParser.InitializeBlockContext):
        pass


    # Enter a parse tree produced by McCompParser#InitializeBlockCopy.
    def enterInitializeBlockCopy(self, ctx:McCompParser.InitializeBlockCopyContext):
        pass

    # Exit a parse tree produced by McCompParser#InitializeBlockCopy.
    def exitInitializeBlockCopy(self, ctx:McCompParser.InitializeBlockCopyContext):
        pass


    # Enter a parse tree produced by McCompParser#SaveBlock.
    def enterSaveBlock(self, ctx:McCompParser.SaveBlockContext):
        pass

    # Exit a parse tree produced by McCompParser#SaveBlock.
    def exitSaveBlock(self, ctx:McCompParser.SaveBlockContext):
        pass


    # Enter a parse tree produced by McCompParser#SaveBlockCopy.
    def enterSaveBlockCopy(self, ctx:McCompParser.SaveBlockCopyContext):
        pass

    # Exit a parse tree produced by McCompParser#SaveBlockCopy.
    def exitSaveBlockCopy(self, ctx:McCompParser.SaveBlockCopyContext):
        pass


    # Enter a parse tree produced by McCompParser#FinallyBlock.
    def enterFinallyBlock(self, ctx:McCompParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by McCompParser#FinallyBlock.
    def exitFinallyBlock(self, ctx:McCompParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by McCompParser#FinallyBlockCopy.
    def enterFinallyBlockCopy(self, ctx:McCompParser.FinallyBlockCopyContext):
        pass

    # Exit a parse tree produced by McCompParser#FinallyBlockCopy.
    def exitFinallyBlockCopy(self, ctx:McCompParser.FinallyBlockCopyContext):
        pass


    # Enter a parse tree produced by McCompParser#DisplayBlock.
    def enterDisplayBlock(self, ctx:McCompParser.DisplayBlockContext):
        pass

    # Exit a parse tree produced by McCompParser#DisplayBlock.
    def exitDisplayBlock(self, ctx:McCompParser.DisplayBlockContext):
        pass


    # Enter a parse tree produced by McCompParser#DisplayBlockCopy.
    def enterDisplayBlockCopy(self, ctx:McCompParser.DisplayBlockCopyContext):
        pass

    # Exit a parse tree produced by McCompParser#DisplayBlockCopy.
    def exitDisplayBlockCopy(self, ctx:McCompParser.DisplayBlockCopyContext):
        pass


    # Enter a parse tree produced by McCompParser#split.
    def enterSplit(self, ctx:McCompParser.SplitContext):
        pass

    # Exit a parse tree produced by McCompParser#split.
    def exitSplit(self, ctx:McCompParser.SplitContext):
        pass


    # Enter a parse tree produced by McCompParser#when.
    def enterWhen(self, ctx:McCompParser.WhenContext):
        pass

    # Exit a parse tree produced by McCompParser#when.
    def exitWhen(self, ctx:McCompParser.WhenContext):
        pass


    # Enter a parse tree produced by McCompParser#place.
    def enterPlace(self, ctx:McCompParser.PlaceContext):
        pass

    # Exit a parse tree produced by McCompParser#place.
    def exitPlace(self, ctx:McCompParser.PlaceContext):
        pass


    # Enter a parse tree produced by McCompParser#orientation.
    def enterOrientation(self, ctx:McCompParser.OrientationContext):
        pass

    # Exit a parse tree produced by McCompParser#orientation.
    def exitOrientation(self, ctx:McCompParser.OrientationContext):
        pass


    # Enter a parse tree produced by McCompParser#groupref.
    def enterGroupref(self, ctx:McCompParser.GrouprefContext):
        pass

    # Exit a parse tree produced by McCompParser#groupref.
    def exitGroupref(self, ctx:McCompParser.GrouprefContext):
        pass


    # Enter a parse tree produced by McCompParser#extend.
    def enterExtend(self, ctx:McCompParser.ExtendContext):
        pass

    # Exit a parse tree produced by McCompParser#extend.
    def exitExtend(self, ctx:McCompParser.ExtendContext):
        pass


    # Enter a parse tree produced by McCompParser#jump.
    def enterJump(self, ctx:McCompParser.JumpContext):
        pass

    # Exit a parse tree produced by McCompParser#jump.
    def exitJump(self, ctx:McCompParser.JumpContext):
        pass


    # Enter a parse tree produced by McCompParser#jumpname.
    def enterJumpname(self, ctx:McCompParser.JumpnameContext):
        pass

    # Exit a parse tree produced by McCompParser#jumpname.
    def exitJumpname(self, ctx:McCompParser.JumpnameContext):
        pass


    # Enter a parse tree produced by McCompParser#MetadataSimpleName.
    def enterMetadataSimpleName(self, ctx:McCompParser.MetadataSimpleNameContext):
        pass

    # Exit a parse tree produced by McCompParser#MetadataSimpleName.
    def exitMetadataSimpleName(self, ctx:McCompParser.MetadataSimpleNameContext):
        pass


    # Enter a parse tree produced by McCompParser#MetadataStringName.
    def enterMetadataStringName(self, ctx:McCompParser.MetadataStringNameContext):
        pass

    # Exit a parse tree produced by McCompParser#MetadataStringName.
    def exitMetadataStringName(self, ctx:McCompParser.MetadataStringNameContext):
        pass


    # Enter a parse tree produced by McCompParser#initializerlist.
    def enterInitializerlist(self, ctx:McCompParser.InitializerlistContext):
        pass

    # Exit a parse tree produced by McCompParser#initializerlist.
    def exitInitializerlist(self, ctx:McCompParser.InitializerlistContext):
        pass


    # Enter a parse tree produced by McCompParser#SimpleExpressionUnaryPM.
    def enterSimpleExpressionUnaryPM(self, ctx:McCompParser.SimpleExpressionUnaryPMContext):
        pass

    # Exit a parse tree produced by McCompParser#SimpleExpressionUnaryPM.
    def exitSimpleExpressionUnaryPM(self, ctx:McCompParser.SimpleExpressionUnaryPMContext):
        pass


    # Enter a parse tree produced by McCompParser#SimpleExpressionGrouping.
    def enterSimpleExpressionGrouping(self, ctx:McCompParser.SimpleExpressionGroupingContext):
        pass

    # Exit a parse tree produced by McCompParser#SimpleExpressionGrouping.
    def exitSimpleExpressionGrouping(self, ctx:McCompParser.SimpleExpressionGroupingContext):
        pass


    # Enter a parse tree produced by McCompParser#SimpleExpressionBinaryMD.
    def enterSimpleExpressionBinaryMD(self, ctx:McCompParser.SimpleExpressionBinaryMDContext):
        pass

    # Exit a parse tree produced by McCompParser#SimpleExpressionBinaryMD.
    def exitSimpleExpressionBinaryMD(self, ctx:McCompParser.SimpleExpressionBinaryMDContext):
        pass


    # Enter a parse tree produced by McCompParser#SimpleExpressionBinaryPM.
    def enterSimpleExpressionBinaryPM(self, ctx:McCompParser.SimpleExpressionBinaryPMContext):
        pass

    # Exit a parse tree produced by McCompParser#SimpleExpressionBinaryPM.
    def exitSimpleExpressionBinaryPM(self, ctx:McCompParser.SimpleExpressionBinaryPMContext):
        pass


    # Enter a parse tree produced by McCompParser#SimpleExpressionArrayAccess.
    def enterSimpleExpressionArrayAccess(self, ctx:McCompParser.SimpleExpressionArrayAccessContext):
        pass

    # Exit a parse tree produced by McCompParser#SimpleExpressionArrayAccess.
    def exitSimpleExpressionArrayAccess(self, ctx:McCompParser.SimpleExpressionArrayAccessContext):
        pass


    # Enter a parse tree produced by McCompParser#SimpleExpressionInteger.
    def enterSimpleExpressionInteger(self, ctx:McCompParser.SimpleExpressionIntegerContext):
        pass

    # Exit a parse tree produced by McCompParser#SimpleExpressionInteger.
    def exitSimpleExpressionInteger(self, ctx:McCompParser.SimpleExpressionIntegerContext):
        pass


    # Enter a parse tree produced by McCompParser#SimpleExpressionFunctionCall.
    def enterSimpleExpressionFunctionCall(self, ctx:McCompParser.SimpleExpressionFunctionCallContext):
        pass

    # Exit a parse tree produced by McCompParser#SimpleExpressionFunctionCall.
    def exitSimpleExpressionFunctionCall(self, ctx:McCompParser.SimpleExpressionFunctionCallContext):
        pass


    # Enter a parse tree produced by McCompParser#SimpleExpressionIdentifier.
    def enterSimpleExpressionIdentifier(self, ctx:McCompParser.SimpleExpressionIdentifierContext):
        pass

    # Exit a parse tree produced by McCompParser#SimpleExpressionIdentifier.
    def exitSimpleExpressionIdentifier(self, ctx:McCompParser.SimpleExpressionIdentifierContext):
        pass


    # Enter a parse tree produced by McCompParser#SimpleExpressionFloat.
    def enterSimpleExpressionFloat(self, ctx:McCompParser.SimpleExpressionFloatContext):
        pass

    # Exit a parse tree produced by McCompParser#SimpleExpressionFloat.
    def exitSimpleExpressionFloat(self, ctx:McCompParser.SimpleExpressionFloatContext):
        pass


    # Enter a parse tree produced by McCompParser#shell.
    def enterShell(self, ctx:McCompParser.ShellContext):
        pass

    # Exit a parse tree produced by McCompParser#shell.
    def exitShell(self, ctx:McCompParser.ShellContext):
        pass


    # Enter a parse tree produced by McCompParser#SearchPath.
    def enterSearchPath(self, ctx:McCompParser.SearchPathContext):
        pass

    # Exit a parse tree produced by McCompParser#SearchPath.
    def exitSearchPath(self, ctx:McCompParser.SearchPathContext):
        pass


    # Enter a parse tree produced by McCompParser#SearchShell.
    def enterSearchShell(self, ctx:McCompParser.SearchShellContext):
        pass

    # Exit a parse tree produced by McCompParser#SearchShell.
    def exitSearchShell(self, ctx:McCompParser.SearchShellContext):
        pass



del McCompParser