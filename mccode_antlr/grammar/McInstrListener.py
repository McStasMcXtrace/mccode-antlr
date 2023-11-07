# Generated from /home/g/Code/mccode_antlr-antlr/mccode_antlr/grammar/McInstr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .McInstrParser import McInstrParser
else:
    from McInstrParser import McInstrParser

# This class defines a complete listener for a parse tree produced by McInstrParser.
class McInstrListener(ParseTreeListener):

    # Enter a parse tree produced by McInstrParser#prog.
    def enterProg(self, ctx:McInstrParser.ProgContext):
        pass

    # Exit a parse tree produced by McInstrParser#prog.
    def exitProg(self, ctx:McInstrParser.ProgContext):
        pass


    # Enter a parse tree produced by McInstrParser#instrument_definition.
    def enterInstrument_definition(self, ctx:McInstrParser.Instrument_definitionContext):
        pass

    # Exit a parse tree produced by McInstrParser#instrument_definition.
    def exitInstrument_definition(self, ctx:McInstrParser.Instrument_definitionContext):
        pass


    # Enter a parse tree produced by McInstrParser#instrument_parameters.
    def enterInstrument_parameters(self, ctx:McInstrParser.Instrument_parametersContext):
        pass

    # Exit a parse tree produced by McInstrParser#instrument_parameters.
    def exitInstrument_parameters(self, ctx:McInstrParser.Instrument_parametersContext):
        pass


    # Enter a parse tree produced by McInstrParser#InstrumentParameterDouble.
    def enterInstrumentParameterDouble(self, ctx:McInstrParser.InstrumentParameterDoubleContext):
        pass

    # Exit a parse tree produced by McInstrParser#InstrumentParameterDouble.
    def exitInstrumentParameterDouble(self, ctx:McInstrParser.InstrumentParameterDoubleContext):
        pass


    # Enter a parse tree produced by McInstrParser#InstrumentParameterInteger.
    def enterInstrumentParameterInteger(self, ctx:McInstrParser.InstrumentParameterIntegerContext):
        pass

    # Exit a parse tree produced by McInstrParser#InstrumentParameterInteger.
    def exitInstrumentParameterInteger(self, ctx:McInstrParser.InstrumentParameterIntegerContext):
        pass


    # Enter a parse tree produced by McInstrParser#InstrumentParameterString.
    def enterInstrumentParameterString(self, ctx:McInstrParser.InstrumentParameterStringContext):
        pass

    # Exit a parse tree produced by McInstrParser#InstrumentParameterString.
    def exitInstrumentParameterString(self, ctx:McInstrParser.InstrumentParameterStringContext):
        pass


    # Enter a parse tree produced by McInstrParser#instrument_parameter_unit.
    def enterInstrument_parameter_unit(self, ctx:McInstrParser.Instrument_parameter_unitContext):
        pass

    # Exit a parse tree produced by McInstrParser#instrument_parameter_unit.
    def exitInstrument_parameter_unit(self, ctx:McInstrParser.Instrument_parameter_unitContext):
        pass


    # Enter a parse tree produced by McInstrParser#instrument_trace.
    def enterInstrument_trace(self, ctx:McInstrParser.Instrument_traceContext):
        pass

    # Exit a parse tree produced by McInstrParser#instrument_trace.
    def exitInstrument_trace(self, ctx:McInstrParser.Instrument_traceContext):
        pass


    # Enter a parse tree produced by McInstrParser#instrument_metadata.
    def enterInstrument_metadata(self, ctx:McInstrParser.Instrument_metadataContext):
        pass

    # Exit a parse tree produced by McInstrParser#instrument_metadata.
    def exitInstrument_metadata(self, ctx:McInstrParser.Instrument_metadataContext):
        pass


    # Enter a parse tree produced by McInstrParser#instrument_trace_include.
    def enterInstrument_trace_include(self, ctx:McInstrParser.Instrument_trace_includeContext):
        pass

    # Exit a parse tree produced by McInstrParser#instrument_trace_include.
    def exitInstrument_trace_include(self, ctx:McInstrParser.Instrument_trace_includeContext):
        pass


    # Enter a parse tree produced by McInstrParser#component_instance.
    def enterComponent_instance(self, ctx:McInstrParser.Component_instanceContext):
        pass

    # Exit a parse tree produced by McInstrParser#component_instance.
    def exitComponent_instance(self, ctx:McInstrParser.Component_instanceContext):
        pass


    # Enter a parse tree produced by McInstrParser#InstanceNameCopyIdentifier.
    def enterInstanceNameCopyIdentifier(self, ctx:McInstrParser.InstanceNameCopyIdentifierContext):
        pass

    # Exit a parse tree produced by McInstrParser#InstanceNameCopyIdentifier.
    def exitInstanceNameCopyIdentifier(self, ctx:McInstrParser.InstanceNameCopyIdentifierContext):
        pass


    # Enter a parse tree produced by McInstrParser#InstanceNameCopy.
    def enterInstanceNameCopy(self, ctx:McInstrParser.InstanceNameCopyContext):
        pass

    # Exit a parse tree produced by McInstrParser#InstanceNameCopy.
    def exitInstanceNameCopy(self, ctx:McInstrParser.InstanceNameCopyContext):
        pass


    # Enter a parse tree produced by McInstrParser#InstanceNameIdentifier.
    def enterInstanceNameIdentifier(self, ctx:McInstrParser.InstanceNameIdentifierContext):
        pass

    # Exit a parse tree produced by McInstrParser#InstanceNameIdentifier.
    def exitInstanceNameIdentifier(self, ctx:McInstrParser.InstanceNameIdentifierContext):
        pass


    # Enter a parse tree produced by McInstrParser#ComponentTypeCopy.
    def enterComponentTypeCopy(self, ctx:McInstrParser.ComponentTypeCopyContext):
        pass

    # Exit a parse tree produced by McInstrParser#ComponentTypeCopy.
    def exitComponentTypeCopy(self, ctx:McInstrParser.ComponentTypeCopyContext):
        pass


    # Enter a parse tree produced by McInstrParser#ComponentTypeIdentifier.
    def enterComponentTypeIdentifier(self, ctx:McInstrParser.ComponentTypeIdentifierContext):
        pass

    # Exit a parse tree produced by McInstrParser#ComponentTypeIdentifier.
    def exitComponentTypeIdentifier(self, ctx:McInstrParser.ComponentTypeIdentifierContext):
        pass


    # Enter a parse tree produced by McInstrParser#instance_parameters.
    def enterInstance_parameters(self, ctx:McInstrParser.Instance_parametersContext):
        pass

    # Exit a parse tree produced by McInstrParser#instance_parameters.
    def exitInstance_parameters(self, ctx:McInstrParser.Instance_parametersContext):
        pass


    # Enter a parse tree produced by McInstrParser#InstanceParameterExpr.
    def enterInstanceParameterExpr(self, ctx:McInstrParser.InstanceParameterExprContext):
        pass

    # Exit a parse tree produced by McInstrParser#InstanceParameterExpr.
    def exitInstanceParameterExpr(self, ctx:McInstrParser.InstanceParameterExprContext):
        pass


    # Enter a parse tree produced by McInstrParser#InstanceParameterNull.
    def enterInstanceParameterNull(self, ctx:McInstrParser.InstanceParameterNullContext):
        pass

    # Exit a parse tree produced by McInstrParser#InstanceParameterNull.
    def exitInstanceParameterNull(self, ctx:McInstrParser.InstanceParameterNullContext):
        pass


    # Enter a parse tree produced by McInstrParser#InstanceParameterVector.
    def enterInstanceParameterVector(self, ctx:McInstrParser.InstanceParameterVectorContext):
        pass

    # Exit a parse tree produced by McInstrParser#InstanceParameterVector.
    def exitInstanceParameterVector(self, ctx:McInstrParser.InstanceParameterVectorContext):
        pass


    # Enter a parse tree produced by McInstrParser#split.
    def enterSplit(self, ctx:McInstrParser.SplitContext):
        pass

    # Exit a parse tree produced by McInstrParser#split.
    def exitSplit(self, ctx:McInstrParser.SplitContext):
        pass


    # Enter a parse tree produced by McInstrParser#when.
    def enterWhen(self, ctx:McInstrParser.WhenContext):
        pass

    # Exit a parse tree produced by McInstrParser#when.
    def exitWhen(self, ctx:McInstrParser.WhenContext):
        pass


    # Enter a parse tree produced by McInstrParser#place.
    def enterPlace(self, ctx:McInstrParser.PlaceContext):
        pass

    # Exit a parse tree produced by McInstrParser#place.
    def exitPlace(self, ctx:McInstrParser.PlaceContext):
        pass


    # Enter a parse tree produced by McInstrParser#orientation.
    def enterOrientation(self, ctx:McInstrParser.OrientationContext):
        pass

    # Exit a parse tree produced by McInstrParser#orientation.
    def exitOrientation(self, ctx:McInstrParser.OrientationContext):
        pass


    # Enter a parse tree produced by McInstrParser#groupref.
    def enterGroupref(self, ctx:McInstrParser.GrouprefContext):
        pass

    # Exit a parse tree produced by McInstrParser#groupref.
    def exitGroupref(self, ctx:McInstrParser.GrouprefContext):
        pass


    # Enter a parse tree produced by McInstrParser#jumps.
    def enterJumps(self, ctx:McInstrParser.JumpsContext):
        pass

    # Exit a parse tree produced by McInstrParser#jumps.
    def exitJumps(self, ctx:McInstrParser.JumpsContext):
        pass


    # Enter a parse tree produced by McInstrParser#jump.
    def enterJump(self, ctx:McInstrParser.JumpContext):
        pass

    # Exit a parse tree produced by McInstrParser#jump.
    def exitJump(self, ctx:McInstrParser.JumpContext):
        pass


    # Enter a parse tree produced by McInstrParser#JumpPrevious.
    def enterJumpPrevious(self, ctx:McInstrParser.JumpPreviousContext):
        pass

    # Exit a parse tree produced by McInstrParser#JumpPrevious.
    def exitJumpPrevious(self, ctx:McInstrParser.JumpPreviousContext):
        pass


    # Enter a parse tree produced by McInstrParser#JumpMyself.
    def enterJumpMyself(self, ctx:McInstrParser.JumpMyselfContext):
        pass

    # Exit a parse tree produced by McInstrParser#JumpMyself.
    def exitJumpMyself(self, ctx:McInstrParser.JumpMyselfContext):
        pass


    # Enter a parse tree produced by McInstrParser#JumpNext.
    def enterJumpNext(self, ctx:McInstrParser.JumpNextContext):
        pass

    # Exit a parse tree produced by McInstrParser#JumpNext.
    def exitJumpNext(self, ctx:McInstrParser.JumpNextContext):
        pass


    # Enter a parse tree produced by McInstrParser#JumpIdentifier.
    def enterJumpIdentifier(self, ctx:McInstrParser.JumpIdentifierContext):
        pass

    # Exit a parse tree produced by McInstrParser#JumpIdentifier.
    def exitJumpIdentifier(self, ctx:McInstrParser.JumpIdentifierContext):
        pass


    # Enter a parse tree produced by McInstrParser#extend.
    def enterExtend(self, ctx:McInstrParser.ExtendContext):
        pass

    # Exit a parse tree produced by McInstrParser#extend.
    def exitExtend(self, ctx:McInstrParser.ExtendContext):
        pass


    # Enter a parse tree produced by McInstrParser#component_ref.
    def enterComponent_ref(self, ctx:McInstrParser.Component_refContext):
        pass

    # Exit a parse tree produced by McInstrParser#component_ref.
    def exitComponent_ref(self, ctx:McInstrParser.Component_refContext):
        pass


    # Enter a parse tree produced by McInstrParser#coords.
    def enterCoords(self, ctx:McInstrParser.CoordsContext):
        pass

    # Exit a parse tree produced by McInstrParser#coords.
    def exitCoords(self, ctx:McInstrParser.CoordsContext):
        pass


    # Enter a parse tree produced by McInstrParser#reference.
    def enterReference(self, ctx:McInstrParser.ReferenceContext):
        pass

    # Exit a parse tree produced by McInstrParser#reference.
    def exitReference(self, ctx:McInstrParser.ReferenceContext):
        pass


    # Enter a parse tree produced by McInstrParser#dependency.
    def enterDependency(self, ctx:McInstrParser.DependencyContext):
        pass

    # Exit a parse tree produced by McInstrParser#dependency.
    def exitDependency(self, ctx:McInstrParser.DependencyContext):
        pass


    # Enter a parse tree produced by McInstrParser#DeclareBlock.
    def enterDeclareBlock(self, ctx:McInstrParser.DeclareBlockContext):
        pass

    # Exit a parse tree produced by McInstrParser#DeclareBlock.
    def exitDeclareBlock(self, ctx:McInstrParser.DeclareBlockContext):
        pass


    # Enter a parse tree produced by McInstrParser#DeclareBlockCopy.
    def enterDeclareBlockCopy(self, ctx:McInstrParser.DeclareBlockCopyContext):
        pass

    # Exit a parse tree produced by McInstrParser#DeclareBlockCopy.
    def exitDeclareBlockCopy(self, ctx:McInstrParser.DeclareBlockCopyContext):
        pass


    # Enter a parse tree produced by McInstrParser#uservars.
    def enterUservars(self, ctx:McInstrParser.UservarsContext):
        pass

    # Exit a parse tree produced by McInstrParser#uservars.
    def exitUservars(self, ctx:McInstrParser.UservarsContext):
        pass


    # Enter a parse tree produced by McInstrParser#InitializeBlock.
    def enterInitializeBlock(self, ctx:McInstrParser.InitializeBlockContext):
        pass

    # Exit a parse tree produced by McInstrParser#InitializeBlock.
    def exitInitializeBlock(self, ctx:McInstrParser.InitializeBlockContext):
        pass


    # Enter a parse tree produced by McInstrParser#InitializeBlockCopy.
    def enterInitializeBlockCopy(self, ctx:McInstrParser.InitializeBlockCopyContext):
        pass

    # Exit a parse tree produced by McInstrParser#InitializeBlockCopy.
    def exitInitializeBlockCopy(self, ctx:McInstrParser.InitializeBlockCopyContext):
        pass


    # Enter a parse tree produced by McInstrParser#SaveBlock.
    def enterSaveBlock(self, ctx:McInstrParser.SaveBlockContext):
        pass

    # Exit a parse tree produced by McInstrParser#SaveBlock.
    def exitSaveBlock(self, ctx:McInstrParser.SaveBlockContext):
        pass


    # Enter a parse tree produced by McInstrParser#SaveBlockCopy.
    def enterSaveBlockCopy(self, ctx:McInstrParser.SaveBlockCopyContext):
        pass

    # Exit a parse tree produced by McInstrParser#SaveBlockCopy.
    def exitSaveBlockCopy(self, ctx:McInstrParser.SaveBlockCopyContext):
        pass


    # Enter a parse tree produced by McInstrParser#FinallyBlock.
    def enterFinallyBlock(self, ctx:McInstrParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by McInstrParser#FinallyBlock.
    def exitFinallyBlock(self, ctx:McInstrParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by McInstrParser#FinallyBlockCopy.
    def enterFinallyBlockCopy(self, ctx:McInstrParser.FinallyBlockCopyContext):
        pass

    # Exit a parse tree produced by McInstrParser#FinallyBlockCopy.
    def exitFinallyBlockCopy(self, ctx:McInstrParser.FinallyBlockCopyContext):
        pass


    # Enter a parse tree produced by McInstrParser#metadata.
    def enterMetadata(self, ctx:McInstrParser.MetadataContext):
        pass

    # Exit a parse tree produced by McInstrParser#metadata.
    def exitMetadata(self, ctx:McInstrParser.MetadataContext):
        pass


    # Enter a parse tree produced by McInstrParser#category.
    def enterCategory(self, ctx:McInstrParser.CategoryContext):
        pass

    # Exit a parse tree produced by McInstrParser#category.
    def exitCategory(self, ctx:McInstrParser.CategoryContext):
        pass


    # Enter a parse tree produced by McInstrParser#initializerlist.
    def enterInitializerlist(self, ctx:McInstrParser.InitializerlistContext):
        pass

    # Exit a parse tree produced by McInstrParser#initializerlist.
    def exitInitializerlist(self, ctx:McInstrParser.InitializerlistContext):
        pass


    # Enter a parse tree produced by McInstrParser#assignment.
    def enterAssignment(self, ctx:McInstrParser.AssignmentContext):
        pass

    # Exit a parse tree produced by McInstrParser#assignment.
    def exitAssignment(self, ctx:McInstrParser.AssignmentContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionBinaryLess.
    def enterExpressionBinaryLess(self, ctx:McInstrParser.ExpressionBinaryLessContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionBinaryLess.
    def exitExpressionBinaryLess(self, ctx:McInstrParser.ExpressionBinaryLessContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionBinaryGreater.
    def enterExpressionBinaryGreater(self, ctx:McInstrParser.ExpressionBinaryGreaterContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionBinaryGreater.
    def exitExpressionBinaryGreater(self, ctx:McInstrParser.ExpressionBinaryGreaterContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionGrouping.
    def enterExpressionGrouping(self, ctx:McInstrParser.ExpressionGroupingContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionGrouping.
    def exitExpressionGrouping(self, ctx:McInstrParser.ExpressionGroupingContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionBinaryLessEqual.
    def enterExpressionBinaryLessEqual(self, ctx:McInstrParser.ExpressionBinaryLessEqualContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionBinaryLessEqual.
    def exitExpressionBinaryLessEqual(self, ctx:McInstrParser.ExpressionBinaryLessEqualContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionArrayAccess.
    def enterExpressionArrayAccess(self, ctx:McInstrParser.ExpressionArrayAccessContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionArrayAccess.
    def exitExpressionArrayAccess(self, ctx:McInstrParser.ExpressionArrayAccessContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionBinaryLogic.
    def enterExpressionBinaryLogic(self, ctx:McInstrParser.ExpressionBinaryLogicContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionBinaryLogic.
    def exitExpressionBinaryLogic(self, ctx:McInstrParser.ExpressionBinaryLogicContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionInteger.
    def enterExpressionInteger(self, ctx:McInstrParser.ExpressionIntegerContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionInteger.
    def exitExpressionInteger(self, ctx:McInstrParser.ExpressionIntegerContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionExponentiation.
    def enterExpressionExponentiation(self, ctx:McInstrParser.ExpressionExponentiationContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionExponentiation.
    def exitExpressionExponentiation(self, ctx:McInstrParser.ExpressionExponentiationContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionBinaryGreaterEqual.
    def enterExpressionBinaryGreaterEqual(self, ctx:McInstrParser.ExpressionBinaryGreaterEqualContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionBinaryGreaterEqual.
    def exitExpressionBinaryGreaterEqual(self, ctx:McInstrParser.ExpressionBinaryGreaterEqualContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionZero.
    def enterExpressionZero(self, ctx:McInstrParser.ExpressionZeroContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionZero.
    def exitExpressionZero(self, ctx:McInstrParser.ExpressionZeroContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionMyself.
    def enterExpressionMyself(self, ctx:McInstrParser.ExpressionMyselfContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionMyself.
    def exitExpressionMyself(self, ctx:McInstrParser.ExpressionMyselfContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionUnaryPM.
    def enterExpressionUnaryPM(self, ctx:McInstrParser.ExpressionUnaryPMContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionUnaryPM.
    def exitExpressionUnaryPM(self, ctx:McInstrParser.ExpressionUnaryPMContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionPrevious.
    def enterExpressionPrevious(self, ctx:McInstrParser.ExpressionPreviousContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionPrevious.
    def exitExpressionPrevious(self, ctx:McInstrParser.ExpressionPreviousContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionTrinaryLogic.
    def enterExpressionTrinaryLogic(self, ctx:McInstrParser.ExpressionTrinaryLogicContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionTrinaryLogic.
    def exitExpressionTrinaryLogic(self, ctx:McInstrParser.ExpressionTrinaryLogicContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionFloat.
    def enterExpressionFloat(self, ctx:McInstrParser.ExpressionFloatContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionFloat.
    def exitExpressionFloat(self, ctx:McInstrParser.ExpressionFloatContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionPointerAccess.
    def enterExpressionPointerAccess(self, ctx:McInstrParser.ExpressionPointerAccessContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionPointerAccess.
    def exitExpressionPointerAccess(self, ctx:McInstrParser.ExpressionPointerAccessContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionIdentifier.
    def enterExpressionIdentifier(self, ctx:McInstrParser.ExpressionIdentifierContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionIdentifier.
    def exitExpressionIdentifier(self, ctx:McInstrParser.ExpressionIdentifierContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionBinaryEqual.
    def enterExpressionBinaryEqual(self, ctx:McInstrParser.ExpressionBinaryEqualContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionBinaryEqual.
    def exitExpressionBinaryEqual(self, ctx:McInstrParser.ExpressionBinaryEqualContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionBinaryPM.
    def enterExpressionBinaryPM(self, ctx:McInstrParser.ExpressionBinaryPMContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionBinaryPM.
    def exitExpressionBinaryPM(self, ctx:McInstrParser.ExpressionBinaryPMContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionUnaryLogic.
    def enterExpressionUnaryLogic(self, ctx:McInstrParser.ExpressionUnaryLogicContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionUnaryLogic.
    def exitExpressionUnaryLogic(self, ctx:McInstrParser.ExpressionUnaryLogicContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionStructAccess.
    def enterExpressionStructAccess(self, ctx:McInstrParser.ExpressionStructAccessContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionStructAccess.
    def exitExpressionStructAccess(self, ctx:McInstrParser.ExpressionStructAccessContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionFunctionCall.
    def enterExpressionFunctionCall(self, ctx:McInstrParser.ExpressionFunctionCallContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionFunctionCall.
    def exitExpressionFunctionCall(self, ctx:McInstrParser.ExpressionFunctionCallContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionBinaryMD.
    def enterExpressionBinaryMD(self, ctx:McInstrParser.ExpressionBinaryMDContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionBinaryMD.
    def exitExpressionBinaryMD(self, ctx:McInstrParser.ExpressionBinaryMDContext):
        pass


    # Enter a parse tree produced by McInstrParser#ExpressionString.
    def enterExpressionString(self, ctx:McInstrParser.ExpressionStringContext):
        pass

    # Exit a parse tree produced by McInstrParser#ExpressionString.
    def exitExpressionString(self, ctx:McInstrParser.ExpressionStringContext):
        pass


    # Enter a parse tree produced by McInstrParser#shell.
    def enterShell(self, ctx:McInstrParser.ShellContext):
        pass

    # Exit a parse tree produced by McInstrParser#shell.
    def exitShell(self, ctx:McInstrParser.ShellContext):
        pass


    # Enter a parse tree produced by McInstrParser#SearchPath.
    def enterSearchPath(self, ctx:McInstrParser.SearchPathContext):
        pass

    # Exit a parse tree produced by McInstrParser#SearchPath.
    def exitSearchPath(self, ctx:McInstrParser.SearchPathContext):
        pass


    # Enter a parse tree produced by McInstrParser#SearchShell.
    def enterSearchShell(self, ctx:McInstrParser.SearchShellContext):
        pass

    # Exit a parse tree produced by McInstrParser#SearchShell.
    def exitSearchShell(self, ctx:McInstrParser.SearchShellContext):
        pass


    # Enter a parse tree produced by McInstrParser#unparsed_block.
    def enterUnparsed_block(self, ctx:McInstrParser.Unparsed_blockContext):
        pass

    # Exit a parse tree produced by McInstrParser#unparsed_block.
    def exitUnparsed_block(self, ctx:McInstrParser.Unparsed_blockContext):
        pass



del McInstrParser