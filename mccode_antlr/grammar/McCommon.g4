grammar McCommon;
import cpp;

// Common parsing rules

component_ref: Previous (LeftParen IntegerLiteral RightParen)? | Identifier;
coords: LeftParen expr Comma expr Comma expr RightParen;
reference: Absolute | Relative (Absolute | component_ref);

dependency: Dependency StringLiteral;

declare
  : Declare unparsed_block                           #DeclareBlock
  | Declare Copy Identifier (Extend unparsed_block)? #DeclareBlockCopy
  ;
uservars: UserVars unparsed_block;
initialize
  : Initialize unparsed_block                           #InitializeBlock
  | Initialize Copy Identifier (Extend unparsed_block)? #InitializeBlockCopy
  ;
save
  : Save unparsed_block                            #SaveBlock
  | Save Copy Identifier (Extend unparsed_block)?  #SaveBlockCopy
  ;
finally_
  : Finally unparsed_block                           #FinallyBlock
  | Finally Copy Identifier (Extend unparsed_block)? #FinallyBlockCopy
  ;


metadata: MetaData mime=(Identifier | StringLiteral) name=(Identifier | StringLiteral) unparsed_block;

category: Category (Identifier | StringLiteral);

initializerlist: '{' values+=expr (Comma values+=expr)* '}';

assignment: Identifier Assign expr; // Not used in McCode, but *could* be used to enable, e.g., loops or other simple control

expr
  : '0'                                             #ExpressionZero
  | IntegerLiteral                                  #ExpressionInteger
  | FloatingLiteral                                 #ExpressionFloat
  | (args+=StringLiteral)*                          #ExpressionString
  | Identifier '->' expr                            #ExpressionPointerAccess
  | Identifier '.' expr                             #ExpressionStructAccess
  | Identifier '[' expr ']'                         #ExpressionArrayAccess
  | Identifier '(' args+=expr (',' args+=expr)* ')' #ExpressionFunctionCall
  | '(' expr ')'                                    #ExpressionGrouping
  | ('+' | '-') expr                                #ExpressionUnaryPM
  | <assoc=right> base=expr '^' exponent=expr       #ExpressionExponentiation
  | left=expr ('*' | '/') right=expr                #ExpressionBinaryMD
  | left=expr ('+' | '-') right=expr                #ExpressionBinaryPM
  | Identifier                                      #ExpressionIdentifier
  | left=expr '==' right=expr                       #ExpressionBinaryEqual
  | left=expr '<=' right=expr                       #ExpressionBinaryLessEqual
  | left=expr '>=' right=expr                       #ExpressionBinaryGreaterEqual
  | left=expr '<' right=expr                        #ExpressionBinaryLess
  | left=expr '>' right=expr                        #ExpressionBinaryGreater
  | Not expr                                        #ExpressionUnaryLogic
  | left=expr (AndAnd | OrOr) right=expr            #ExpressionBinaryLogic
  | test=expr '?' true=expr ':' false=expr          #ExpressionTrinaryLogic
  | Previous                                        #ExpressionPrevious
  | Myself                                          #ExpressionMyself
  ;

shell: Shell StringLiteral;
search
  : Search StringLiteral       #SearchPath
  | Search Shell StringLiteral #SearchShell
  ;

//unparsed_block: '%{' (.)*? '%}';
unparsed_block: UnparsedBlock;

// Common lexer tokens
/* The McCode grammar _is_ case sensitive, but should it be? Is there any benefit to allowing lowercase keywords? */
/* FIXME The McCode grammar _is not_(!!) case sensitive since `flex` is called with the `-i` option */
Absolute: 'ABSOLUTE' | 'Absolute' | 'absolute';
At : 'AT' | 'At' | 'at';
Category: 'CATEGORY' | 'Category' | 'category';
Component : 'COMPONENT' | 'Component' | 'component';
UserVars: 'USERVARS' | 'UserVars' | 'uservars';
Define: 'DEFINE' | 'Define' | 'define';
Declare: 'DECLARE';
Definition: 'DEFINITION' | 'Definition' | 'definition';
End: 'END' | 'End' | 'end';
McDisplay: 'MCDISPLAY' | 'DISPLAY' | 'McDisplay' | 'mcdisplay' | 'Display' | 'display';
Finally: 'FINALLY' | 'Finally' | 'finally';
Initialize: 'INITIALIZE' | 'INITIALISE' | 'Initialize' | 'initialize' | 'Initialise' | 'initialise' ;
Instrument: 'INSTRUMENT' | 'Instrument' | 'instrument';
Output: 'OUTPUT' | 'Output' | 'output';
Private: 'PRIVATE' | 'Private' | 'private';
Parameters: 'PARAMETERS' | 'Parameters' | 'parameters';
Relative: 'RELATIVE' | 'Relative' | 'relative';
Rotated: 'ROTATED' | 'Rotated' | 'rotated';
Previous: 'PREVIOUS' | 'Previous' | 'previous';
Setting: 'SETTING' | 'Setting' | 'setting';
Trace: 'TRACE' | 'Trace' | 'trace';
Share: 'SHARE' | 'Share' | 'share';
Extend: 'EXTEND' | 'Extend' | 'extend';
Group: 'GROUP' | 'Group' | 'group';
Save: 'SAVE' | 'Save' | 'save';
Jump: 'JUMP' | 'Jump' | 'jump';
When: 'WHEN' | 'When' | 'when';
Next: 'NEXT' | 'Next' | 'next';
Iterate: 'ITERATE' | 'Iterate' | 'iterate';
Myself: 'MYSELF' | 'Myself' | 'myself';
Copy: 'COPY' | 'Copy' | 'copy';
Split : 'SPLIT' | 'Split' | 'split';
Removable: 'REMOVABLE' | 'Removabel' | 'removable';
Cpu: 'CPU' | 'cpu';
NoAcc: 'NOACC' | 'NoACC' | 'NoAcc' | 'noacc';
Dependency: 'DEPENDENCY' | 'Dependency' | 'dependency';
Shell: 'SHELL' | 'Shell' | 'shell';
Search: 'SEARCH' | 'Search' | 'search';
MetaData: 'METADATA' | 'MetaData' | 'metadata';

String: 'string';  // McCode string-literal instrument/component parameter type; always(?) equivalent to `char *`
Vector: 'vector';  // McCode (double) array component parameter type -- does or does not allow initializer lists?
Symbol: 'symbol';  // McCode ???? type ????!?!?!
UnparsedBlock: '%{' (.)*? '%}'; // Used for raw C code blocks and metadata, etc.
Include: '%include';

Null: 'NULL'; // remove if we switch to underlying C grammar?