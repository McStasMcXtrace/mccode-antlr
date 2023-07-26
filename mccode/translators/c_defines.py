from ..comp import Comp
from ..common import ComponentParameter


def define(a: ComponentParameter):
    return f'#define {a.name} (_comp->_parameters.{a.name})'


def undef(a: ComponentParameter):
    return f'#undef {a.name}'


def cogen_parameter_define(comp: Comp, declares: dict):
    # All parameters get defines? Not just DEFINE PARAMETERS
    lines = [define(par) for pars in (comp.define, comp.setting, comp.output) for par in pars]
    # TODO change this to define(par) once declares is list[CDeclaration] instead of dict
    lines.extend([f'#define {par} (_comp->_parameters.{par})' for par in declares])
    return '\n'.join(lines)


def cogen_parameter_undef(comp: Comp, declares: dict):
    # The same parameters that were defined need to be undefined:
    lines = [undef(par) for pars in (comp.define, comp.setting, comp.output) for par in pars]
    # TODO change this to undef(par) once declares is list[CDeclaration] instead of dict
    lines.extend([f'#undef {par}' for par in declares])
    return '\n'.join(lines)
