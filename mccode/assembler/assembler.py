from typing import Union
from ..common import Expr, InstrumentParameter
from ..instr import Instr, Instance
from ..reader import Reader, Registry
from zenlog import log


class Assembler:
    """Interactive instrument assembly"""

    def __init__(self, name: str, registries: list[Registry] = None):
        self.instrument = Instr(name, source='interactive')
        self.reader = Reader(registries=registries) if registries is not None else Reader()
        self.instrument.registries = self.reader.registries

    @property
    def name(self):
        return self.instrument.name

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
        v = tuple(x if isinstance(x, Expr) else Expr.best(x) for x in v)
        return (v[0], v[1], v[2]), ref

    def component(self, name: str, type_name: str, at=None, rotate=None, parameters=None):
        comp_type = self.reader.get_component(type_name)
        instance = Instance(name, comp_type, self._handle_at_rotate(at), self._handle_at_rotate(rotate))
        self.instrument.add_component(instance)
        if isinstance(parameters, dict):
            instance.set_parameters(**parameters)
        return instance

    def parameter(self, par, ignore_repeated=False):
        """Add a parameter to the underlying Instr.

        Note
        ----
        The ignore_repeated keyword argument can be set to True in order to merely ensure that a parameter exists.
        Otherwise, repeatedly specifying the same parameter will raise a RuntimeError.
        """
        if isinstance(par, str):
            par = InstrumentParameter.parse(par)
        if not isinstance(par, InstrumentParameter):
            log.warning(f'Unhandled parameter {par}')
        self.instrument.add_parameter(par, ignore_repeated=ignore_repeated)

    def parameters(self, *pars, **pairs):
        for par in list(pars):
            if isinstance(par, str):
                par = InstrumentParameter.parse(par)
            if not isinstance(par, InstrumentParameter):
                log.warning(f'Unhandled parameter(s) {par}')
            self.instrument.add_parameter(par)

        for name, value in pairs.items():
            if not isinstance(value, InstrumentParameter):
                if isinstance(value, dict) and 'unit' in value and 'value' in value:
                    value, unit = value['value'], value['unit']
                elif isinstance(value, (list, tuple)) and len(value) == 2 and isinstance(value[1], str):
                    value, unit = value
                else:
                    unit = ''
                value = InstrumentParameter(name, unit, value if isinstance(value, Expr) else Expr.best(value))
            self.instrument.add_parameter(value)

    def declare(self, string, source=None, line=-1):
        return _rawc_call(self.instrument.DECLARE, string, source, line)

    def declare_array(self, dtype: str, name: str, init: list, source=None, line=-1):
        return self.declare(f'{dtype} {name}[] = {{{",".join(str(x) for x in init)}}};', source=source, line=line)

    def user_vars(self, string, source=None, line=-1):
        return _rawc_call(self.instrument.USERVARS, string, source, line)

    def ensure_user_var(self, string, source=None, line=-1):
        # tying the Assembler to work with C might not be great
        from mccode.translators.c_listener import extract_c_declared_variables as parse
        input = parse(string)
        if len(input) == 0:
            raise ValueError(f'The provided input {string} does not specify a C parameter declaration.')
        if len(input) != 1:
            print(f'The provided input {string} specifies {len(input)} C parameter declarations, using only the first')
        name = list(input.keys())[0]
        dtype, _ = input[name]
        for user_vars in self.instrument.user:
            dec_type_init_dict = parse(user_vars.source)
            if any(d == dtype and n == name for n, (d, _) in dec_type_init_dict.items()):
                return
            if any(n == name for n in dec_type_init_dict):
                print(f'A USERVARS variable with name {name} but type different than {dtype} has already been defined.')
                return
        return self.user_vars(string, source=source, line=line)

    def initialize(self, string, source=None, line=-1):
        return _rawc_call(self.instrument.INITIALIZE, string, source, line)

    def save(self, string, source=None, line=-1):
        return _rawc_call(self.instrument.SAVE, string, source, line)

    def final(self, string, source=None, line=-1):
        return _rawc_call(self.instrument.FINALLY, string, source, line)

    def metadata(self, name: str, mimetype: str, value: str, source=None):
        from mccode.common.metadata import MetaData
        self.instrument.add_metadata(MetaData.from_instrument_tokens(source, mimetype, name, value))


def _rawc_call(method, string: str, source: str = None, line: int = -1):
    from mccode.common import RawC
    return method(RawC(str(source), line, string))


INTENDED_USAGE = """
bifrost = Assembler('bifrost', registries=[MCSTAS_REGISTRY, local_bifrost_components])
bifrost.parameters(par1=5.11, par2=('m', 100), par3={'value': 3.14159, 'unit': 'radian'})
...
bifrost.component('source, 'ESS_BUTTERFLY').set_parameters(...)
...
"""