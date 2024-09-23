grammar McDisplay;
// parse rules
instrument_open: INSTRUMENT COLON Instrument SINGLEQUOTE instrument_name SINGLEQUOTE OPENPAREN abspath CLOSEPAREN;
instrument_end: INSTRUMENT END COLON;
instrument_name: Identifier;

component_definition: COMPONENT ':' '"' component_name '"' POS ':' constants; // Expecting 12 values
component_name: Identifier;

draw_lines: (draw_line)+;
draw_line: draw_header | draw_command | draw_open | draw_close;
draw_header: MCDISPLAY ':' LittleCOMPONENT component_name;
draw_command
 : MANTID_PIXEL ':' constants                                                        #Draw_Mantid_Pixel  // 19 values
 | MANTID_BANANA_DET ':' constants                                                   #Draw_Mantid_Banana // 8 values
 | MANTID_RECTANGULAR_DET ':' constants                                              #Draw_Mantid_Rectangle // 7 values
 | MCDISPLAY ':' drawcall OPENPAREN constants CLOSEPAREN                             #Draw_One
 | MCDISPLAY ':' drawcall OPENPAREN quoted_constant? (COMMA constants )?  CLOSEPAREN #Draw_Three
 ;
draw_open: MCDISPLAY ':' LittleSTART;
draw_close: MCDISPLAY ':' LittleEND;

quoted_constant: SINGLEQUOTE Constant SINGLEQUOTE;
constants: values+=Constant (',' values+=Constant)*;

abspath: (LETTER | DIGIT | '/' | ':' | '\\' | '-' | '_' )+ '.instr';

drawcall
    : (MAGNIFY | LINE | DASHEDLINE | RECTANGLE | BOX | CIRCLE)  #Drawcall_Not_Multiline
    | MULTILINE                                                 #Drawcall_Multiline
    ;


// Tokens
INSTRUMENT: 'INSTRUMENT';
END: 'END';
Instrument: 'Instrument';
COMPONENT: 'COMPONENT';
POS: 'POS';
MCDISPLAY: 'MCDISPLAY';
LittleSTART: 'start';
LittleEND: 'end';
LittleCOMPONENT: 'component';

MAGNIFY: 'magnify';
LINE: 'line';
DASHEDLINE: 'dashed_line';
MULTILINE: 'multiline';
RECTANGLE: 'rectangle';
BOX: 'box';
CIRCLE: 'circle';

MANTID_PIXEL: 'MANTID_PIXEL';
MANTID_BANANA_DET: 'MANTID_BANANA_DET';
MANTID_RECTANGULAR_DET: 'MANTID_RECTANGULAR_DET';

OPENPAREN: '(';
CLOSEPAREN: ')';
COLON: ':';
DOUBLEQUOTE: '"';
SINGLEQUOTE: '\'';
COMMA: ',';
NEWLINE: ('\r' '\n'? | '\n') -> channel(HIDDEN);

NUMBER: '-'? DIGIT+ ('.' DIGIT+ );
LETTER: [a-zA-Z];
DIGIT: [0-9];

WHITESPACE: [ \t]+ -> channel(HIDDEN);


Identifier:   Nondigit (Nondigit | Digit)*;
fragment Nondigit: [a-zA-Z_];
fragment Digit: [0-9];

Constant: IntegerConstant | FloatingConstant;
IntegerConstant: NonzeroDigit Digit*;
fragment NonzeroDigit: [1-9];
FloatingConstant: FractionalConstant ExponentPart?;
fragment FractionalConstant: DigitSequence? '.' DigitSequence | DigitSequence '.';
fragment ExponentPart: [eE] Sign? DigitSequence;
DigitSequence: Digit+;
fragment Sign: [+-];