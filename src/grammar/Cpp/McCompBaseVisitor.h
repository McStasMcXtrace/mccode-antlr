
// Generated from /home/g/Code/mccode-antlr/src/grammar/McComp.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "McCompVisitor.h"


/**
 * This class provides an empty implementation of McCompVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  McCompBaseVisitor : public McCompVisitor {
public:

  virtual std::any visitProg(McCompParser::ProgContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentDefineNew(McCompParser::ComponentDefineNewContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentDefineCopy(McCompParser::ComponentDefineCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTraceBlock(McCompParser::TraceBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTraceBlockCopy(McCompParser::TraceBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponent_parameter_set(McCompParser::Component_parameter_setContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponent_define_parameters(McCompParser::Component_define_parametersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponent_set_parameters(McCompParser::Component_set_parametersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponent_out_parameters(McCompParser::Component_out_parametersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponent_parameters(McCompParser::Component_parametersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentParameterDouble(McCompParser::ComponentParameterDoubleContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentParameterInteger(McCompParser::ComponentParameterIntegerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentParameterString(McCompParser::ComponentParameterStringContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentParameterVector(McCompParser::ComponentParameterVectorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentParameterSymbol(McCompParser::ComponentParameterSymbolContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentParameterDoubleArray(McCompParser::ComponentParameterDoubleArrayContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponentParameterIntegerArray(McCompParser::ComponentParameterIntegerArrayContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShareBlock(McCompParser::ShareBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShareBlockCopy(McCompParser::ShareBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDisplayBlock(McCompParser::DisplayBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDisplayBlockCopy(McCompParser::DisplayBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComponent_ref(McCompParser::Component_refContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCoords(McCompParser::CoordsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitReference(McCompParser::ReferenceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDependency(McCompParser::DependencyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDeclareBlock(McCompParser::DeclareBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDeclareBlockCopy(McCompParser::DeclareBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitUservars(McCompParser::UservarsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInitializeBlock(McCompParser::InitializeBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInitializeBlockCopy(McCompParser::InitializeBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSaveBlock(McCompParser::SaveBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSaveBlockCopy(McCompParser::SaveBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFinallyBlock(McCompParser::FinallyBlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFinallyBlockCopy(McCompParser::FinallyBlockCopyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitMetadata(McCompParser::MetadataContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCategory(McCompParser::CategoryContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInitializerlist(McCompParser::InitializerlistContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAssignment(McCompParser::AssignmentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryMod(McCompParser::ExpressionBinaryModContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryLess(McCompParser::ExpressionBinaryLessContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryGreater(McCompParser::ExpressionBinaryGreaterContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryLessEqual(McCompParser::ExpressionBinaryLessEqualContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionArrayAccess(McCompParser::ExpressionArrayAccessContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryLogic(McCompParser::ExpressionBinaryLogicContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionInteger(McCompParser::ExpressionIntegerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryRightShift(McCompParser::ExpressionBinaryRightShiftContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionMyself(McCompParser::ExpressionMyselfContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionPrevious(McCompParser::ExpressionPreviousContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionIdentifier(McCompParser::ExpressionIdentifierContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionStructAccess(McCompParser::ExpressionStructAccessContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionFunctionCall(McCompParser::ExpressionFunctionCallContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryMD(McCompParser::ExpressionBinaryMDContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionString(McCompParser::ExpressionStringContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionGrouping(McCompParser::ExpressionGroupingContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionExponentiation(McCompParser::ExpressionExponentiationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryLeftShift(McCompParser::ExpressionBinaryLeftShiftContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryGreaterEqual(McCompParser::ExpressionBinaryGreaterEqualContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionZero(McCompParser::ExpressionZeroContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionUnaryPM(McCompParser::ExpressionUnaryPMContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionTrinaryLogic(McCompParser::ExpressionTrinaryLogicContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionFloat(McCompParser::ExpressionFloatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionPointerAccess(McCompParser::ExpressionPointerAccessContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryEqual(McCompParser::ExpressionBinaryEqualContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionBinaryPM(McCompParser::ExpressionBinaryPMContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpressionUnaryLogic(McCompParser::ExpressionUnaryLogicContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShell(McCompParser::ShellContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSearchPath(McCompParser::SearchPathContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSearchShell(McCompParser::SearchShellContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitUnparsed_block(McCompParser::Unparsed_blockContext *ctx) override {
    return visitChildren(ctx);
  }


};

