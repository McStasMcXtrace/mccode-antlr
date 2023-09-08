grammar McComp;
import McCommon;
// Grammar for McCode .comp files:
/* A component definition file contains a description of the input and output for a component plus any
 component-specific function defintions (inserted at global scope, due to lack of namespaces in C),
 component-specific variable declarations (added to a component data structure),
 component-specific initialization (run once at the start of the runtime),
 particle trace-code which implments the interaction(s) with the component (run per particle),
 component-specific cleanup in two steps, performed as the runtime reaches its end state,
 a save-step to output any end-of-simulation information, and a final-step to deallocate the component struct
*/
prog :  component_definition EOF;

/*
DEFINE COMPONENT {name} [COPY {other_component_name}]?
DEFINITION PARAMETERS ([{parameter}, ...])
SETTING PARAMETERS ([{paraemter}, ...])
OUTPUT PARAMETERS ([{parameter}, ...])
SHARE %{
    {C code defining component functions}
%}
USERVARS %{
    {C parameter definitions, inserted into the *particle* structure (and therefore parsed!)}
%}
DECLARE %{
    {C Code specifying component parameters, inserted into component structure (and therefore parsed!)}
%}
INITIALIZE %{
    {C code setting up component parameters, run at initialization of runtime}
%}
TRACE %{
    {C code implementing interactions between particle and component}
%}
SAVE %{
    {C code run when the runtime is finished and any output should be produced.}
%}
FINALLY %{
    {C code finalizing all component processes and deallocating any memory.}
%}
END
*/
component_definition
    : Define Component Identifier component_parameter_set
      category?
      metadata* shell? dependency? NoAcc? share? uservars? declare? initialize?
      component_trace? save? finally_? display? End                               #ComponentDefineNew
    | Define Component Identifier Copy Identifier component_parameter_set
      category?
      metadata* shell? dependency? NoAcc? share? uservars? declare? initialize?
      component_trace? save? finally_? display? End                               #ComponentDefineCopy
    ;

component_trace
    : Trace unparsed_block                          #TraceBlock
    | Trace Copy Identifier (Extend unparsed_block)? #TraceBlockCopy
    ;

component_parameter_set: component_define_parameters? component_set_parameters? component_out_parameters?;
component_define_parameters: Definition Parameters component_parameters;
component_set_parameters: Setting Parameters component_parameters;
component_out_parameters: (Output | Private) Parameters component_parameters;


component_parameters: '(' (component_parameter (Comma component_parameter)*)? ')';
component_parameter
    : Double? Identifier (Assign (expr | '0'))?                                    #ComponentParameterDouble
    | Int Identifier (Assign (expr | '0'))?                                        #ComponentParameterInteger
    | (String | (Char Star)) Identifier (Assign (StringLiteral | Null | '0'))?     #ComponentParameterString
    | Vector Identifier (Assign (Identifier | initializerlist | Null | '0'))?      #ComponentParameterVector
    | Symbol Identifier (Assign expr)                                              #ComponentParameterSymbol
    | Double '*' Identifier (Assign (Identifier | initializerlist | Null | '0'))?  #ComponentParameterDoubleArray
    | Int '*' Identifier (Assign (Identifier | initializerlist | Null | '0'))?     #ComponentParameterIntegerArray
    ;

// Similar to `declare`, `uservars`, `initialize`, `save`, `finally_`, but only used in Comp(onent) definitions
share
  : Share unparsed_block                           #ShareBlock
  | Share Copy Identifier (Extend unparsed_block)?  #ShareBlockCopy
  ;
display
  : McDisplay unparsed_block                           #DisplayBlock
  | McDisplay Copy Identifier (Extend unparsed_block)? #DisplayBlockCopy
  ;
