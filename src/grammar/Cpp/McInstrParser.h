
// Generated from /home/g/PycharmProjects/mccode-antlr/src/grammar/McInstr.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  McInstrParser : public antlr4::Parser {
public:
  enum {
    T__0 = 1, T__1 = 2, T__2 = 3, Absolute = 4, At = 5, Category = 6, Component = 7, 
    UserVars = 8, Define = 9, Declare = 10, Definition = 11, End = 12, McDisplay = 13, 
    Finally = 14, Initialize = 15, Instrument = 16, Output = 17, Private = 18, 
    Parameters = 19, Relative = 20, Rotated = 21, Previous = 22, Setting = 23, 
    Trace = 24, Share = 25, Extend = 26, Group = 27, Save = 28, Jump = 29, 
    When = 30, Next = 31, Iterate = 32, Myself = 33, Copy = 34, Split = 35, 
    Removable = 36, Cpu = 37, NoAcc = 38, Dependency = 39, Shell = 40, Search = 41, 
    MetaData = 42, String = 43, Vector = 44, Symbol = 45, UnparsedBlock = 46, 
    Include = 47, Null = 48, IntegerLiteral = 49, CharacterLiteral = 50, 
    FloatingLiteral = 51, StringLiteral = 52, BooleanLitteral = 53, PointerLiteral = 54, 
    UserDefinedLiteral = 55, MultiLineMacro = 56, Directive = 57, Alignas = 58, 
    Alignof = 59, Asm = 60, Auto = 61, Bool = 62, Break = 63, Case = 64, 
    Catch = 65, Char = 66, Char16 = 67, Char32 = 68, Class = 69, Const = 70, 
    Constexpr = 71, Const_cast = 72, Continue = 73, Decltype = 74, Default = 75, 
    Delete = 76, Do = 77, Double = 78, Dynamic_cast = 79, Else = 80, Enum = 81, 
    Explicit = 82, Export = 83, Extern = 84, False_ = 85, Final = 86, Float = 87, 
    For = 88, Friend = 89, Goto = 90, If = 91, Inline = 92, Int = 93, Long = 94, 
    Mutable = 95, Namespace = 96, New = 97, Noexcept = 98, Nullptr = 99, 
    Operator = 100, Override = 101, Protected = 102, Public = 103, Register = 104, 
    Reinterpret_cast = 105, Return = 106, Short = 107, Signed = 108, Sizeof = 109, 
    Static = 110, Static_assert = 111, Static_cast = 112, Struct = 113, 
    Switch = 114, Template = 115, This = 116, Thread_local = 117, Throw = 118, 
    True_ = 119, Try = 120, Typedef = 121, Typeid_ = 122, Typename_ = 123, 
    Union = 124, Unsigned = 125, Using = 126, Virtual = 127, Void = 128, 
    Volatile = 129, Wchar = 130, While = 131, LeftParen = 132, RightParen = 133, 
    LeftBracket = 134, RightBracket = 135, LeftBrace = 136, RightBrace = 137, 
    Plus = 138, Minus = 139, Star = 140, Div = 141, Mod = 142, Caret = 143, 
    And = 144, Or = 145, Tilde = 146, Not = 147, Assign = 148, Less = 149, 
    Greater = 150, PlusAssign = 151, MinusAssign = 152, StarAssign = 153, 
    DivAssign = 154, ModAssign = 155, XorAssign = 156, AndAssign = 157, 
    OrAssign = 158, LeftShiftAssign = 159, RightShiftAssign = 160, Equal = 161, 
    NotEqual = 162, LessEqual = 163, GreaterEqual = 164, AndAnd = 165, OrOr = 166, 
    PlusPlus = 167, MinusMinus = 168, Comma = 169, ArrowStar = 170, Arrow = 171, 
    Question = 172, Colon = 173, Doublecolon = 174, Semi = 175, Dot = 176, 
    DotStar = 177, Ellipsis = 178, Identifier = 179, DecimalLiteral = 180, 
    OctalLiteral = 181, HexadecimalLiteral = 182, BinaryLiteral = 183, IntegerSuffix = 184, 
    UserDefinedIntegerLiteral = 185, UserDefinedFloatingLiteral = 186, UserDefinedStringLiteral = 187, 
    UserDefinedCharacterLiteral = 188, Whitespace = 189, Newline = 190, 
    BlockComment = 191, LineComment = 192
  };

  enum {
    RuleProg = 0, RuleInstrument_definition = 1, RuleInstrument_parameters = 2, 
    RuleInstrument_parameter = 3, RuleInstrument_parameter_unit = 4, RuleInstrument_trace = 5, 
    RuleInstrument_metadata = 6, RuleInstrument_trace_include = 7, RuleComponent_instance = 8, 
    RuleInstance_name = 9, RuleComponent_type = 10, RuleInstance_parameters = 11, 
    RuleInstance_parameter = 12, RuleSplit = 13, RuleWhen = 14, RulePlace = 15, 
    RuleOrientation = 16, RuleGroupref = 17, RuleJumps = 18, RuleJump = 19, 
    RuleJumpname = 20, RuleExtend = 21, RuleComponent_ref = 22, RuleCoords = 23, 
    RuleReference = 24, RuleDependency = 25, RuleDeclare = 26, RuleUservars = 27, 
    RuleInitialise = 28, RuleSave = 29, RuleFinally_ = 30, RuleMetadata = 31, 
    RuleCategory = 32, RuleInitializerlist = 33, RuleAssignment = 34, RuleExpr = 35, 
    RuleShell = 36, RuleSearch = 37, RuleUnparsed_block = 38
  };

  explicit McInstrParser(antlr4::TokenStream *input);

  McInstrParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~McInstrParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class ProgContext;
  class Instrument_definitionContext;
  class Instrument_parametersContext;
  class Instrument_parameterContext;
  class Instrument_parameter_unitContext;
  class Instrument_traceContext;
  class Instrument_metadataContext;
  class Instrument_trace_includeContext;
  class Component_instanceContext;
  class Instance_nameContext;
  class Component_typeContext;
  class Instance_parametersContext;
  class Instance_parameterContext;
  class SplitContext;
  class WhenContext;
  class PlaceContext;
  class OrientationContext;
  class GrouprefContext;
  class JumpsContext;
  class JumpContext;
  class JumpnameContext;
  class ExtendContext;
  class Component_refContext;
  class CoordsContext;
  class ReferenceContext;
  class DependencyContext;
  class DeclareContext;
  class UservarsContext;
  class InitialiseContext;
  class SaveContext;
  class Finally_Context;
  class MetadataContext;
  class CategoryContext;
  class InitializerlistContext;
  class AssignmentContext;
  class ExprContext;
  class ShellContext;
  class SearchContext;
  class Unparsed_blockContext; 

  class  ProgContext : public antlr4::ParserRuleContext {
  public:
    ProgContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Instrument_definitionContext *instrument_definition();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ProgContext* prog();

  class  Instrument_definitionContext : public antlr4::ParserRuleContext {
  public:
    Instrument_definitionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Define();
    antlr4::tree::TerminalNode *Instrument();
    antlr4::tree::TerminalNode *Identifier();
    Instrument_parametersContext *instrument_parameters();
    Instrument_traceContext *instrument_trace();
    antlr4::tree::TerminalNode *End();
    ShellContext *shell();
    SearchContext *search();
    Instrument_metadataContext *instrument_metadata();
    DependencyContext *dependency();
    DeclareContext *declare();
    UservarsContext *uservars();
    InitialiseContext *initialise();
    SaveContext *save();
    Finally_Context *finally_();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Instrument_definitionContext* instrument_definition();

  class  Instrument_parametersContext : public antlr4::ParserRuleContext {
  public:
    McInstrParser::Instrument_parameterContext *instrument_parameterContext = nullptr;
    std::vector<Instrument_parameterContext *> params;
    Instrument_parametersContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LeftParen();
    antlr4::tree::TerminalNode *RightParen();
    std::vector<Instrument_parameterContext *> instrument_parameter();
    Instrument_parameterContext* instrument_parameter(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Instrument_parametersContext* instrument_parameters();

  class  Instrument_parameterContext : public antlr4::ParserRuleContext {
  public:
    Instrument_parameterContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    Instrument_parameterContext() = default;
    void copyFrom(Instrument_parameterContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  InstrumentParameterIntegerContext : public Instrument_parameterContext {
  public:
    InstrumentParameterIntegerContext(Instrument_parameterContext *ctx);

    antlr4::tree::TerminalNode *Int();
    antlr4::tree::TerminalNode *Identifier();
    Instrument_parameter_unitContext *instrument_parameter_unit();
    antlr4::tree::TerminalNode *Assign();
    ExprContext *expr();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  InstrumentParameterDoubleContext : public Instrument_parameterContext {
  public:
    InstrumentParameterDoubleContext(Instrument_parameterContext *ctx);

    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Double();
    Instrument_parameter_unitContext *instrument_parameter_unit();
    antlr4::tree::TerminalNode *Assign();
    ExprContext *expr();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  InstrumentParameterStringContext : public Instrument_parameterContext {
  public:
    InstrumentParameterStringContext(Instrument_parameterContext *ctx);

    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *String();
    Instrument_parameter_unitContext *instrument_parameter_unit();
    antlr4::tree::TerminalNode *Assign();
    antlr4::tree::TerminalNode *Char();
    antlr4::tree::TerminalNode *Star();
    antlr4::tree::TerminalNode *StringLiteral();
    antlr4::tree::TerminalNode *Null();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  Instrument_parameterContext* instrument_parameter();

  class  Instrument_parameter_unitContext : public antlr4::ParserRuleContext {
  public:
    Instrument_parameter_unitContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Div();
    antlr4::tree::TerminalNode *StringLiteral();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Instrument_parameter_unitContext* instrument_parameter_unit();

  class  Instrument_traceContext : public antlr4::ParserRuleContext {
  public:
    Instrument_traceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Trace();
    std::vector<Component_instanceContext *> component_instance();
    Component_instanceContext* component_instance(size_t i);
    std::vector<SearchContext *> search();
    SearchContext* search(size_t i);
    std::vector<Instrument_trace_includeContext *> instrument_trace_include();
    Instrument_trace_includeContext* instrument_trace_include(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Instrument_traceContext* instrument_trace();

  class  Instrument_metadataContext : public antlr4::ParserRuleContext {
  public:
    Instrument_metadataContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<MetadataContext *> metadata();
    MetadataContext* metadata(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Instrument_metadataContext* instrument_metadata();

  class  Instrument_trace_includeContext : public antlr4::ParserRuleContext {
  public:
    Instrument_trace_includeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Include();
    antlr4::tree::TerminalNode *StringLiteral();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Instrument_trace_includeContext* instrument_trace_include();

  class  Component_instanceContext : public antlr4::ParserRuleContext {
  public:
    Component_instanceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Component();
    Instance_nameContext *instance_name();
    antlr4::tree::TerminalNode *Assign();
    Component_typeContext *component_type();
    PlaceContext *place();
    antlr4::tree::TerminalNode *Removable();
    antlr4::tree::TerminalNode *Cpu();
    SplitContext *split();
    Instance_parametersContext *instance_parameters();
    WhenContext *when();
    OrientationContext *orientation();
    GrouprefContext *groupref();
    ExtendContext *extend();
    JumpsContext *jumps();
    std::vector<MetadataContext *> metadata();
    MetadataContext* metadata(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Component_instanceContext* component_instance();

  class  Instance_nameContext : public antlr4::ParserRuleContext {
  public:
    Instance_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    Instance_nameContext() = default;
    void copyFrom(Instance_nameContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  InstanceNameCopyIdentifierContext : public Instance_nameContext {
  public:
    InstanceNameCopyIdentifierContext(Instance_nameContext *ctx);

    antlr4::tree::TerminalNode *Copy();
    antlr4::tree::TerminalNode *LeftParen();
    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *RightParen();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  InstanceNameCopyContext : public Instance_nameContext {
  public:
    InstanceNameCopyContext(Instance_nameContext *ctx);

    antlr4::tree::TerminalNode *Myself();
    antlr4::tree::TerminalNode *Copy();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  InstanceNameIdentifierContext : public Instance_nameContext {
  public:
    InstanceNameIdentifierContext(Instance_nameContext *ctx);

    antlr4::tree::TerminalNode *Identifier();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  Instance_nameContext* instance_name();

  class  Component_typeContext : public antlr4::ParserRuleContext {
  public:
    Component_typeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    Component_typeContext() = default;
    void copyFrom(Component_typeContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  ComponentTypeIdentifierContext : public Component_typeContext {
  public:
    ComponentTypeIdentifierContext(Component_typeContext *ctx);

    antlr4::tree::TerminalNode *Identifier();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ComponentTypeCopyContext : public Component_typeContext {
  public:
    ComponentTypeCopyContext(Component_typeContext *ctx);

    antlr4::tree::TerminalNode *Copy();
    antlr4::tree::TerminalNode *LeftParen();
    Component_refContext *component_ref();
    antlr4::tree::TerminalNode *RightParen();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  Component_typeContext* component_type();

  class  Instance_parametersContext : public antlr4::ParserRuleContext {
  public:
    McInstrParser::Instance_parameterContext *instance_parameterContext = nullptr;
    std::vector<Instance_parameterContext *> params;
    Instance_parametersContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LeftParen();
    antlr4::tree::TerminalNode *RightParen();
    std::vector<Instance_parameterContext *> instance_parameter();
    Instance_parameterContext* instance_parameter(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Instance_parametersContext* instance_parameters();

  class  Instance_parameterContext : public antlr4::ParserRuleContext {
  public:
    Instance_parameterContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    Instance_parameterContext() = default;
    void copyFrom(Instance_parameterContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  InstanceParameterExprContext : public Instance_parameterContext {
  public:
    InstanceParameterExprContext(Instance_parameterContext *ctx);

    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Assign();
    ExprContext *expr();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  InstanceParameterNullContext : public Instance_parameterContext {
  public:
    InstanceParameterNullContext(Instance_parameterContext *ctx);

    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Assign();
    antlr4::tree::TerminalNode *Null();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  InstanceParameterVectorContext : public Instance_parameterContext {
  public:
    InstanceParameterVectorContext(Instance_parameterContext *ctx);

    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Assign();
    InitializerlistContext *initializerlist();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  Instance_parameterContext* instance_parameter();

  class  SplitContext : public antlr4::ParserRuleContext {
  public:
    SplitContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Split();
    ExprContext *expr();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SplitContext* split();

  class  WhenContext : public antlr4::ParserRuleContext {
  public:
    WhenContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *When();
    ExprContext *expr();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  WhenContext* when();

  class  PlaceContext : public antlr4::ParserRuleContext {
  public:
    PlaceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *At();
    CoordsContext *coords();
    ReferenceContext *reference();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  PlaceContext* place();

  class  OrientationContext : public antlr4::ParserRuleContext {
  public:
    OrientationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Rotated();
    CoordsContext *coords();
    ReferenceContext *reference();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  OrientationContext* orientation();

  class  GrouprefContext : public antlr4::ParserRuleContext {
  public:
    GrouprefContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Group();
    antlr4::tree::TerminalNode *Identifier();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  GrouprefContext* groupref();

  class  JumpsContext : public antlr4::ParserRuleContext {
  public:
    JumpsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<JumpContext *> jump();
    JumpContext* jump(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  JumpsContext* jumps();

  class  JumpContext : public antlr4::ParserRuleContext {
  public:
    JumpContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Jump();
    JumpnameContext *jumpname();
    ExprContext *expr();
    antlr4::tree::TerminalNode *When();
    antlr4::tree::TerminalNode *Iterate();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  JumpContext* jump();

  class  JumpnameContext : public antlr4::ParserRuleContext {
  public:
    JumpnameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    JumpnameContext() = default;
    void copyFrom(JumpnameContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  JumpPreviousContext : public JumpnameContext {
  public:
    JumpPreviousContext(JumpnameContext *ctx);

    antlr4::tree::TerminalNode *Previous();
    antlr4::tree::TerminalNode *LeftParen();
    antlr4::tree::TerminalNode *IntegerLiteral();
    antlr4::tree::TerminalNode *RightParen();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  JumpMyselfContext : public JumpnameContext {
  public:
    JumpMyselfContext(JumpnameContext *ctx);

    antlr4::tree::TerminalNode *Myself();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  JumpIdentifierContext : public JumpnameContext {
  public:
    JumpIdentifierContext(JumpnameContext *ctx);

    antlr4::tree::TerminalNode *Identifier();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  JumpNextContext : public JumpnameContext {
  public:
    JumpNextContext(JumpnameContext *ctx);

    antlr4::tree::TerminalNode *Next();
    antlr4::tree::TerminalNode *LeftParen();
    antlr4::tree::TerminalNode *IntegerLiteral();
    antlr4::tree::TerminalNode *RightParen();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  JumpnameContext* jumpname();

  class  ExtendContext : public antlr4::ParserRuleContext {
  public:
    ExtendContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Extend();
    Unparsed_blockContext *unparsed_block();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ExtendContext* extend();

  class  Component_refContext : public antlr4::ParserRuleContext {
  public:
    Component_refContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Previous();
    antlr4::tree::TerminalNode *LeftParen();
    antlr4::tree::TerminalNode *IntegerLiteral();
    antlr4::tree::TerminalNode *RightParen();
    antlr4::tree::TerminalNode *Identifier();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Component_refContext* component_ref();

  class  CoordsContext : public antlr4::ParserRuleContext {
  public:
    CoordsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LeftParen();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);
    antlr4::tree::TerminalNode *RightParen();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CoordsContext* coords();

  class  ReferenceContext : public antlr4::ParserRuleContext {
  public:
    ReferenceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Absolute();
    antlr4::tree::TerminalNode *Relative();
    Component_refContext *component_ref();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ReferenceContext* reference();

  class  DependencyContext : public antlr4::ParserRuleContext {
  public:
    DependencyContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Dependency();
    antlr4::tree::TerminalNode *StringLiteral();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  DependencyContext* dependency();

  class  DeclareContext : public antlr4::ParserRuleContext {
  public:
    DeclareContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    DeclareContext() = default;
    void copyFrom(DeclareContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  DeclareBlockContext : public DeclareContext {
  public:
    DeclareBlockContext(DeclareContext *ctx);

    antlr4::tree::TerminalNode *Declare();
    Unparsed_blockContext *unparsed_block();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  DeclareBlockCopyContext : public DeclareContext {
  public:
    DeclareBlockCopyContext(DeclareContext *ctx);

    antlr4::tree::TerminalNode *Declare();
    antlr4::tree::TerminalNode *Copy();
    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Extend();
    Unparsed_blockContext *unparsed_block();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  DeclareContext* declare();

  class  UservarsContext : public antlr4::ParserRuleContext {
  public:
    UservarsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *UserVars();
    Unparsed_blockContext *unparsed_block();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  UservarsContext* uservars();

  class  InitialiseContext : public antlr4::ParserRuleContext {
  public:
    InitialiseContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    InitialiseContext() = default;
    void copyFrom(InitialiseContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  InitializeBlockContext : public InitialiseContext {
  public:
    InitializeBlockContext(InitialiseContext *ctx);

    antlr4::tree::TerminalNode *Initialize();
    Unparsed_blockContext *unparsed_block();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  InitializeBlockCopyContext : public InitialiseContext {
  public:
    InitializeBlockCopyContext(InitialiseContext *ctx);

    antlr4::tree::TerminalNode *Initialize();
    antlr4::tree::TerminalNode *Copy();
    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Extend();
    Unparsed_blockContext *unparsed_block();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  InitialiseContext* initialise();

  class  SaveContext : public antlr4::ParserRuleContext {
  public:
    SaveContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    SaveContext() = default;
    void copyFrom(SaveContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  SaveBlockCopyContext : public SaveContext {
  public:
    SaveBlockCopyContext(SaveContext *ctx);

    antlr4::tree::TerminalNode *Save();
    antlr4::tree::TerminalNode *Copy();
    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Extend();
    Unparsed_blockContext *unparsed_block();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  SaveBlockContext : public SaveContext {
  public:
    SaveBlockContext(SaveContext *ctx);

    antlr4::tree::TerminalNode *Save();
    Unparsed_blockContext *unparsed_block();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  SaveContext* save();

  class  Finally_Context : public antlr4::ParserRuleContext {
  public:
    Finally_Context(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    Finally_Context() = default;
    void copyFrom(Finally_Context *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  FinallyBlockContext : public Finally_Context {
  public:
    FinallyBlockContext(Finally_Context *ctx);

    antlr4::tree::TerminalNode *Finally();
    Unparsed_blockContext *unparsed_block();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  FinallyBlockCopyContext : public Finally_Context {
  public:
    FinallyBlockCopyContext(Finally_Context *ctx);

    antlr4::tree::TerminalNode *Finally();
    antlr4::tree::TerminalNode *Copy();
    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Extend();
    Unparsed_blockContext *unparsed_block();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  Finally_Context* finally_();

  class  MetadataContext : public antlr4::ParserRuleContext {
  public:
    antlr4::Token *mime = nullptr;
    antlr4::Token *name = nullptr;
    MetadataContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *MetaData();
    Unparsed_blockContext *unparsed_block();
    std::vector<antlr4::tree::TerminalNode *> Identifier();
    antlr4::tree::TerminalNode* Identifier(size_t i);
    std::vector<antlr4::tree::TerminalNode *> StringLiteral();
    antlr4::tree::TerminalNode* StringLiteral(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  MetadataContext* metadata();

  class  CategoryContext : public antlr4::ParserRuleContext {
  public:
    CategoryContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Category();
    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *StringLiteral();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CategoryContext* category();

  class  InitializerlistContext : public antlr4::ParserRuleContext {
  public:
    McInstrParser::ExprContext *exprContext = nullptr;
    std::vector<ExprContext *> values;
    InitializerlistContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LeftBrace();
    antlr4::tree::TerminalNode *RightBrace();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  InitializerlistContext* initializerlist();

  class  AssignmentContext : public antlr4::ParserRuleContext {
  public:
    AssignmentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Assign();
    ExprContext *expr();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  AssignmentContext* assignment();

  class  ExprContext : public antlr4::ParserRuleContext {
  public:
    ExprContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    ExprContext() = default;
    void copyFrom(ExprContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  ExpressionBinaryModContext : public ExprContext {
  public:
    ExpressionBinaryModContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    antlr4::tree::TerminalNode *Mod();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryLessContext : public ExprContext {
  public:
    ExpressionBinaryLessContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    antlr4::tree::TerminalNode *Less();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryGreaterContext : public ExprContext {
  public:
    ExpressionBinaryGreaterContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    antlr4::tree::TerminalNode *Greater();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryLessEqualContext : public ExprContext {
  public:
    ExpressionBinaryLessEqualContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    antlr4::tree::TerminalNode *LessEqual();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionArrayAccessContext : public ExprContext {
  public:
    ExpressionArrayAccessContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *LeftBracket();
    ExprContext *expr();
    antlr4::tree::TerminalNode *RightBracket();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryLogicContext : public ExprContext {
  public:
    ExpressionBinaryLogicContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    antlr4::tree::TerminalNode *AndAnd();
    antlr4::tree::TerminalNode *OrOr();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionIntegerContext : public ExprContext {
  public:
    ExpressionIntegerContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *IntegerLiteral();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryRightShiftContext : public ExprContext {
  public:
    ExpressionBinaryRightShiftContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionMyselfContext : public ExprContext {
  public:
    ExpressionMyselfContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *Myself();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionPreviousContext : public ExprContext {
  public:
    ExpressionPreviousContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *Previous();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionIdentifierContext : public ExprContext {
  public:
    ExpressionIdentifierContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *Identifier();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionStructAccessContext : public ExprContext {
  public:
    ExpressionStructAccessContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Dot();
    ExprContext *expr();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionFunctionCallContext : public ExprContext {
  public:
    ExpressionFunctionCallContext(ExprContext *ctx);

    McInstrParser::ExprContext *exprContext = nullptr;
    std::vector<ExprContext *> args;
    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *LeftParen();
    antlr4::tree::TerminalNode *RightParen();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryMDContext : public ExprContext {
  public:
    ExpressionBinaryMDContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    antlr4::tree::TerminalNode *Star();
    antlr4::tree::TerminalNode *Div();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionStringContext : public ExprContext {
  public:
    ExpressionStringContext(ExprContext *ctx);

    antlr4::Token *stringliteralToken = nullptr;
    std::vector<antlr4::Token *> args;
    std::vector<antlr4::tree::TerminalNode *> StringLiteral();
    antlr4::tree::TerminalNode* StringLiteral(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionGroupingContext : public ExprContext {
  public:
    ExpressionGroupingContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *LeftParen();
    ExprContext *expr();
    antlr4::tree::TerminalNode *RightParen();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionExponentiationContext : public ExprContext {
  public:
    ExpressionExponentiationContext(ExprContext *ctx);

    McInstrParser::ExprContext *base = nullptr;
    McInstrParser::ExprContext *exponent = nullptr;
    antlr4::tree::TerminalNode *Caret();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryLeftShiftContext : public ExprContext {
  public:
    ExpressionBinaryLeftShiftContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryGreaterEqualContext : public ExprContext {
  public:
    ExpressionBinaryGreaterEqualContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    antlr4::tree::TerminalNode *GreaterEqual();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionZeroContext : public ExprContext {
  public:
    ExpressionZeroContext(ExprContext *ctx);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionUnaryPMContext : public ExprContext {
  public:
    ExpressionUnaryPMContext(ExprContext *ctx);

    ExprContext *expr();
    antlr4::tree::TerminalNode *Plus();
    antlr4::tree::TerminalNode *Minus();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionTrinaryLogicContext : public ExprContext {
  public:
    ExpressionTrinaryLogicContext(ExprContext *ctx);

    McInstrParser::ExprContext *test = nullptr;
    McInstrParser::ExprContext *true_ = nullptr;
    McInstrParser::ExprContext *false_ = nullptr;
    antlr4::tree::TerminalNode *Question();
    antlr4::tree::TerminalNode *Colon();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionFloatContext : public ExprContext {
  public:
    ExpressionFloatContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *FloatingLiteral();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionPointerAccessContext : public ExprContext {
  public:
    ExpressionPointerAccessContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *Identifier();
    antlr4::tree::TerminalNode *Arrow();
    ExprContext *expr();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryEqualContext : public ExprContext {
  public:
    ExpressionBinaryEqualContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    antlr4::tree::TerminalNode *Equal();
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionBinaryPMContext : public ExprContext {
  public:
    ExpressionBinaryPMContext(ExprContext *ctx);

    McInstrParser::ExprContext *left = nullptr;
    McInstrParser::ExprContext *right = nullptr;
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    antlr4::tree::TerminalNode *Plus();
    antlr4::tree::TerminalNode *Minus();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  ExpressionUnaryLogicContext : public ExprContext {
  public:
    ExpressionUnaryLogicContext(ExprContext *ctx);

    antlr4::tree::TerminalNode *Not();
    ExprContext *expr();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  ExprContext* expr();
  ExprContext* expr(int precedence);
  class  ShellContext : public antlr4::ParserRuleContext {
  public:
    ShellContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Shell();
    antlr4::tree::TerminalNode *StringLiteral();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ShellContext* shell();

  class  SearchContext : public antlr4::ParserRuleContext {
  public:
    SearchContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    SearchContext() = default;
    void copyFrom(SearchContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  SearchPathContext : public SearchContext {
  public:
    SearchPathContext(SearchContext *ctx);

    antlr4::tree::TerminalNode *Search();
    antlr4::tree::TerminalNode *StringLiteral();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  SearchShellContext : public SearchContext {
  public:
    SearchShellContext(SearchContext *ctx);

    antlr4::tree::TerminalNode *Search();
    antlr4::tree::TerminalNode *Shell();
    antlr4::tree::TerminalNode *StringLiteral();

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  SearchContext* search();

  class  Unparsed_blockContext : public antlr4::ParserRuleContext {
  public:
    Unparsed_blockContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *UnparsedBlock();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Unparsed_blockContext* unparsed_block();


  bool sempred(antlr4::RuleContext *_localctx, size_t ruleIndex, size_t predicateIndex) override;

  bool exprSempred(ExprContext *_localctx, size_t predicateIndex);

  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

