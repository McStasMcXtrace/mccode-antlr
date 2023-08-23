from typing import Union
from ..common import Expr, InstrumentParameter
from ..instr import Instr, Instance
from ..reader import Reader, Registry


class Assembler:
    """Interactive instrument assembly"""

    def __init__(self, name: str, registries: list[Registry] = None):
        self.instrument = Instr(name, source='interactive')
        self.reader = Reader(registries=registries) if registries is not None else Reader()

    def _handle_at_rotate(self, a=None) -> tuple[tuple[Expr, Expr, Expr], Union[Instance,  None]]:
        if a is None:
            return (Expr.float(0), Expr.float(0), Expr.float(0)), None
        if hasattr(a, '__len__') and len(a) == 3:
            a = a, 'ABSOLUTE'
        if not hasattr(a, '__len__') or len(a) != 2:
            raise RuntimeError('Require two-tuple of three values and a reference')
        v, ref = a
        if ref is not None and not isinstance(ref, Instance):
            if 'absolute' == ref.lower():
                ref = None
            elif isinstance(ref, str):
                # Get the component instance by name
                ref = self.instrument.get_component(ref)
            else:
                raise RuntimeError(f'No logic pathway for instance reference {ref}')
        if not hasattr(v, '__len__') or len(v) != 3:
            raise RuntimeError('Position/orientation must have three elements')
        v = tuple(x if isinstance(Expr, x) else Expr.best(x) for x in v)
        return (v[0], v[1], v[2]), ref

    def component(self, name: str, type_name: str, at=None, rotate=None, parameters=None):
        comp_type = self.reader.get_component(type_name)
        instance = Instance(name, comp_type, self._handle_at_rotate(at), self._handle_at_rotate(rotate))
        self.instrument.add_component(instance)
        if isinstance(parameters, dict):
            instance.set_parameters(**parameters)
        return instance

    def parameter(self, string):
        self.instrument.add_parameter(InstrumentParameter.parse(string))

    def parameters(self, **pairs):
        for name, value in pairs.items():
            if not isinstance(pairs, InstrumentParameter):
                if hasattr(value, '__len__') and len(value) == 2 and isinstance(value[1], str):
                    value, unit = value
                elif isinstance(value, dict) and 'unit' in value and 'value' in dict:
                    value, unit = value['value'], value['unit']
                else:
                    unit = ''
                value = InstrumentParameter(name, unit, value if isinstance(value, Expr) else Expr.best(value))
            self.instrument.add_parameter(value)


INTENDED_USAGE = """
bifrost = Assembler('bifrost', registries=[MCSTAS_REGISTRY, local_bifrost_components])
bifrost.parameters(par1=5.11, par2=('m', 100), par3={'value': 3.14159, 'unit': 'radian'})
...
bifrost.component('source, 'ESS_BUTTERFLY').set_parameters(...)
...
"""