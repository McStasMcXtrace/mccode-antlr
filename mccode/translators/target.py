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
    target_language = 'undefined'

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
        self.registries = registries
        self.libraries = []
        self.typedefs = None
        self.__post__init__()

    def __post__init__(self):
        pass

    def library_path(self, filename=None):
        from importlib.resources import files
        from pathlib import Path
        traversable = files('mccode').joinpath('libraries')
        location = Path(traversable).joinpath(self.target_language)
        if filename:
            location.joinpath(filename)
        if (filename and not location.is_file()) or not location.is_dir():
            raise RuntimeError(f"Expected library location {location} is not a valid.")
        return location

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

    def embed_file(self, filename):
        """Reads the library file, even if embedded in a module archive, writes to the output IO Stream"""
        from importlib.resources import as_file
        with as_file(self.library_path(filename)) as file_at:
            with open(file_at, 'r') as file:
                self.output.write(file.read())

    def include_path(self, filename=None):
        #TODO figure out what to do if the module lives in a Zip file
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
        # TODO implement this here (or move it into Instr itself, more likely)
        pass

    def enter_trace(self):
        """Walk the component instances definition(s) section..."""
        for instance in self.source.components:
            self.enter_instance(instance)
            
    def exit_trace(self):
        """Walk the component instances deallocate section..."""
        for instance in self.source.components:
            self.leave_instance(instance)

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

        
        

