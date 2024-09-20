
// Generated from /home/g/Code/mccode-antlr/src/grammar/McInstr.g4 by ANTLR 4.13.2


#include "McInstrVisitor.h"

#include "McInstrParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct McInstrParserStaticData final {
  McInstrParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  McInstrParserStaticData(const McInstrParserStaticData&) = delete;
  McInstrParserStaticData(McInstrParserStaticData&&) = delete;
  McInstrParserStaticData& operator=(const McInstrParserStaticData&) = delete;
  McInstrParserStaticData& operator=(McInstrParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag mcinstrParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<McInstrParserStaticData> mcinstrParserStaticData = nullptr;

void mcinstrParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (mcinstrParserStaticData != nullptr) {
    return;
  }
#else
  assert(mcinstrParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<McInstrParserStaticData>(
    std::vector<std::string>{
      "prog", "instrument_definition", "instrument_parameters", "instrument_parameter", 
      "instrument_parameter_unit", "instrument_trace", "instrument_metadata", 
      "instrument_trace_include", "component_instance", "instance_name", 
      "component_type", "instance_parameters", "instance_parameter", "split", 
      "when", "place", "orientation", "groupref", "jumps", "jump", "jumpname", 
      "extend", "component_ref", "coords", "reference", "dependency", "declare", 
      "uservars", "initialize", "save", "finally_", "metadata", "category", 
      "initializerlist", "assignment", "expr", "shell", "search", "unparsed_block"
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
  	4,1,192,514,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,
  	87,8,1,1,1,3,1,90,8,1,1,1,3,1,93,8,1,1,1,3,1,96,8,1,1,1,3,1,99,8,1,1,
  	1,3,1,102,8,1,1,1,3,1,105,8,1,1,1,1,1,3,1,109,8,1,1,1,3,1,112,8,1,1,1,
  	1,1,1,2,1,2,1,2,1,2,5,2,120,8,2,10,2,12,2,123,9,2,3,2,125,8,2,1,2,1,2,
  	1,3,3,3,130,8,3,1,3,1,3,3,3,134,8,3,1,3,1,3,3,3,138,8,3,1,3,1,3,1,3,3,
  	3,143,8,3,1,3,1,3,3,3,147,8,3,1,3,1,3,1,3,3,3,152,8,3,1,3,1,3,3,3,156,
  	8,3,1,3,1,3,3,3,160,8,3,3,3,162,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,4,5,171,
  	8,5,11,5,12,5,172,3,5,175,8,5,1,6,4,6,178,8,6,11,6,12,6,179,1,7,1,7,1,
  	7,1,8,3,8,186,8,8,1,8,3,8,189,8,8,1,8,3,8,192,8,8,1,8,1,8,1,8,1,8,1,8,
  	3,8,199,8,8,1,8,3,8,202,8,8,1,8,1,8,3,8,206,8,8,1,8,3,8,209,8,8,1,8,3,
  	8,212,8,8,1,8,3,8,215,8,8,1,8,5,8,218,8,8,10,8,12,8,221,9,8,1,9,1,9,1,
  	9,1,9,1,9,1,9,3,9,229,8,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,237,8,10,
  	1,11,1,11,1,11,1,11,5,11,243,8,11,10,11,12,11,246,9,11,3,11,248,8,11,
  	1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,261,8,12,
  	1,13,1,13,1,13,3,13,266,8,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,
  	1,16,1,16,1,16,1,17,1,17,1,17,1,18,4,18,283,8,18,11,18,12,18,284,1,19,
  	1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,3,20,296,8,20,1,20,1,20,1,20,
  	1,20,1,20,3,20,303,8,20,1,20,3,20,306,8,20,1,21,1,21,1,21,1,22,1,22,1,
  	22,1,22,3,22,315,8,22,1,22,3,22,318,8,22,1,23,1,23,1,23,1,23,1,23,1,23,
  	1,23,1,23,1,24,1,24,1,24,1,24,3,24,332,8,24,3,24,334,8,24,1,25,1,25,1,
  	25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,346,8,26,3,26,348,8,26,1,27,
  	1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,360,8,28,3,28,362,8,
  	28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,371,8,29,3,29,373,8,29,1,30,
  	1,30,1,30,1,30,1,30,1,30,1,30,3,30,382,8,30,3,30,384,8,30,1,31,1,31,1,
  	31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,33,1,33,5,33,398,8,33,10,33,12,
  	33,401,9,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,5,
  	35,414,8,35,10,35,12,35,417,9,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
  	35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,5,35,435,8,35,10,35,12,35,
  	438,9,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
  	1,35,3,35,453,8,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
  	1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
  	1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
  	1,35,1,35,1,35,1,35,5,35,497,8,35,10,35,12,35,500,9,35,1,36,1,36,1,36,
  	1,37,1,37,1,37,1,37,1,37,3,37,510,8,37,1,38,1,38,1,38,0,1,70,39,0,2,4,
  	6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
  	54,56,58,60,62,64,66,68,70,72,74,76,0,7,3,0,1,1,48,48,52,52,1,0,33,34,
  	2,0,30,30,32,32,2,0,52,52,179,179,1,0,138,139,1,0,140,141,1,0,165,166,
  	566,0,78,1,0,0,0,2,81,1,0,0,0,4,115,1,0,0,0,6,161,1,0,0,0,8,163,1,0,0,
  	0,10,166,1,0,0,0,12,177,1,0,0,0,14,181,1,0,0,0,16,185,1,0,0,0,18,228,
  	1,0,0,0,20,236,1,0,0,0,22,238,1,0,0,0,24,260,1,0,0,0,26,262,1,0,0,0,28,
  	267,1,0,0,0,30,270,1,0,0,0,32,274,1,0,0,0,34,278,1,0,0,0,36,282,1,0,0,
  	0,38,286,1,0,0,0,40,305,1,0,0,0,42,307,1,0,0,0,44,317,1,0,0,0,46,319,
  	1,0,0,0,48,333,1,0,0,0,50,335,1,0,0,0,52,347,1,0,0,0,54,349,1,0,0,0,56,
  	361,1,0,0,0,58,372,1,0,0,0,60,383,1,0,0,0,62,385,1,0,0,0,64,390,1,0,0,
  	0,66,393,1,0,0,0,68,404,1,0,0,0,70,452,1,0,0,0,72,501,1,0,0,0,74,509,
  	1,0,0,0,76,511,1,0,0,0,78,79,3,2,1,0,79,80,5,0,0,1,80,1,1,0,0,0,81,82,
  	5,9,0,0,82,83,5,16,0,0,83,84,5,179,0,0,84,86,3,4,2,0,85,87,3,72,36,0,
  	86,85,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,90,3,74,37,0,89,88,1,0,0,
  	0,89,90,1,0,0,0,90,92,1,0,0,0,91,93,3,12,6,0,92,91,1,0,0,0,92,93,1,0,
  	0,0,93,95,1,0,0,0,94,96,3,50,25,0,95,94,1,0,0,0,95,96,1,0,0,0,96,98,1,
  	0,0,0,97,99,3,52,26,0,98,97,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,
  	102,3,54,27,0,101,100,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,105,
  	3,56,28,0,104,103,1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,108,3,10,
  	5,0,107,109,3,58,29,0,108,107,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,
  	110,112,3,60,30,0,111,110,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,
  	114,5,12,0,0,114,3,1,0,0,0,115,124,5,132,0,0,116,121,3,6,3,0,117,118,
  	5,169,0,0,118,120,3,6,3,0,119,117,1,0,0,0,120,123,1,0,0,0,121,119,1,0,
  	0,0,121,122,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,124,116,1,0,0,0,124,
  	125,1,0,0,0,125,126,1,0,0,0,126,127,5,133,0,0,127,5,1,0,0,0,128,130,5,
  	78,0,0,129,128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,133,5,179,
  	0,0,132,134,3,8,4,0,133,132,1,0,0,0,133,134,1,0,0,0,134,137,1,0,0,0,135,
  	136,5,148,0,0,136,138,3,70,35,0,137,135,1,0,0,0,137,138,1,0,0,0,138,162,
  	1,0,0,0,139,140,5,93,0,0,140,142,5,179,0,0,141,143,3,8,4,0,142,141,1,
  	0,0,0,142,143,1,0,0,0,143,146,1,0,0,0,144,145,5,148,0,0,145,147,3,70,
  	35,0,146,144,1,0,0,0,146,147,1,0,0,0,147,162,1,0,0,0,148,152,5,43,0,0,
  	149,150,5,66,0,0,150,152,5,140,0,0,151,148,1,0,0,0,151,149,1,0,0,0,152,
  	153,1,0,0,0,153,155,5,179,0,0,154,156,3,8,4,0,155,154,1,0,0,0,155,156,
  	1,0,0,0,156,159,1,0,0,0,157,158,5,148,0,0,158,160,7,0,0,0,159,157,1,0,
  	0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,129,1,0,0,0,161,139,1,0,0,0,161,
  	151,1,0,0,0,162,7,1,0,0,0,163,164,5,141,0,0,164,165,5,52,0,0,165,9,1,
  	0,0,0,166,174,5,24,0,0,167,171,3,16,8,0,168,171,3,74,37,0,169,171,3,14,
  	7,0,170,167,1,0,0,0,170,168,1,0,0,0,170,169,1,0,0,0,171,172,1,0,0,0,172,
  	170,1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,170,1,0,0,0,174,175,1,
  	0,0,0,175,11,1,0,0,0,176,178,3,62,31,0,177,176,1,0,0,0,178,179,1,0,0,
  	0,179,177,1,0,0,0,179,180,1,0,0,0,180,13,1,0,0,0,181,182,5,47,0,0,182,
  	183,5,52,0,0,183,15,1,0,0,0,184,186,5,36,0,0,185,184,1,0,0,0,185,186,
  	1,0,0,0,186,188,1,0,0,0,187,189,5,37,0,0,188,187,1,0,0,0,188,189,1,0,
  	0,0,189,191,1,0,0,0,190,192,3,26,13,0,191,190,1,0,0,0,191,192,1,0,0,0,
  	192,193,1,0,0,0,193,194,5,7,0,0,194,195,3,18,9,0,195,196,5,148,0,0,196,
  	198,3,20,10,0,197,199,3,22,11,0,198,197,1,0,0,0,198,199,1,0,0,0,199,201,
  	1,0,0,0,200,202,3,28,14,0,201,200,1,0,0,0,201,202,1,0,0,0,202,203,1,0,
  	0,0,203,205,3,30,15,0,204,206,3,32,16,0,205,204,1,0,0,0,205,206,1,0,0,
  	0,206,208,1,0,0,0,207,209,3,34,17,0,208,207,1,0,0,0,208,209,1,0,0,0,209,
  	211,1,0,0,0,210,212,3,42,21,0,211,210,1,0,0,0,211,212,1,0,0,0,212,214,
  	1,0,0,0,213,215,3,36,18,0,214,213,1,0,0,0,214,215,1,0,0,0,215,219,1,0,
  	0,0,216,218,3,62,31,0,217,216,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,
  	219,220,1,0,0,0,220,17,1,0,0,0,221,219,1,0,0,0,222,223,5,34,0,0,223,224,
  	5,132,0,0,224,225,5,179,0,0,225,229,5,133,0,0,226,229,7,1,0,0,227,229,
  	5,179,0,0,228,222,1,0,0,0,228,226,1,0,0,0,228,227,1,0,0,0,229,19,1,0,
  	0,0,230,231,5,34,0,0,231,232,5,132,0,0,232,233,3,44,22,0,233,234,5,133,
  	0,0,234,237,1,0,0,0,235,237,5,179,0,0,236,230,1,0,0,0,236,235,1,0,0,0,
  	237,21,1,0,0,0,238,247,5,132,0,0,239,244,3,24,12,0,240,241,5,169,0,0,
  	241,243,3,24,12,0,242,240,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,
  	245,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,247,239,1,0,0,0,247,248,1,
  	0,0,0,248,249,1,0,0,0,249,250,5,133,0,0,250,23,1,0,0,0,251,252,5,179,
  	0,0,252,253,5,148,0,0,253,261,3,70,35,0,254,255,5,179,0,0,255,256,5,148,
  	0,0,256,261,5,48,0,0,257,258,5,179,0,0,258,259,5,148,0,0,259,261,3,66,
  	33,0,260,251,1,0,0,0,260,254,1,0,0,0,260,257,1,0,0,0,261,25,1,0,0,0,262,
  	265,5,35,0,0,263,266,1,0,0,0,264,266,3,70,35,0,265,263,1,0,0,0,265,264,
  	1,0,0,0,266,27,1,0,0,0,267,268,5,30,0,0,268,269,3,70,35,0,269,29,1,0,
  	0,0,270,271,5,5,0,0,271,272,3,46,23,0,272,273,3,48,24,0,273,31,1,0,0,
  	0,274,275,5,21,0,0,275,276,3,46,23,0,276,277,3,48,24,0,277,33,1,0,0,0,
  	278,279,5,27,0,0,279,280,5,179,0,0,280,35,1,0,0,0,281,283,3,38,19,0,282,
  	281,1,0,0,0,283,284,1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,37,1,
  	0,0,0,286,287,5,29,0,0,287,288,3,40,20,0,288,289,7,2,0,0,289,290,3,70,
  	35,0,290,39,1,0,0,0,291,295,5,22,0,0,292,293,5,132,0,0,293,294,5,49,0,
  	0,294,296,5,133,0,0,295,292,1,0,0,0,295,296,1,0,0,0,296,306,1,0,0,0,297,
  	306,5,33,0,0,298,302,5,31,0,0,299,300,5,132,0,0,300,301,5,49,0,0,301,
  	303,5,133,0,0,302,299,1,0,0,0,302,303,1,0,0,0,303,306,1,0,0,0,304,306,
  	5,179,0,0,305,291,1,0,0,0,305,297,1,0,0,0,305,298,1,0,0,0,305,304,1,0,
  	0,0,306,41,1,0,0,0,307,308,5,26,0,0,308,309,3,76,38,0,309,43,1,0,0,0,
  	310,314,5,22,0,0,311,312,5,132,0,0,312,313,5,49,0,0,313,315,5,133,0,0,
  	314,311,1,0,0,0,314,315,1,0,0,0,315,318,1,0,0,0,316,318,5,179,0,0,317,
  	310,1,0,0,0,317,316,1,0,0,0,318,45,1,0,0,0,319,320,5,132,0,0,320,321,
  	3,70,35,0,321,322,5,169,0,0,322,323,3,70,35,0,323,324,5,169,0,0,324,325,
  	3,70,35,0,325,326,5,133,0,0,326,47,1,0,0,0,327,334,5,4,0,0,328,331,5,
  	20,0,0,329,332,5,4,0,0,330,332,3,44,22,0,331,329,1,0,0,0,331,330,1,0,
  	0,0,332,334,1,0,0,0,333,327,1,0,0,0,333,328,1,0,0,0,334,49,1,0,0,0,335,
  	336,5,39,0,0,336,337,5,52,0,0,337,51,1,0,0,0,338,339,5,10,0,0,339,348,
  	3,76,38,0,340,341,5,10,0,0,341,342,5,34,0,0,342,345,5,179,0,0,343,344,
  	5,26,0,0,344,346,3,76,38,0,345,343,1,0,0,0,345,346,1,0,0,0,346,348,1,
  	0,0,0,347,338,1,0,0,0,347,340,1,0,0,0,348,53,1,0,0,0,349,350,5,8,0,0,
  	350,351,3,76,38,0,351,55,1,0,0,0,352,353,5,15,0,0,353,362,3,76,38,0,354,
  	355,5,15,0,0,355,356,5,34,0,0,356,359,5,179,0,0,357,358,5,26,0,0,358,
  	360,3,76,38,0,359,357,1,0,0,0,359,360,1,0,0,0,360,362,1,0,0,0,361,352,
  	1,0,0,0,361,354,1,0,0,0,362,57,1,0,0,0,363,364,5,28,0,0,364,373,3,76,
  	38,0,365,366,5,28,0,0,366,367,5,34,0,0,367,370,5,179,0,0,368,369,5,26,
  	0,0,369,371,3,76,38,0,370,368,1,0,0,0,370,371,1,0,0,0,371,373,1,0,0,0,
  	372,363,1,0,0,0,372,365,1,0,0,0,373,59,1,0,0,0,374,375,5,14,0,0,375,384,
  	3,76,38,0,376,377,5,14,0,0,377,378,5,34,0,0,378,381,5,179,0,0,379,380,
  	5,26,0,0,380,382,3,76,38,0,381,379,1,0,0,0,381,382,1,0,0,0,382,384,1,
  	0,0,0,383,374,1,0,0,0,383,376,1,0,0,0,384,61,1,0,0,0,385,386,5,42,0,0,
  	386,387,7,3,0,0,387,388,7,3,0,0,388,389,3,76,38,0,389,63,1,0,0,0,390,
  	391,5,6,0,0,391,392,7,3,0,0,392,65,1,0,0,0,393,394,5,136,0,0,394,399,
  	3,70,35,0,395,396,5,169,0,0,396,398,3,70,35,0,397,395,1,0,0,0,398,401,
  	1,0,0,0,399,397,1,0,0,0,399,400,1,0,0,0,400,402,1,0,0,0,401,399,1,0,0,
  	0,402,403,5,137,0,0,403,67,1,0,0,0,404,405,5,179,0,0,405,406,5,148,0,
  	0,406,407,3,70,35,0,407,69,1,0,0,0,408,409,6,35,-1,0,409,453,5,1,0,0,
  	410,453,5,49,0,0,411,453,5,51,0,0,412,414,5,52,0,0,413,412,1,0,0,0,414,
  	417,1,0,0,0,415,413,1,0,0,0,415,416,1,0,0,0,416,453,1,0,0,0,417,415,1,
  	0,0,0,418,419,5,179,0,0,419,420,5,171,0,0,420,453,3,70,35,23,421,422,
  	5,179,0,0,422,423,5,176,0,0,423,453,3,70,35,22,424,425,5,179,0,0,425,
  	426,5,134,0,0,426,427,3,70,35,0,427,428,5,135,0,0,428,453,1,0,0,0,429,
  	430,5,179,0,0,430,431,5,132,0,0,431,436,3,70,35,0,432,433,5,169,0,0,433,
  	435,3,70,35,0,434,432,1,0,0,0,435,438,1,0,0,0,436,434,1,0,0,0,436,437,
  	1,0,0,0,437,439,1,0,0,0,438,436,1,0,0,0,439,440,5,133,0,0,440,453,1,0,
  	0,0,441,442,5,132,0,0,442,443,3,70,35,0,443,444,5,133,0,0,444,453,1,0,
  	0,0,445,446,7,4,0,0,446,453,3,70,35,18,447,453,5,179,0,0,448,449,5,147,
  	0,0,449,453,3,70,35,5,450,453,5,22,0,0,451,453,5,33,0,0,452,408,1,0,0,
  	0,452,410,1,0,0,0,452,411,1,0,0,0,452,415,1,0,0,0,452,418,1,0,0,0,452,
  	421,1,0,0,0,452,424,1,0,0,0,452,429,1,0,0,0,452,441,1,0,0,0,452,445,1,
  	0,0,0,452,447,1,0,0,0,452,448,1,0,0,0,452,450,1,0,0,0,452,451,1,0,0,0,
  	453,498,1,0,0,0,454,455,10,17,0,0,455,456,5,143,0,0,456,497,3,70,35,17,
  	457,458,10,16,0,0,458,459,7,5,0,0,459,497,3,70,35,17,460,461,10,15,0,
  	0,461,462,7,4,0,0,462,497,3,70,35,16,463,464,10,14,0,0,464,465,5,142,
  	0,0,465,497,3,70,35,15,466,467,10,13,0,0,467,468,5,2,0,0,468,497,3,70,
  	35,14,469,470,10,12,0,0,470,471,5,3,0,0,471,497,3,70,35,13,472,473,10,
  	10,0,0,473,474,5,161,0,0,474,497,3,70,35,11,475,476,10,9,0,0,476,477,
  	5,163,0,0,477,497,3,70,35,10,478,479,10,8,0,0,479,480,5,164,0,0,480,497,
  	3,70,35,9,481,482,10,7,0,0,482,483,5,149,0,0,483,497,3,70,35,8,484,485,
  	10,6,0,0,485,486,5,150,0,0,486,497,3,70,35,7,487,488,10,4,0,0,488,489,
  	7,6,0,0,489,497,3,70,35,5,490,491,10,3,0,0,491,492,5,172,0,0,492,493,
  	3,70,35,0,493,494,5,173,0,0,494,495,3,70,35,4,495,497,1,0,0,0,496,454,
  	1,0,0,0,496,457,1,0,0,0,496,460,1,0,0,0,496,463,1,0,0,0,496,466,1,0,0,
  	0,496,469,1,0,0,0,496,472,1,0,0,0,496,475,1,0,0,0,496,478,1,0,0,0,496,
  	481,1,0,0,0,496,484,1,0,0,0,496,487,1,0,0,0,496,490,1,0,0,0,497,500,1,
  	0,0,0,498,496,1,0,0,0,498,499,1,0,0,0,499,71,1,0,0,0,500,498,1,0,0,0,
  	501,502,5,40,0,0,502,503,5,52,0,0,503,73,1,0,0,0,504,505,5,41,0,0,505,
  	510,5,52,0,0,506,507,5,41,0,0,507,508,5,40,0,0,508,510,5,52,0,0,509,504,
  	1,0,0,0,509,506,1,0,0,0,510,75,1,0,0,0,511,512,5,46,0,0,512,77,1,0,0,
  	0,63,86,89,92,95,98,101,104,108,111,121,124,129,133,137,142,146,151,155,
  	159,161,170,172,174,179,185,188,191,198,201,205,208,211,214,219,228,236,
  	244,247,260,265,284,295,302,305,314,317,331,333,345,347,359,361,370,372,
  	381,383,399,415,436,452,496,498,509
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  mcinstrParserStaticData = std::move(staticData);
}

}

McInstrParser::McInstrParser(TokenStream *input) : McInstrParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

McInstrParser::McInstrParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  McInstrParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *mcinstrParserStaticData->atn, mcinstrParserStaticData->decisionToDFA, mcinstrParserStaticData->sharedContextCache, options);
}

McInstrParser::~McInstrParser() {
  delete _interpreter;
}

const atn::ATN& McInstrParser::getATN() const {
  return *mcinstrParserStaticData->atn;
}

std::string McInstrParser::getGrammarFileName() const {
  return "McInstr.g4";
}

const std::vector<std::string>& McInstrParser::getRuleNames() const {
  return mcinstrParserStaticData->ruleNames;
}

const dfa::Vocabulary& McInstrParser::getVocabulary() const {
  return mcinstrParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView McInstrParser::getSerializedATN() const {
  return mcinstrParserStaticData->serializedATN;
}


//----------------- ProgContext ------------------------------------------------------------------

McInstrParser::ProgContext::ProgContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

McInstrParser::Instrument_definitionContext* McInstrParser::ProgContext::instrument_definition() {
  return getRuleContext<McInstrParser::Instrument_definitionContext>(0);
}

tree::TerminalNode* McInstrParser::ProgContext::EOF() {
  return getToken(McInstrParser::EOF, 0);
}


size_t McInstrParser::ProgContext::getRuleIndex() const {
  return McInstrParser::RuleProg;
}


std::any McInstrParser::ProgContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitProg(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::ProgContext* McInstrParser::prog() {
  ProgContext *_localctx = _tracker.createInstance<ProgContext>(_ctx, getState());
  enterRule(_localctx, 0, McInstrParser::RuleProg);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(78);
    instrument_definition();
    setState(79);
    match(McInstrParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Instrument_definitionContext ------------------------------------------------------------------

McInstrParser::Instrument_definitionContext::Instrument_definitionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::Instrument_definitionContext::Define() {
  return getToken(McInstrParser::Define, 0);
}

tree::TerminalNode* McInstrParser::Instrument_definitionContext::Instrument() {
  return getToken(McInstrParser::Instrument, 0);
}

tree::TerminalNode* McInstrParser::Instrument_definitionContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

McInstrParser::Instrument_parametersContext* McInstrParser::Instrument_definitionContext::instrument_parameters() {
  return getRuleContext<McInstrParser::Instrument_parametersContext>(0);
}

McInstrParser::Instrument_traceContext* McInstrParser::Instrument_definitionContext::instrument_trace() {
  return getRuleContext<McInstrParser::Instrument_traceContext>(0);
}

tree::TerminalNode* McInstrParser::Instrument_definitionContext::End() {
  return getToken(McInstrParser::End, 0);
}

McInstrParser::ShellContext* McInstrParser::Instrument_definitionContext::shell() {
  return getRuleContext<McInstrParser::ShellContext>(0);
}

McInstrParser::SearchContext* McInstrParser::Instrument_definitionContext::search() {
  return getRuleContext<McInstrParser::SearchContext>(0);
}

McInstrParser::Instrument_metadataContext* McInstrParser::Instrument_definitionContext::instrument_metadata() {
  return getRuleContext<McInstrParser::Instrument_metadataContext>(0);
}

McInstrParser::DependencyContext* McInstrParser::Instrument_definitionContext::dependency() {
  return getRuleContext<McInstrParser::DependencyContext>(0);
}

McInstrParser::DeclareContext* McInstrParser::Instrument_definitionContext::declare() {
  return getRuleContext<McInstrParser::DeclareContext>(0);
}

McInstrParser::UservarsContext* McInstrParser::Instrument_definitionContext::uservars() {
  return getRuleContext<McInstrParser::UservarsContext>(0);
}

McInstrParser::InitializeContext* McInstrParser::Instrument_definitionContext::initialize() {
  return getRuleContext<McInstrParser::InitializeContext>(0);
}

McInstrParser::SaveContext* McInstrParser::Instrument_definitionContext::save() {
  return getRuleContext<McInstrParser::SaveContext>(0);
}

McInstrParser::Finally_Context* McInstrParser::Instrument_definitionContext::finally_() {
  return getRuleContext<McInstrParser::Finally_Context>(0);
}


size_t McInstrParser::Instrument_definitionContext::getRuleIndex() const {
  return McInstrParser::RuleInstrument_definition;
}


std::any McInstrParser::Instrument_definitionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstrument_definition(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Instrument_definitionContext* McInstrParser::instrument_definition() {
  Instrument_definitionContext *_localctx = _tracker.createInstance<Instrument_definitionContext>(_ctx, getState());
  enterRule(_localctx, 2, McInstrParser::RuleInstrument_definition);
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
    setState(81);
    match(McInstrParser::Define);
    setState(82);
    match(McInstrParser::Instrument);
    setState(83);
    match(McInstrParser::Identifier);
    setState(84);
    instrument_parameters();
    setState(86);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Shell) {
      setState(85);
      shell();
    }
    setState(89);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Search) {
      setState(88);
      search();
    }
    setState(92);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::MetaData) {
      setState(91);
      instrument_metadata();
    }
    setState(95);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Dependency) {
      setState(94);
      dependency();
    }
    setState(98);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Declare) {
      setState(97);
      declare();
    }
    setState(101);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::UserVars) {
      setState(100);
      uservars();
    }
    setState(104);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Initialize) {
      setState(103);
      initialize();
    }
    setState(106);
    instrument_trace();
    setState(108);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Save) {
      setState(107);
      save();
    }
    setState(111);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Finally) {
      setState(110);
      finally_();
    }
    setState(113);
    match(McInstrParser::End);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Instrument_parametersContext ------------------------------------------------------------------

McInstrParser::Instrument_parametersContext::Instrument_parametersContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::Instrument_parametersContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

tree::TerminalNode* McInstrParser::Instrument_parametersContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}

std::vector<McInstrParser::Instrument_parameterContext *> McInstrParser::Instrument_parametersContext::instrument_parameter() {
  return getRuleContexts<McInstrParser::Instrument_parameterContext>();
}

McInstrParser::Instrument_parameterContext* McInstrParser::Instrument_parametersContext::instrument_parameter(size_t i) {
  return getRuleContext<McInstrParser::Instrument_parameterContext>(i);
}

std::vector<tree::TerminalNode *> McInstrParser::Instrument_parametersContext::Comma() {
  return getTokens(McInstrParser::Comma);
}

tree::TerminalNode* McInstrParser::Instrument_parametersContext::Comma(size_t i) {
  return getToken(McInstrParser::Comma, i);
}


size_t McInstrParser::Instrument_parametersContext::getRuleIndex() const {
  return McInstrParser::RuleInstrument_parameters;
}


std::any McInstrParser::Instrument_parametersContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstrument_parameters(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Instrument_parametersContext* McInstrParser::instrument_parameters() {
  Instrument_parametersContext *_localctx = _tracker.createInstance<Instrument_parametersContext>(_ctx, getState());
  enterRule(_localctx, 4, McInstrParser::RuleInstrument_parameters);
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
    setState(115);
    match(McInstrParser::LeftParen);
    setState(124);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (((((_la - 43) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 43)) & 1125934274969601) != 0) || _la == McInstrParser::Identifier) {
      setState(116);
      antlrcpp::downCast<Instrument_parametersContext *>(_localctx)->instrument_parameterContext = instrument_parameter();
      antlrcpp::downCast<Instrument_parametersContext *>(_localctx)->params.push_back(antlrcpp::downCast<Instrument_parametersContext *>(_localctx)->instrument_parameterContext);
      setState(121);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == McInstrParser::Comma) {
        setState(117);
        match(McInstrParser::Comma);
        setState(118);
        antlrcpp::downCast<Instrument_parametersContext *>(_localctx)->instrument_parameterContext = instrument_parameter();
        antlrcpp::downCast<Instrument_parametersContext *>(_localctx)->params.push_back(antlrcpp::downCast<Instrument_parametersContext *>(_localctx)->instrument_parameterContext);
        setState(123);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(126);
    match(McInstrParser::RightParen);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Instrument_parameterContext ------------------------------------------------------------------

McInstrParser::Instrument_parameterContext::Instrument_parameterContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::Instrument_parameterContext::getRuleIndex() const {
  return McInstrParser::RuleInstrument_parameter;
}

void McInstrParser::Instrument_parameterContext::copyFrom(Instrument_parameterContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- InstrumentParameterIntegerContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InstrumentParameterIntegerContext::Int() {
  return getToken(McInstrParser::Int, 0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterIntegerContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

McInstrParser::Instrument_parameter_unitContext* McInstrParser::InstrumentParameterIntegerContext::instrument_parameter_unit() {
  return getRuleContext<McInstrParser::Instrument_parameter_unitContext>(0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterIntegerContext::Assign() {
  return getToken(McInstrParser::Assign, 0);
}

McInstrParser::ExprContext* McInstrParser::InstrumentParameterIntegerContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

McInstrParser::InstrumentParameterIntegerContext::InstrumentParameterIntegerContext(Instrument_parameterContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InstrumentParameterIntegerContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstrumentParameterInteger(this);
  else
    return visitor->visitChildren(this);
}
//----------------- InstrumentParameterDoubleContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InstrumentParameterDoubleContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterDoubleContext::Double() {
  return getToken(McInstrParser::Double, 0);
}

McInstrParser::Instrument_parameter_unitContext* McInstrParser::InstrumentParameterDoubleContext::instrument_parameter_unit() {
  return getRuleContext<McInstrParser::Instrument_parameter_unitContext>(0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterDoubleContext::Assign() {
  return getToken(McInstrParser::Assign, 0);
}

McInstrParser::ExprContext* McInstrParser::InstrumentParameterDoubleContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

McInstrParser::InstrumentParameterDoubleContext::InstrumentParameterDoubleContext(Instrument_parameterContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InstrumentParameterDoubleContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstrumentParameterDouble(this);
  else
    return visitor->visitChildren(this);
}
//----------------- InstrumentParameterStringContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InstrumentParameterStringContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterStringContext::String() {
  return getToken(McInstrParser::String, 0);
}

McInstrParser::Instrument_parameter_unitContext* McInstrParser::InstrumentParameterStringContext::instrument_parameter_unit() {
  return getRuleContext<McInstrParser::Instrument_parameter_unitContext>(0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterStringContext::Assign() {
  return getToken(McInstrParser::Assign, 0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterStringContext::Char() {
  return getToken(McInstrParser::Char, 0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterStringContext::Star() {
  return getToken(McInstrParser::Star, 0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterStringContext::StringLiteral() {
  return getToken(McInstrParser::StringLiteral, 0);
}

tree::TerminalNode* McInstrParser::InstrumentParameterStringContext::Null() {
  return getToken(McInstrParser::Null, 0);
}

McInstrParser::InstrumentParameterStringContext::InstrumentParameterStringContext(Instrument_parameterContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InstrumentParameterStringContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstrumentParameterString(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::Instrument_parameterContext* McInstrParser::instrument_parameter() {
  Instrument_parameterContext *_localctx = _tracker.createInstance<Instrument_parameterContext>(_ctx, getState());
  enterRule(_localctx, 6, McInstrParser::RuleInstrument_parameter);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(161);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case McInstrParser::Double:
      case McInstrParser::Identifier: {
        _localctx = _tracker.createInstance<McInstrParser::InstrumentParameterDoubleContext>(_localctx);
        enterOuterAlt(_localctx, 1);
        setState(129);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::Double) {
          setState(128);
          match(McInstrParser::Double);
        }
        setState(131);
        match(McInstrParser::Identifier);
        setState(133);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::Div) {
          setState(132);
          instrument_parameter_unit();
        }
        setState(137);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::Assign) {
          setState(135);
          match(McInstrParser::Assign);
          setState(136);
          expr(0);
        }
        break;
      }

      case McInstrParser::Int: {
        _localctx = _tracker.createInstance<McInstrParser::InstrumentParameterIntegerContext>(_localctx);
        enterOuterAlt(_localctx, 2);
        setState(139);
        match(McInstrParser::Int);
        setState(140);
        match(McInstrParser::Identifier);
        setState(142);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::Div) {
          setState(141);
          instrument_parameter_unit();
        }
        setState(146);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::Assign) {
          setState(144);
          match(McInstrParser::Assign);
          setState(145);
          expr(0);
        }
        break;
      }

      case McInstrParser::String:
      case McInstrParser::Char: {
        _localctx = _tracker.createInstance<McInstrParser::InstrumentParameterStringContext>(_localctx);
        enterOuterAlt(_localctx, 3);
        setState(151);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case McInstrParser::String: {
            setState(148);
            match(McInstrParser::String);
            break;
          }

          case McInstrParser::Char: {
            setState(149);
            match(McInstrParser::Char);
            setState(150);
            match(McInstrParser::Star);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        setState(153);
        match(McInstrParser::Identifier);
        setState(155);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::Div) {
          setState(154);
          instrument_parameter_unit();
        }
        setState(159);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::Assign) {
          setState(157);
          match(McInstrParser::Assign);
          setState(158);
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

//----------------- Instrument_parameter_unitContext ------------------------------------------------------------------

McInstrParser::Instrument_parameter_unitContext::Instrument_parameter_unitContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::Instrument_parameter_unitContext::Div() {
  return getToken(McInstrParser::Div, 0);
}

tree::TerminalNode* McInstrParser::Instrument_parameter_unitContext::StringLiteral() {
  return getToken(McInstrParser::StringLiteral, 0);
}


size_t McInstrParser::Instrument_parameter_unitContext::getRuleIndex() const {
  return McInstrParser::RuleInstrument_parameter_unit;
}


std::any McInstrParser::Instrument_parameter_unitContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstrument_parameter_unit(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Instrument_parameter_unitContext* McInstrParser::instrument_parameter_unit() {
  Instrument_parameter_unitContext *_localctx = _tracker.createInstance<Instrument_parameter_unitContext>(_ctx, getState());
  enterRule(_localctx, 8, McInstrParser::RuleInstrument_parameter_unit);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(163);
    match(McInstrParser::Div);
    setState(164);
    match(McInstrParser::StringLiteral);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Instrument_traceContext ------------------------------------------------------------------

McInstrParser::Instrument_traceContext::Instrument_traceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::Instrument_traceContext::Trace() {
  return getToken(McInstrParser::Trace, 0);
}

std::vector<McInstrParser::Component_instanceContext *> McInstrParser::Instrument_traceContext::component_instance() {
  return getRuleContexts<McInstrParser::Component_instanceContext>();
}

McInstrParser::Component_instanceContext* McInstrParser::Instrument_traceContext::component_instance(size_t i) {
  return getRuleContext<McInstrParser::Component_instanceContext>(i);
}

std::vector<McInstrParser::SearchContext *> McInstrParser::Instrument_traceContext::search() {
  return getRuleContexts<McInstrParser::SearchContext>();
}

McInstrParser::SearchContext* McInstrParser::Instrument_traceContext::search(size_t i) {
  return getRuleContext<McInstrParser::SearchContext>(i);
}

std::vector<McInstrParser::Instrument_trace_includeContext *> McInstrParser::Instrument_traceContext::instrument_trace_include() {
  return getRuleContexts<McInstrParser::Instrument_trace_includeContext>();
}

McInstrParser::Instrument_trace_includeContext* McInstrParser::Instrument_traceContext::instrument_trace_include(size_t i) {
  return getRuleContext<McInstrParser::Instrument_trace_includeContext>(i);
}


size_t McInstrParser::Instrument_traceContext::getRuleIndex() const {
  return McInstrParser::RuleInstrument_trace;
}


std::any McInstrParser::Instrument_traceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstrument_trace(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Instrument_traceContext* McInstrParser::instrument_trace() {
  Instrument_traceContext *_localctx = _tracker.createInstance<Instrument_traceContext>(_ctx, getState());
  enterRule(_localctx, 10, McInstrParser::RuleInstrument_trace);
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
    setState(166);
    match(McInstrParser::Trace);
    setState(174);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 143177029779584) != 0)) {
      setState(170); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(170);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case McInstrParser::Component:
          case McInstrParser::Split:
          case McInstrParser::Removable:
          case McInstrParser::Cpu: {
            setState(167);
            component_instance();
            break;
          }

          case McInstrParser::Search: {
            setState(168);
            search();
            break;
          }

          case McInstrParser::Include: {
            setState(169);
            instrument_trace_include();
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        setState(172); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while ((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 143177029779584) != 0));
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Instrument_metadataContext ------------------------------------------------------------------

McInstrParser::Instrument_metadataContext::Instrument_metadataContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<McInstrParser::MetadataContext *> McInstrParser::Instrument_metadataContext::metadata() {
  return getRuleContexts<McInstrParser::MetadataContext>();
}

McInstrParser::MetadataContext* McInstrParser::Instrument_metadataContext::metadata(size_t i) {
  return getRuleContext<McInstrParser::MetadataContext>(i);
}


size_t McInstrParser::Instrument_metadataContext::getRuleIndex() const {
  return McInstrParser::RuleInstrument_metadata;
}


std::any McInstrParser::Instrument_metadataContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstrument_metadata(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Instrument_metadataContext* McInstrParser::instrument_metadata() {
  Instrument_metadataContext *_localctx = _tracker.createInstance<Instrument_metadataContext>(_ctx, getState());
  enterRule(_localctx, 12, McInstrParser::RuleInstrument_metadata);
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
    setState(177); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(176);
      metadata();
      setState(179); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == McInstrParser::MetaData);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Instrument_trace_includeContext ------------------------------------------------------------------

McInstrParser::Instrument_trace_includeContext::Instrument_trace_includeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::Instrument_trace_includeContext::Include() {
  return getToken(McInstrParser::Include, 0);
}

tree::TerminalNode* McInstrParser::Instrument_trace_includeContext::StringLiteral() {
  return getToken(McInstrParser::StringLiteral, 0);
}


size_t McInstrParser::Instrument_trace_includeContext::getRuleIndex() const {
  return McInstrParser::RuleInstrument_trace_include;
}


std::any McInstrParser::Instrument_trace_includeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstrument_trace_include(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Instrument_trace_includeContext* McInstrParser::instrument_trace_include() {
  Instrument_trace_includeContext *_localctx = _tracker.createInstance<Instrument_trace_includeContext>(_ctx, getState());
  enterRule(_localctx, 14, McInstrParser::RuleInstrument_trace_include);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(181);
    match(McInstrParser::Include);
    setState(182);
    match(McInstrParser::StringLiteral);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_instanceContext ------------------------------------------------------------------

McInstrParser::Component_instanceContext::Component_instanceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::Component_instanceContext::Component() {
  return getToken(McInstrParser::Component, 0);
}

McInstrParser::Instance_nameContext* McInstrParser::Component_instanceContext::instance_name() {
  return getRuleContext<McInstrParser::Instance_nameContext>(0);
}

tree::TerminalNode* McInstrParser::Component_instanceContext::Assign() {
  return getToken(McInstrParser::Assign, 0);
}

McInstrParser::Component_typeContext* McInstrParser::Component_instanceContext::component_type() {
  return getRuleContext<McInstrParser::Component_typeContext>(0);
}

McInstrParser::PlaceContext* McInstrParser::Component_instanceContext::place() {
  return getRuleContext<McInstrParser::PlaceContext>(0);
}

tree::TerminalNode* McInstrParser::Component_instanceContext::Removable() {
  return getToken(McInstrParser::Removable, 0);
}

tree::TerminalNode* McInstrParser::Component_instanceContext::Cpu() {
  return getToken(McInstrParser::Cpu, 0);
}

McInstrParser::SplitContext* McInstrParser::Component_instanceContext::split() {
  return getRuleContext<McInstrParser::SplitContext>(0);
}

McInstrParser::Instance_parametersContext* McInstrParser::Component_instanceContext::instance_parameters() {
  return getRuleContext<McInstrParser::Instance_parametersContext>(0);
}

McInstrParser::WhenContext* McInstrParser::Component_instanceContext::when() {
  return getRuleContext<McInstrParser::WhenContext>(0);
}

McInstrParser::OrientationContext* McInstrParser::Component_instanceContext::orientation() {
  return getRuleContext<McInstrParser::OrientationContext>(0);
}

McInstrParser::GrouprefContext* McInstrParser::Component_instanceContext::groupref() {
  return getRuleContext<McInstrParser::GrouprefContext>(0);
}

McInstrParser::ExtendContext* McInstrParser::Component_instanceContext::extend() {
  return getRuleContext<McInstrParser::ExtendContext>(0);
}

McInstrParser::JumpsContext* McInstrParser::Component_instanceContext::jumps() {
  return getRuleContext<McInstrParser::JumpsContext>(0);
}

std::vector<McInstrParser::MetadataContext *> McInstrParser::Component_instanceContext::metadata() {
  return getRuleContexts<McInstrParser::MetadataContext>();
}

McInstrParser::MetadataContext* McInstrParser::Component_instanceContext::metadata(size_t i) {
  return getRuleContext<McInstrParser::MetadataContext>(i);
}


size_t McInstrParser::Component_instanceContext::getRuleIndex() const {
  return McInstrParser::RuleComponent_instance;
}


std::any McInstrParser::Component_instanceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitComponent_instance(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Component_instanceContext* McInstrParser::component_instance() {
  Component_instanceContext *_localctx = _tracker.createInstance<Component_instanceContext>(_ctx, getState());
  enterRule(_localctx, 16, McInstrParser::RuleComponent_instance);
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
    setState(185);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Removable) {
      setState(184);
      match(McInstrParser::Removable);
    }
    setState(188);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Cpu) {
      setState(187);
      match(McInstrParser::Cpu);
    }
    setState(191);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Split) {
      setState(190);
      split();
    }
    setState(193);
    match(McInstrParser::Component);
    setState(194);
    instance_name();
    setState(195);
    match(McInstrParser::Assign);
    setState(196);
    component_type();
    setState(198);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::LeftParen) {
      setState(197);
      instance_parameters();
    }
    setState(201);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::When) {
      setState(200);
      when();
    }
    setState(203);
    place();
    setState(205);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Rotated) {
      setState(204);
      orientation();
    }
    setState(208);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Group) {
      setState(207);
      groupref();
    }
    setState(211);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Extend) {
      setState(210);
      extend();
    }
    setState(214);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Jump) {
      setState(213);
      jumps();
    }
    setState(219);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == McInstrParser::MetaData) {
      setState(216);
      metadata();
      setState(221);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Instance_nameContext ------------------------------------------------------------------

McInstrParser::Instance_nameContext::Instance_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::Instance_nameContext::getRuleIndex() const {
  return McInstrParser::RuleInstance_name;
}

void McInstrParser::Instance_nameContext::copyFrom(Instance_nameContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- InstanceNameCopyIdentifierContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InstanceNameCopyIdentifierContext::Copy() {
  return getToken(McInstrParser::Copy, 0);
}

tree::TerminalNode* McInstrParser::InstanceNameCopyIdentifierContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

tree::TerminalNode* McInstrParser::InstanceNameCopyIdentifierContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::InstanceNameCopyIdentifierContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}

McInstrParser::InstanceNameCopyIdentifierContext::InstanceNameCopyIdentifierContext(Instance_nameContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InstanceNameCopyIdentifierContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstanceNameCopyIdentifier(this);
  else
    return visitor->visitChildren(this);
}
//----------------- InstanceNameCopyContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InstanceNameCopyContext::Myself() {
  return getToken(McInstrParser::Myself, 0);
}

tree::TerminalNode* McInstrParser::InstanceNameCopyContext::Copy() {
  return getToken(McInstrParser::Copy, 0);
}

McInstrParser::InstanceNameCopyContext::InstanceNameCopyContext(Instance_nameContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InstanceNameCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstanceNameCopy(this);
  else
    return visitor->visitChildren(this);
}
//----------------- InstanceNameIdentifierContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InstanceNameIdentifierContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

McInstrParser::InstanceNameIdentifierContext::InstanceNameIdentifierContext(Instance_nameContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InstanceNameIdentifierContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstanceNameIdentifier(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::Instance_nameContext* McInstrParser::instance_name() {
  Instance_nameContext *_localctx = _tracker.createInstance<Instance_nameContext>(_ctx, getState());
  enterRule(_localctx, 18, McInstrParser::RuleInstance_name);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(228);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 34, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McInstrParser::InstanceNameCopyIdentifierContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(222);
      match(McInstrParser::Copy);
      setState(223);
      match(McInstrParser::LeftParen);
      setState(224);
      match(McInstrParser::Identifier);
      setState(225);
      match(McInstrParser::RightParen);
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McInstrParser::InstanceNameCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(226);
      _la = _input->LA(1);
      if (!(_la == McInstrParser::Myself

      || _la == McInstrParser::Copy)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      break;
    }

    case 3: {
      _localctx = _tracker.createInstance<McInstrParser::InstanceNameIdentifierContext>(_localctx);
      enterOuterAlt(_localctx, 3);
      setState(227);
      match(McInstrParser::Identifier);
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

//----------------- Component_typeContext ------------------------------------------------------------------

McInstrParser::Component_typeContext::Component_typeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::Component_typeContext::getRuleIndex() const {
  return McInstrParser::RuleComponent_type;
}

void McInstrParser::Component_typeContext::copyFrom(Component_typeContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- ComponentTypeIdentifierContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ComponentTypeIdentifierContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

McInstrParser::ComponentTypeIdentifierContext::ComponentTypeIdentifierContext(Component_typeContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ComponentTypeIdentifierContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitComponentTypeIdentifier(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ComponentTypeCopyContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ComponentTypeCopyContext::Copy() {
  return getToken(McInstrParser::Copy, 0);
}

tree::TerminalNode* McInstrParser::ComponentTypeCopyContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

McInstrParser::Component_refContext* McInstrParser::ComponentTypeCopyContext::component_ref() {
  return getRuleContext<McInstrParser::Component_refContext>(0);
}

tree::TerminalNode* McInstrParser::ComponentTypeCopyContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}

McInstrParser::ComponentTypeCopyContext::ComponentTypeCopyContext(Component_typeContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ComponentTypeCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitComponentTypeCopy(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::Component_typeContext* McInstrParser::component_type() {
  Component_typeContext *_localctx = _tracker.createInstance<Component_typeContext>(_ctx, getState());
  enterRule(_localctx, 20, McInstrParser::RuleComponent_type);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(236);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case McInstrParser::Copy: {
        _localctx = _tracker.createInstance<McInstrParser::ComponentTypeCopyContext>(_localctx);
        enterOuterAlt(_localctx, 1);
        setState(230);
        match(McInstrParser::Copy);
        setState(231);
        match(McInstrParser::LeftParen);
        setState(232);
        component_ref();
        setState(233);
        match(McInstrParser::RightParen);
        break;
      }

      case McInstrParser::Identifier: {
        _localctx = _tracker.createInstance<McInstrParser::ComponentTypeIdentifierContext>(_localctx);
        enterOuterAlt(_localctx, 2);
        setState(235);
        match(McInstrParser::Identifier);
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

//----------------- Instance_parametersContext ------------------------------------------------------------------

McInstrParser::Instance_parametersContext::Instance_parametersContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::Instance_parametersContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

tree::TerminalNode* McInstrParser::Instance_parametersContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}

std::vector<McInstrParser::Instance_parameterContext *> McInstrParser::Instance_parametersContext::instance_parameter() {
  return getRuleContexts<McInstrParser::Instance_parameterContext>();
}

McInstrParser::Instance_parameterContext* McInstrParser::Instance_parametersContext::instance_parameter(size_t i) {
  return getRuleContext<McInstrParser::Instance_parameterContext>(i);
}

std::vector<tree::TerminalNode *> McInstrParser::Instance_parametersContext::Comma() {
  return getTokens(McInstrParser::Comma);
}

tree::TerminalNode* McInstrParser::Instance_parametersContext::Comma(size_t i) {
  return getToken(McInstrParser::Comma, i);
}


size_t McInstrParser::Instance_parametersContext::getRuleIndex() const {
  return McInstrParser::RuleInstance_parameters;
}


std::any McInstrParser::Instance_parametersContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstance_parameters(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Instance_parametersContext* McInstrParser::instance_parameters() {
  Instance_parametersContext *_localctx = _tracker.createInstance<Instance_parametersContext>(_ctx, getState());
  enterRule(_localctx, 22, McInstrParser::RuleInstance_parameters);
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
    setState(238);
    match(McInstrParser::LeftParen);
    setState(247);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == McInstrParser::Identifier) {
      setState(239);
      antlrcpp::downCast<Instance_parametersContext *>(_localctx)->instance_parameterContext = instance_parameter();
      antlrcpp::downCast<Instance_parametersContext *>(_localctx)->params.push_back(antlrcpp::downCast<Instance_parametersContext *>(_localctx)->instance_parameterContext);
      setState(244);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == McInstrParser::Comma) {
        setState(240);
        match(McInstrParser::Comma);
        setState(241);
        antlrcpp::downCast<Instance_parametersContext *>(_localctx)->instance_parameterContext = instance_parameter();
        antlrcpp::downCast<Instance_parametersContext *>(_localctx)->params.push_back(antlrcpp::downCast<Instance_parametersContext *>(_localctx)->instance_parameterContext);
        setState(246);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(249);
    match(McInstrParser::RightParen);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Instance_parameterContext ------------------------------------------------------------------

McInstrParser::Instance_parameterContext::Instance_parameterContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::Instance_parameterContext::getRuleIndex() const {
  return McInstrParser::RuleInstance_parameter;
}

void McInstrParser::Instance_parameterContext::copyFrom(Instance_parameterContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- InstanceParameterExprContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InstanceParameterExprContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::InstanceParameterExprContext::Assign() {
  return getToken(McInstrParser::Assign, 0);
}

McInstrParser::ExprContext* McInstrParser::InstanceParameterExprContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

McInstrParser::InstanceParameterExprContext::InstanceParameterExprContext(Instance_parameterContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InstanceParameterExprContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstanceParameterExpr(this);
  else
    return visitor->visitChildren(this);
}
//----------------- InstanceParameterNullContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InstanceParameterNullContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::InstanceParameterNullContext::Assign() {
  return getToken(McInstrParser::Assign, 0);
}

tree::TerminalNode* McInstrParser::InstanceParameterNullContext::Null() {
  return getToken(McInstrParser::Null, 0);
}

McInstrParser::InstanceParameterNullContext::InstanceParameterNullContext(Instance_parameterContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InstanceParameterNullContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstanceParameterNull(this);
  else
    return visitor->visitChildren(this);
}
//----------------- InstanceParameterVectorContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InstanceParameterVectorContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::InstanceParameterVectorContext::Assign() {
  return getToken(McInstrParser::Assign, 0);
}

McInstrParser::InitializerlistContext* McInstrParser::InstanceParameterVectorContext::initializerlist() {
  return getRuleContext<McInstrParser::InitializerlistContext>(0);
}

McInstrParser::InstanceParameterVectorContext::InstanceParameterVectorContext(Instance_parameterContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InstanceParameterVectorContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInstanceParameterVector(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::Instance_parameterContext* McInstrParser::instance_parameter() {
  Instance_parameterContext *_localctx = _tracker.createInstance<Instance_parameterContext>(_ctx, getState());
  enterRule(_localctx, 24, McInstrParser::RuleInstance_parameter);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(260);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McInstrParser::InstanceParameterExprContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(251);
      match(McInstrParser::Identifier);
      setState(252);
      match(McInstrParser::Assign);
      setState(253);
      expr(0);
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McInstrParser::InstanceParameterNullContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(254);
      match(McInstrParser::Identifier);
      setState(255);
      match(McInstrParser::Assign);
      setState(256);
      match(McInstrParser::Null);
      break;
    }

    case 3: {
      _localctx = _tracker.createInstance<McInstrParser::InstanceParameterVectorContext>(_localctx);
      enterOuterAlt(_localctx, 3);
      setState(257);
      match(McInstrParser::Identifier);
      setState(258);
      match(McInstrParser::Assign);
      setState(259);
      initializerlist();
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

//----------------- SplitContext ------------------------------------------------------------------

McInstrParser::SplitContext::SplitContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::SplitContext::Split() {
  return getToken(McInstrParser::Split, 0);
}

McInstrParser::ExprContext* McInstrParser::SplitContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}


size_t McInstrParser::SplitContext::getRuleIndex() const {
  return McInstrParser::RuleSplit;
}


std::any McInstrParser::SplitContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitSplit(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::SplitContext* McInstrParser::split() {
  SplitContext *_localctx = _tracker.createInstance<SplitContext>(_ctx, getState());
  enterRule(_localctx, 26, McInstrParser::RuleSplit);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(262);
    match(McInstrParser::Split);
    setState(265);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 39, _ctx)) {
    case 1: {
      break;
    }

    case 2: {
      setState(264);
      expr(0);
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

//----------------- WhenContext ------------------------------------------------------------------

McInstrParser::WhenContext::WhenContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::WhenContext::When() {
  return getToken(McInstrParser::When, 0);
}

McInstrParser::ExprContext* McInstrParser::WhenContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}


size_t McInstrParser::WhenContext::getRuleIndex() const {
  return McInstrParser::RuleWhen;
}


std::any McInstrParser::WhenContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitWhen(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::WhenContext* McInstrParser::when() {
  WhenContext *_localctx = _tracker.createInstance<WhenContext>(_ctx, getState());
  enterRule(_localctx, 28, McInstrParser::RuleWhen);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(267);
    match(McInstrParser::When);
    setState(268);
    expr(0);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- PlaceContext ------------------------------------------------------------------

McInstrParser::PlaceContext::PlaceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::PlaceContext::At() {
  return getToken(McInstrParser::At, 0);
}

McInstrParser::CoordsContext* McInstrParser::PlaceContext::coords() {
  return getRuleContext<McInstrParser::CoordsContext>(0);
}

McInstrParser::ReferenceContext* McInstrParser::PlaceContext::reference() {
  return getRuleContext<McInstrParser::ReferenceContext>(0);
}


size_t McInstrParser::PlaceContext::getRuleIndex() const {
  return McInstrParser::RulePlace;
}


std::any McInstrParser::PlaceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitPlace(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::PlaceContext* McInstrParser::place() {
  PlaceContext *_localctx = _tracker.createInstance<PlaceContext>(_ctx, getState());
  enterRule(_localctx, 30, McInstrParser::RulePlace);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(270);
    match(McInstrParser::At);
    setState(271);
    coords();
    setState(272);
    reference();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- OrientationContext ------------------------------------------------------------------

McInstrParser::OrientationContext::OrientationContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::OrientationContext::Rotated() {
  return getToken(McInstrParser::Rotated, 0);
}

McInstrParser::CoordsContext* McInstrParser::OrientationContext::coords() {
  return getRuleContext<McInstrParser::CoordsContext>(0);
}

McInstrParser::ReferenceContext* McInstrParser::OrientationContext::reference() {
  return getRuleContext<McInstrParser::ReferenceContext>(0);
}


size_t McInstrParser::OrientationContext::getRuleIndex() const {
  return McInstrParser::RuleOrientation;
}


std::any McInstrParser::OrientationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitOrientation(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::OrientationContext* McInstrParser::orientation() {
  OrientationContext *_localctx = _tracker.createInstance<OrientationContext>(_ctx, getState());
  enterRule(_localctx, 32, McInstrParser::RuleOrientation);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(274);
    match(McInstrParser::Rotated);
    setState(275);
    coords();
    setState(276);
    reference();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- GrouprefContext ------------------------------------------------------------------

McInstrParser::GrouprefContext::GrouprefContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::GrouprefContext::Group() {
  return getToken(McInstrParser::Group, 0);
}

tree::TerminalNode* McInstrParser::GrouprefContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}


size_t McInstrParser::GrouprefContext::getRuleIndex() const {
  return McInstrParser::RuleGroupref;
}


std::any McInstrParser::GrouprefContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitGroupref(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::GrouprefContext* McInstrParser::groupref() {
  GrouprefContext *_localctx = _tracker.createInstance<GrouprefContext>(_ctx, getState());
  enterRule(_localctx, 34, McInstrParser::RuleGroupref);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(278);
    match(McInstrParser::Group);
    setState(279);
    match(McInstrParser::Identifier);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- JumpsContext ------------------------------------------------------------------

McInstrParser::JumpsContext::JumpsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<McInstrParser::JumpContext *> McInstrParser::JumpsContext::jump() {
  return getRuleContexts<McInstrParser::JumpContext>();
}

McInstrParser::JumpContext* McInstrParser::JumpsContext::jump(size_t i) {
  return getRuleContext<McInstrParser::JumpContext>(i);
}


size_t McInstrParser::JumpsContext::getRuleIndex() const {
  return McInstrParser::RuleJumps;
}


std::any McInstrParser::JumpsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitJumps(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::JumpsContext* McInstrParser::jumps() {
  JumpsContext *_localctx = _tracker.createInstance<JumpsContext>(_ctx, getState());
  enterRule(_localctx, 36, McInstrParser::RuleJumps);
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
    setState(282); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(281);
      jump();
      setState(284); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == McInstrParser::Jump);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- JumpContext ------------------------------------------------------------------

McInstrParser::JumpContext::JumpContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::JumpContext::Jump() {
  return getToken(McInstrParser::Jump, 0);
}

McInstrParser::JumpnameContext* McInstrParser::JumpContext::jumpname() {
  return getRuleContext<McInstrParser::JumpnameContext>(0);
}

McInstrParser::ExprContext* McInstrParser::JumpContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

tree::TerminalNode* McInstrParser::JumpContext::When() {
  return getToken(McInstrParser::When, 0);
}

tree::TerminalNode* McInstrParser::JumpContext::Iterate() {
  return getToken(McInstrParser::Iterate, 0);
}


size_t McInstrParser::JumpContext::getRuleIndex() const {
  return McInstrParser::RuleJump;
}


std::any McInstrParser::JumpContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitJump(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::JumpContext* McInstrParser::jump() {
  JumpContext *_localctx = _tracker.createInstance<JumpContext>(_ctx, getState());
  enterRule(_localctx, 38, McInstrParser::RuleJump);
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
    setState(286);
    match(McInstrParser::Jump);
    setState(287);
    jumpname();
    setState(288);
    _la = _input->LA(1);
    if (!(_la == McInstrParser::When

    || _la == McInstrParser::Iterate)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(289);
    expr(0);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- JumpnameContext ------------------------------------------------------------------

McInstrParser::JumpnameContext::JumpnameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::JumpnameContext::getRuleIndex() const {
  return McInstrParser::RuleJumpname;
}

void McInstrParser::JumpnameContext::copyFrom(JumpnameContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- JumpPreviousContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::JumpPreviousContext::Previous() {
  return getToken(McInstrParser::Previous, 0);
}

tree::TerminalNode* McInstrParser::JumpPreviousContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

tree::TerminalNode* McInstrParser::JumpPreviousContext::IntegerLiteral() {
  return getToken(McInstrParser::IntegerLiteral, 0);
}

tree::TerminalNode* McInstrParser::JumpPreviousContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}

McInstrParser::JumpPreviousContext::JumpPreviousContext(JumpnameContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::JumpPreviousContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitJumpPrevious(this);
  else
    return visitor->visitChildren(this);
}
//----------------- JumpMyselfContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::JumpMyselfContext::Myself() {
  return getToken(McInstrParser::Myself, 0);
}

McInstrParser::JumpMyselfContext::JumpMyselfContext(JumpnameContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::JumpMyselfContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitJumpMyself(this);
  else
    return visitor->visitChildren(this);
}
//----------------- JumpIdentifierContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::JumpIdentifierContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

McInstrParser::JumpIdentifierContext::JumpIdentifierContext(JumpnameContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::JumpIdentifierContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitJumpIdentifier(this);
  else
    return visitor->visitChildren(this);
}
//----------------- JumpNextContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::JumpNextContext::Next() {
  return getToken(McInstrParser::Next, 0);
}

tree::TerminalNode* McInstrParser::JumpNextContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

tree::TerminalNode* McInstrParser::JumpNextContext::IntegerLiteral() {
  return getToken(McInstrParser::IntegerLiteral, 0);
}

tree::TerminalNode* McInstrParser::JumpNextContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}

McInstrParser::JumpNextContext::JumpNextContext(JumpnameContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::JumpNextContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitJumpNext(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::JumpnameContext* McInstrParser::jumpname() {
  JumpnameContext *_localctx = _tracker.createInstance<JumpnameContext>(_ctx, getState());
  enterRule(_localctx, 40, McInstrParser::RuleJumpname);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(305);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case McInstrParser::Previous: {
        _localctx = _tracker.createInstance<McInstrParser::JumpPreviousContext>(_localctx);
        enterOuterAlt(_localctx, 1);
        setState(291);
        match(McInstrParser::Previous);
        setState(295);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::LeftParen) {
          setState(292);
          match(McInstrParser::LeftParen);
          setState(293);
          match(McInstrParser::IntegerLiteral);
          setState(294);
          match(McInstrParser::RightParen);
        }
        break;
      }

      case McInstrParser::Myself: {
        _localctx = _tracker.createInstance<McInstrParser::JumpMyselfContext>(_localctx);
        enterOuterAlt(_localctx, 2);
        setState(297);
        match(McInstrParser::Myself);
        break;
      }

      case McInstrParser::Next: {
        _localctx = _tracker.createInstance<McInstrParser::JumpNextContext>(_localctx);
        enterOuterAlt(_localctx, 3);
        setState(298);
        match(McInstrParser::Next);
        setState(302);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::LeftParen) {
          setState(299);
          match(McInstrParser::LeftParen);
          setState(300);
          match(McInstrParser::IntegerLiteral);
          setState(301);
          match(McInstrParser::RightParen);
        }
        break;
      }

      case McInstrParser::Identifier: {
        _localctx = _tracker.createInstance<McInstrParser::JumpIdentifierContext>(_localctx);
        enterOuterAlt(_localctx, 4);
        setState(304);
        match(McInstrParser::Identifier);
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

//----------------- ExtendContext ------------------------------------------------------------------

McInstrParser::ExtendContext::ExtendContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::ExtendContext::Extend() {
  return getToken(McInstrParser::Extend, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::ExtendContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}


size_t McInstrParser::ExtendContext::getRuleIndex() const {
  return McInstrParser::RuleExtend;
}


std::any McInstrParser::ExtendContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExtend(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::ExtendContext* McInstrParser::extend() {
  ExtendContext *_localctx = _tracker.createInstance<ExtendContext>(_ctx, getState());
  enterRule(_localctx, 42, McInstrParser::RuleExtend);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(307);
    match(McInstrParser::Extend);
    setState(308);
    unparsed_block();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Component_refContext ------------------------------------------------------------------

McInstrParser::Component_refContext::Component_refContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::Component_refContext::Previous() {
  return getToken(McInstrParser::Previous, 0);
}

tree::TerminalNode* McInstrParser::Component_refContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

tree::TerminalNode* McInstrParser::Component_refContext::IntegerLiteral() {
  return getToken(McInstrParser::IntegerLiteral, 0);
}

tree::TerminalNode* McInstrParser::Component_refContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}

tree::TerminalNode* McInstrParser::Component_refContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}


size_t McInstrParser::Component_refContext::getRuleIndex() const {
  return McInstrParser::RuleComponent_ref;
}


std::any McInstrParser::Component_refContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitComponent_ref(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Component_refContext* McInstrParser::component_ref() {
  Component_refContext *_localctx = _tracker.createInstance<Component_refContext>(_ctx, getState());
  enterRule(_localctx, 44, McInstrParser::RuleComponent_ref);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(317);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case McInstrParser::Previous: {
        enterOuterAlt(_localctx, 1);
        setState(310);
        match(McInstrParser::Previous);
        setState(314);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == McInstrParser::LeftParen) {
          setState(311);
          match(McInstrParser::LeftParen);
          setState(312);
          match(McInstrParser::IntegerLiteral);
          setState(313);
          match(McInstrParser::RightParen);
        }
        break;
      }

      case McInstrParser::Identifier: {
        enterOuterAlt(_localctx, 2);
        setState(316);
        match(McInstrParser::Identifier);
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

McInstrParser::CoordsContext::CoordsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::CoordsContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::CoordsContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::CoordsContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

std::vector<tree::TerminalNode *> McInstrParser::CoordsContext::Comma() {
  return getTokens(McInstrParser::Comma);
}

tree::TerminalNode* McInstrParser::CoordsContext::Comma(size_t i) {
  return getToken(McInstrParser::Comma, i);
}

tree::TerminalNode* McInstrParser::CoordsContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}


size_t McInstrParser::CoordsContext::getRuleIndex() const {
  return McInstrParser::RuleCoords;
}


std::any McInstrParser::CoordsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitCoords(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::CoordsContext* McInstrParser::coords() {
  CoordsContext *_localctx = _tracker.createInstance<CoordsContext>(_ctx, getState());
  enterRule(_localctx, 46, McInstrParser::RuleCoords);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(319);
    match(McInstrParser::LeftParen);
    setState(320);
    expr(0);
    setState(321);
    match(McInstrParser::Comma);
    setState(322);
    expr(0);
    setState(323);
    match(McInstrParser::Comma);
    setState(324);
    expr(0);
    setState(325);
    match(McInstrParser::RightParen);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ReferenceContext ------------------------------------------------------------------

McInstrParser::ReferenceContext::ReferenceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::ReferenceContext::Absolute() {
  return getToken(McInstrParser::Absolute, 0);
}

tree::TerminalNode* McInstrParser::ReferenceContext::Relative() {
  return getToken(McInstrParser::Relative, 0);
}

McInstrParser::Component_refContext* McInstrParser::ReferenceContext::component_ref() {
  return getRuleContext<McInstrParser::Component_refContext>(0);
}


size_t McInstrParser::ReferenceContext::getRuleIndex() const {
  return McInstrParser::RuleReference;
}


std::any McInstrParser::ReferenceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitReference(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::ReferenceContext* McInstrParser::reference() {
  ReferenceContext *_localctx = _tracker.createInstance<ReferenceContext>(_ctx, getState());
  enterRule(_localctx, 48, McInstrParser::RuleReference);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(333);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case McInstrParser::Absolute: {
        enterOuterAlt(_localctx, 1);
        setState(327);
        match(McInstrParser::Absolute);
        break;
      }

      case McInstrParser::Relative: {
        enterOuterAlt(_localctx, 2);
        setState(328);
        match(McInstrParser::Relative);
        setState(331);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case McInstrParser::Absolute: {
            setState(329);
            match(McInstrParser::Absolute);
            break;
          }

          case McInstrParser::Previous:
          case McInstrParser::Identifier: {
            setState(330);
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

McInstrParser::DependencyContext::DependencyContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::DependencyContext::Dependency() {
  return getToken(McInstrParser::Dependency, 0);
}

tree::TerminalNode* McInstrParser::DependencyContext::StringLiteral() {
  return getToken(McInstrParser::StringLiteral, 0);
}


size_t McInstrParser::DependencyContext::getRuleIndex() const {
  return McInstrParser::RuleDependency;
}


std::any McInstrParser::DependencyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitDependency(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::DependencyContext* McInstrParser::dependency() {
  DependencyContext *_localctx = _tracker.createInstance<DependencyContext>(_ctx, getState());
  enterRule(_localctx, 50, McInstrParser::RuleDependency);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(335);
    match(McInstrParser::Dependency);
    setState(336);
    match(McInstrParser::StringLiteral);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DeclareContext ------------------------------------------------------------------

McInstrParser::DeclareContext::DeclareContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::DeclareContext::getRuleIndex() const {
  return McInstrParser::RuleDeclare;
}

void McInstrParser::DeclareContext::copyFrom(DeclareContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- DeclareBlockContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::DeclareBlockContext::Declare() {
  return getToken(McInstrParser::Declare, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::DeclareBlockContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}

McInstrParser::DeclareBlockContext::DeclareBlockContext(DeclareContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::DeclareBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitDeclareBlock(this);
  else
    return visitor->visitChildren(this);
}
//----------------- DeclareBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::DeclareBlockCopyContext::Declare() {
  return getToken(McInstrParser::Declare, 0);
}

tree::TerminalNode* McInstrParser::DeclareBlockCopyContext::Copy() {
  return getToken(McInstrParser::Copy, 0);
}

tree::TerminalNode* McInstrParser::DeclareBlockCopyContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::DeclareBlockCopyContext::Extend() {
  return getToken(McInstrParser::Extend, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::DeclareBlockCopyContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}

McInstrParser::DeclareBlockCopyContext::DeclareBlockCopyContext(DeclareContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::DeclareBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitDeclareBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::DeclareContext* McInstrParser::declare() {
  DeclareContext *_localctx = _tracker.createInstance<DeclareContext>(_ctx, getState());
  enterRule(_localctx, 52, McInstrParser::RuleDeclare);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(347);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 49, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McInstrParser::DeclareBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(338);
      match(McInstrParser::Declare);
      setState(339);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McInstrParser::DeclareBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(340);
      match(McInstrParser::Declare);
      setState(341);
      match(McInstrParser::Copy);
      setState(342);
      match(McInstrParser::Identifier);
      setState(345);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McInstrParser::Extend) {
        setState(343);
        match(McInstrParser::Extend);
        setState(344);
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

McInstrParser::UservarsContext::UservarsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::UservarsContext::UserVars() {
  return getToken(McInstrParser::UserVars, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::UservarsContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}


size_t McInstrParser::UservarsContext::getRuleIndex() const {
  return McInstrParser::RuleUservars;
}


std::any McInstrParser::UservarsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitUservars(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::UservarsContext* McInstrParser::uservars() {
  UservarsContext *_localctx = _tracker.createInstance<UservarsContext>(_ctx, getState());
  enterRule(_localctx, 54, McInstrParser::RuleUservars);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(349);
    match(McInstrParser::UserVars);
    setState(350);
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

McInstrParser::InitializeContext::InitializeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::InitializeContext::getRuleIndex() const {
  return McInstrParser::RuleInitialize;
}

void McInstrParser::InitializeContext::copyFrom(InitializeContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- InitializeBlockContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InitializeBlockContext::Initialize() {
  return getToken(McInstrParser::Initialize, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::InitializeBlockContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}

McInstrParser::InitializeBlockContext::InitializeBlockContext(InitializeContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InitializeBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInitializeBlock(this);
  else
    return visitor->visitChildren(this);
}
//----------------- InitializeBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::InitializeBlockCopyContext::Initialize() {
  return getToken(McInstrParser::Initialize, 0);
}

tree::TerminalNode* McInstrParser::InitializeBlockCopyContext::Copy() {
  return getToken(McInstrParser::Copy, 0);
}

tree::TerminalNode* McInstrParser::InitializeBlockCopyContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::InitializeBlockCopyContext::Extend() {
  return getToken(McInstrParser::Extend, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::InitializeBlockCopyContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}

McInstrParser::InitializeBlockCopyContext::InitializeBlockCopyContext(InitializeContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::InitializeBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInitializeBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::InitializeContext* McInstrParser::initialize() {
  InitializeContext *_localctx = _tracker.createInstance<InitializeContext>(_ctx, getState());
  enterRule(_localctx, 56, McInstrParser::RuleInitialize);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(361);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 51, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McInstrParser::InitializeBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(352);
      match(McInstrParser::Initialize);
      setState(353);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McInstrParser::InitializeBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(354);
      match(McInstrParser::Initialize);
      setState(355);
      match(McInstrParser::Copy);
      setState(356);
      match(McInstrParser::Identifier);
      setState(359);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McInstrParser::Extend) {
        setState(357);
        match(McInstrParser::Extend);
        setState(358);
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

McInstrParser::SaveContext::SaveContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::SaveContext::getRuleIndex() const {
  return McInstrParser::RuleSave;
}

void McInstrParser::SaveContext::copyFrom(SaveContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- SaveBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::SaveBlockCopyContext::Save() {
  return getToken(McInstrParser::Save, 0);
}

tree::TerminalNode* McInstrParser::SaveBlockCopyContext::Copy() {
  return getToken(McInstrParser::Copy, 0);
}

tree::TerminalNode* McInstrParser::SaveBlockCopyContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::SaveBlockCopyContext::Extend() {
  return getToken(McInstrParser::Extend, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::SaveBlockCopyContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}

McInstrParser::SaveBlockCopyContext::SaveBlockCopyContext(SaveContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::SaveBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitSaveBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
//----------------- SaveBlockContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::SaveBlockContext::Save() {
  return getToken(McInstrParser::Save, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::SaveBlockContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}

McInstrParser::SaveBlockContext::SaveBlockContext(SaveContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::SaveBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitSaveBlock(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::SaveContext* McInstrParser::save() {
  SaveContext *_localctx = _tracker.createInstance<SaveContext>(_ctx, getState());
  enterRule(_localctx, 58, McInstrParser::RuleSave);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(372);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 53, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McInstrParser::SaveBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(363);
      match(McInstrParser::Save);
      setState(364);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McInstrParser::SaveBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(365);
      match(McInstrParser::Save);
      setState(366);
      match(McInstrParser::Copy);
      setState(367);
      match(McInstrParser::Identifier);
      setState(370);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McInstrParser::Extend) {
        setState(368);
        match(McInstrParser::Extend);
        setState(369);
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

McInstrParser::Finally_Context::Finally_Context(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::Finally_Context::getRuleIndex() const {
  return McInstrParser::RuleFinally_;
}

void McInstrParser::Finally_Context::copyFrom(Finally_Context *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- FinallyBlockContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::FinallyBlockContext::Finally() {
  return getToken(McInstrParser::Finally, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::FinallyBlockContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}

McInstrParser::FinallyBlockContext::FinallyBlockContext(Finally_Context *ctx) { copyFrom(ctx); }


std::any McInstrParser::FinallyBlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitFinallyBlock(this);
  else
    return visitor->visitChildren(this);
}
//----------------- FinallyBlockCopyContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::FinallyBlockCopyContext::Finally() {
  return getToken(McInstrParser::Finally, 0);
}

tree::TerminalNode* McInstrParser::FinallyBlockCopyContext::Copy() {
  return getToken(McInstrParser::Copy, 0);
}

tree::TerminalNode* McInstrParser::FinallyBlockCopyContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::FinallyBlockCopyContext::Extend() {
  return getToken(McInstrParser::Extend, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::FinallyBlockCopyContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}

McInstrParser::FinallyBlockCopyContext::FinallyBlockCopyContext(Finally_Context *ctx) { copyFrom(ctx); }


std::any McInstrParser::FinallyBlockCopyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitFinallyBlockCopy(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::Finally_Context* McInstrParser::finally_() {
  Finally_Context *_localctx = _tracker.createInstance<Finally_Context>(_ctx, getState());
  enterRule(_localctx, 60, McInstrParser::RuleFinally_);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(383);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 55, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McInstrParser::FinallyBlockContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(374);
      match(McInstrParser::Finally);
      setState(375);
      unparsed_block();
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McInstrParser::FinallyBlockCopyContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(376);
      match(McInstrParser::Finally);
      setState(377);
      match(McInstrParser::Copy);
      setState(378);
      match(McInstrParser::Identifier);
      setState(381);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == McInstrParser::Extend) {
        setState(379);
        match(McInstrParser::Extend);
        setState(380);
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

McInstrParser::MetadataContext::MetadataContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::MetadataContext::MetaData() {
  return getToken(McInstrParser::MetaData, 0);
}

McInstrParser::Unparsed_blockContext* McInstrParser::MetadataContext::unparsed_block() {
  return getRuleContext<McInstrParser::Unparsed_blockContext>(0);
}

std::vector<tree::TerminalNode *> McInstrParser::MetadataContext::Identifier() {
  return getTokens(McInstrParser::Identifier);
}

tree::TerminalNode* McInstrParser::MetadataContext::Identifier(size_t i) {
  return getToken(McInstrParser::Identifier, i);
}

std::vector<tree::TerminalNode *> McInstrParser::MetadataContext::StringLiteral() {
  return getTokens(McInstrParser::StringLiteral);
}

tree::TerminalNode* McInstrParser::MetadataContext::StringLiteral(size_t i) {
  return getToken(McInstrParser::StringLiteral, i);
}


size_t McInstrParser::MetadataContext::getRuleIndex() const {
  return McInstrParser::RuleMetadata;
}


std::any McInstrParser::MetadataContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitMetadata(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::MetadataContext* McInstrParser::metadata() {
  MetadataContext *_localctx = _tracker.createInstance<MetadataContext>(_ctx, getState());
  enterRule(_localctx, 62, McInstrParser::RuleMetadata);
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
    setState(385);
    match(McInstrParser::MetaData);
    setState(386);
    antlrcpp::downCast<MetadataContext *>(_localctx)->mime = _input->LT(1);
    _la = _input->LA(1);
    if (!(_la == McInstrParser::StringLiteral || _la == McInstrParser::Identifier)) {
      antlrcpp::downCast<MetadataContext *>(_localctx)->mime = _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(387);
    antlrcpp::downCast<MetadataContext *>(_localctx)->name = _input->LT(1);
    _la = _input->LA(1);
    if (!(_la == McInstrParser::StringLiteral || _la == McInstrParser::Identifier)) {
      antlrcpp::downCast<MetadataContext *>(_localctx)->name = _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(388);
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

McInstrParser::CategoryContext::CategoryContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::CategoryContext::Category() {
  return getToken(McInstrParser::Category, 0);
}

tree::TerminalNode* McInstrParser::CategoryContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::CategoryContext::StringLiteral() {
  return getToken(McInstrParser::StringLiteral, 0);
}


size_t McInstrParser::CategoryContext::getRuleIndex() const {
  return McInstrParser::RuleCategory;
}


std::any McInstrParser::CategoryContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitCategory(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::CategoryContext* McInstrParser::category() {
  CategoryContext *_localctx = _tracker.createInstance<CategoryContext>(_ctx, getState());
  enterRule(_localctx, 64, McInstrParser::RuleCategory);
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
    setState(390);
    match(McInstrParser::Category);
    setState(391);
    _la = _input->LA(1);
    if (!(_la == McInstrParser::StringLiteral || _la == McInstrParser::Identifier)) {
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

McInstrParser::InitializerlistContext::InitializerlistContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::InitializerlistContext::LeftBrace() {
  return getToken(McInstrParser::LeftBrace, 0);
}

tree::TerminalNode* McInstrParser::InitializerlistContext::RightBrace() {
  return getToken(McInstrParser::RightBrace, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::InitializerlistContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::InitializerlistContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

std::vector<tree::TerminalNode *> McInstrParser::InitializerlistContext::Comma() {
  return getTokens(McInstrParser::Comma);
}

tree::TerminalNode* McInstrParser::InitializerlistContext::Comma(size_t i) {
  return getToken(McInstrParser::Comma, i);
}


size_t McInstrParser::InitializerlistContext::getRuleIndex() const {
  return McInstrParser::RuleInitializerlist;
}


std::any McInstrParser::InitializerlistContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitInitializerlist(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::InitializerlistContext* McInstrParser::initializerlist() {
  InitializerlistContext *_localctx = _tracker.createInstance<InitializerlistContext>(_ctx, getState());
  enterRule(_localctx, 66, McInstrParser::RuleInitializerlist);
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
    setState(393);
    match(McInstrParser::LeftBrace);
    setState(394);
    antlrcpp::downCast<InitializerlistContext *>(_localctx)->exprContext = expr(0);
    antlrcpp::downCast<InitializerlistContext *>(_localctx)->values.push_back(antlrcpp::downCast<InitializerlistContext *>(_localctx)->exprContext);
    setState(399);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == McInstrParser::Comma) {
      setState(395);
      match(McInstrParser::Comma);
      setState(396);
      antlrcpp::downCast<InitializerlistContext *>(_localctx)->exprContext = expr(0);
      antlrcpp::downCast<InitializerlistContext *>(_localctx)->values.push_back(antlrcpp::downCast<InitializerlistContext *>(_localctx)->exprContext);
      setState(401);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(402);
    match(McInstrParser::RightBrace);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AssignmentContext ------------------------------------------------------------------

McInstrParser::AssignmentContext::AssignmentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::AssignmentContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::AssignmentContext::Assign() {
  return getToken(McInstrParser::Assign, 0);
}

McInstrParser::ExprContext* McInstrParser::AssignmentContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}


size_t McInstrParser::AssignmentContext::getRuleIndex() const {
  return McInstrParser::RuleAssignment;
}


std::any McInstrParser::AssignmentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitAssignment(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::AssignmentContext* McInstrParser::assignment() {
  AssignmentContext *_localctx = _tracker.createInstance<AssignmentContext>(_ctx, getState());
  enterRule(_localctx, 68, McInstrParser::RuleAssignment);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(404);
    match(McInstrParser::Identifier);
    setState(405);
    match(McInstrParser::Assign);
    setState(406);
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

McInstrParser::ExprContext::ExprContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::ExprContext::getRuleIndex() const {
  return McInstrParser::RuleExpr;
}

void McInstrParser::ExprContext::copyFrom(ExprContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- ExpressionBinaryModContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionBinaryModContext::Mod() {
  return getToken(McInstrParser::Mod, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryModContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryModContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionBinaryModContext::ExpressionBinaryModContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryModContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryMod(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryLessContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionBinaryLessContext::Less() {
  return getToken(McInstrParser::Less, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryLessContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryLessContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionBinaryLessContext::ExpressionBinaryLessContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryLessContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryLess(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryGreaterContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionBinaryGreaterContext::Greater() {
  return getToken(McInstrParser::Greater, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryGreaterContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryGreaterContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionBinaryGreaterContext::ExpressionBinaryGreaterContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryGreaterContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryGreater(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryLessEqualContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionBinaryLessEqualContext::LessEqual() {
  return getToken(McInstrParser::LessEqual, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryLessEqualContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryLessEqualContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionBinaryLessEqualContext::ExpressionBinaryLessEqualContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryLessEqualContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryLessEqual(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionArrayAccessContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionArrayAccessContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::ExpressionArrayAccessContext::LeftBracket() {
  return getToken(McInstrParser::LeftBracket, 0);
}

McInstrParser::ExprContext* McInstrParser::ExpressionArrayAccessContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

tree::TerminalNode* McInstrParser::ExpressionArrayAccessContext::RightBracket() {
  return getToken(McInstrParser::RightBracket, 0);
}

McInstrParser::ExpressionArrayAccessContext::ExpressionArrayAccessContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionArrayAccessContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionArrayAccess(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryLogicContext ------------------------------------------------------------------

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryLogicContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryLogicContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

tree::TerminalNode* McInstrParser::ExpressionBinaryLogicContext::AndAnd() {
  return getToken(McInstrParser::AndAnd, 0);
}

tree::TerminalNode* McInstrParser::ExpressionBinaryLogicContext::OrOr() {
  return getToken(McInstrParser::OrOr, 0);
}

McInstrParser::ExpressionBinaryLogicContext::ExpressionBinaryLogicContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryLogicContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryLogic(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionIntegerContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionIntegerContext::IntegerLiteral() {
  return getToken(McInstrParser::IntegerLiteral, 0);
}

McInstrParser::ExpressionIntegerContext::ExpressionIntegerContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionIntegerContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionInteger(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryRightShiftContext ------------------------------------------------------------------

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryRightShiftContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryRightShiftContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionBinaryRightShiftContext::ExpressionBinaryRightShiftContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryRightShiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryRightShift(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionMyselfContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionMyselfContext::Myself() {
  return getToken(McInstrParser::Myself, 0);
}

McInstrParser::ExpressionMyselfContext::ExpressionMyselfContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionMyselfContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionMyself(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionPreviousContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionPreviousContext::Previous() {
  return getToken(McInstrParser::Previous, 0);
}

McInstrParser::ExpressionPreviousContext::ExpressionPreviousContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionPreviousContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionPrevious(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionIdentifierContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionIdentifierContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

McInstrParser::ExpressionIdentifierContext::ExpressionIdentifierContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionIdentifierContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionIdentifier(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionStructAccessContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionStructAccessContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::ExpressionStructAccessContext::Dot() {
  return getToken(McInstrParser::Dot, 0);
}

McInstrParser::ExprContext* McInstrParser::ExpressionStructAccessContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

McInstrParser::ExpressionStructAccessContext::ExpressionStructAccessContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionStructAccessContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionStructAccess(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionFunctionCallContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionFunctionCallContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::ExpressionFunctionCallContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

tree::TerminalNode* McInstrParser::ExpressionFunctionCallContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionFunctionCallContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionFunctionCallContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

std::vector<tree::TerminalNode *> McInstrParser::ExpressionFunctionCallContext::Comma() {
  return getTokens(McInstrParser::Comma);
}

tree::TerminalNode* McInstrParser::ExpressionFunctionCallContext::Comma(size_t i) {
  return getToken(McInstrParser::Comma, i);
}

McInstrParser::ExpressionFunctionCallContext::ExpressionFunctionCallContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionFunctionCallContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionFunctionCall(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryMDContext ------------------------------------------------------------------

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryMDContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryMDContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

tree::TerminalNode* McInstrParser::ExpressionBinaryMDContext::Star() {
  return getToken(McInstrParser::Star, 0);
}

tree::TerminalNode* McInstrParser::ExpressionBinaryMDContext::Div() {
  return getToken(McInstrParser::Div, 0);
}

McInstrParser::ExpressionBinaryMDContext::ExpressionBinaryMDContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryMDContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryMD(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionStringContext ------------------------------------------------------------------

std::vector<tree::TerminalNode *> McInstrParser::ExpressionStringContext::StringLiteral() {
  return getTokens(McInstrParser::StringLiteral);
}

tree::TerminalNode* McInstrParser::ExpressionStringContext::StringLiteral(size_t i) {
  return getToken(McInstrParser::StringLiteral, i);
}

McInstrParser::ExpressionStringContext::ExpressionStringContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionStringContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionString(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionGroupingContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionGroupingContext::LeftParen() {
  return getToken(McInstrParser::LeftParen, 0);
}

McInstrParser::ExprContext* McInstrParser::ExpressionGroupingContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

tree::TerminalNode* McInstrParser::ExpressionGroupingContext::RightParen() {
  return getToken(McInstrParser::RightParen, 0);
}

McInstrParser::ExpressionGroupingContext::ExpressionGroupingContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionGroupingContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionGrouping(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionExponentiationContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionExponentiationContext::Caret() {
  return getToken(McInstrParser::Caret, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionExponentiationContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionExponentiationContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionExponentiationContext::ExpressionExponentiationContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionExponentiationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionExponentiation(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryLeftShiftContext ------------------------------------------------------------------

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryLeftShiftContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryLeftShiftContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionBinaryLeftShiftContext::ExpressionBinaryLeftShiftContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryLeftShiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryLeftShift(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryGreaterEqualContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionBinaryGreaterEqualContext::GreaterEqual() {
  return getToken(McInstrParser::GreaterEqual, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryGreaterEqualContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryGreaterEqualContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionBinaryGreaterEqualContext::ExpressionBinaryGreaterEqualContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryGreaterEqualContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryGreaterEqual(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionZeroContext ------------------------------------------------------------------

McInstrParser::ExpressionZeroContext::ExpressionZeroContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionZeroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionZero(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionUnaryPMContext ------------------------------------------------------------------

McInstrParser::ExprContext* McInstrParser::ExpressionUnaryPMContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

tree::TerminalNode* McInstrParser::ExpressionUnaryPMContext::Plus() {
  return getToken(McInstrParser::Plus, 0);
}

tree::TerminalNode* McInstrParser::ExpressionUnaryPMContext::Minus() {
  return getToken(McInstrParser::Minus, 0);
}

McInstrParser::ExpressionUnaryPMContext::ExpressionUnaryPMContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionUnaryPMContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionUnaryPM(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionTrinaryLogicContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionTrinaryLogicContext::Question() {
  return getToken(McInstrParser::Question, 0);
}

tree::TerminalNode* McInstrParser::ExpressionTrinaryLogicContext::Colon() {
  return getToken(McInstrParser::Colon, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionTrinaryLogicContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionTrinaryLogicContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionTrinaryLogicContext::ExpressionTrinaryLogicContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionTrinaryLogicContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionTrinaryLogic(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionFloatContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionFloatContext::FloatingLiteral() {
  return getToken(McInstrParser::FloatingLiteral, 0);
}

McInstrParser::ExpressionFloatContext::ExpressionFloatContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionFloatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionFloat(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionPointerAccessContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionPointerAccessContext::Identifier() {
  return getToken(McInstrParser::Identifier, 0);
}

tree::TerminalNode* McInstrParser::ExpressionPointerAccessContext::Arrow() {
  return getToken(McInstrParser::Arrow, 0);
}

McInstrParser::ExprContext* McInstrParser::ExpressionPointerAccessContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

McInstrParser::ExpressionPointerAccessContext::ExpressionPointerAccessContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionPointerAccessContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionPointerAccess(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryEqualContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionBinaryEqualContext::Equal() {
  return getToken(McInstrParser::Equal, 0);
}

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryEqualContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryEqualContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

McInstrParser::ExpressionBinaryEqualContext::ExpressionBinaryEqualContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryEqualContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryEqual(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionBinaryPMContext ------------------------------------------------------------------

std::vector<McInstrParser::ExprContext *> McInstrParser::ExpressionBinaryPMContext::expr() {
  return getRuleContexts<McInstrParser::ExprContext>();
}

McInstrParser::ExprContext* McInstrParser::ExpressionBinaryPMContext::expr(size_t i) {
  return getRuleContext<McInstrParser::ExprContext>(i);
}

tree::TerminalNode* McInstrParser::ExpressionBinaryPMContext::Plus() {
  return getToken(McInstrParser::Plus, 0);
}

tree::TerminalNode* McInstrParser::ExpressionBinaryPMContext::Minus() {
  return getToken(McInstrParser::Minus, 0);
}

McInstrParser::ExpressionBinaryPMContext::ExpressionBinaryPMContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionBinaryPMContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionBinaryPM(this);
  else
    return visitor->visitChildren(this);
}
//----------------- ExpressionUnaryLogicContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::ExpressionUnaryLogicContext::Not() {
  return getToken(McInstrParser::Not, 0);
}

McInstrParser::ExprContext* McInstrParser::ExpressionUnaryLogicContext::expr() {
  return getRuleContext<McInstrParser::ExprContext>(0);
}

McInstrParser::ExpressionUnaryLogicContext::ExpressionUnaryLogicContext(ExprContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::ExpressionUnaryLogicContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitExpressionUnaryLogic(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::ExprContext* McInstrParser::expr() {
   return expr(0);
}

McInstrParser::ExprContext* McInstrParser::expr(int precedence) {
  ParserRuleContext *parentContext = _ctx;
  size_t parentState = getState();
  McInstrParser::ExprContext *_localctx = _tracker.createInstance<ExprContext>(_ctx, parentState);
  McInstrParser::ExprContext *previousContext = _localctx;
  (void)previousContext; // Silence compiler, in case the context is not used by generated code.
  size_t startState = 70;
  enterRecursionRule(_localctx, 70, McInstrParser::RuleExpr, precedence);

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
    setState(452);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<ExpressionZeroContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;

      setState(409);
      match(McInstrParser::T__0);
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<ExpressionIntegerContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(410);
      match(McInstrParser::IntegerLiteral);
      break;
    }

    case 3: {
      _localctx = _tracker.createInstance<ExpressionFloatContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(411);
      match(McInstrParser::FloatingLiteral);
      break;
    }

    case 4: {
      _localctx = _tracker.createInstance<ExpressionStringContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(415);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx);
      while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
        if (alt == 1) {
          setState(412);
          antlrcpp::downCast<ExpressionStringContext *>(_localctx)->stringliteralToken = match(McInstrParser::StringLiteral);
          antlrcpp::downCast<ExpressionStringContext *>(_localctx)->args.push_back(antlrcpp::downCast<ExpressionStringContext *>(_localctx)->stringliteralToken); 
        }
        setState(417);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx);
      }
      break;
    }

    case 5: {
      _localctx = _tracker.createInstance<ExpressionPointerAccessContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(418);
      match(McInstrParser::Identifier);
      setState(419);
      match(McInstrParser::Arrow);
      setState(420);
      expr(23);
      break;
    }

    case 6: {
      _localctx = _tracker.createInstance<ExpressionStructAccessContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(421);
      match(McInstrParser::Identifier);
      setState(422);
      match(McInstrParser::Dot);
      setState(423);
      expr(22);
      break;
    }

    case 7: {
      _localctx = _tracker.createInstance<ExpressionArrayAccessContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(424);
      match(McInstrParser::Identifier);
      setState(425);
      match(McInstrParser::LeftBracket);
      setState(426);
      expr(0);
      setState(427);
      match(McInstrParser::RightBracket);
      break;
    }

    case 8: {
      _localctx = _tracker.createInstance<ExpressionFunctionCallContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(429);
      match(McInstrParser::Identifier);
      setState(430);
      match(McInstrParser::LeftParen);
      setState(431);
      antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->exprContext = expr(0);
      antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->args.push_back(antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->exprContext);
      setState(436);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == McInstrParser::Comma) {
        setState(432);
        match(McInstrParser::Comma);
        setState(433);
        antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->exprContext = expr(0);
        antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->args.push_back(antlrcpp::downCast<ExpressionFunctionCallContext *>(_localctx)->exprContext);
        setState(438);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(439);
      match(McInstrParser::RightParen);
      break;
    }

    case 9: {
      _localctx = _tracker.createInstance<ExpressionGroupingContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(441);
      match(McInstrParser::LeftParen);
      setState(442);
      expr(0);
      setState(443);
      match(McInstrParser::RightParen);
      break;
    }

    case 10: {
      _localctx = _tracker.createInstance<ExpressionUnaryPMContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(445);
      _la = _input->LA(1);
      if (!(_la == McInstrParser::Plus

      || _la == McInstrParser::Minus)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(446);
      expr(18);
      break;
    }

    case 11: {
      _localctx = _tracker.createInstance<ExpressionIdentifierContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(447);
      match(McInstrParser::Identifier);
      break;
    }

    case 12: {
      _localctx = _tracker.createInstance<ExpressionUnaryLogicContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(448);
      match(McInstrParser::Not);
      setState(449);
      expr(5);
      break;
    }

    case 13: {
      _localctx = _tracker.createInstance<ExpressionPreviousContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(450);
      match(McInstrParser::Previous);
      break;
    }

    case 14: {
      _localctx = _tracker.createInstance<ExpressionMyselfContext>(_localctx);
      _ctx = _localctx;
      previousContext = _localctx;
      setState(451);
      match(McInstrParser::Myself);
      break;
    }

    default:
      break;
    }
    _ctx->stop = _input->LT(-1);
    setState(498);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 61, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        if (!_parseListeners.empty())
          triggerExitRuleEvent();
        previousContext = _localctx;
        setState(496);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 60, _ctx)) {
        case 1: {
          auto newContext = _tracker.createInstance<ExpressionExponentiationContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->base = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(454);

          if (!(precpred(_ctx, 17))) throw FailedPredicateException(this, "precpred(_ctx, 17)");
          setState(455);
          match(McInstrParser::Caret);
          setState(456);
          antlrcpp::downCast<ExpressionExponentiationContext *>(_localctx)->exponent = expr(17);
          break;
        }

        case 2: {
          auto newContext = _tracker.createInstance<ExpressionBinaryMDContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(457);

          if (!(precpred(_ctx, 16))) throw FailedPredicateException(this, "precpred(_ctx, 16)");
          setState(458);
          _la = _input->LA(1);
          if (!(_la == McInstrParser::Star

          || _la == McInstrParser::Div)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(459);
          antlrcpp::downCast<ExpressionBinaryMDContext *>(_localctx)->right = expr(17);
          break;
        }

        case 3: {
          auto newContext = _tracker.createInstance<ExpressionBinaryPMContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(460);

          if (!(precpred(_ctx, 15))) throw FailedPredicateException(this, "precpred(_ctx, 15)");
          setState(461);
          _la = _input->LA(1);
          if (!(_la == McInstrParser::Plus

          || _la == McInstrParser::Minus)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(462);
          antlrcpp::downCast<ExpressionBinaryPMContext *>(_localctx)->right = expr(16);
          break;
        }

        case 4: {
          auto newContext = _tracker.createInstance<ExpressionBinaryModContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(463);

          if (!(precpred(_ctx, 14))) throw FailedPredicateException(this, "precpred(_ctx, 14)");
          setState(464);
          match(McInstrParser::Mod);
          setState(465);
          antlrcpp::downCast<ExpressionBinaryModContext *>(_localctx)->right = expr(15);
          break;
        }

        case 5: {
          auto newContext = _tracker.createInstance<ExpressionBinaryRightShiftContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(466);

          if (!(precpred(_ctx, 13))) throw FailedPredicateException(this, "precpred(_ctx, 13)");
          setState(467);
          match(McInstrParser::T__1);
          setState(468);
          antlrcpp::downCast<ExpressionBinaryRightShiftContext *>(_localctx)->right = expr(14);
          break;
        }

        case 6: {
          auto newContext = _tracker.createInstance<ExpressionBinaryLeftShiftContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(469);

          if (!(precpred(_ctx, 12))) throw FailedPredicateException(this, "precpred(_ctx, 12)");
          setState(470);
          match(McInstrParser::T__2);
          setState(471);
          antlrcpp::downCast<ExpressionBinaryLeftShiftContext *>(_localctx)->right = expr(13);
          break;
        }

        case 7: {
          auto newContext = _tracker.createInstance<ExpressionBinaryEqualContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(472);

          if (!(precpred(_ctx, 10))) throw FailedPredicateException(this, "precpred(_ctx, 10)");
          setState(473);
          match(McInstrParser::Equal);
          setState(474);
          antlrcpp::downCast<ExpressionBinaryEqualContext *>(_localctx)->right = expr(11);
          break;
        }

        case 8: {
          auto newContext = _tracker.createInstance<ExpressionBinaryLessEqualContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(475);

          if (!(precpred(_ctx, 9))) throw FailedPredicateException(this, "precpred(_ctx, 9)");
          setState(476);
          match(McInstrParser::LessEqual);
          setState(477);
          antlrcpp::downCast<ExpressionBinaryLessEqualContext *>(_localctx)->right = expr(10);
          break;
        }

        case 9: {
          auto newContext = _tracker.createInstance<ExpressionBinaryGreaterEqualContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(478);

          if (!(precpred(_ctx, 8))) throw FailedPredicateException(this, "precpred(_ctx, 8)");
          setState(479);
          match(McInstrParser::GreaterEqual);
          setState(480);
          antlrcpp::downCast<ExpressionBinaryGreaterEqualContext *>(_localctx)->right = expr(9);
          break;
        }

        case 10: {
          auto newContext = _tracker.createInstance<ExpressionBinaryLessContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(481);

          if (!(precpred(_ctx, 7))) throw FailedPredicateException(this, "precpred(_ctx, 7)");
          setState(482);
          match(McInstrParser::Less);
          setState(483);
          antlrcpp::downCast<ExpressionBinaryLessContext *>(_localctx)->right = expr(8);
          break;
        }

        case 11: {
          auto newContext = _tracker.createInstance<ExpressionBinaryGreaterContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(484);

          if (!(precpred(_ctx, 6))) throw FailedPredicateException(this, "precpred(_ctx, 6)");
          setState(485);
          match(McInstrParser::Greater);
          setState(486);
          antlrcpp::downCast<ExpressionBinaryGreaterContext *>(_localctx)->right = expr(7);
          break;
        }

        case 12: {
          auto newContext = _tracker.createInstance<ExpressionBinaryLogicContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(487);

          if (!(precpred(_ctx, 4))) throw FailedPredicateException(this, "precpred(_ctx, 4)");
          setState(488);
          _la = _input->LA(1);
          if (!(_la == McInstrParser::AndAnd

          || _la == McInstrParser::OrOr)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(489);
          antlrcpp::downCast<ExpressionBinaryLogicContext *>(_localctx)->right = expr(5);
          break;
        }

        case 13: {
          auto newContext = _tracker.createInstance<ExpressionTrinaryLogicContext>(_tracker.createInstance<ExprContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->test = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpr);
          setState(490);

          if (!(precpred(_ctx, 3))) throw FailedPredicateException(this, "precpred(_ctx, 3)");
          setState(491);
          match(McInstrParser::Question);
          setState(492);
          antlrcpp::downCast<ExpressionTrinaryLogicContext *>(_localctx)->true_ = expr(0);
          setState(493);
          match(McInstrParser::Colon);
          setState(494);
          antlrcpp::downCast<ExpressionTrinaryLogicContext *>(_localctx)->false_ = expr(4);
          break;
        }

        default:
          break;
        } 
      }
      setState(500);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 61, _ctx);
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

McInstrParser::ShellContext::ShellContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::ShellContext::Shell() {
  return getToken(McInstrParser::Shell, 0);
}

tree::TerminalNode* McInstrParser::ShellContext::StringLiteral() {
  return getToken(McInstrParser::StringLiteral, 0);
}


size_t McInstrParser::ShellContext::getRuleIndex() const {
  return McInstrParser::RuleShell;
}


std::any McInstrParser::ShellContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitShell(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::ShellContext* McInstrParser::shell() {
  ShellContext *_localctx = _tracker.createInstance<ShellContext>(_ctx, getState());
  enterRule(_localctx, 72, McInstrParser::RuleShell);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(501);
    match(McInstrParser::Shell);
    setState(502);
    match(McInstrParser::StringLiteral);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SearchContext ------------------------------------------------------------------

McInstrParser::SearchContext::SearchContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t McInstrParser::SearchContext::getRuleIndex() const {
  return McInstrParser::RuleSearch;
}

void McInstrParser::SearchContext::copyFrom(SearchContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- SearchPathContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::SearchPathContext::Search() {
  return getToken(McInstrParser::Search, 0);
}

tree::TerminalNode* McInstrParser::SearchPathContext::StringLiteral() {
  return getToken(McInstrParser::StringLiteral, 0);
}

McInstrParser::SearchPathContext::SearchPathContext(SearchContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::SearchPathContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitSearchPath(this);
  else
    return visitor->visitChildren(this);
}
//----------------- SearchShellContext ------------------------------------------------------------------

tree::TerminalNode* McInstrParser::SearchShellContext::Search() {
  return getToken(McInstrParser::Search, 0);
}

tree::TerminalNode* McInstrParser::SearchShellContext::Shell() {
  return getToken(McInstrParser::Shell, 0);
}

tree::TerminalNode* McInstrParser::SearchShellContext::StringLiteral() {
  return getToken(McInstrParser::StringLiteral, 0);
}

McInstrParser::SearchShellContext::SearchShellContext(SearchContext *ctx) { copyFrom(ctx); }


std::any McInstrParser::SearchShellContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitSearchShell(this);
  else
    return visitor->visitChildren(this);
}
McInstrParser::SearchContext* McInstrParser::search() {
  SearchContext *_localctx = _tracker.createInstance<SearchContext>(_ctx, getState());
  enterRule(_localctx, 74, McInstrParser::RuleSearch);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(509);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 62, _ctx)) {
    case 1: {
      _localctx = _tracker.createInstance<McInstrParser::SearchPathContext>(_localctx);
      enterOuterAlt(_localctx, 1);
      setState(504);
      match(McInstrParser::Search);
      setState(505);
      match(McInstrParser::StringLiteral);
      break;
    }

    case 2: {
      _localctx = _tracker.createInstance<McInstrParser::SearchShellContext>(_localctx);
      enterOuterAlt(_localctx, 2);
      setState(506);
      match(McInstrParser::Search);
      setState(507);
      match(McInstrParser::Shell);
      setState(508);
      match(McInstrParser::StringLiteral);
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

McInstrParser::Unparsed_blockContext::Unparsed_blockContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* McInstrParser::Unparsed_blockContext::UnparsedBlock() {
  return getToken(McInstrParser::UnparsedBlock, 0);
}


size_t McInstrParser::Unparsed_blockContext::getRuleIndex() const {
  return McInstrParser::RuleUnparsed_block;
}


std::any McInstrParser::Unparsed_blockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<McInstrVisitor*>(visitor))
    return parserVisitor->visitUnparsed_block(this);
  else
    return visitor->visitChildren(this);
}

McInstrParser::Unparsed_blockContext* McInstrParser::unparsed_block() {
  Unparsed_blockContext *_localctx = _tracker.createInstance<Unparsed_blockContext>(_ctx, getState());
  enterRule(_localctx, 76, McInstrParser::RuleUnparsed_block);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(511);
    match(McInstrParser::UnparsedBlock);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

bool McInstrParser::sempred(RuleContext *context, size_t ruleIndex, size_t predicateIndex) {
  switch (ruleIndex) {
    case 35: return exprSempred(antlrcpp::downCast<ExprContext *>(context), predicateIndex);

  default:
    break;
  }
  return true;
}

bool McInstrParser::exprSempred(ExprContext *_localctx, size_t predicateIndex) {
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

void McInstrParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  mcinstrParserInitialize();
#else
  ::antlr4::internal::call_once(mcinstrParserOnceFlag, mcinstrParserInitialize);
#endif
}
