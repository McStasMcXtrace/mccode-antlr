
// Generated from /home/g/Code/mccode-antlr/src/grammar/McInstr.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  McInstrLexer : public antlr4::Lexer {
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

  explicit McInstrLexer(antlr4::CharStream *input);

  ~McInstrLexer() override;


  std::string getGrammarFileName() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const std::vector<std::string>& getChannelNames() const override;

  const std::vector<std::string>& getModeNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;

  const antlr4::atn::ATN& getATN() const override;

  // By default the static state used to implement the lexer is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:

  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

};

