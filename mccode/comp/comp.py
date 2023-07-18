"""Data structures required for representing the contents of a McCode comp file"""
from dataclasses import dataclass, field
from ..common import ComponentParameter, MetaData, parameter_name_present


# Could this be replaced by a subclassed 'name' class? E.g., Slit.comp <=> class McCompSlit(McComp)?
@dataclass
class Comp:
    name: str = None           # Component *type* name, e.g. {name}.comp
    parameters: tuple[ComponentParameter] = field(default_factory=tuple)  # instance-set component parameters
    settings: tuple[ComponentParameter] = field(default_factory=tuple)    # ??? 'setting' parameters
    output: tuple[ComponentParameter] = field(default_factory=tuple)      # 'output' parameters
    metadata: tuple[MetaData] = field(default_factory=tuple)              # metadata for use by simulation consumers
    dependency: str = None     # compile-time dependency
    acc: bool = True           # False if this component *can not* work under OpenACC
    share: str = None          # literal string providing C function(s) useful for all instances of this class
    user: str = None           # literal string providing C struct members for _particle
    declare: str = None        # literal string providing C global parameters used in component trace
    initialize: str = None     # literal string providing C initialization of global declare parameters
    trace: str = None          # literal string providing C per-particle interaction code executed at TRACE time
    save: str = None           # literal string providing C statements executed after TRACE to save results
    final: str = None          # literal string providing C to clean-up initialized memory for global declare parameters
    display: str = None        # literal string providing C to draw this component, using specialized routines/macros

    def has_parameter(self, a: ComponentParameter):
        return parameter_name_present(self.parameters, a)

    def parameter_name_used(self, parameter_type: str, a: ComponentParameter):
        """Verify that a new parameter name is not already in use."""
        if parameter_name_present(self.parameters, a):
            raise RuntimeError(f"{parameter_type} parameter {a.name} is already an instance parameter!")
        if parameter_name_present(self.settings, a):
            raise RuntimeError(f"{parameter_type} parameter {a.name} is already a setting parameter!")
        if parameter_name_present(self.output, a):
            raise RuntimeError(f"{parameter_type} parameter {a.name} is already an output parameter!")

    def add_parameter(self, a: ComponentParameter):
        self.parameter_name_used('Instance', a)
        self.parameters = (*self.parameters, a) if len(self.parameters) else (a, )

    def add_setting(self, a: ComponentParameter):
        self.parameter_name_used('Setting', a)
        self.settings = (*self.settings, a) if len(self.settings) else (a,)

    def add_output(self, a: ComponentParameter):
        self.parameter_name_used('Output', a)
        self.output = (*self.output, a) if len(self.output) else (a,)

    def no_acc(self):
        self.acc = False

    # Meta programming these block setting methods is more pain than its worth:
    def SHARE(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.share = block

    def USERVARS(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.user = block

    def DECLARE(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.declare = block

    def INITIALIZE(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.initialize = block

    def TRACE(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.trace = block

    def SAVE(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.save = block

    def FINALLY(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.final = block

    def DISPLAY(self, block):
        if not isinstance(block, str):
            block = str(block)
        if '%{' == block[:2] and '%}' == block[-2:]:
            block = block[2:-2]
        self.display = block
