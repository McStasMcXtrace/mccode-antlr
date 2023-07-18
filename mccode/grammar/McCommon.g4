grammar McCommon;
import cpp;

// Common parsing rules

component_ref: Previous (LeftParen IntegerLiteral RightParen)? | Identifier;
coords: LeftParen expr Comma expr Comma expr RightParen;
reference: Absolute | Relative (Absolute | component_ref);

dependency: Dependency StringLiteral;
declare
  : Declare UnparsedBlock                           #DeclareBlock
  | Declare Copy Identifier (Extend UnparsedBlock)? #DeclareBlockCopy
  ;
share
  : Share UnparsedBlock                           #ShareBlock
  | Share Copy Identifier (Extend UnparsedBlock)  #ShareBlockCopy
  ;
uservars: UserVars UnparsedBlock;
initialize
  : Initialize UnparsedBlock                           #InitializeBlock
  | Initialize Copy Identifier (Extend UnparsedBlock)? #InitializeBlockCopy
  ;
save
  : Save UnparsedBlock                            #SaveBlock
  | Save Copy Identifier (Extend UnparsedBlock)?  #SaveBlockCopy
  ;
finally_
  : Finally UnparsedBlock                           #FinallyBlock
  | Finally Copy Identifier (Extend UnparsedBlock)? #FinallyBlockCopy
  ;
display
  : McDisplay UnparsedBlock                           #DisplayBlock
  | McDisplay Copy Identifier (Extend UnparsedBlock)? #DisplayBlockCopy
  ;
split: Split expr?;
when: When expr;
place: At coords reference;
orientation: Rotated coords reference;
groupref: Group Identifier;
extend: Extend UnparsedBlock;
jump: (Jump jumpname (When|Iterate) expr)+;
jumpname: Previous ('(' IntegerLiteral ')')? | Myself | Next ('(' IntegerLiteral ')')? | Identifier;


metadata
  : MetaData Identifier Identifier UnparsedBlock       #MetadataIdId
  | MetaData Identifier StringLiteral UnparsedBlock    #MetadataIdStr
  | MetaData StringLiteral Identifier UnparsedBlock    #MetadataStrId
  | MetaData StringLiteral StringLiteral UnparsedBlock #MetadataStrStr
  ;

initializerlist: '{' expr (Comma expr)* '}';

assignment: Identifier Assign expr; // Not used in McCode, but *could* be used to enable, e.g., loops or other simple control

expr
  : Identifier '[' expr ']'      #ExpressionArrayAccess
  | Identifier '(' expr ')'      #ExpressionFunctionCall
  | ('+' | '-') expr             #ExpressionUnaryPM
  | <assoc=right> expr '^' expr  #ExpressionExponentiation
  | expr ('*' | '/') expr        #ExpressionBinaryMD
  | expr ('+' | '-') expr        #ExpressionBinaryPM
  | '(' expr ')'                 #ExpressionGrouping
  | Identifier                   #ExpressionIdentifier
  | FloatingLiteral              #ExpressionFloat
  | IntegerLiteral               #ExpressionInteger
  ;

shell: Shell StringLiteral;
search
  : Search StringLiteral       #SearchPath
  | Search Shell StringLiteral #SearchShell
  ;

// Common lexer tokens
/* The McCode grammar _is_ case sensitive, but should it be? Is there any benefit to allowing lowercase keywords? */
Absolute: 'ABSOLUTE'; // | 'Absolute' | 'absolute';
At : 'AT'; // | 'At' | 'at';
Component : 'COMPONENT'; // | 'Component' | 'component';
UserVars: 'USERVARS'; // | 'UserVars' | 'uservars';
Define: 'DEFINE'; // | 'Define' | 'define';
Declare: 'DECLARE';
Definition: 'DEFINITION'; // | 'Definition' | 'definition';
End: 'END'; // | 'End' | 'end';
McDisplay: 'MCDISPLAY' | 'DISPLAY'; // | 'McDisplay' | 'mcdisplay' | 'Display' | 'display';
Finally: 'FINALLY'; // | 'Finally' | 'finally';
Initialize: 'INITIALIZE' | 'INITIALISE'; // | 'Initialize' | 'initialize' | 'Initialise' | 'initialise' ;
Instrument: 'INSTRUMENT'; // | 'Instrument' | 'instrument';
Output: 'OUTPUT' | 'PRIVATE'; // | 'Output' | 'output' | 'Private' | 'private';
Parameters: 'PARAMETERS'; // | 'Parameters' | 'parameters';
Relative: 'RELATIVE'; // | 'Relative' | 'relative';
Rotated: 'ROTATED'; // | 'Rotated' | 'rotated';
Previous: 'PREVIOUS'; // | 'Previous' | 'previous';
Setting: 'SETTING'; // | 'Setting' | 'setting';
Trace: 'TRACE'; // | 'Trace' | 'trace';
Share: 'SHARE'; // | 'Share' | 'share';
Extend: 'EXTEND'; // | 'Extend' | 'extend';
Group: 'GROUP'; // | 'Group' | 'group';
Save: 'SAVE'; // | 'Save' | 'save';
Jump: 'JUMP'; // | 'Jump' | 'jump';
When: 'WHEN'; // | 'When' | 'when';
Next: 'NEXT'; // | 'Next' | 'next';
Iterate: 'ITERATE'; // | 'Iterate' | 'iterate';
Myself: 'MYSELF'; // | 'Myself' | 'myself';
Copy: 'COPY'; // | 'Copy' | 'copy';
Split : 'SPLIT'; // | 'Split' | 'split';
Removable: 'REMOVABLE'; // | 'Removabel' | 'removable';
Cpu: 'CPU'; // | 'cpu';
NoAcc: 'NOACC'; // | 'NoACC' | 'NoAcc' | 'noacc';
Dependency: 'DEPENDENCY'; // | 'Dependency' | 'dependency';
Shell: 'SHELL'; // | 'Shell' | 'shell';
Search: 'SEARCH'; // | 'Search' | 'search';
MetaData: 'METADATA'; // | 'MetaData' | 'metadata';

String: 'string';  // McCode string-literal instrument/component parameter type; always(?) equivalent to `char *`
Vector: 'vector';  // McCode (double) array component parameter type -- does or does not allow initializer lists?
Symbol: 'symbol';  // McCode ???? type ????!?!?!
UnparsedBlock: '%{' (.)*? '%}'; // Used for raw C code blocks and metadata, etc.
Include: '%include';

Null: 'NULL'; // remove if we switch to underlying C grammar?