from ..comp import Comp
from ..common import ComponentParameter


def define(a: ComponentParameter):
    return f'#define {a.name} (_comp->_parameters.{a.name})'


def undef(a: ComponentParameter):
    return f'#undef {a.name}'


def cogen_parameter_define(comp: Comp):
    # All parameters get defines? Not just DEFINE PARAMETERS
    lines = [define(par) for pars in (comp.define, comp.setting, comp.output) for par in pars]
    # # Mistakenly(?), the component DECLARE'ed parameters were defined here too.
    # for par in declared_parameters:
    #     lines.append(f'  #define {par} (_comp->_parameters.{par})')
    return '\n'.join(lines)


def cogen_parameter_undef(comp: Comp):
    # The same parameters that were defined need to be undefined:
    lines = [undef(par) for pars in (comp.define, comp.setting, comp.output) for par in pars]
    return '\n'.join(lines)
