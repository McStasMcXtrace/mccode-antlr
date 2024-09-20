
// Generated from /home/g/PycharmProjects/mccode-antlr/src/grammar/McInstr.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "McInstrParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by McInstrParser.
 */
class  McInstrVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by McInstrParser.
   */
    virtual std::any visitProg(McInstrParser::ProgContext *context) = 0;

    virtual std::any visitInstrument_definition(McInstrParser::Instrument_definitionContext *context) = 0;

    virtual std::any visitInstrument_parameters(McInstrParser::Instrument_parametersContext *context) = 0;

    virtual std::any visitInstrumentParameterDouble(McInstrParser::InstrumentParameterDoubleContext *context) = 0;

    virtual std::any visitInstrumentParameterInteger(McInstrParser::InstrumentParameterIntegerContext *context) = 0;

    virtual std::any visitInstrumentParameterString(McInstrParser::InstrumentParameterStringContext *context) = 0;

    virtual std::any visitInstrument_parameter_unit(McInstrParser::Instrument_parameter_unitContext *context) = 0;

    virtual std::any visitInstrument_trace(McInstrParser::Instrument_traceContext *context) = 0;

    virtual std::any visitInstrument_metadata(McInstrParser::Instrument_metadataContext *context) = 0;

    virtual std::any visitInstrument_trace_include(McInstrParser::Instrument_trace_includeContext *context) = 0;

    virtual std::any visitComponent_instance(McInstrParser::Component_instanceContext *context) = 0;

    virtual std::any visitInstanceNameCopyIdentifier(McInstrParser::InstanceNameCopyIdentifierContext *context) = 0;

    virtual std::any visitInstanceNameCopy(McInstrParser::InstanceNameCopyContext *context) = 0;

    virtual std::any visitInstanceNameIdentifier(McInstrParser::InstanceNameIdentifierContext *context) = 0;

    virtual std::any visitComponentTypeCopy(McInstrParser::ComponentTypeCopyContext *context) = 0;

    virtual std::any visitComponentTypeIdentifier(McInstrParser::ComponentTypeIdentifierContext *context) = 0;

    virtual std::any visitInstance_parameters(McInstrParser::Instance_parametersContext *context) = 0;

    virtual std::any visitInstanceParameterExpr(McInstrParser::InstanceParameterExprContext *context) = 0;

    virtual std::any visitInstanceParameterNull(McInstrParser::InstanceParameterNullContext *context) = 0;

    virtual std::any visitInstanceParameterVector(McInstrParser::InstanceParameterVectorContext *context) = 0;

    virtual std::any visitSplit(McInstrParser::SplitContext *context) = 0;

    virtual std::any visitWhen(McInstrParser::WhenContext *context) = 0;

    virtual std::any visitPlace(McInstrParser::PlaceContext *context) = 0;

    virtual std::any visitOrientation(McInstrParser::OrientationContext *context) = 0;

    virtual std::any visitGroupref(McInstrParser::GrouprefContext *context) = 0;

    virtual std::any visitJumps(McInstrParser::JumpsContext *context) = 0;

    virtual std::any visitJump(McInstrParser::JumpContext *context) = 0;

    virtual std::any visitJumpPrevious(McInstrParser::JumpPreviousContext *context) = 0;

    virtual std::any visitJumpMyself(McInstrParser::JumpMyselfContext *context) = 0;

    virtual std::any visitJumpNext(McInstrParser::JumpNextContext *context) = 0;

    virtual std::any visitJumpIdentifier(McInstrParser::JumpIdentifierContext *context) = 0;

    virtual std::any visitExtend(McInstrParser::ExtendContext *context) = 0;

    virtual std::any visitComponent_ref(McInstrParser::Component_refContext *context) = 0;

    virtual std::any visitCoords(McInstrParser::CoordsContext *context) = 0;

    virtual std::any visitReference(McInstrParser::ReferenceContext *context) = 0;

    virtual std::any visitDependency(McInstrParser::DependencyContext *context) = 0;

    virtual std::any visitDeclareBlock(McInstrParser::DeclareBlockContext *context) = 0;

    virtual std::any visitDeclareBlockCopy(McInstrParser::DeclareBlockCopyContext *context) = 0;

    virtual std::any visitUservars(McInstrParser::UservarsContext *context) = 0;

    virtual std::any visitInitializeBlock(McInstrParser::InitializeBlockContext *context) = 0;

    virtual std::any visitInitializeBlockCopy(McInstrParser::InitializeBlockCopyContext *context) = 0;

    virtual std::any visitSaveBlock(McInstrParser::SaveBlockContext *context) = 0;

    virtual std::any visitSaveBlockCopy(McInstrParser::SaveBlockCopyContext *context) = 0;

    virtual std::any visitFinallyBlock(McInstrParser::FinallyBlockContext *context) = 0;

    virtual std::any visitFinallyBlockCopy(McInstrParser::FinallyBlockCopyContext *context) = 0;

    virtual std::any visitMetadata(McInstrParser::MetadataContext *context) = 0;

    virtual std::any visitCategory(McInstrParser::CategoryContext *context) = 0;

    virtual std::any visitInitializerlist(McInstrParser::InitializerlistContext *context) = 0;

    virtual std::any visitAssignment(McInstrParser::AssignmentContext *context) = 0;

    virtual std::any visitExpressionBinaryMod(McInstrParser::ExpressionBinaryModContext *context) = 0;

    virtual std::any visitExpressionBinaryLess(McInstrParser::ExpressionBinaryLessContext *context) = 0;

    virtual std::any visitExpressionBinaryGreater(McInstrParser::ExpressionBinaryGreaterContext *context) = 0;

    virtual std::any visitExpressionBinaryLessEqual(McInstrParser::ExpressionBinaryLessEqualContext *context) = 0;

    virtual std::any visitExpressionArrayAccess(McInstrParser::ExpressionArrayAccessContext *context) = 0;

    virtual std::any visitExpressionBinaryLogic(McInstrParser::ExpressionBinaryLogicContext *context) = 0;

    virtual std::any visitExpressionInteger(McInstrParser::ExpressionIntegerContext *context) = 0;

    virtual std::any visitExpressionBinaryRightShift(McInstrParser::ExpressionBinaryRightShiftContext *context) = 0;

    virtual std::any visitExpressionMyself(McInstrParser::ExpressionMyselfContext *context) = 0;

    virtual std::any visitExpressionPrevious(McInstrParser::ExpressionPreviousContext *context) = 0;

    virtual std::any visitExpressionIdentifier(McInstrParser::ExpressionIdentifierContext *context) = 0;

    virtual std::any visitExpressionStructAccess(McInstrParser::ExpressionStructAccessContext *context) = 0;

    virtual std::any visitExpressionFunctionCall(McInstrParser::ExpressionFunctionCallContext *context) = 0;

    virtual std::any visitExpressionBinaryMD(McInstrParser::ExpressionBinaryMDContext *context) = 0;

    virtual std::any visitExpressionString(McInstrParser::ExpressionStringContext *context) = 0;

    virtual std::any visitExpressionGrouping(McInstrParser::ExpressionGroupingContext *context) = 0;

    virtual std::any visitExpressionExponentiation(McInstrParser::ExpressionExponentiationContext *context) = 0;

    virtual std::any visitExpressionBinaryLeftShift(McInstrParser::ExpressionBinaryLeftShiftContext *context) = 0;

    virtual std::any visitExpressionBinaryGreaterEqual(McInstrParser::ExpressionBinaryGreaterEqualContext *context) = 0;

    virtual std::any visitExpressionZero(McInstrParser::ExpressionZeroContext *context) = 0;

    virtual std::any visitExpressionUnaryPM(McInstrParser::ExpressionUnaryPMContext *context) = 0;

    virtual std::any visitExpressionTrinaryLogic(McInstrParser::ExpressionTrinaryLogicContext *context) = 0;

    virtual std::any visitExpressionFloat(McInstrParser::ExpressionFloatContext *context) = 0;

    virtual std::any visitExpressionPointerAccess(McInstrParser::ExpressionPointerAccessContext *context) = 0;

    virtual std::any visitExpressionBinaryEqual(McInstrParser::ExpressionBinaryEqualContext *context) = 0;

    virtual std::any visitExpressionBinaryPM(McInstrParser::ExpressionBinaryPMContext *context) = 0;

    virtual std::any visitExpressionUnaryLogic(McInstrParser::ExpressionUnaryLogicContext *context) = 0;

    virtual std::any visitShell(McInstrParser::ShellContext *context) = 0;

    virtual std::any visitSearchPath(McInstrParser::SearchPathContext *context) = 0;

    virtual std::any visitSearchShell(McInstrParser::SearchShellContext *context) = 0;

    virtual std::any visitUnparsed_block(McInstrParser::Unparsed_blockContext *context) = 0;


};

