from io import StringIO
from ..instr import Instr, Instance
from ..comp import Comp

MCSTAS_GENERATOR = dict(project=1, name="mcstas", fancy="McStas", url='http://www.mcstas.org')
MCXTRACE_GENERATOR = dict(project=2, name='mcxtrace', fancy='McXtrace', url='http://www.mcxtrace.org')

# These _should_ be set in a call to, e.g., `mcstas4`,
# They were previously set in the yacc generated main function
CONFIG = dict(default_main=True, enable_trace=True, portable=True, include_runtime=True,
              embed_instrument_file=False,)


# Follow the logic of codegen.c(.in) from McCode-3, but make use of visitor semantics for possible alternate runtimes
class TargetVisitor:
    def __init__(self, instr: Instr, generate: dict = None, config: dict = None, verbose=False,
                 registries=None):
        self.runtime = MCSTAS_GENERATOR if generate is None else generate
        self.config = CONFIG if config is None else config
        self.source = instr
        self.sink = None
        self.output = None
        self.verbose = verbose
        self.warnings = 0
        self.uservars = ()
        self.registries = [] if registries is None else registries
        self.libraries = []
        self.typedefs = None
        self.component_declared_parameters = dict()
        self.ok_to_skip = None
        #
        self.__post__init__()

    def __init_subclass__(cls, **kwargs):
        target_language = kwargs.get('target_language', 'none')
        if 'target_language' in kwargs:
            del kwargs['target_language']
        super().__init_subclass__(**kwargs)
        cls.target_language = target_language

    def __post__init__(self):
        pass

    def known(self, name: str, which: str = None):
        if self.registries is None:
            return False
        registries = self.registries if which is None else [x for x in self.registries if x.name in which]
        return any([reg.known(name) for reg in registries])

    def locate(self, name: str, which: str = None):
        registries = self.registries if which is None else [x for x in self.registries if x.name in which]
        for reg in registries:
            if reg.known(name):
                return reg.path(name)
        names = [reg.name for reg in registries]
        msg = "registry " + names[0] if len(names) == 1 else 'registries: ' + ','.join(names)
        raise RuntimeError(f'{name} not found in {msg}')

    def library_path(self, filename=None):
        return self.locate(filename)

    def embed_file(self, filename):
        """Reads the library file, even if embedded in a module archive, writes to the output IO Stream"""
        from importlib.resources import as_file
        with as_file(self.library_path(filename)) as file_at:
            with open(file_at, 'r') as file:
                self.output.write(file.read())

    def include_path(self, filename=None):
        return self.library_path(filename)

    def out(self, value):
        if self.output is None:
            raise RuntimeError('Printing only enabled once translation has begun!')
        print(value, file=self.output)

    def translate(self, filename=None):
        self.output = StringIO()
        self.sink = filename

        self.visit_header()
        self.visit_declare()
        self.detect_skipable_transforms()
        self.visit_initialize()
        self.enter_trace()
        self.enter_uservars()
        self.visit_raytrace()
        self.visit_raytrace_funnel()
        self.leave_uservars()
        self.exit_trace()
        self.visit_save()
        self.visit_finally()
        self.visit_display()
        self.visit_macros()

        if self.verbose and self.warnings:
            print(f"Build of instrument {self.source.name} had {self.warnings} warnings")

        if self.sink:
            with open(self.sink, 'w') as file:
                file.write(self.output.getvalue())
        self.output.close()

    def detect_skipable_transforms(self):
        def can_skip(comp):
            # Any component with a TRACE or EXTEND can not be skipped
            if any(not x.is_empty for x in comp.extend) or any(not x.is_empty for x in comp.type.trace):
                return False
            # Any component jumping elsewhere can not be skipped
            if len(comp.jump):
                return False

        can_skip_transform = [can_skip(comp) for comp in self.source.components]

        # Any component that is jumped *to* can not be skipped
        for index, jumps in [(i, c.jump) for i, c in enumerate(self.source.components) if len(c.jump)]:
            for jump in jumps:
                # jump has ('target', 'index', iterate, condition) -- if index == 0, target is a component name or 'MYSELF'
                # if index != 0 it is a relative component index compared to the current one
                if jump.target_index == 0 and jump.target.lower() != 'myself':
                    target_index = [i for i, c in self.source.components if jump.target == c.name][0]
                else:
                    target_index = index + jump.target_index
                can_skip_transform[target_index] = False

        self.ok_to_skip = can_skip_transform

    def enter_trace(self):
        """Walk the component instances definition(s) section..."""
        self.visit_pre_trace()
        for instance in self.source.components:
            self.enter_instance(instance)
            
    def exit_trace(self):
        """Walk the component instances deallocate section..."""
        for instance in self.source.components:
            self.leave_instance(instance)
        self.visit_post_trace()

    def visit_pre_trace(self):
        pass

    def visit_post_trace(self):
        pass

    def visit_header(self):
        pass

    def visit_declare(self):
        pass

    def visit_initialize(self):
        # likely target dependent
        pass

    def enter_instance(self, instance: Instance):
        pass
    
    def leave_instance(self, instance: Instance):
        pass

    def visit_component(self, instance: Instance):
        pass
    
    def enter_uservars(self):
        pass
    
    def leave_uservars(self):
        pass
    
    def visit_raytrace(self):
        pass
    
    def visit_raytrace_funnel(self):
        pass

    def visit_save(self):
        pass

    def visit_finally(self):
        pass

    def visit_display(self):
        pass

    def visit_macros(self):
        pass

        
        

