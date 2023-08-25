from ..comp import Comp
from ..common import ComponentParameter


def define(a: ComponentParameter):
    return f'#define {a.name} (_comp->_parameters.{a.name})'


def undef(a: ComponentParameter):
    return f'#undef {a.name}'


def cogen_parameter_define(comp: Comp, declares: list):
    # All parameters get defines? Not just DEFINE PARAMETERS
    lines = [define(par) for pars in (comp.define, comp.setting, comp.output, declares) for par in pars]
    return '\n'.join(lines)


def cogen_parameter_undef(comp: Comp, declares: list):
    # The same parameters that were defined need to be undefined:
    lines = [undef(par) for pars in (comp.define, comp.setting, comp.output, declares) for par in pars]
    return '\n'.join(lines)
