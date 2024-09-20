
// Generated from /home/g/PycharmProjects/mccode-antlr/src/grammar/McInstr.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "McInstrVisitor.h"


/**
 * This class provides an empty implementation of McInstrVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  McInstrBaseVisitor : public McInstrVisitor {
public:

  virtual std::any visitProg(McInstrParser::ProgContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstrument_definition(McInstrParser::Instrument_definitionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstrument_parameters(McInstrParser::Instrument_parametersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstrumentParameterDouble(McInstrParser::InstrumentParameterDoubleContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstrumentParameterInteger(McInstrParser::InstrumentParameterIntegerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstrumentParameterString(McInstrParser::InstrumentParameterStringContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstrument_parameter_unit(McInstrParser::Instrument_parameter_unitContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstrument_trace(McInstrParser::Instrument_traceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstrument_metadata(McInstrParser::Instrument_metadataContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstrument_trace_include(McInstrParser::Instrument_trace_includeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponent_instance(McInstrParser::Component_instanceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstanceNameCopyIdentifier(McInstrParser::InstanceNameCopyIdentifierContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstanceNameCopy(McInstrParser::InstanceNameCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstanceNameIdentifier(McInstrParser::InstanceNameIdentifierContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentTypeCopy(McInstrParser::ComponentTypeCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentTypeIdentifier(McInstrParser::ComponentTypeIdentifierContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstance_parameters(McInstrParser::Instance_parametersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstanceParameterExpr(McInstrParser::InstanceParameterExprContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstanceParameterNull(McInstrParser::InstanceParameterNullContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInstanceParameterVector(McInstrParser::InstanceParameterVectorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSplit(McInstrParser::SplitContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitWhen(McInstrParser::WhenContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPlace(McInstrParser::PlaceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitOrientation(McInstrParser::OrientationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitGroupref(McInstrParser::GrouprefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitJumps(McInstrParser::JumpsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitJump(McInstrParser::JumpContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitJumpPrevious(McInstrParser::JumpPreviousContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitJumpMyself(McInstrParser::JumpMyselfContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitJumpNext(McInstrParser::JumpNextContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitJumpIdentifier(McInstrParser::JumpIdentifierContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExtend(McInstrParser::ExtendContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponent_ref(McInstrParser::Component_refContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCoords(McInstrParser::CoordsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitReference(McInstrParser::ReferenceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDependency(McInstrParser::DependencyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDeclareBlock(McInstrParser::DeclareBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDeclareBlockCopy(McInstrParser::DeclareBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitUservars(McInstrParser::UservarsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInitializeBlock(McInstrParser::InitializeBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInitializeBlockCopy(McInstrParser::InitializeBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSaveBlock(McInstrParser::SaveBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSaveBlockCopy(McInstrParser::SaveBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFinallyBlock(McInstrParser::FinallyBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFinallyBlockCopy(McInstrParser::FinallyBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitMetadata(McInstrParser::MetadataContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCategory(McInstrParser::CategoryContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInitializerlist(McInstrParser::InitializerlistContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAssignment(McInstrParser::AssignmentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryMod(McInstrParser::ExpressionBinaryModContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryLess(McInstrParser::ExpressionBinaryLessContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryGreater(McInstrParser::ExpressionBinaryGreaterContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryLessEqual(McInstrParser::ExpressionBinaryLessEqualContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionArrayAccess(McInstrParser::ExpressionArrayAccessContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryLogic(McInstrParser::ExpressionBinaryLogicContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionInteger(McInstrParser::ExpressionIntegerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryRightShift(McInstrParser::ExpressionBinaryRightShiftContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionMyself(McInstrParser::ExpressionMyselfContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionPrevious(McInstrParser::ExpressionPreviousContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionIdentifier(McInstrParser::ExpressionIdentifierContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionStructAccess(McInstrParser::ExpressionStructAccessContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionFunctionCall(McInstrParser::ExpressionFunctionCallContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryMD(McInstrParser::ExpressionBinaryMDContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionString(McInstrParser::ExpressionStringContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionGrouping(McInstrParser::ExpressionGroupingContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionExponentiation(McInstrParser::ExpressionExponentiationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryLeftShift(McInstrParser::ExpressionBinaryLeftShiftContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryGreaterEqual(McInstrParser::ExpressionBinaryGreaterEqualContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionZero(McInstrParser::ExpressionZeroContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionUnaryPM(McInstrParser::ExpressionUnaryPMContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionTrinaryLogic(McInstrParser::ExpressionTrinaryLogicContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionFloat(McInstrParser::ExpressionFloatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionPointerAccess(McInstrParser::ExpressionPointerAccessContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryEqual(McInstrParser::ExpressionBinaryEqualContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryPM(McInstrParser::ExpressionBinaryPMContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionUnaryLogic(McInstrParser::ExpressionUnaryLogicContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShell(McInstrParser::ShellContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSearchPath(McInstrParser::SearchPathContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSearchShell(McInstrParser::SearchShellContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitUnparsed_block(McInstrParser::Unparsed_blockContext *ctx) override {
    return visitChildren(ctx);
  }


};

