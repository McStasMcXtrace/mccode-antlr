
// Generated from /home/g/Code/mccode-antlr/src/grammar/McComp.g4 by ANTLR 4.13.2


#include "McCompVisitor.h"

#include "McCompParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct McCompParserStaticData final {
  McCompParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  McCompParserStaticData(const McCompParserStaticData&) = delete;
  McCompParserStaticData(McCompParserStaticData&&) = delete;
  McCompParserStaticData& operator=(const McCompParserStaticData&) = delete;
  McCompParserStaticData& operator=(McCompParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag mccompParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<McCompParserStaticData> mccompParserStaticData = nullptr;

void mccompParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (mccompParserStaticData != nullptr) {
    return;
  }
#else
  assert(mccompParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<McCompParserStaticData>(
    std::vector<std::string>{
      "prog", "component_definition", "component_trace", "component_parameter_set", 
      "component_define_parameters", "component_set_parameters", "component_out_parameters", 
      "component_parameters", "component_parameter", "share", "display", 
      "component_ref", "coords", "reference", "dependency", "declare", "uservars", 
      "initialize", "save", "finally_", "metadata", "category", "initializerlist", 
      "assignment", "expr", "shell", "search", "unparsed_block"
    },
    std::vector<std::string>{
      "", "'0'", "'>>'", "'<<'", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "", "", "", "'string'", "'vector'", 
      "'symbol'", "", "'%include'", "'NULL'", "", "", "", "", "", "", "", 
      "", "", "'alignas'", "'alignof'", "'asm'", "'auto'", "'bool'", "'break'", 
      "'case'", "'catch'", "'char'", "'char16_t'", "'char32_t'", "'class'", 
      "'const'", "'constexpr'", "'const_cast'", "'continue'", "'decltype'", 
      "'default'", "'delete'", "'do'", "'double'", "'dynamic_cast'", "'else'", 
      "'enum'", "'explicit'", "'export'", "'extern'", "'false'", "'final'", 
      "'float'", "'for'", "'friend'", "'goto'", "'if'", "'inline'", "'int'", 
      "'long'", "'mutable'", "'namespace'", "'new'", "'noexcept'", "'nullptr'", 
      "'operator'", "'override'", "'protected'", "'public'", "'register'", 
      "'reinterpret_cast'", "'return'", "'short'", "'signed'", "'sizeof'", 
      "'static'", "'static_assert'", "'static_cast'", "'struct'", "'switch'", 
      "'template'", "'this'", "'thread_local'", "'throw'", "'true'", "'try'", 
      "'typedef'", "'typeid'", "'typename'", "'union'", "'unsigned'", "'using'", 
      "'virtual'", "'void'", "'volatile'", "'wchar_t'", "'while'", "'('", 
      "')'", "'['", "']'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", 
      "'^'", "'&'", "'|'", "'~'", "", "'='", "'<'", "'>'", "'+='", "'-='", 
      "'*='", "'/='", "'%='", "'^='", "'&='", "'|='", "'<<='", "'>>='", 
      "'=='", "'!='", "'<='", "'>='", "", "", "'++'", "'--'", "','", "'->*'", 
      "'->'", "'\\u003F'", "':'", "'::'", "';'", "'.'", "'.*'", "'...'"
    },
    std::vector<std::string>{
      "", "", "", "", "Absolute", "At", "Category", "Component", "UserVars", 
      "Define", "Declare", "Definition", "End", "McDisplay", "Finally", 
      "Initialize", "Instrument", "Output", "Private", "Parameters", "Relative", 
      "Rotated", "Previous", "Setting", "Trace", "Share", "Extend", "Group", 
      "Save", "Jump", "When", "Next", "Iterate", "Myself", "Copy", "Split", 
      "Removable", "Cpu", "NoAcc", "Dependency", "Shell", "Search", "MetaData", 
      "String", "Vector", "Symbol", "UnparsedBlock", "Include", "Null", 
      "IntegerLiteral", "CharacterLiteral", "FloatingLiteral", "StringLiteral", 
      "BooleanLitteral", "PointerLiteral", "UserDefinedLiteral", "MultiLineMacro", 
      "Directive", "Alignas", "Alignof", "Asm", "Auto", "Bool", "Break", 
      "Case", "Catch", "Char", "Char16", "Char32", "Class", "Const", "Constexpr", 
      "Const_cast", "Continue", "Decltype", "Default", "Delete", "Do", "Double", 
      "Dynamic_cast", "Else", "Enum", "Explicit", "Export", "Extern", "False_", 
      "Final", "Float", "For", "Friend", "Goto", "If", "Inline", "Int", 
      "Long", "Mutable", "Namespace", "New", "Noexcept", "Nullptr", "Operator", 
      "Override", "Protected", "Public", "Register", "Reinterpret_cast", 
      "Return", "Short", "Signed", "Sizeof", "Static", "Static_assert", 
      "Static_cast", "Struct", "Switch", "Template", "This", "Thread_local", 
      "Throw", "True_", "Try", "Typedef", "Typeid_", "Typename_", "Union", 
      "Unsigned", "Using", "Virtual", "Void", "Volatile", "Wchar", "While", 
      "LeftParen", "RightParen", "LeftBracket", "RightBracket", "LeftBrace", 
      "RightBrace", "Plus", "Minus", "Star", "Div", "Mod", "Caret", "And", 
      "Or", "Tilde", "Not", "Assign", "Less", "Greater", "PlusAssign", "MinusAssign", 
      "StarAssign", "DivAssign", "ModAssign", "XorAssign", "AndAssign", 
      "OrAssign", "LeftShiftAssign", "RightShiftAssign", "Equal", "NotEqual", 
      "LessEqual", "GreaterEqual", "AndAnd", "OrOr", "PlusPlus", "MinusMinus", 
      "Comma", "ArrowStar", "Arrow", "Question", "Colon", "Doublecolon", 
      "Semi", "Dot", "DotStar", "Ellipsis", "Identifier", "DecimalLiteral", 
      "OctalLiteral", "HexadecimalLiteral", "BinaryLiteral", "IntegerSuffix", 
      "UserDefinedIntegerLiteral", "UserDefinedFloatingLiteral", "UserDefinedStringLiteral", 
      "UserDefinedCharacterLiteral", "Whitespace", "Newline", "BlockComment", 
      "LineComment"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,192,501,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,1,0,1,
  	0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,1,5,1,68,8,1,10,1,12,1,71,9,1,
  	1,1,3,1,74,8,1,1,1,3,1,77,8,1,1,1,3,1,80,8,1,1,1,3,1,83,8,1,1,1,3,1,86,
  	8,1,1,1,3,1,89,8,1,1,1,3,1,92,8,1,1,1,3,1,95,8,1,1,1,3,1,98,8,1,1,1,3,
  	1,101,8,1,1,1,3,1,104,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,115,
  	8,1,1,1,5,1,118,8,1,10,1,12,1,121,9,1,1,1,3,1,124,8,1,1,1,3,1,127,8,1,
  	1,1,3,1,130,8,1,1,1,3,1,133,8,1,1,1,3,1,136,8,1,1,1,3,1,139,8,1,1,1,3,
  	1,142,8,1,1,1,3,1,145,8,1,1,1,3,1,148,8,1,1,1,3,1,151,8,1,1,1,3,1,154,
  	8,1,1,1,1,1,3,1,158,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,167,8,2,3,2,169,
  	8,2,1,3,3,3,172,8,3,1,3,3,3,175,8,3,1,3,3,3,178,8,3,1,4,1,4,1,4,1,4,1,
  	5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,196,8,7,10,7,12,7,199,
  	9,7,3,7,201,8,7,1,7,1,7,1,8,3,8,206,8,8,1,8,1,8,1,8,1,8,3,8,212,8,8,3,
  	8,214,8,8,1,8,1,8,1,8,1,8,1,8,3,8,221,8,8,3,8,223,8,8,1,8,1,8,1,8,3,8,
  	228,8,8,1,8,1,8,1,8,3,8,233,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,242,8,
  	8,3,8,244,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,258,
  	8,8,3,8,260,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,270,8,8,3,8,272,8,
  	8,3,8,274,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,283,8,9,3,9,285,8,9,1,10,
  	1,10,1,10,1,10,1,10,1,10,1,10,3,10,294,8,10,3,10,296,8,10,1,11,1,11,1,
  	11,1,11,3,11,302,8,11,1,11,3,11,305,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,12,1,13,1,13,1,13,1,13,3,13,319,8,13,3,13,321,8,13,1,14,1,14,1,
  	14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,333,8,15,3,15,335,8,15,1,16,
  	1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,347,8,17,3,17,349,8,
  	17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,358,8,18,3,18,360,8,18,1,19,
  	1,19,1,19,1,19,1,19,1,19,1,19,3,19,369,8,19,3,19,371,8,19,1,20,1,20,1,
  	20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,5,22,385,8,22,10,22,12,
  	22,388,9,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,5,
  	24,401,8,24,10,24,12,24,404,9,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
  	24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,5,24,422,8,24,10,24,12,24,
  	425,9,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
  	1,24,3,24,440,8,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
  	1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
  	1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
  	1,24,1,24,1,24,1,24,5,24,484,8,24,10,24,12,24,487,9,24,1,25,1,25,1,25,
  	1,26,1,26,1,26,1,26,1,26,3,26,497,8,26,1,27,1,27,1,27,0,1,48,28,0,2,4,
  	6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
  	54,0,6,1,0,17,18,3,0,1,1,48,48,52,52,2,0,52,52,179,179,1,0,138,139,1,
  	0,140,141,1,0,165,166,577,0,56,1,0,0,0,2,157,1,0,0,0,4,168,1,0,0,0,6,
  	171,1,0,0,0,8,179,1,0,0,0,10,183,1,0,0,0,12,187,1,0,0,0,14,191,1,0,0,
  	0,16,273,1,0,0,0,18,284,1,0,0,0,20,295,1,0,0,0,22,304,1,0,0,0,24,306,
  	1,0,0,0,26,320,1,0,0,0,28,322,1,0,0,0,30,334,1,0,0,0,32,336,1,0,0,0,34,
  	348,1,0,0,0,36,359,1,0,0,0,38,370,1,0,0,0,40,372,1,0,0,0,42,377,1,0,0,
  	0,44,380,1,0,0,0,46,391,1,0,0,0,48,439,1,0,0,0,50,488,1,0,0,0,52,496,
  	1,0,0,0,54,498,1,0,0,0,56,57,3,2,1,0,57,58,5,0,0,1,58,1,1,0,0,0,59,60,
  	5,9,0,0,60,61,5,7,0,0,61,62,5,179,0,0,62,64,3,6,3,0,63,65,3,42,21,0,64,
  	63,1,0,0,0,64,65,1,0,0,0,65,69,1,0,0,0,66,68,3,40,20,0,67,66,1,0,0,0,
  	68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,
  	72,74,3,50,25,0,73,72,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,77,3,28,
  	14,0,76,75,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,80,5,38,0,0,79,78,1,
  	0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,83,3,18,9,0,82,81,1,0,0,0,82,83,
  	1,0,0,0,83,85,1,0,0,0,84,86,3,32,16,0,85,84,1,0,0,0,85,86,1,0,0,0,86,
  	88,1,0,0,0,87,89,3,30,15,0,88,87,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,
  	90,92,3,34,17,0,91,90,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,95,3,4,2,
  	0,94,93,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,98,3,36,18,0,97,96,1,0,
  	0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,101,3,38,19,0,100,99,1,0,0,0,100,
  	101,1,0,0,0,101,103,1,0,0,0,102,104,3,20,10,0,103,102,1,0,0,0,103,104,
  	1,0,0,0,104,105,1,0,0,0,105,106,5,12,0,0,106,158,1,0,0,0,107,108,5,9,
  	0,0,108,109,5,7,0,0,109,110,5,179,0,0,110,111,5,34,0,0,111,112,5,179,
  	0,0,112,114,3,6,3,0,113,115,3,42,21,0,114,113,1,0,0,0,114,115,1,0,0,0,
  	115,119,1,0,0,0,116,118,3,40,20,0,117,116,1,0,0,0,118,121,1,0,0,0,119,
  	117,1,0,0,0,119,120,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,122,124,3,
  	50,25,0,123,122,1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,127,3,28,
  	14,0,126,125,1,0,0,0,126,127,1,0,0,0,127,129,1,0,0,0,128,130,5,38,0,0,
  	129,128,1,0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,133,3,18,9,0,132,
  	131,1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,136,3,32,16,0,135,134,
  	1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,139,3,30,15,0,138,137,1,0,
  	0,0,138,139,1,0,0,0,139,141,1,0,0,0,140,142,3,34,17,0,141,140,1,0,0,0,
  	141,142,1,0,0,0,142,144,1,0,0,0,143,145,3,4,2,0,144,143,1,0,0,0,144,145,
  	1,0,0,0,145,147,1,0,0,0,146,148,3,36,18,0,147,146,1,0,0,0,147,148,1,0,
  	0,0,148,150,1,0,0,0,149,151,3,38,19,0,150,149,1,0,0,0,150,151,1,0,0,0,
  	151,153,1,0,0,0,152,154,3,20,10,0,153,152,1,0,0,0,153,154,1,0,0,0,154,
  	155,1,0,0,0,155,156,5,12,0,0,156,158,1,0,0,0,157,59,1,0,0,0,157,107,1,
  	0,0,0,158,3,1,0,0,0,159,160,5,24,0,0,160,169,3,54,27,0,161,162,5,24,0,
  	0,162,163,5,34,0,0,163,166,5,179,0,0,164,165,5,26,0,0,165,167,3,54,27,
  	0,166,164,1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,159,1,0,0,0,168,
  	161,1,0,0,0,169,5,1,0,0,0,170,172,3,8,4,0,171,170,1,0,0,0,171,172,1,0,
  	0,0,172,174,1,0,0,0,173,175,3,10,5,0,174,173,1,0,0,0,174,175,1,0,0,0,
  	175,177,1,0,0,0,176,178,3,12,6,0,177,176,1,0,0,0,177,178,1,0,0,0,178,
  	7,1,0,0,0,179,180,5,11,0,0,180,181,5,19,0,0,181,182,3,14,7,0,182,9,1,
  	0,0,0,183,184,5,23,0,0,184,185,5,19,0,0,185,186,3,14,7,0,186,11,1,0,0,
  	0,187,188,7,0,0,0,188,189,5,19,0,0,189,190,3,14,7,0,190,13,1,0,0,0,191,
  	200,5,132,0,0,192,197,3,16,8,0,193,194,5,169,0,0,194,196,3,16,8,0,195,
  	193,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,201,1,
  	0,0,0,199,197,1,0,0,0,200,192,1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,
  	202,203,5,133,0,0,203,15,1,0,0,0,204,206,5,78,0,0,205,204,1,0,0,0,205,
  	206,1,0,0,0,206,207,1,0,0,0,207,213,5,179,0,0,208,211,5,148,0,0,209,212,
  	3,48,24,0,210,212,5,1,0,0,211,209,1,0,0,0,211,210,1,0,0,0,212,214,1,0,
  	0,0,213,208,1,0,0,0,213,214,1,0,0,0,214,274,1,0,0,0,215,216,5,93,0,0,
  	216,222,5,179,0,0,217,220,5,148,0,0,218,221,3,48,24,0,219,221,5,1,0,0,
  	220,218,1,0,0,0,220,219,1,0,0,0,221,223,1,0,0,0,222,217,1,0,0,0,222,223,
  	1,0,0,0,223,274,1,0,0,0,224,228,5,43,0,0,225,226,5,66,0,0,226,228,5,140,
  	0,0,227,224,1,0,0,0,227,225,1,0,0,0,228,229,1,0,0,0,229,232,5,179,0,0,
  	230,231,5,148,0,0,231,233,7,1,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,
  	274,1,0,0,0,234,235,5,44,0,0,235,243,5,179,0,0,236,241,5,148,0,0,237,
  	242,5,179,0,0,238,242,3,44,22,0,239,242,5,48,0,0,240,242,5,1,0,0,241,
  	237,1,0,0,0,241,238,1,0,0,0,241,239,1,0,0,0,241,240,1,0,0,0,242,244,1,
  	0,0,0,243,236,1,0,0,0,243,244,1,0,0,0,244,274,1,0,0,0,245,246,5,45,0,
  	0,246,247,5,179,0,0,247,248,5,148,0,0,248,274,3,48,24,0,249,250,5,78,
  	0,0,250,251,5,140,0,0,251,259,5,179,0,0,252,257,5,148,0,0,253,258,5,179,
  	0,0,254,258,3,44,22,0,255,258,5,48,0,0,256,258,5,1,0,0,257,253,1,0,0,
  	0,257,254,1,0,0,0,257,255,1,0,0,0,257,256,1,0,0,0,258,260,1,0,0,0,259,
  	252,1,0,0,0,259,260,1,0,0,0,260,274,1,0,0,0,261,262,5,93,0,0,262,263,
  	5,140,0,0,263,271,5,179,0,0,264,269,5,148,0,0,265,270,5,179,0,0,266,270,
  	3,44,22,0,267,270,5,48,0,0,268,270,5,1,0,0,269,265,1,0,0,0,269,266,1,
  	0,0,0,269,267,1,0,0,0,269,268,1,0,0,0,270,272,1,0,0,0,271,264,1,0,0,0,
  	271,272,1,0,0,0,272,274,1,0,0,0,273,205,1,0,0,0,273,215,1,0,0,0,273,227,
  	1,0,0,0,273,234,1,0,0,0,273,245,1,0,0,0,273,249,1,0,0,0,273,261,1,0,0,
  	0,274,17,1,0,0,0,275,276,5,25,0,0,276,285,3,54,27,0,277,278,5,25,0,0,
  	278,279,5,34,0,0,279,282,5,179,0,0,280,281,5,26,0,0,281,283,3,54,27,0,
  	282,280,1,0,0,0,282,283,1,0,0,0,283,285,1,0,0,0,284,275,1,0,0,0,284,277,
  	1,0,0,0,285,19,1,0,0,0,286,287,5,13,0,0,287,296,3,54,27,0,288,289,5,13,
  	0,0,289,290,5,34,0,0,290,293,5,179,0,0,291,292,5,26,0,0,292,294,3,54,
  	27,0,293,291,1,0,0,0,293,294,1,0,0,0,294,296,1,0,0,0,295,286,1,0,0,0,
  	295,288,1,0,0,0,296,21,1,0,0,0,297,301,5,22,0,0,298,299,5,132,0,0,299,
  	300,5,49,0,0,300,302,5,133,0,0,301,298,1,0,0,0,301,302,1,0,0,0,302,305,
  	1,0,0,0,303,305,5,179,0,0,304,297,1,0,0,0,304,303,1,0,0,0,305,23,1,0,
  	0,0,306,307,5,132,0,0,307,308,3,48,24,0,308,309,5,169,0,0,309,310,3,48,
  	24,0,310,311,5,169,0,0,311,312,3,48,24,0,312,313,5,133,0,0,313,25,1,0,
  	0,0,314,321,5,4,0,0,315,318,5,20,0,0,316,319,5,4,0,0,317,319,3,22,11,
  	0,318,316,1,0,0,0,318,317,1,0,0,0,319,321,1,0,0,0,320,314,1,0,0,0,320,
  	315,1,0,0,0,321,27,1,0,0,0,322,323,5,39,0,0,323,324,5,52,0,0,324,29,1,
  	0,0,0,325,326,5,10,0,0,326,335,3,54,27,0,327,328,5,10,0,0,328,329,5,34,
  	0,0,329,332,5,179,0,0,330,331,5,26,0,0,331,333,3,54,27,0,332,330,1,0,
  	0,0,332,333,1,0,0,0,333,335,1,0,0,0,334,325,1,0,0,0,334,327,1,0,0,0,335,
  	31,1,0,0,0,336,337,5,8,0,0,337,338,3,54,27,0,338,33,1,0,0,0,339,340,5,
  	15,0,0,340,349,3,54,27,0,341,342,5,15,0,0,342,343,5,34,0,0,343,346,5,
  	179,0,0,344,345,5,26,0,0,345,347,3,54,27,0,346,344,1,0,0,0,346,347,1,
  	0,0,0,347,349,1,0,0,0,348,339,1,0,0,0,348,341,1,0,0,0,349,35,1,0,0,0,
  	350,351,5,28,0,0,351,360,3,54,27,0,352,353,5,28,0,0,353,354,5,34,0,0,
  	354,357,5,179,0,0,355,356,5,26,0,0,356,358,3,54,27,0,357,355,1,0,0,0,
  	357,358,1,0,0,0,358,360,1,0,0,0,359,350,1,0,0,0,359,352,1,0,0,0,360,37,
  	1,0,0,0,361,362,5,14,0,0,362,371,3,54,27,0,363,364,5,14,0,0,364,365,5,
  	34,0,0,365,368,5,179,0,0,366,367,5,26,0,0,367,369,3,54,27,0,368,366,1,
  	0,0,0,368,369,1,0,0,0,369,371,1,0,0,0,370,361,1,0,0,0,370,363,1,0,0,0,
  	371,39,1,0,0,0,372,373,5,42,0,0,373,374,7,2,0,0,374,375,7,2,0,0,375,376,
  	3,54,27,0,376,41,1,0,0,0,377,378,5,6,0,0,378,379,7,2,0,0,379,43,1,0,0,
  	0,380,381,5,136,0,0,381,386,3,48,24,0,382,383,5,169,0,0,383,385,3,48,
  	24,0,384,382,1,0,0,0,385,388,1,0,0,0,386,384,1,0,0,0,386,387,1,0,0,0,
  	387,389,1,0,0,0,388,386,1,0,0,0,389,390,5,137,0,0,390,45,1,0,0,0,391,
  	392,5,179,0,0,392,393,5,148,0,0,393,394,3,48,24,0,394,47,1,0,0,0,395,
  	396,6,24,-1,0,396,440,5,1,0,0,397,440,5,49,0,0,398,440,5,51,0,0,399,401,
  	5,52,0,0,400,399,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,403,1,0,
  	0,0,403,440,1,0,0,0,404,402,1,0,0,0,405,406,5,179,0,0,406,407,5,171,0,
  	0,407,440,3,48,24,23,408,409,5,179,0,0,409,410,5,176,0,0,410,440,3,48,
  	24,22,411,412,5,179,0,0,412,413,5,134,0,0,413,414,3,48,24,0,414,415,5,
  	135,0,0,415,440,1,0,0,0,416,417,5,179,0,0,417,418,5,132,0,0,418,423,3,
  	48,24,0,419,420,5,169,0,0,420,422,3,48,24,0,421,419,1,0,0,0,422,425,1,
  	0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,426,1,0,0,0,425,423,1,0,0,0,
  	426,427,5,133,0,0,427,440,1,0,0,0,428,429,5,132,0,0,429,430,3,48,24,0,
  	430,431,5,133,0,0,431,440,1,0,0,0,432,433,7,3,0,0,433,440,3,48,24,18,
  	434,440,5,179,0,0,435,436,5,147,0,0,436,440,3,48,24,5,437,440,5,22,0,
  	0,438,440,5,33,0,0,439,395,1,0,0,0,439,397,1,0,0,0,439,398,1,0,0,0,439,
  	402,1,0,0,0,439,405,1,0,0,0,439,408,1,0,0,0,439,411,1,0,0,0,439,416,1,
  	0,0,0,439,428,1,0,0,0,439,432,1,0,0,0,439,434,1,0,0,0,439,435,1,0,0,0,
  	439,437,1,0,0,0,439,438,1,0,0,0,440,485,1,0,0,0,441,442,10,17,0,0,442,
  	443,5,143,0,0,443,484,3,48,24,17,444,445,10,16,0,0,445,446,7,4,0,0,446,
  	484,3,48,24,17,447,448,10,15,0,0,448,449,7,3,0,0,449,484,3,48,24,16,450,
  	451,10,14,0,0,451,452,5,142,0,0,452,484,3,48,24,15,453,454,10,13,0,0,
  	454,455,5,2,0,0,455,484,3,48,24,14,456,457,10,12,0,0,457,458,5,3,0,0,
  	458,484,3,48,24,13,459,460,10,10,0,0,460,461,5,161,0,0,461,484,3,48,24,
  	11,462,463,10,9,0,0,463,464,5,163,0,0,464,484,3,48,24,10,465,466,10,8,
  	0,0,466,467,5,164,0,0,467,484,3,48,24,9,468,469,10,7,0,0,469,470,5,149,
  	0,0,470,484,3,48,24,8,471,472,10,6,0,0,472,473,5,150,0,0,473,484,3,48,
  	24,7,474,475,10,4,0,0,475,476,7,5,0,0,476,484,3,48,24,5,477,478,10,3,
  	0,0,478,479,5,172,0,0,479,480,3,48,24,0,480,481,5,173,0,0,481,482,3,48,
  	24,4,482,484,1,0,0,0,483,441,1,0,0,0,483,444,1,0,0,0,483,447,1,0,0,0,
  	483,450,1,0,0,0,483,453,1,0,0,0,483,456,1,0,0,0,483,459,1,0,0,0,483,462,
  	1,0,0,0,483,465,1,0,0,0,483,468,1,0,0,0,483,471,1,0,0,0,483,474,1,0,0,
  	0,483,477,1,0,0,0,484,487,1,0,0,0,485,483,1,0,0,0,485,486,1,0,0,0,486,
  	49,1,0,0,0,487,485,1,0,0,0,488,489,5,40,0,0,489,490,5,52,0,0,490,51,1,
  	0,0,0,491,492,5,41,0,0,492,497,5,52,0,0,493,494,5,41,0,0,494,495,5,40,
  	0,0,495,497,5,52,0,0,496,491,1,0,0,0,496,493,1,0,0,0,497,53,1,0,0,0,498,
  	499,5,46,0,0,499,55,1,0,0,0,71,64,69,73,76,79,82,85,88,91,94,97,100,103,
  	114,119,123,126,129,132,135,138,141,144,147,150,153,157,166,168,171,174,
  	177,197,200,205,211,213,220,222,227,232,241,243,257,259,269,271,273,282,
  	284,293,295,301,304,318,320,332,334,346,348,357,359,368,370,386,402,423,
  	439,483,485,496
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  mccompParserStaticData = std::move(staticData);
}

}

McCompParser::McCompParser(TokenStream *input) : McCompParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

McCompParser::McCompParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  McCompParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *mccompParserStaticData->atn, mccompParserStaticData->decisionToDFA, mccompParserStaticData->sharedContextCache, options);
}

McCompParser::~McCompParser() {
  delete _interpreter;
}

const atn::ATN& McCompParser::getATN() const {
  return *mccompParserStaticData->atn;
}

std::string McCompParser::getGrammarFileName() const {
  return "McComp.g4";
}

const std::vector<std::string>& McCompParser::getRuleNames() const {
  return mccompParserStaticData->ruleNames;
}

const dfa::Vocabulary& McCompParser::getVocabulary() const {
  return mccompParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView McCompParser::getSerializedATN() const {
  return mccompParserStaticData->serializedATN;
}


//----------------- ProgContext ------------------------------------------------------------------

McCompParser::ProgContext::ProgContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

McCompParser::Component_definitionContext* McCompParser::ProgContext::component_definition() {
  return getRuleContext<McCompParser::Component_definitionContext>(0);
}

tree::TerminalNode* McCompParser::ProgContext::EOF() {
  return getToken(McCompParser::EOF, 0);
}


size_t McCompParser::ProgContext::getRuleIndex() const {
  return McCompParser::RuleProg;
}


std::any McCompParser::ProgContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitProg(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::ProgContext* McCompParser::prog() {
  ProgContext *_localctx = _tracker.createInstance<ProgContext>(_ctx, getState());
  enterRule(_localctx, 0, McCompParser::RuleProg);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(56);
    component_definition();
    setState(57);
    match(McCompParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_definitionContext ------------------------------------------------------------------

McCompParser::Component_definitionContext::Component_definitionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::Component_definitionContext::getRuleIndex() const {
  return McCompParser::RuleComponent_definition;
}

void McCompParser::Component_definitionContext::copyFrom(Component_definitionContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- ComponentDefineNewContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ComponentDefineNewContext::Define() {
  return getToken(McCompParser::Define, 0);
}

tree::TerminalNode* McCompParser::ComponentDefineNewContext::Component() {
  return getToken(McCompParser::Component, 0);
}

tree::TerminalNode* McCompParser::ComponentDefineNewContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

McCompParser::Component_parameter_setContext* McCompParser::ComponentDefineNewContext::component_parameter_set() {
  return getRuleContext<McCompParser::Component_parameter_setContext>(0);
}

tree::TerminalNode* McCompParser::ComponentDefineNewContext::End() {
  return getToken(McCompParser::End, 0);
}

McCompParser::CategoryContext* McCompParser::ComponentDefineNewContext::category() {
  return getRuleContext<McCompParser::CategoryContext>(0);
}

std::vector<McCompParser::MetadataContext *> McCompParser::ComponentDefineNewContext::metadata() {
  return getRuleContexts<McCompParser::MetadataContext>();
}

McCompParser::MetadataContext* McCompParser::ComponentDefineNewContext::metadata(size_t i) {
  return getRuleContext<McCompParser::MetadataContext>(i);
}

McCompParser::ShellContext* McCompParser::ComponentDefineNewContext::shell() {
  return getRuleContext<McCompParser::ShellContext>(0);
}

McCompParser::DependencyContext* McCompParser::ComponentDefineNewContext::dependency() {
  return getRuleContext<McCompParser::DependencyContext>(0);
}

tree::TerminalNode* McCompParser::ComponentDefineNewContext::NoAcc() {
  return getToken(McCompParser::NoAcc, 0);
}

McCompParser::ShareContext* McCompParser::ComponentDefineNewContext::share() {
  return getRuleContext<McCompParser::ShareContext>(0);
}

McCompParser::UservarsContext* McCompParser::ComponentDefineNewContext::uservars() {
  return getRuleContext<McCompParser::UservarsContext>(0);
}

McCompParser::DeclareContext* McCompParser::ComponentDefineNewContext::declare() {
  return getRuleContext<McCompParser::DeclareContext>(0);
}

McCompParser::InitializeContext* McCompParser::ComponentDefineNewContext::initialize() {
  return getRuleContext<McCompParser::InitializeContext>(0);
}

McCompParser::Component_traceContext* McCompParser::ComponentDefineNewContext::component_trace() {
  return getRuleContext<McCompParser::Component_traceContext>(0);
}

McCompParser::SaveContext* McCompParser::ComponentDefineNewContext::save() {
  return getRuleContext<McCompParser::SaveContext>(0);
}

McCompParser::Finally_Context* McCompParser::ComponentDefineNewContext::finally_() {
  return getRuleContext<McCompParser::Finally_Context>(0);
}

McCompParser::DisplayContext* McCompParser::ComponentDefineNewContext::display() {
  return getRuleContext<McCompParser::DisplayContext>(0);
}

McCompParser::ComponentDefineNewContext::ComponentDefineNewContext(Component_definitionContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ComponentDefineNewContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponentDefineNew(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ComponentDefineCopyContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ComponentDefineCopyContext::Define() {
  return getToken(McCompParser::Define, 0);
}

tree::TerminalNode* McCompParser::ComponentDefineCopyContext::Component() {
  return getToken(McCompParser::Component, 0);
}

std::vector<tree::TerminalNode *> McCompParser::ComponentDefineCopyContext::Identifier() {
  return getTokens(McCompParser::Identifier);
}

tree::TerminalNode* McCompParser::ComponentDefineCopyContext::Identifier(size_t i) {
  return getToken(McCompParser::Identifier, i);
}

tree::TerminalNode* McCompParser::ComponentDefineCopyContext::Copy() {
  return getToken(McCompParser::Copy, 0);
}

McCompParser::Component_parameter_setContext* McCompParser::ComponentDefineCopyContext::component_parameter_set() {
  return getRuleContext<McCompParser::Component_parameter_setContext>(0);
}

tree::TerminalNode* McCompParser::ComponentDefineCopyContext::End() {
  return getToken(McCompParser::End, 0);
}

McCompParser::CategoryContext* McCompParser::ComponentDefineCopyContext::category() {
  return getRuleContext<McCompParser::CategoryContext>(0);
}

std::vector<McCompParser::MetadataContext *> McCompParser::ComponentDefineCopyContext::metadata() {
  return getRuleContexts<McCompParser::MetadataContext>();
}

McCompParser::MetadataContext* McCompParser::ComponentDefineCopyContext::metadata(size_t i) {
  return getRuleContext<McCompParser::MetadataContext>(i);
}

McCompParser::ShellContext* McCompParser::ComponentDefineCopyContext::shell() {
  return getRuleContext<McCompParser::ShellContext>(0);
}

McCompParser::DependencyContext* McCompParser::ComponentDefineCopyContext::dependency() {
  return getRuleContext<McCompParser::DependencyContext>(0);
}

tree::TerminalNode* McCompParser::ComponentDefineCopyContext::NoAcc() {
  return getToken(McCompParser::NoAcc, 0);
}

McCompParser::ShareContext* McCompParser::ComponentDefineCopyContext::share() {
  return getRuleContext<McCompParser::ShareContext>(0);
}

McCompParser::UservarsContext* McCompParser::ComponentDefineCopyContext::uservars() {
  return getRuleContext<McCompParser::UservarsContext>(0);
}

McCompParser::DeclareContext* McCompParser::ComponentDefineCopyContext::declare() {
  return getRuleContext<McCompParser::DeclareContext>(0);
}

McCompParser::InitializeContext* McCompParser::ComponentDefineCopyContext::initialize() {
  return getRuleContext<McCompParser::InitializeContext>(0);
}

McCompParser::Component_traceContext* McCompParser::ComponentDefineCopyContext::component_trace() {
  return getRuleContext<McCompParser::Component_traceContext>(0);
}

McCompParser::SaveContext* McCompParser::ComponentDefineCopyContext::save() {
  return getRuleContext<McCompParser::SaveContext>(0);
}

McCompParser::Finally_Context* McCompParser::ComponentDefineCopyContext::finally_() {
  return getRuleContext<McCompParser::Finally_Context>(0);
}

McCompParser::DisplayContext* McCompParser::ComponentDefineCopyContext::display() {
  return getRuleContext<McCompParser::DisplayContext>(0);
}

McCompParser::ComponentDefineCopyContext::ComponentDefineCopyContext(Component_definitionContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ComponentDefineCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponentDefineCopy(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::Component_definitionContext* McCompParser::component_definition() {
  Component_definitionContext *_localctx = _tracker.createInstance<Component_definitionContext>(_ctx, getState());
  enterRule(_localctx, 2, McCompParser::RuleComponent_definition);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(157);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::ComponentDefineNewContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(59);
      match(McCompParser::Define);
      setState(60);
      match(McCompParser::Component);
      setState(61);
      match(McCompParser::Identifier);
      setState(62);
      component_parameter_set();
      setState(64);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Category) {
        setState(63);
        category();
      }
      setState(69);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == McCompParser::MetaData) {
        setState(66);
        metadata();
        setState(71);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(73);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Shell) {
        setState(72);
        shell();
      }
      setState(76);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Dependency) {
        setState(75);
        dependency();
      }
      setState(79);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::NoAcc) {
        setState(78);
        match(McCompParser::NoAcc);
      }
      setState(82);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Share) {
        setState(81);
        share();
      }
      setState(85);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::UserVars) {
        setState(84);
        uservars();
      }
      setState(88);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Declare) {
        setState(87);
        declare();
      }
      setState(91);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Initialize) {
        setState(90);
        initialize();
      }
      setState(94);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Trace) {
        setState(93);
        component_trace();
      }
      setState(97);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Save) {
        setState(96);
        save();
      }
      setState(100);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Finally) {
        setState(99);
        finally_();
      }
      setState(103);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::McDisplay) {
        setState(102);
        display();
      }
      setState(105);
      match(McCompParser::End);
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::ComponentDefineCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(107);
      match(McCompParser::Define);
      setState(108);
      match(McCompParser::Component);
      setState(109);
      match(McCompParser::Identifier);
      setState(110);
      match(McCompParser::Copy);
      setState(111);
      match(McCompParser::Identifier);
      setState(112);
      component_parameter_set();
      setState(114);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Category) {
        setState(113);
        category();
      }
      setState(119);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == McCompParser::MetaData) {
        setState(116);
        metadata();
        setState(121);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(123);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Shell) {
        setState(122);
        shell();
      }
      setState(126);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Dependency) {
        setState(125);
        dependency();
      }
      setState(129);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::NoAcc) {
        setState(128);
        match(McCompParser::NoAcc);
      }
      setState(132);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Share) {
        setState(131);
        share();
      }
      setState(135);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::UserVars) {
        setState(134);
        uservars();
      }
      setState(138);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Declare) {
        setState(137);
        declare();
      }
      setState(141);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Initialize) {
        setState(140);
        initialize();
      }
      setState(144);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Trace) {
        setState(143);
        component_trace();
      }
      setState(147);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Save) {
        setState(146);
        save();
      }
      setState(150);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Finally) {
        setState(149);
        finally_();
      }
      setState(153);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::McDisplay) {
        setState(152);
        display();
      }
      setState(155);
      match(McCompParser::End);
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_traceContext ------------------------------------------------------------------

McCompParser::Component_traceContext::Component_traceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::Component_traceContext::getRuleIndex() const {
  return McCompParser::RuleComponent_trace;
}

void McCompParser::Component_traceContext::copyFrom(Component_traceContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- TraceBlockContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::TraceBlockContext::Trace() {
  return getToken(McCompParser::Trace, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::TraceBlockContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::TraceBlockContext::TraceBlockContext(Component_traceContext *ctx) { copyFrom(ctx); }


std::any McCompParser::TraceBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitTraceBlock(this);
  else
    return visitor->visitChildren(this);
}
//----------------- TraceBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::TraceBlockCopyContext::Trace() {
  return getToken(McCompParser::Trace, 0);
}

tree::TerminalNode* McCompParser::TraceBlockCopyContext::Copy() {
  return getToken(McCompParser::Copy, 0);
}

tree::TerminalNode* McCompParser::TraceBlockCopyContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::TraceBlockCopyContext::Extend() {
  return getToken(McCompParser::Extend, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::TraceBlockCopyContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::TraceBlockCopyContext::TraceBlockCopyContext(Component_traceContext *ctx) { copyFrom(ctx); }


std::any McCompParser::TraceBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitTraceBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::Component_traceContext* McCompParser::component_trace() {
  Component_traceContext *_localctx = _tracker.createInstance<Component_traceContext>(_ctx, getState());
  enterRule(_localctx, 4, McCompParser::RuleComponent_trace);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(168);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 28, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::TraceBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(159);
      match(McCompParser::Trace);
      setState(160);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::TraceBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(161);
      match(McCompParser::Trace);
      setState(162);
      match(McCompParser::Copy);
      setState(163);
      match(McCompParser::Identifier);
      setState(166);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Extend) {
        setState(164);
        match(McCompParser::Extend);
        setState(165);
        unparsed_block();
      }
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_parameter_setContext ------------------------------------------------------------------

McCompParser::Component_parameter_setContext::Component_parameter_setContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

McCompParser::Component_define_parametersContext* McCompParser::Component_parameter_setContext::component_define_parameters() {
  return getRuleContext<McCompParser::Component_define_parametersContext>(0);
}

McCompParser::Component_set_parametersContext* McCompParser::Component_parameter_setContext::component_set_parameters() {
  return getRuleContext<McCompParser::Component_set_parametersContext>(0);
}

McCompParser::Component_out_parametersContext* McCompParser::Component_parameter_setContext::component_out_parameters() {
  return getRuleContext<McCompParser::Component_out_parametersContext>(0);
}


size_t McCompParser::Component_parameter_setContext::getRuleIndex() const {
  return McCompParser::RuleComponent_parameter_set;
}


std::any McCompParser::Component_parameter_setContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponent_parameter_set(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::Component_parameter_setContext* McCompParser::component_parameter_set() {
  Component_parameter_setContext *_localctx = _tracker.createInstance<Component_parameter_setContext>(_ctx, getState());
  enterRule(_localctx, 6, McCompParser::RuleComponent_parameter_set);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(171);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McCompParser::Definition) {
      setState(170);
      component_define_parameters();
    }
    setState(174);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McCompParser::Setting) {
      setState(173);
      component_set_parameters();
    }
    setState(177);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McCompParser::Output

    || _la == McCompParser::Private) {
      setState(176);
      component_out_parameters();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_define_parametersContext ------------------------------------------------------------------

McCompParser::Component_define_parametersContext::Component_define_parametersContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::Component_define_parametersContext::Definition() {
  return getToken(McCompParser::Definition, 0);
}

tree::TerminalNode* McCompParser::Component_define_parametersContext::Parameters() {
  return getToken(McCompParser::Parameters, 0);
}

McCompParser::Component_parametersContext* McCompParser::Component_define_parametersContext::component_parameters() {
  return getRuleContext<McCompParser::Component_parametersContext>(0);
}


size_t McCompParser::Component_define_parametersContext::getRuleIndex() const {
  return McCompParser::RuleComponent_define_parameters;
}


std::any McCompParser::Component_define_parametersContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponent_define_parameters(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::Component_define_parametersContext* McCompParser::component_define_parameters() {
  Component_define_parametersContext *_localctx = _tracker.createInstance<Component_define_parametersContext>(_ctx, getState());
  enterRule(_localctx, 8, McCompParser::RuleComponent_define_parameters);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(179);
    match(McCompParser::Definition);
    setState(180);
    match(McCompParser::Parameters);
    setState(181);
    component_parameters();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_set_parametersContext ------------------------------------------------------------------

McCompParser::Component_set_parametersContext::Component_set_parametersContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::Component_set_parametersContext::Setting() {
  return getToken(McCompParser::Setting, 0);
}

tree::TerminalNode* McCompParser::Component_set_parametersContext::Parameters() {
  return getToken(McCompParser::Parameters, 0);
}

McCompParser::Component_parametersContext* McCompParser::Component_set_parametersContext::component_parameters() {
  return getRuleContext<McCompParser::Component_parametersContext>(0);
}


size_t McCompParser::Component_set_parametersContext::getRuleIndex() const {
  return McCompParser::RuleComponent_set_parameters;
}


std::any McCompParser::Component_set_parametersContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponent_set_parameters(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::Component_set_parametersContext* McCompParser::component_set_parameters() {
  Component_set_parametersContext *_localctx = _tracker.createInstance<Component_set_parametersContext>(_ctx, getState());
  enterRule(_localctx, 10, McCompParser::RuleComponent_set_parameters);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(183);
    match(McCompParser::Setting);
    setState(184);
    match(McCompParser::Parameters);
    setState(185);
    component_parameters();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_out_parametersContext ------------------------------------------------------------------

McCompParser::Component_out_parametersContext::Component_out_parametersContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::Component_out_parametersContext::Parameters() {
  return getToken(McCompParser::Parameters, 0);
}

McCompParser::Component_parametersContext* McCompParser::Component_out_parametersContext::component_parameters() {
  return getRuleContext<McCompParser::Component_parametersContext>(0);
}

tree::TerminalNode* McCompParser::Component_out_parametersContext::Output() {
  return getToken(McCompParser::Output, 0);
}

tree::TerminalNode* McCompParser::Component_out_parametersContext::Private() {
  return getToken(McCompParser::Private, 0);
}


size_t McCompParser::Component_out_parametersContext::getRuleIndex() const {
  return McCompParser::RuleComponent_out_parameters;
}


std::any McCompParser::Component_out_parametersContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponent_out_parameters(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::Component_out_parametersContext* McCompParser::component_out_parameters() {
  Component_out_parametersContext *_localctx = _tracker.createInstance<Component_out_parametersContext>(_ctx, getState());
  enterRule(_localctx, 12, McCompParser::RuleComponent_out_parameters);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(187);
    _la = _input->LA(1);
    if (!(_la == McCompParser::Output

    || _la == McCompParser::Private)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(188);
    match(McCompParser::Parameters);
    setState(189);
    component_parameters();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_parametersContext ------------------------------------------------------------------

McCompParser::Component_parametersContext::Component_parametersContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::Component_parametersContext::LeftParen() {
  return getToken(McCompParser::LeftParen, 0);
}

tree::TerminalNode* McCompParser::Component_parametersContext::RightParen() {
  return getToken(McCompParser::RightParen, 0);
}

std::vector<McCompParser::Component_parameterContext *> McCompParser::Component_parametersContext::component_parameter() {
  return getRuleContexts<McCompParser::Component_parameterContext>();
}

McCompParser::Component_parameterContext* McCompParser::Component_parametersContext::component_parameter(size_t i) {
  return getRuleContext<McCompParser::Component_parameterContext>(i);
}

std::vector<tree::TerminalNode *> McCompParser::Component_parametersContext::Comma() {
  return getTokens(McCompParser::Comma);
}

tree::TerminalNode* McCompParser::Component_parametersContext::Comma(size_t i) {
  return getToken(McCompParser::Comma, i);
}


size_t McCompParser::Component_parametersContext::getRuleIndex() const {
  return McCompParser::RuleComponent_parameters;
}


std::any McCompParser::Component_parametersContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponent_parameters(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::Component_parametersContext* McCompParser::component_parameters() {
  Component_parametersContext *_localctx = _tracker.createInstance<Component_parametersContext>(_ctx, getState());
  enterRule(_localctx, 14, McCompParser::RuleComponent_parameters);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(191);
    match(McCompParser::LeftParen);
    setState(200);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (((((_la - 43) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 43)) & 1125934274969607) != 0) || _la == McCompParser::Identifier) {
      setState(192);
      component_parameter();
      setState(197);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == McCompParser::Comma) {
        setState(193);
        match(McCompParser::Comma);
        setState(194);
        component_parameter();
        setState(199);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(202);
    match(McCompParser::RightParen);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_parameterContext ------------------------------------------------------------------

McCompParser::Component_parameterContext::Component_parameterContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::Component_parameterContext::getRuleIndex() const {
  return McCompParser::RuleComponent_parameter;
}

void McCompParser::Component_parameterContext::copyFrom(Component_parameterContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- ComponentParameterSymbolContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ComponentParameterSymbolContext::Symbol() {
  return getToken(McCompParser::Symbol, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterSymbolContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterSymbolContext::Assign() {
  return getToken(McCompParser::Assign, 0);
}

McCompParser::ExprContext* McCompParser::ComponentParameterSymbolContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}

McCompParser::ComponentParameterSymbolContext::ComponentParameterSymbolContext(Component_parameterContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ComponentParameterSymbolContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponentParameterSymbol(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ComponentParameterDoubleArrayContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ComponentParameterDoubleArrayContext::Double() {
  return getToken(McCompParser::Double, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterDoubleArrayContext::Star() {
  return getToken(McCompParser::Star, 0);
}

std::vector<tree::TerminalNode *> McCompParser::ComponentParameterDoubleArrayContext::Identifier() {
  return getTokens(McCompParser::Identifier);
}

tree::TerminalNode* McCompParser::ComponentParameterDoubleArrayContext::Identifier(size_t i) {
  return getToken(McCompParser::Identifier, i);
}

tree::TerminalNode* McCompParser::ComponentParameterDoubleArrayContext::Assign() {
  return getToken(McCompParser::Assign, 0);
}

McCompParser::InitializerlistContext* McCompParser::ComponentParameterDoubleArrayContext::initializerlist() {
  return getRuleContext<McCompParser::InitializerlistContext>(0);
}

tree::TerminalNode* McCompParser::ComponentParameterDoubleArrayContext::Null() {
  return getToken(McCompParser::Null, 0);
}

McCompParser::ComponentParameterDoubleArrayContext::ComponentParameterDoubleArrayContext(Component_parameterContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ComponentParameterDoubleArrayContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponentParameterDoubleArray(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ComponentParameterDoubleContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ComponentParameterDoubleContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterDoubleContext::Double() {
  return getToken(McCompParser::Double, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterDoubleContext::Assign() {
  return getToken(McCompParser::Assign, 0);
}

McCompParser::ExprContext* McCompParser::ComponentParameterDoubleContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}

McCompParser::ComponentParameterDoubleContext::ComponentParameterDoubleContext(Component_parameterContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ComponentParameterDoubleContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponentParameterDouble(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ComponentParameterVectorContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ComponentParameterVectorContext::Vector() {
  return getToken(McCompParser::Vector, 0);
}

std::vector<tree::TerminalNode *> McCompParser::ComponentParameterVectorContext::Identifier() {
  return getTokens(McCompParser::Identifier);
}

tree::TerminalNode* McCompParser::ComponentParameterVectorContext::Identifier(size_t i) {
  return getToken(McCompParser::Identifier, i);
}

tree::TerminalNode* McCompParser::ComponentParameterVectorContext::Assign() {
  return getToken(McCompParser::Assign, 0);
}

McCompParser::InitializerlistContext* McCompParser::ComponentParameterVectorContext::initializerlist() {
  return getRuleContext<McCompParser::InitializerlistContext>(0);
}

tree::TerminalNode* McCompParser::ComponentParameterVectorContext::Null() {
  return getToken(McCompParser::Null, 0);
}

McCompParser::ComponentParameterVectorContext::ComponentParameterVectorContext(Component_parameterContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ComponentParameterVectorContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponentParameterVector(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ComponentParameterIntegerContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ComponentParameterIntegerContext::Int() {
  return getToken(McCompParser::Int, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterIntegerContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterIntegerContext::Assign() {
  return getToken(McCompParser::Assign, 0);
}

McCompParser::ExprContext* McCompParser::ComponentParameterIntegerContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}

McCompParser::ComponentParameterIntegerContext::ComponentParameterIntegerContext(Component_parameterContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ComponentParameterIntegerContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponentParameterInteger(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ComponentParameterIntegerArrayContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ComponentParameterIntegerArrayContext::Int() {
  return getToken(McCompParser::Int, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterIntegerArrayContext::Star() {
  return getToken(McCompParser::Star, 0);
}

std::vector<tree::TerminalNode *> McCompParser::ComponentParameterIntegerArrayContext::Identifier() {
  return getTokens(McCompParser::Identifier);
}

tree::TerminalNode* McCompParser::ComponentParameterIntegerArrayContext::Identifier(size_t i) {
  return getToken(McCompParser::Identifier, i);
}

tree::TerminalNode* McCompParser::ComponentParameterIntegerArrayContext::Assign() {
  return getToken(McCompParser::Assign, 0);
}

McCompParser::InitializerlistContext* McCompParser::ComponentParameterIntegerArrayContext::initializerlist() {
  return getRuleContext<McCompParser::InitializerlistContext>(0);
}

tree::TerminalNode* McCompParser::ComponentParameterIntegerArrayContext::Null() {
  return getToken(McCompParser::Null, 0);
}

McCompParser::ComponentParameterIntegerArrayContext::ComponentParameterIntegerArrayContext(Component_parameterContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ComponentParameterIntegerArrayContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponentParameterIntegerArray(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ComponentParameterStringContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ComponentParameterStringContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterStringContext::String() {
  return getToken(McCompParser::String, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterStringContext::Assign() {
  return getToken(McCompParser::Assign, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterStringContext::Char() {
  return getToken(McCompParser::Char, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterStringContext::Star() {
  return getToken(McCompParser::Star, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterStringContext::StringLiteral() {
  return getToken(McCompParser::StringLiteral, 0);
}

tree::TerminalNode* McCompParser::ComponentParameterStringContext::Null() {
  return getToken(McCompParser::Null, 0);
}

McCompParser::ComponentParameterStringContext::ComponentParameterStringContext(Component_parameterContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ComponentParameterStringContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponentParameterString(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::Component_parameterContext* McCompParser::component_parameter() {
  Component_parameterContext *_localctx = _tracker.createInstance<Component_parameterContext>(_ctx, getState());
  enterRule(_localctx, 16, McCompParser::RuleComponent_parameter);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(273);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 47, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::ComponentParameterDoubleContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(205);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Double) {
        setState(204);
        match(McCompParser::Double);
      }
      setState(207);
      match(McCompParser::Identifier);
      setState(213);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Assign) {
        setState(208);
        match(McCompParser::Assign);
        setState(211);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 35, _ctx)) {
        case 1: {
          setState(209);
          expr(0);
          break;
        }

        case 2: {
          setState(210);
          match(McCompParser::T__0);
          break;
        }

        default:
          break;
        }
      }
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::ComponentParameterIntegerContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(215);
      match(McCompParser::Int);
      setState(216);
      match(McCompParser::Identifier);
      setState(222);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Assign) {
        setState(217);
        match(McCompParser::Assign);
        setState(220);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx)) {
        case 1: {
          setState(218);
          expr(0);
          break;
        }

        case 2: {
          setState(219);
          match(McCompParser::T__0);
          break;
        }

        default:
          break;
        }
      }
      break;
    }

    case 3: {
      _localctx = _tracker.createInstance<McCompParser::ComponentParameterStringContext>(_localctx);
      enterOuterAlt(_localctx, 3);
      setState(227);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case McCompParser::String: {
          setState(224);
          match(McCompParser::String);
          break;
        }

        case McCompParser::Char: {
          setState(225);
          match(McCompParser::Char);
          setState(226);
          match(McCompParser::Star);
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(229);
      match(McCompParser::Identifier);
      setState(232);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Assign) {
        setState(230);
        match(McCompParser::Assign);
        setState(231);
        _la = _input->LA(1);
        if (!((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 4785074604081154) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
      }
      break;
    }

    case 4: {
      _localctx = _tracker.createInstance<McCompParser::ComponentParameterVectorContext>(_localctx);
      enterOuterAlt(_localctx, 4);
      setState(234);
      match(McCompParser::Vector);
      setState(235);
      match(McCompParser::Identifier);
      setState(243);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Assign) {
        setState(236);
        match(McCompParser::Assign);
        setState(241);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case McCompParser::Identifier: {
            setState(237);
            match(McCompParser::Identifier);
            break;
          }

          case McCompParser::LeftBrace: {
            setState(238);
            initializerlist();
            break;
          }

          case McCompParser::Null: {
            setState(239);
            match(McCompParser::Null);
            break;
          }

          case McCompParser::T__0: {
            setState(240);
            match(McCompParser::T__0);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
      }
      break;
    }

    case 5: {
      _localctx = _tracker.createInstance<McCompParser::ComponentParameterSymbolContext>(_localctx);
      enterOuterAlt(_localctx, 5);
      setState(245);
      match(McCompParser::Symbol);
      setState(246);
      match(McCompParser::Identifier);

      setState(247);
      match(McCompParser::Assign);
      setState(248);
      expr(0);
      break;
    }

    case 6: {
      _localctx = _tracker.createInstance<McCompParser::ComponentParameterDoubleArrayContext>(_localctx);
      enterOuterAlt(_localctx, 6);
      setState(249);
      match(McCompParser::Double);
      setState(250);
      match(McCompParser::Star);
      setState(251);
      match(McCompParser::Identifier);
      setState(259);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Assign) {
        setState(252);
        match(McCompParser::Assign);
        setState(257);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case McCompParser::Identifier: {
            setState(253);
            match(McCompParser::Identifier);
            break;
          }

          case McCompParser::LeftBrace: {
            setState(254);
            initializerlist();
            break;
          }

          case McCompParser::Null: {
            setState(255);
            match(McCompParser::Null);
            break;
          }

          case McCompParser::T__0: {
            setState(256);
            match(McCompParser::T__0);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
      }
      break;
    }

    case 7: {
      _localctx = _tracker.createInstance<McCompParser::ComponentParameterIntegerArrayContext>(_localctx);
      enterOuterAlt(_localctx, 7);
      setState(261);
      match(McCompParser::Int);
      setState(262);
      match(McCompParser::Star);
      setState(263);
      match(McCompParser::Identifier);
      setState(271);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Assign) {
        setState(264);
        match(McCompParser::Assign);
        setState(269);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case McCompParser::Identifier: {
            setState(265);
            match(McCompParser::Identifier);
            break;
          }

          case McCompParser::LeftBrace: {
            setState(266);
            initializerlist();
            break;
          }

          case McCompParser::Null: {
            setState(267);
            match(McCompParser::Null);
            break;
          }

          case McCompParser::T__0: {
            setState(268);
            match(McCompParser::T__0);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
      }
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ShareContext ------------------------------------------------------------------

McCompParser::ShareContext::ShareContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::ShareContext::getRuleIndex() const {
  return McCompParser::RuleShare;
}

void McCompParser::ShareContext::copyFrom(ShareContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- ShareBlockContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ShareBlockContext::Share() {
  return getToken(McCompParser::Share, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::ShareBlockContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::ShareBlockContext::ShareBlockContext(ShareContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ShareBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitShareBlock(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ShareBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ShareBlockCopyContext::Share() {
  return getToken(McCompParser::Share, 0);
}

tree::TerminalNode* McCompParser::ShareBlockCopyContext::Copy() {
  return getToken(McCompParser::Copy, 0);
}

tree::TerminalNode* McCompParser::ShareBlockCopyContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::ShareBlockCopyContext::Extend() {
  return getToken(McCompParser::Extend, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::ShareBlockCopyContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::ShareBlockCopyContext::ShareBlockCopyContext(ShareContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ShareBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitShareBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::ShareContext* McCompParser::share() {
  ShareContext *_localctx = _tracker.createInstance<ShareContext>(_ctx, getState());
  enterRule(_localctx, 18, McCompParser::RuleShare);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(284);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 49, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::ShareBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(275);
      match(McCompParser::Share);
      setState(276);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::ShareBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(277);
      match(McCompParser::Share);
      setState(278);
      match(McCompParser::Copy);
      setState(279);
      match(McCompParser::Identifier);
      setState(282);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Extend) {
        setState(280);
        match(McCompParser::Extend);
        setState(281);
        unparsed_block();
      }
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DisplayContext ------------------------------------------------------------------

McCompParser::DisplayContext::DisplayContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::DisplayContext::getRuleIndex() const {
  return McCompParser::RuleDisplay;
}

void McCompParser::DisplayContext::copyFrom(DisplayContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- DisplayBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::DisplayBlockCopyContext::McDisplay() {
  return getToken(McCompParser::McDisplay, 0);
}

tree::TerminalNode* McCompParser::DisplayBlockCopyContext::Copy() {
  return getToken(McCompParser::Copy, 0);
}

tree::TerminalNode* McCompParser::DisplayBlockCopyContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::DisplayBlockCopyContext::Extend() {
  return getToken(McCompParser::Extend, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::DisplayBlockCopyContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::DisplayBlockCopyContext::DisplayBlockCopyContext(DisplayContext *ctx) { copyFrom(ctx); }


std::any McCompParser::DisplayBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitDisplayBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
//----------------- DisplayBlockContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::DisplayBlockContext::McDisplay() {
  return getToken(McCompParser::McDisplay, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::DisplayBlockContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::DisplayBlockContext::DisplayBlockContext(DisplayContext *ctx) { copyFrom(ctx); }


std::any McCompParser::DisplayBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitDisplayBlock(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::DisplayContext* McCompParser::display() {
  DisplayContext *_localctx = _tracker.createInstance<DisplayContext>(_ctx, getState());
  enterRule(_localctx, 20, McCompParser::RuleDisplay);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(295);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 51, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::DisplayBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(286);
      match(McCompParser::McDisplay);
      setState(287);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::DisplayBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(288);
      match(McCompParser::McDisplay);
      setState(289);
      match(McCompParser::Copy);
      setState(290);
      match(McCompParser::Identifier);
      setState(293);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Extend) {
        setState(291);
        match(McCompParser::Extend);
        setState(292);
        unparsed_block();
      }
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_refContext ------------------------------------------------------------------

McCompParser::Component_refContext::Component_refContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::Component_refContext::Previous() {
  return getToken(McCompParser::Previous, 0);
}

tree::TerminalNode* McCompParser::Component_refContext::LeftParen() {
  return getToken(McCompParser::LeftParen, 0);
}

tree::TerminalNode* McCompParser::Component_refContext::IntegerLiteral() {
  return getToken(McCompParser::IntegerLiteral, 0);
}

tree::TerminalNode* McCompParser::Component_refContext::RightParen() {
  return getToken(McCompParser::RightParen, 0);
}

tree::TerminalNode* McCompParser::Component_refContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}


size_t McCompParser::Component_refContext::getRuleIndex() const {
  return McCompParser::RuleComponent_ref;
}


std::any McCompParser::Component_refContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitComponent_ref(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::Component_refContext* McCompParser::component_ref() {
  Component_refContext *_localctx = _tracker.createInstance<Component_refContext>(_ctx, getState());
  enterRule(_localctx, 22, McCompParser::RuleComponent_ref);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(304);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case McCompParser::Previous: {
        enterOuterAlt(_localctx, 1);
        setState(297);
        match(McCompParser::Previous);
        setState(301);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McCompParser::LeftParen) {
          setState(298);
          match(McCompParser::LeftParen);
          setState(299);
          match(McCompParser::IntegerLiteral);
          setState(300);
          match(McCompParser::RightParen);
        }
        break;
      }

      case McCompParser::Identifier: {
        enterOuterAlt(_localctx, 2);
        setState(303);
        match(McCompParser::Identifier);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CoordsContext ------------------------------------------------------------------

McCompParser::CoordsContext::CoordsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::CoordsContext::LeftParen() {
  return getToken(McCompParser::LeftParen, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::CoordsContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::CoordsContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

std::vector<tree::TerminalNode *> McCompParser::CoordsContext::Comma() {
  return getTokens(McCompParser::Comma);
}

tree::TerminalNode* McCompParser::CoordsContext::Comma(size_t i) {
  return getToken(McCompParser::Comma, i);
}

tree::TerminalNode* McCompParser::CoordsContext::RightParen() {
  return getToken(McCompParser::RightParen, 0);
}


size_t McCompParser::CoordsContext::getRuleIndex() const {
  return McCompParser::RuleCoords;
}


std::any McCompParser::CoordsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitCoords(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::CoordsContext* McCompParser::coords() {
  CoordsContext *_localctx = _tracker.createInstance<CoordsContext>(_ctx, getState());
  enterRule(_localctx, 24, McCompParser::RuleCoords);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(306);
    match(McCompParser::LeftParen);
    setState(307);
    expr(0);
    setState(308);
    match(McCompParser::Comma);
    setState(309);
    expr(0);
    setState(310);
    match(McCompParser::Comma);
    setState(311);
    expr(0);
    setState(312);
    match(McCompParser::RightParen);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ReferenceContext ------------------------------------------------------------------

McCompParser::ReferenceContext::ReferenceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::ReferenceContext::Absolute() {
  return getToken(McCompParser::Absolute, 0);
}

tree::TerminalNode* McCompParser::ReferenceContext::Relative() {
  return getToken(McCompParser::Relative, 0);
}

McCompParser::Component_refContext* McCompParser::ReferenceContext::component_ref() {
  return getRuleContext<McCompParser::Component_refContext>(0);
}


size_t McCompParser::ReferenceContext::getRuleIndex() const {
  return McCompParser::RuleReference;
}


std::any McCompParser::ReferenceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitReference(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::ReferenceContext* McCompParser::reference() {
  ReferenceContext *_localctx = _tracker.createInstance<ReferenceContext>(_ctx, getState());
  enterRule(_localctx, 26, McCompParser::RuleReference);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(320);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case McCompParser::Absolute: {
        enterOuterAlt(_localctx, 1);
        setState(314);
        match(McCompParser::Absolute);
        break;
      }

      case McCompParser::Relative: {
        enterOuterAlt(_localctx, 2);
        setState(315);
        match(McCompParser::Relative);
        setState(318);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case McCompParser::Absolute: {
            setState(316);
            match(McCompParser::Absolute);
            break;
          }

          case McCompParser::Previous:
          case McCompParser::Identifier: {
            setState(317);
            component_ref();
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DependencyContext ------------------------------------------------------------------

McCompParser::DependencyContext::DependencyContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::DependencyContext::Dependency() {
  return getToken(McCompParser::Dependency, 0);
}

tree::TerminalNode* McCompParser::DependencyContext::StringLiteral() {
  return getToken(McCompParser::StringLiteral, 0);
}


size_t McCompParser::DependencyContext::getRuleIndex() const {
  return McCompParser::RuleDependency;
}


std::any McCompParser::DependencyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitDependency(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::DependencyContext* McCompParser::dependency() {
  DependencyContext *_localctx = _tracker.createInstance<DependencyContext>(_ctx, getState());
  enterRule(_localctx, 28, McCompParser::RuleDependency);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(322);
    match(McCompParser::Dependency);
    setState(323);
    match(McCompParser::StringLiteral);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DeclareContext ------------------------------------------------------------------

McCompParser::DeclareContext::DeclareContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::DeclareContext::getRuleIndex() const {
  return McCompParser::RuleDeclare;
}

void McCompParser::DeclareContext::copyFrom(DeclareContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- DeclareBlockContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::DeclareBlockContext::Declare() {
  return getToken(McCompParser::Declare, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::DeclareBlockContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::DeclareBlockContext::DeclareBlockContext(DeclareContext *ctx) { copyFrom(ctx); }


std::any McCompParser::DeclareBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitDeclareBlock(this);
  else
    return visitor->visitChildren(this);
}
//----------------- DeclareBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::DeclareBlockCopyContext::Declare() {
  return getToken(McCompParser::Declare, 0);
}

tree::TerminalNode* McCompParser::DeclareBlockCopyContext::Copy() {
  return getToken(McCompParser::Copy, 0);
}

tree::TerminalNode* McCompParser::DeclareBlockCopyContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::DeclareBlockCopyContext::Extend() {
  return getToken(McCompParser::Extend, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::DeclareBlockCopyContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::DeclareBlockCopyContext::DeclareBlockCopyContext(DeclareContext *ctx) { copyFrom(ctx); }


std::any McCompParser::DeclareBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitDeclareBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::DeclareContext* McCompParser::declare() {
  DeclareContext *_localctx = _tracker.createInstance<DeclareContext>(_ctx, getState());
  enterRule(_localctx, 30, McCompParser::RuleDeclare);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(334);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::DeclareBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(325);
      match(McCompParser::Declare);
      setState(326);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::DeclareBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(327);
      match(McCompParser::Declare);
      setState(328);
      match(McCompParser::Copy);
      setState(329);
      match(McCompParser::Identifier);
      setState(332);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Extend) {
        setState(330);
        match(McCompParser::Extend);
        setState(331);
        unparsed_block();
      }
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- UservarsContext ------------------------------------------------------------------

McCompParser::UservarsContext::UservarsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::UservarsContext::UserVars() {
  return getToken(McCompParser::UserVars, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::UservarsContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}


size_t McCompParser::UservarsContext::getRuleIndex() const {
  return McCompParser::RuleUservars;
}


std::any McCompParser::UservarsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitUservars(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::UservarsContext* McCompParser::uservars() {
  UservarsContext *_localctx = _tracker.createInstance<UservarsContext>(_ctx, getState());
  enterRule(_localctx, 32, McCompParser::RuleUservars);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(336);
    match(McCompParser::UserVars);
    setState(337);
    unparsed_block();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- InitializeContext ------------------------------------------------------------------

McCompParser::InitializeContext::InitializeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::InitializeContext::getRuleIndex() const {
  return McCompParser::RuleInitialize;
}

void McCompParser::InitializeContext::copyFrom(InitializeContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- InitializeBlockContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::InitializeBlockContext::Initialize() {
  return getToken(McCompParser::Initialize, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::InitializeBlockContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::InitializeBlockContext::InitializeBlockContext(InitializeContext *ctx) { copyFrom(ctx); }


std::any McCompParser::InitializeBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitInitializeBlock(this);
  else
    return visitor->visitChildren(this);
}
//----------------- InitializeBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::InitializeBlockCopyContext::Initialize() {
  return getToken(McCompParser::Initialize, 0);
}

tree::TerminalNode* McCompParser::InitializeBlockCopyContext::Copy() {
  return getToken(McCompParser::Copy, 0);
}

tree::TerminalNode* McCompParser::InitializeBlockCopyContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::InitializeBlockCopyContext::Extend() {
  return getToken(McCompParser::Extend, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::InitializeBlockCopyContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::InitializeBlockCopyContext::InitializeBlockCopyContext(InitializeContext *ctx) { copyFrom(ctx); }


std::any McCompParser::InitializeBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitInitializeBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::InitializeContext* McCompParser::initialize() {
  InitializeContext *_localctx = _tracker.createInstance<InitializeContext>(_ctx, getState());
  enterRule(_localctx, 34, McCompParser::RuleInitialize);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(348);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::InitializeBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(339);
      match(McCompParser::Initialize);
      setState(340);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::InitializeBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(341);
      match(McCompParser::Initialize);
      setState(342);
      match(McCompParser::Copy);
      setState(343);
      match(McCompParser::Identifier);
      setState(346);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Extend) {
        setState(344);
        match(McCompParser::Extend);
        setState(345);
        unparsed_block();
      }
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SaveContext ------------------------------------------------------------------

McCompParser::SaveContext::SaveContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::SaveContext::getRuleIndex() const {
  return McCompParser::RuleSave;
}

void McCompParser::SaveContext::copyFrom(SaveContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- SaveBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::SaveBlockCopyContext::Save() {
  return getToken(McCompParser::Save, 0);
}

tree::TerminalNode* McCompParser::SaveBlockCopyContext::Copy() {
  return getToken(McCompParser::Copy, 0);
}

tree::TerminalNode* McCompParser::SaveBlockCopyContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::SaveBlockCopyContext::Extend() {
  return getToken(McCompParser::Extend, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::SaveBlockCopyContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::SaveBlockCopyContext::SaveBlockCopyContext(SaveContext *ctx) { copyFrom(ctx); }


std::any McCompParser::SaveBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitSaveBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
//----------------- SaveBlockContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::SaveBlockContext::Save() {
  return getToken(McCompParser::Save, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::SaveBlockContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::SaveBlockContext::SaveBlockContext(SaveContext *ctx) { copyFrom(ctx); }


std::any McCompParser::SaveBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitSaveBlock(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::SaveContext* McCompParser::save() {
  SaveContext *_localctx = _tracker.createInstance<SaveContext>(_ctx, getState());
  enterRule(_localctx, 36, McCompParser::RuleSave);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(359);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 61, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::SaveBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(350);
      match(McCompParser::Save);
      setState(351);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::SaveBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(352);
      match(McCompParser::Save);
      setState(353);
      match(McCompParser::Copy);
      setState(354);
      match(McCompParser::Identifier);
      setState(357);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Extend) {
        setState(355);
        match(McCompParser::Extend);
        setState(356);
        unparsed_block();
      }
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Finally_Context ------------------------------------------------------------------

McCompParser::Finally_Context::Finally_Context(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::Finally_Context::getRuleIndex() const {
  return McCompParser::RuleFinally_;
}

void McCompParser::Finally_Context::copyFrom(Finally_Context *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- FinallyBlockContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::FinallyBlockContext::Finally() {
  return getToken(McCompParser::Finally, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::FinallyBlockContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::FinallyBlockContext::FinallyBlockContext(Finally_Context *ctx) { copyFrom(ctx); }


std::any McCompParser::FinallyBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitFinallyBlock(this);
  else
    return visitor->visitChildren(this);
}
//----------------- FinallyBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::FinallyBlockCopyContext::Finally() {
  return getToken(McCompParser::Finally, 0);
}

tree::TerminalNode* McCompParser::FinallyBlockCopyContext::Copy() {
  return getToken(McCompParser::Copy, 0);
}

tree::TerminalNode* McCompParser::FinallyBlockCopyContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::FinallyBlockCopyContext::Extend() {
  return getToken(McCompParser::Extend, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::FinallyBlockCopyContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

McCompParser::FinallyBlockCopyContext::FinallyBlockCopyContext(Finally_Context *ctx) { copyFrom(ctx); }


std::any McCompParser::FinallyBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitFinallyBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::Finally_Context* McCompParser::finally_() {
  Finally_Context *_localctx = _tracker.createInstance<Finally_Context>(_ctx, getState());
  enterRule(_localctx, 38, McCompParser::RuleFinally_);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(370);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 63, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::FinallyBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(361);
      match(McCompParser::Finally);
      setState(362);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::FinallyBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(363);
      match(McCompParser::Finally);
      setState(364);
      match(McCompParser::Copy);
      setState(365);
      match(McCompParser::Identifier);
      setState(368);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McCompParser::Extend) {
        setState(366);
        match(McCompParser::Extend);
        setState(367);
        unparsed_block();
      }
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- MetadataContext ------------------------------------------------------------------

McCompParser::MetadataContext::MetadataContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::MetadataContext::MetaData() {
  return getToken(McCompParser::MetaData, 0);
}

McCompParser::Unparsed_blockContext* McCompParser::MetadataContext::unparsed_block() {
  return getRuleContext<McCompParser::Unparsed_blockContext>(0);
}

std::vector<tree::TerminalNode *> McCompParser::MetadataContext::Identifier() {
  return getTokens(McCompParser::Identifier);
}

tree::TerminalNode* McCompParser::MetadataContext::Identifier(size_t i) {
  return getToken(McCompParser::Identifier, i);
}

std::vector<tree::TerminalNode *> McCompParser::MetadataContext::StringLiteral() {
  return getTokens(McCompParser::StringLiteral);
}

tree::TerminalNode* McCompParser::MetadataContext::StringLiteral(size_t i) {
  return getToken(McCompParser::StringLiteral, i);
}


size_t McCompParser::MetadataContext::getRuleIndex() const {
  return McCompParser::RuleMetadata;
}


std::any McCompParser::MetadataContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitMetadata(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::MetadataContext* McCompParser::metadata() {
  MetadataContext *_localctx = _tracker.createInstance<MetadataContext>(_ctx, getState());
  enterRule(_localctx, 40, McCompParser::RuleMetadata);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(372);
    match(McCompParser::MetaData);
    setState(373);
    antlrcpp::downCast<MetadataContext *>(_localctx)->mime = _input->LT(1);
    _la = _input->LA(1);
    if (!(_la == McCompParser::StringLiteral || _la == McCompParser::Identifier)) {
      antlrcpp::downCast<MetadataContext *>(_localctx)->mime = _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(374);
    antlrcpp::downCast<MetadataContext *>(_localctx)->name = _input->LT(1);
    _la = _input->LA(1);
    if (!(_la == McCompParser::StringLiteral || _la == McCompParser::Identifier)) {
      antlrcpp::downCast<MetadataContext *>(_localctx)->name = _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(375);
    unparsed_block();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CategoryContext ------------------------------------------------------------------

McCompParser::CategoryContext::CategoryContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::CategoryContext::Category() {
  return getToken(McCompParser::Category, 0);
}

tree::TerminalNode* McCompParser::CategoryContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::CategoryContext::StringLiteral() {
  return getToken(McCompParser::StringLiteral, 0);
}


size_t McCompParser::CategoryContext::getRuleIndex() const {
  return McCompParser::RuleCategory;
}


std::any McCompParser::CategoryContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitCategory(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::CategoryContext* McCompParser::category() {
  CategoryContext *_localctx = _tracker.createInstance<CategoryContext>(_ctx, getState());
  enterRule(_localctx, 42, McCompParser::RuleCategory);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(377);
    match(McCompParser::Category);
    setState(378);
    _la = _input->LA(1);
    if (!(_la == McCompParser::StringLiteral || _la == McCompParser::Identifier)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- InitializerlistContext ------------------------------------------------------------------

McCompParser::InitializerlistContext::InitializerlistContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::InitializerlistContext::LeftBrace() {
  return getToken(McCompParser::LeftBrace, 0);
}

tree::TerminalNode* McCompParser::InitializerlistContext::RightBrace() {
  return getToken(McCompParser::RightBrace, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::InitializerlistContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::InitializerlistContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

std::vector<tree::TerminalNode *> McCompParser::InitializerlistContext::Comma() {
  return getTokens(McCompParser::Comma);
}

tree::TerminalNode* McCompParser::InitializerlistContext::Comma(size_t i) {
  return getToken(McCompParser::Comma, i);
}


size_t McCompParser::InitializerlistContext::getRuleIndex() const {
  return McCompParser::RuleInitializerlist;
}


std::any McCompParser::InitializerlistContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitInitializerlist(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::InitializerlistContext* McCompParser::initializerlist() {
  InitializerlistContext *_localctx = _tracker.createInstance<InitializerlistContext>(_ctx, getState());
  enterRule(_localctx, 44, McCompParser::RuleInitializerlist);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(380);
    match(McCompParser::LeftBrace);
    setState(381);
    antlrcpp::downCast<InitializerlistContext *>(_localctx)->exprContext = expr(0);
    antlrcpp::downCast<InitializerlistContext *>(_localctx)->values.push_back(antlrcpp::downCast<InitializerlistContext *>(_localctx)->exprContext);
    setState(386);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == McCompParser::Comma) {
      setState(382);
      match(McCompParser::Comma);
      setState(383);
      antlrcpp::downCast<InitializerlistContext *>(_localctx)->exprContext = expr(0);
      antlrcpp::downCast<InitializerlistContext *>(_localctx)->values.push_back(antlrcpp::downCast<InitializerlistContext *>(_localctx)->exprContext);
      setState(388);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(389);
    match(McCompParser::RightBrace);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AssignmentContext ------------------------------------------------------------------

McCompParser::AssignmentContext::AssignmentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::AssignmentContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::AssignmentContext::Assign() {
  return getToken(McCompParser::Assign, 0);
}

McCompParser::ExprContext* McCompParser::AssignmentContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}


size_t McCompParser::AssignmentContext::getRuleIndex() const {
  return McCompParser::RuleAssignment;
}


std::any McCompParser::AssignmentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitAssignment(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::AssignmentContext* McCompParser::assignment() {
  AssignmentContext *_localctx = _tracker.createInstance<AssignmentContext>(_ctx, getState());
  enterRule(_localctx, 46, McCompParser::RuleAssignment);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(391);
    match(McCompParser::Identifier);
    setState(392);
    match(McCompParser::Assign);
    setState(393);
    expr(0);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ExprContext ------------------------------------------------------------------

McCompParser::ExprContext::ExprContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::ExprContext::getRuleIndex() const {
  return McCompParser::RuleExpr;
}

void McCompParser::ExprContext::copyFrom(ExprContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- ExpressionBinaryModContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionBinaryModContext::Mod() {
  return getToken(McCompParser::Mod, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryModContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryModContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionBinaryModContext::ExpressionBinaryModContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryModContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryMod(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryLessContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionBinaryLessContext::Less() {
  return getToken(McCompParser::Less, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryLessContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryLessContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionBinaryLessContext::ExpressionBinaryLessContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryLessContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryLess(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryGreaterContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionBinaryGreaterContext::Greater() {
  return getToken(McCompParser::Greater, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryGreaterContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryGreaterContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionBinaryGreaterContext::ExpressionBinaryGreaterContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryGreaterContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryGreater(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryLessEqualContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionBinaryLessEqualContext::LessEqual() {
  return getToken(McCompParser::LessEqual, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryLessEqualContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryLessEqualContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionBinaryLessEqualContext::ExpressionBinaryLessEqualContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryLessEqualContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryLessEqual(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionArrayAccessContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionArrayAccessContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::ExpressionArrayAccessContext::LeftBracket() {
  return getToken(McCompParser::LeftBracket, 0);
}

McCompParser::ExprContext* McCompParser::ExpressionArrayAccessContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}

tree::TerminalNode* McCompParser::ExpressionArrayAccessContext::RightBracket() {
  return getToken(McCompParser::RightBracket, 0);
}

McCompParser::ExpressionArrayAccessContext::ExpressionArrayAccessContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionArrayAccessContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionArrayAccess(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryLogicContext ------------------------------------------------------------------

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryLogicContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryLogicContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

tree::TerminalNode* McCompParser::ExpressionBinaryLogicContext::AndAnd() {
  return getToken(McCompParser::AndAnd, 0);
}

tree::TerminalNode* McCompParser::ExpressionBinaryLogicContext::OrOr() {
  return getToken(McCompParser::OrOr, 0);
}

McCompParser::ExpressionBinaryLogicContext::ExpressionBinaryLogicContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryLogicContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryLogic(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionIntegerContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionIntegerContext::IntegerLiteral() {
  return getToken(McCompParser::IntegerLiteral, 0);
}

McCompParser::ExpressionIntegerContext::ExpressionIntegerContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionIntegerContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionInteger(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryRightShiftContext ------------------------------------------------------------------

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryRightShiftContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryRightShiftContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionBinaryRightShiftContext::ExpressionBinaryRightShiftContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryRightShiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryRightShift(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionMyselfContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionMyselfContext::Myself() {
  return getToken(McCompParser::Myself, 0);
}

McCompParser::ExpressionMyselfContext::ExpressionMyselfContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionMyselfContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionMyself(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionPreviousContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionPreviousContext::Previous() {
  return getToken(McCompParser::Previous, 0);
}

McCompParser::ExpressionPreviousContext::ExpressionPreviousContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionPreviousContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionPrevious(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionIdentifierContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionIdentifierContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

McCompParser::ExpressionIdentifierContext::ExpressionIdentifierContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionIdentifierContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionIdentifier(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionStructAccessContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionStructAccessContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::ExpressionStructAccessContext::Dot() {
  return getToken(McCompParser::Dot, 0);
}

McCompParser::ExprContext* McCompParser::ExpressionStructAccessContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}

McCompParser::ExpressionStructAccessContext::ExpressionStructAccessContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionStructAccessContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionStructAccess(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionFunctionCallContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionFunctionCallContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::ExpressionFunctionCallContext::LeftParen() {
  return getToken(McCompParser::LeftParen, 0);
}

tree::TerminalNode* McCompParser::ExpressionFunctionCallContext::RightParen() {
  return getToken(McCompParser::RightParen, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionFunctionCallContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionFunctionCallContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

std::vector<tree::TerminalNode *> McCompParser::ExpressionFunctionCallContext::Comma() {
  return getTokens(McCompParser::Comma);
}

tree::TerminalNode* McCompParser::ExpressionFunctionCallContext::Comma(size_t i) {
  return getToken(McCompParser::Comma, i);
}

McCompParser::ExpressionFunctionCallContext::ExpressionFunctionCallContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionFunctionCallContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionFunctionCall(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryMDContext ------------------------------------------------------------------

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryMDContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryMDContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

tree::TerminalNode* McCompParser::ExpressionBinaryMDContext::Star() {
  return getToken(McCompParser::Star, 0);
}

tree::TerminalNode* McCompParser::ExpressionBinaryMDContext::Div() {
  return getToken(McCompParser::Div, 0);
}

McCompParser::ExpressionBinaryMDContext::ExpressionBinaryMDContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryMDContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryMD(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionStringContext ------------------------------------------------------------------

std::vector<tree::TerminalNode *> McCompParser::ExpressionStringContext::StringLiteral() {
  return getTokens(McCompParser::StringLiteral);
}

tree::TerminalNode* McCompParser::ExpressionStringContext::StringLiteral(size_t i) {
  return getToken(McCompParser::StringLiteral, i);
}

McCompParser::ExpressionStringContext::ExpressionStringContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionStringContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionString(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionGroupingContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionGroupingContext::LeftParen() {
  return getToken(McCompParser::LeftParen, 0);
}

McCompParser::ExprContext* McCompParser::ExpressionGroupingContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}

tree::TerminalNode* McCompParser::ExpressionGroupingContext::RightParen() {
  return getToken(McCompParser::RightParen, 0);
}

McCompParser::ExpressionGroupingContext::ExpressionGroupingContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionGroupingContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionGrouping(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionExponentiationContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionExponentiationContext::Caret() {
  return getToken(McCompParser::Caret, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionExponentiationContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionExponentiationContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionExponentiationContext::ExpressionExponentiationContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionExponentiationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionExponentiation(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryLeftShiftContext ------------------------------------------------------------------

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryLeftShiftContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryLeftShiftContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionBinaryLeftShiftContext::ExpressionBinaryLeftShiftContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryLeftShiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryLeftShift(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryGreaterEqualContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionBinaryGreaterEqualContext::GreaterEqual() {
  return getToken(McCompParser::GreaterEqual, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryGreaterEqualContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryGreaterEqualContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionBinaryGreaterEqualContext::ExpressionBinaryGreaterEqualContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryGreaterEqualContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryGreaterEqual(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionZeroContext ------------------------------------------------------------------

McCompParser::ExpressionZeroContext::ExpressionZeroContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionZeroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionZero(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionUnaryPMContext ------------------------------------------------------------------

McCompParser::ExprContext* McCompParser::ExpressionUnaryPMContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}

tree::TerminalNode* McCompParser::ExpressionUnaryPMContext::Plus() {
  return getToken(McCompParser::Plus, 0);
}

tree::TerminalNode* McCompParser::ExpressionUnaryPMContext::Minus() {
  return getToken(McCompParser::Minus, 0);
}

McCompParser::ExpressionUnaryPMContext::ExpressionUnaryPMContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionUnaryPMContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionUnaryPM(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionTrinaryLogicContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionTrinaryLogicContext::Question() {
  return getToken(McCompParser::Question, 0);
}

tree::TerminalNode* McCompParser::ExpressionTrinaryLogicContext::Colon() {
  return getToken(McCompParser::Colon, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionTrinaryLogicContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionTrinaryLogicContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionTrinaryLogicContext::ExpressionTrinaryLogicContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionTrinaryLogicContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionTrinaryLogic(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionFloatContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionFloatContext::FloatingLiteral() {
  return getToken(McCompParser::FloatingLiteral, 0);
}

McCompParser::ExpressionFloatContext::ExpressionFloatContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionFloatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionFloat(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionPointerAccessContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionPointerAccessContext::Identifier() {
  return getToken(McCompParser::Identifier, 0);
}

tree::TerminalNode* McCompParser::ExpressionPointerAccessContext::Arrow() {
  return getToken(McCompParser::Arrow, 0);
}

McCompParser::ExprContext* McCompParser::ExpressionPointerAccessContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}

McCompParser::ExpressionPointerAccessContext::ExpressionPointerAccessContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionPointerAccessContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionPointerAccess(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryEqualContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionBinaryEqualContext::Equal() {
  return getToken(McCompParser::Equal, 0);
}

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryEqualContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryEqualContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

McCompParser::ExpressionBinaryEqualContext::ExpressionBinaryEqualContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryEqualContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryEqual(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryPMContext ------------------------------------------------------------------

std::vector<McCompParser::ExprContext *> McCompParser::ExpressionBinaryPMContext::expr() {
  return getRuleContexts<McCompParser::ExprContext>();
}

McCompParser::ExprContext* McCompParser::ExpressionBinaryPMContext::expr(size_t i) {
  return getRuleContext<McCompParser::ExprContext>(i);
}

tree::TerminalNode* McCompParser::ExpressionBinaryPMContext::Plus() {
  return getToken(McCompParser::Plus, 0);
}

tree::TerminalNode* McCompParser::ExpressionBinaryPMContext::Minus() {
  return getToken(McCompParser::Minus, 0);
}

McCompParser::ExpressionBinaryPMContext::ExpressionBinaryPMContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionBinaryPMContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryPM(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionUnaryLogicContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::ExpressionUnaryLogicContext::Not() {
  return getToken(McCompParser::Not, 0);
}

McCompParser::ExprContext* McCompParser::ExpressionUnaryLogicContext::expr() {
  return getRuleContext<McCompParser::ExprContext>(0);
}

McCompParser::ExpressionUnaryLogicContext::ExpressionUnaryLogicContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McCompParser::ExpressionUnaryLogicContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitExpressionUnaryLogic(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::ExprContext* McCompParser::expr() {
   return expr(0);
}

McCompParser::ExprContext* McCompParser::expr(int precedence) {
  ParserRuleContext *parentContext = _ctx;
  size_t parentState = getState();
  McCompParser::ExprContext *_localctx = _tracker.createInstance<ExprContext>(_ctx, parentState);
  McCompParser::ExprContext *previousContext = _localctx;
  (void)previousContext; // Silence compiler, in case the context is not used by generated code.
  size_t startState = 48;
  enterRecursionRule(_localctx, 48, McCompParser::RuleExpr, precedence);

    size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    unrollRecursionContexts(parentContext);
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(439);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 67, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<ExpressionZeroContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;

      setState(396);
      match(McCompParser::T__0);
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<ExpressionIntegerContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(397);
      match(McCompParser::IntegerLiteral);
      break;
    }

    case 3: {
      _localctx = _tracker.createInstance<ExpressionFloatContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(398);
      match(McCompParser::FloatingLiteral);
      break;
    }

    case 4: {
      _localctx = _tracker.createInstance<ExpressionStringContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(402);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 65, _ctx);
      while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
        if (alt == 1) {
          setState(399);
          antlrcpp::downCast<ExpressionStringContext *>(_localctx)->stringliteralToken = match(McCompParser::StringLiteral);
          antlrcpp::downCast<ExpressionStringContext *>(_localctx)->args.push_back(antlrcpp::downCast<ExpressionStringContext *>(_localctx)->stringliteralToken); 
        }
        setState(404);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 65, _ctx);
      }
      break;
    }

    case 5: {
      _localctx = _tracker.createInstance<ExpressionPointerAccessContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(405);
      match(McCompParser::Identifier);
      setState(406);
      match(McCompParser::Arrow);
      setState(407);
      expr(23);
      break;
    }

    case 6: {
      _localctx = _tracker.createInstance<ExpressionStructAccessContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(408);
      match(McCompParser::Identifier);
      setState(409);
      match(McCompParser::Dot);
      setState(410);
      expr(22);
      break;
    }

    case 7: {
      _localctx = _tracker.createInstance<ExpressionArrayAccessContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(411);
      match(McCompParser::Identifier);
      setState(412);
      match(McCompParser::LeftBracket);
      setState(413);
      expr(0);
      setState(414);
      match(McCompParser::RightBracket);
      break;
    }

    case 8: {
      _localctx = _tracker.createInstance<ExpressionFunctionCallContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(416);
      match(McCompParser::Identifier);
      setState(417);
      match(McCompParser::LeftParen);
      setState(418);
      antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->exprContext = expr(0);
      antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->args.push_back(antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->exprContext);
      setState(423);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == McCompParser::Comma) {
        setState(419);
        match(McCompParser::Comma);
        setState(420);
        antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->exprContext = expr(0);
        antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->args.push_back(antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->exprContext);
        setState(425);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(426);
      match(McCompParser::RightParen);
      break;
    }

    case 9: {
      _localctx = _tracker.createInstance<ExpressionGroupingContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(428);
      match(McCompParser::LeftParen);
      setState(429);
      expr(0);
      setState(430);
      match(McCompParser::RightParen);
      break;
    }

    case 10: {
      _localctx = _tracker.createInstance<ExpressionUnaryPMContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(432);
      _la = _input->LA(1);
      if (!(_la == McCompParser::Plus

      || _la == McCompParser::Minus)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(433);
      expr(18);
      break;
    }

    case 11: {
      _localctx = _tracker.createInstance<ExpressionIdentifierContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(434);
      match(McCompParser::Identifier);
      break;
    }

    case 12: {
      _localctx = _tracker.createInstance<ExpressionUnaryLogicContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(435);
      match(McCompParser::Not);
      setState(436);
      expr(5);
      break;
    }

    case 13: {
      _localctx = _tracker.createInstance<ExpressionPreviousContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(437);
      match(McCompParser::Previous);
      break;
    }

    case 14: {
      _localctx = _tracker.createInstance<ExpressionMyselfContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(438);
      match(McCompParser::Myself);
      break;
    }

    default:
      break;
    }
    _ctx->stop = _input->LT(-1);
    setState(485);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 69, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        if (!_parseListeners.empty())
          triggerExitRuleEvent();
        previousContext = _localctx;
        setState(483);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 68, _ctx)) {
        case 1: {
          auto newContext = _tracker.createInstance<ExpressionExponentiationContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->base = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(441);

          if (!(precpred(_ctx, 17))) throw FailedPredicateException(this, "precpred(_ctx, 17)");
          setState(442);
          match(McCompParser::Caret);
          setState(443);
          antlrcpp::downCast<ExpressionExponentiationContext *>(_localctx)->exponent = expr(17);
          break;
        }

        case 2: {
          auto newContext = _tracker.createInstance<ExpressionBinaryMDContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(444);

          if (!(precpred(_ctx, 16))) throw FailedPredicateException(this, "precpred(_ctx, 16)");
          setState(445);
          _la = _input->LA(1);
          if (!(_la == McCompParser::Star

          || _la == McCompParser::Div)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(446);
          antlrcpp::downCast<ExpressionBinaryMDContext *>(_localctx)->right = expr(17);
          break;
        }

        case 3: {
          auto newContext = _tracker.createInstance<ExpressionBinaryPMContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(447);

          if (!(precpred(_ctx, 15))) throw FailedPredicateException(this, "precpred(_ctx, 15)");
          setState(448);
          _la = _input->LA(1);
          if (!(_la == McCompParser::Plus

          || _la == McCompParser::Minus)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(449);
          antlrcpp::downCast<ExpressionBinaryPMContext *>(_localctx)->right = expr(16);
          break;
        }

        case 4: {
          auto newContext = _tracker.createInstance<ExpressionBinaryModContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(450);

          if (!(precpred(_ctx, 14))) throw FailedPredicateException(this, "precpred(_ctx, 14)");
          setState(451);
          match(McCompParser::Mod);
          setState(452);
          antlrcpp::downCast<ExpressionBinaryModContext *>(_localctx)->right = expr(15);
          break;
        }

        case 5: {
          auto newContext = _tracker.createInstance<ExpressionBinaryRightShiftContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(453);

          if (!(precpred(_ctx, 13))) throw FailedPredicateException(this, "precpred(_ctx, 13)");
          setState(454);
          match(McCompParser::T__1);
          setState(455);
          antlrcpp::downCast<ExpressionBinaryRightShiftContext *>(_localctx)->right = expr(14);
          break;
        }

        case 6: {
          auto newContext = _tracker.createInstance<ExpressionBinaryLeftShiftContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(456);

          if (!(precpred(_ctx, 12))) throw FailedPredicateException(this, "precpred(_ctx, 12)");
          setState(457);
          match(McCompParser::T__2);
          setState(458);
          antlrcpp::downCast<ExpressionBinaryLeftShiftContext *>(_localctx)->right = expr(13);
          break;
        }

        case 7: {
          auto newContext = _tracker.createInstance<ExpressionBinaryEqualContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(459);

          if (!(precpred(_ctx, 10))) throw FailedPredicateException(this, "precpred(_ctx, 10)");
          setState(460);
          match(McCompParser::Equal);
          setState(461);
          antlrcpp::downCast<ExpressionBinaryEqualContext *>(_localctx)->right = expr(11);
          break;
        }

        case 8: {
          auto newContext = _tracker.createInstance<ExpressionBinaryLessEqualContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(462);

          if (!(precpred(_ctx, 9))) throw FailedPredicateException(this, "precpred(_ctx, 9)");
          setState(463);
          match(McCompParser::LessEqual);
          setState(464);
          antlrcpp::downCast<ExpressionBinaryLessEqualContext *>(_localctx)->right = expr(10);
          break;
        }

        case 9: {
          auto newContext = _tracker.createInstance<ExpressionBinaryGreaterEqualContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(465);

          if (!(precpred(_ctx, 8))) throw FailedPredicateException(this, "precpred(_ctx, 8)");
          setState(466);
          match(McCompParser::GreaterEqual);
          setState(467);
          antlrcpp::downCast<ExpressionBinaryGreaterEqualContext *>(_localctx)->right = expr(9);
          break;
        }

        case 10: {
          auto newContext = _tracker.createInstance<ExpressionBinaryLessContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(468);

          if (!(precpred(_ctx, 7))) throw FailedPredicateException(this, "precpred(_ctx, 7)");
          setState(469);
          match(McCompParser::Less);
          setState(470);
          antlrcpp::downCast<ExpressionBinaryLessContext *>(_localctx)->right = expr(8);
          break;
        }

        case 11: {
          auto newContext = _tracker.createInstance<ExpressionBinaryGreaterContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(471);

          if (!(precpred(_ctx, 6))) throw FailedPredicateException(this, "precpred(_ctx, 6)");
          setState(472);
          match(McCompParser::Greater);
          setState(473);
          antlrcpp::downCast<ExpressionBinaryGreaterContext *>(_localctx)->right = expr(7);
          break;
        }

        case 12: {
          auto newContext = _tracker.createInstance<ExpressionBinaryLogicContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(474);

          if (!(precpred(_ctx, 4))) throw FailedPredicateException(this, "precpred(_ctx, 4)");
          setState(475);
          _la = _input->LA(1);
          if (!(_la == McCompParser::AndAnd

          || _la == McCompParser::OrOr)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(476);
          antlrcpp::downCast<ExpressionBinaryLogicContext *>(_localctx)->right = expr(5);
          break;
        }

        case 13: {
          auto newContext = _tracker.createInstance<ExpressionTrinaryLogicContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->test = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(477);

          if (!(precpred(_ctx, 3))) throw FailedPredicateException(this, "precpred(_ctx, 3)");
          setState(478);
          match(McCompParser::Question);
          setState(479);
          antlrcpp::downCast<ExpressionTrinaryLogicContext *>(_localctx)->true_ = expr(0);
          setState(480);
          match(McCompParser::Colon);
          setState(481);
          antlrcpp::downCast<ExpressionTrinaryLogicContext *>(_localctx)->false_ = expr(4);
          break;
        }

        default:
          break;
        } 
      }
      setState(487);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 69, _ctx);
    }
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }
  return _localctx;
}

//----------------- ShellContext ------------------------------------------------------------------

McCompParser::ShellContext::ShellContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::ShellContext::Shell() {
  return getToken(McCompParser::Shell, 0);
}

tree::TerminalNode* McCompParser::ShellContext::StringLiteral() {
  return getToken(McCompParser::StringLiteral, 0);
}


size_t McCompParser::ShellContext::getRuleIndex() const {
  return McCompParser::RuleShell;
}


std::any McCompParser::ShellContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitShell(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::ShellContext* McCompParser::shell() {
  ShellContext *_localctx = _tracker.createInstance<ShellContext>(_ctx, getState());
  enterRule(_localctx, 50, McCompParser::RuleShell);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(488);
    match(McCompParser::Shell);
    setState(489);
    match(McCompParser::StringLiteral);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SearchContext ------------------------------------------------------------------

McCompParser::SearchContext::SearchContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McCompParser::SearchContext::getRuleIndex() const {
  return McCompParser::RuleSearch;
}

void McCompParser::SearchContext::copyFrom(SearchContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- SearchPathContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::SearchPathContext::Search() {
  return getToken(McCompParser::Search, 0);
}

tree::TerminalNode* McCompParser::SearchPathContext::StringLiteral() {
  return getToken(McCompParser::StringLiteral, 0);
}

McCompParser::SearchPathContext::SearchPathContext(SearchContext *ctx) { copyFrom(ctx); }


std::any McCompParser::SearchPathContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitSearchPath(this);
  else
    return visitor->visitChildren(this);
}
//----------------- SearchShellContext ------------------------------------------------------------------

tree::TerminalNode* McCompParser::SearchShellContext::Search() {
  return getToken(McCompParser::Search, 0);
}

tree::TerminalNode* McCompParser::SearchShellContext::Shell() {
  return getToken(McCompParser::Shell, 0);
}

tree::TerminalNode* McCompParser::SearchShellContext::StringLiteral() {
  return getToken(McCompParser::StringLiteral, 0);
}

McCompParser::SearchShellContext::SearchShellContext(SearchContext *ctx) { copyFrom(ctx); }


std::any McCompParser::SearchShellContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitSearchShell(this);
  else
    return visitor->visitChildren(this);
}
McCompParser::SearchContext* McCompParser::search() {
  SearchContext *_localctx = _tracker.createInstance<SearchContext>(_ctx, getState());
  enterRule(_localctx, 52, McCompParser::RuleSearch);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(496);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 70, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McCompParser::SearchPathContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(491);
      match(McCompParser::Search);
      setState(492);
      match(McCompParser::StringLiteral);
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McCompParser::SearchShellContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(493);
      match(McCompParser::Search);
      setState(494);
      match(McCompParser::Shell);
      setState(495);
      match(McCompParser::StringLiteral);
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Unparsed_blockContext ------------------------------------------------------------------

McCompParser::Unparsed_blockContext::Unparsed_blockContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McCompParser::Unparsed_blockContext::UnparsedBlock() {
  return getToken(McCompParser::UnparsedBlock, 0);
}


size_t McCompParser::Unparsed_blockContext::getRuleIndex() const {
  return McCompParser::RuleUnparsed_block;
}


std::any McCompParser::Unparsed_blockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McCompVisitor*>(visitor))
    return parserVisitor->visitUnparsed_block(this);
  else
    return visitor->visitChildren(this);
}

McCompParser::Unparsed_blockContext* McCompParser::unparsed_block() {
  Unparsed_blockContext *_localctx = _tracker.createInstance<Unparsed_blockContext>(_ctx, getState());
  enterRule(_localctx, 54, McCompParser::RuleUnparsed_block);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(498);
    match(McCompParser::UnparsedBlock);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

bool McCompParser::sempred(RuleContext *context, size_t ruleIndex, size_t predicateIndex) {
  switch (ruleIndex) {
    case 24: return exprSempred(antlrcpp::downCast<ExprContext *>(context), predicateIndex);

  default:
    break;
  }
  return true;
}

bool McCompParser::exprSempred(ExprContext *_localctx, size_t predicateIndex) {
  switch (predicateIndex) {
    case 0: return precpred(_ctx, 17);
    case 1: return precpred(_ctx, 16);
    case 2: return precpred(_ctx, 15);
    case 3: return precpred(_ctx, 14);
    case 4: return precpred(_ctx, 13);
    case 5: return precpred(_ctx, 12);
    case 6: return precpred(_ctx, 10);
    case 7: return precpred(_ctx, 9);
    case 8: return precpred(_ctx, 8);
    case 9: return precpred(_ctx, 7);
    case 10: return precpred(_ctx, 6);
    case 11: return precpred(_ctx, 4);
    case 12: return precpred(_ctx, 3);

  default:
    break;
  }
  return true;
}

void McCompParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  mccompParserInitialize();
#else
  ::antlr4::internal::call_once(mccompParserOnceFlag, mccompParserInitialize);
#endif
}
