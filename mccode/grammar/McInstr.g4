grammar McInstr;
import McCommon;
/* Parser rules for McCode .instr files, which define instruments with a general format like:

DEFINE INSTRUMENT {name} ({parameters,})
DECLARE %{
    {C-language global parameter definitions}
%}
INITIALIZE %{
    {C-language initialization of global parameters. Executed once at start of runtime.}
%}
TRACE
{Any number of COMPONENT instances, SEARCH path specifications, or instrument INCLUDE statements}
FINALLY %{
    {C-language global parameter deconstruction statements}
%}
*/
prog: instrument_definition EOF;

instrument_definition
  : Define Instrument Identifier instrument_parameters
    shell? search? instrument_metadata? dependency? declare? uservars? initialize?
    instrument_trace
    save? finally_?
    End
  ;

/* Instrument parameters can be set at runtime by the calling user.
They are presented in an instr file as a comma sepeparated list between parentheses.
They may identify their data type, but are assumed `double` if not specified;
valid data types are `double`, `int`, `string` or `char*` (of which the last two are equivalent).
Parameters may be specified with their *expected* units, but this is only informative for the user.
A default value may be specified for each parameter.

The general format of an instrument paraemter in the instr file is
    {data type} {parameter name} [/ "{unit}"] [= {default value}]
*/
instrument_parameters: '(' (params+=instrument_parameter (',' params+=instrument_parameter)*)? ')';
instrument_parameter
  : Double? Identifier instrument_parameter_unit? (Assign expr)?                         #InstrumentParameterDouble
  | Int Identifier instrument_parameter_unit? (Assign expr)?                             #InstrumentParameterInteger
  | (String | (Char Star)) Identifier instrument_parameter_unit? (Assign (StringLiteral | Null | '0'))? #InstrumentParameterString
  ;

instrument_parameter_unit: Div StringLiteral;

// Why not make TRACE optional?
instrument_trace: Trace ((component_instance | search | instrument_trace_include)+)?;

instrument_metadata: metadata+;

// Insert components from another instr file `%include "filename.instr"`
instrument_trace_include: Include StringLiteral;

/* instantiate a component; generally has the form

COMPONENT {name} = {.comp type name} ({instance parameters})
AT {place} RELATIVE {reference}
[ROTATED {angles} RELATIVE {reference}]

TODO: Think about specifying AFFINE ((xx, xy, xz), (yx, yy, yz), (zx, zy, zz)), (x0, y0, z0)
*/
component_instance:
  Removable? Cpu? split? Component instance_name Assign component_type instance_parameters?
  when? place orientation? groupref? extend? jumps? metadata*;

// There are three special forms of component instance names.
// Typically a user-defined valid identifier is given.
instance_name
  : Copy '(' Identifier ')'  #InstanceNameCopyIdentifier
  | (Myself | Copy )         #InstanceNameCopy
  | Identifier               #InstanceNameIdentifier
  ;

/* The instantiation of a component can start from a 'default' as-defined in its .comp file
 component *OR* from a pre-instantiated component instance. In the second case any provided
 instance parameters override those copied from the earlier instantiated component.
*/
component_type
  : Copy LeftParen component_ref RightParen   #ComponentTypeCopy
  | Identifier                                #ComponentTypeIdentifier
  ;

/* Instance parameters do not specify their type or unit.
They are expected to be an appropriate value matching the component definition file.
*/
instance_parameters: '(' (params+=instance_parameter (',' params+=instance_parameter)*)? ')';
instance_parameter
  : Identifier Assign expr            #InstanceParameterExpr
  | Identifier Assign Null            #InstanceParameterNull
  | Identifier Assign initializerlist #InstanceParameterVector
//  | Identifier Assign StringLiteral #InstanceParameterString
  ;



split: Split (|expr);
when: When expr;
place: At coords reference;
orientation: Rotated coords reference;
groupref: Group Identifier;
jumps: jump+;
jump: Jump jumpname (When|Iterate) expr;
jumpname
  : Previous ('(' IntegerLiteral ')')?  #JumpPrevious
  | Myself                              #JumpMyself
  | Next ('(' IntegerLiteral ')')?      #JumpNext
  | Identifier                          #JumpIdentifier
  ;

// Component instance post-trace C code statements
extend: Extend unparsed_block;  // Original McCode3 erroneously identified EXTEND as common grammar