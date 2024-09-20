
// Generated from /home/g/Code/mccode-antlr/src/grammar/McComp.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "McCompParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by McCompParser.
 */
class  McCompVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by McCompParser.
   */
    virtual std::any visitProg(McCompParser::ProgContext *context) = 0;

    virtual std::any visitComponentDefineNew(McCompParser::ComponentDefineNewContext *context) = 0;

    virtual std::any visitComponentDefineCopy(McCompParser::ComponentDefineCopyContext *context) = 0;

    virtual std::any visitTraceBlock(McCompParser::TraceBlockContext *context) = 0;

    virtual std::any visitTraceBlockCopy(McCompParser::TraceBlockCopyContext *context) = 0;

    virtual std::any visitComponent_parameter_set(McCompParser::Component_parameter_setContext *context) = 0;

    virtual std::any visitComponent_define_parameters(McCompParser::Component_define_parametersContext *context) = 0;

    virtual std::any visitComponent_set_parameters(McCompParser::Component_set_parametersContext *context) = 0;

    virtual std::any visitComponent_out_parameters(McCompParser::Component_out_parametersContext *context) = 0;

    virtual std::any visitComponent_parameters(McCompParser::Component_parametersContext *context) = 0;

    virtual std::any visitComponentParameterDouble(McCompParser::ComponentParameterDoubleContext *context) = 0;

    virtual std::any visitComponentParameterInteger(McCompParser::ComponentParameterIntegerContext *context) = 0;

    virtual std::any visitComponentParameterString(McCompParser::ComponentParameterStringContext *context) = 0;

    virtual std::any visitComponentParameterVector(McCompParser::ComponentParameterVectorContext *context) = 0;

    virtual std::any visitComponentParameterSymbol(McCompParser::ComponentParameterSymbolContext *context) = 0;

    virtual std::any visitComponentParameterDoubleArray(McCompParser::ComponentParameterDoubleArrayContext *context) = 0;

    virtual std::any visitComponentParameterIntegerArray(McCompParser::ComponentParameterIntegerArrayContext *context) = 0;

    virtual std::any visitShareBlock(McCompParser::ShareBlockContext *context) = 0;

    virtual std::any visitShareBlockCopy(McCompParser::ShareBlockCopyContext *context) = 0;

    virtual std::any visitDisplayBlock(McCompParser::DisplayBlockContext *context) = 0;

    virtual std::any visitDisplayBlockCopy(McCompParser::DisplayBlockCopyContext *context) = 0;

    virtual std::any visitComponent_ref(McCompParser::Component_refContext *context) = 0;

    virtual std::any visitCoords(McCompParser::CoordsContext *context) = 0;

    virtual std::any visitReference(McCompParser::ReferenceContext *context) = 0;

    virtual std::any visitDependency(McCompParser::DependencyContext *context) = 0;

    virtual std::any visitDeclareBlock(McCompParser::DeclareBlockContext *context) = 0;

    virtual std::any visitDeclareBlockCopy(McCompParser::DeclareBlockCopyContext *context) = 0;

    virtual std::any visitUservars(McCompParser::UservarsContext *context) = 0;

    virtual std::any visitInitializeBlock(McCompParser::InitializeBlockContext *context) = 0;

    virtual std::any visitInitializeBlockCopy(McCompParser::InitializeBlockCopyContext *context) = 0;

    virtual std::any visitSaveBlock(McCompParser::SaveBlockContext *context) = 0;

    virtual std::any visitSaveBlockCopy(McCompParser::SaveBlockCopyContext *context) = 0;

    virtual std::any visitFinallyBlock(McCompParser::FinallyBlockContext *context) = 0;

    virtual std::any visitFinallyBlockCopy(McCompParser::FinallyBlockCopyContext *context) = 0;

    virtual std::any visitMetadata(McCompParser::MetadataContext *context) = 0;

    virtual std::any visitCategory(McCompParser::CategoryContext *context) = 0;

    virtual std::any visitInitializerlist(McCompParser::InitializerlistContext *context) = 0;

    virtual std::any visitAssignment(McCompParser::AssignmentContext *context) = 0;

    virtual std::any visitExpressionBinaryMod(McCompParser::ExpressionBinaryModContext *context) = 0;

    virtual std::any visitExpressionBinaryLess(McCompParser::ExpressionBinaryLessContext *context) = 0;

    virtual std::any visitExpressionBinaryGreater(McCompParser::ExpressionBinaryGreaterContext *context) = 0;

    virtual std::any visitExpressionBinaryLessEqual(McCompParser::ExpressionBinaryLessEqualContext *context) = 0;

    virtual std::any visitExpressionArrayAccess(McCompParser::ExpressionArrayAccessContext *context) = 0;

    virtual std::any visitExpressionBinaryLogic(McCompParser::ExpressionBinaryLogicContext *context) = 0;

    virtual std::any visitExpressionInteger(McCompParser::ExpressionIntegerContext *context) = 0;

    virtual std::any visitExpressionBinaryRightShift(McCompParser::ExpressionBinaryRightShiftContext *context) = 0;

    virtual std::any visitExpressionMyself(McCompParser::ExpressionMyselfContext *context) = 0;

    virtual std::any visitExpressionPrevious(McCompParser::ExpressionPreviousContext *context) = 0;

    virtual std::any visitExpressionIdentifier(McCompParser::ExpressionIdentifierContext *context) = 0;

    virtual std::any visitExpressionStructAccess(McCompParser::ExpressionStructAccessContext *context) = 0;

    virtual std::any visitExpressionFunctionCall(McCompParser::ExpressionFunctionCallContext *context) = 0;

    virtual std::any visitExpressionBinaryMD(McCompParser::ExpressionBinaryMDContext *context) = 0;

    virtual std::any visitExpressionString(McCompParser::ExpressionStringContext *context) = 0;

    virtual std::any visitExpressionGrouping(McCompParser::ExpressionGroupingContext *context) = 0;

    virtual std::any visitExpressionExponentiation(McCompParser::ExpressionExponentiationContext *context) = 0;

    virtual std::any visitExpressionBinaryLeftShift(McCompParser::ExpressionBinaryLeftShiftContext *context) = 0;

    virtual std::any visitExpressionBinaryGreaterEqual(McCompParser::ExpressionBinaryGreaterEqualContext *context) = 0;

    virtual std::any visitExpressionZero(McCompParser::ExpressionZeroContext *context) = 0;

    virtual std::any visitExpressionUnaryPM(McCompParser::ExpressionUnaryPMContext *context) = 0;

    virtual std::any visitExpressionTrinaryLogic(McCompParser::ExpressionTrinaryLogicContext *context) = 0;

    virtual std::any visitExpressionFloat(McCompParser::ExpressionFloatContext *context) = 0;

    virtual std::any visitExpressionPointerAccess(McCompParser::ExpressionPointerAccessContext *context) = 0;

    virtual std::any visitExpressionBinaryEqual(McCompParser::ExpressionBinaryEqualContext *context) = 0;

    virtual std::any visitExpressionBinaryPM(McCompParser::ExpressionBinaryPMContext *context) = 0;

    virtual std::any visitExpressionUnaryLogic(McCompParser::ExpressionUnaryLogicContext *context) = 0;

    virtual std::any visitShell(McCompParser::ShellContext *context) = 0;

    virtual std::any visitSearchPath(McCompParser::SearchPathContext *context) = 0;

    virtual std::any visitSearchShell(McCompParser::SearchShellContext *context) = 0;

    virtual std::any visitUnparsed_block(McCompParser::Unparsed_blockContext *context) = 0;


};

