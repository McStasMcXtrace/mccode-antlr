from io import StringIO
from ..instr import Instr, Instance
from ..comp import Comp
from zenlog import log

MCSTAS_GENERATOR = dict(project=1, name="mcstas", fancy="McStas", url='http://www.mcstas.org')
MCXTRACE_GENERATOR = dict(project=2, name='mcxtrace', fancy='McXtrace', url='http://www.mcxtrace.org')

# These _should_ be set in a call to, e.g., `mcstas4`,
# They were previously set in the yacc generated main function
CONFIG = dict(default_main=True, enable_trace=True, portable=True, include_runtime=True,
              embed_instrument_file=False,)


# Follow the logic of codegen.c(.in) from McCode-3, but make use of visitor semantics for possible alternate runtimes
class TargetVisitor:
    def __init__(self, instr: Instr, generate: dict = None, config: dict = None, verbose=False):
        self.runtime = MCSTAS_GENERATOR if generate is None else generate
        self.config = CONFIG if config is None else config
        self.source = instr
        self.output = None
        self.verbose = verbose
        self.warnings = 0
        self.instrument_uservars = ()
        self.component_uservars = dict()
        self.includes = []
        self.typedefs = None
        self.component_declared_parameters = dict()
        self.ok_to_skip = None
        #
        self.source.verify_instance_parameters()
        self.__post_init__()

    def __init_subclass__(cls, **kwargs):
        target_language = kwargs.get('target_language', 'none')
        if 'target_language' in kwargs:
            del kwargs['target_language']
        super().__init_subclass__(**kwargs)
        cls.target_language = target_language

    def __post_init__(self):
        pass

    @property
    def is_mcstas(self):
        index = self.runtime.get('project')
        if index != 1 and index != 2:
            raise RuntimeError(f'Unknown runtime for project index {index}')
        return index == 1

    @property
    def registries(self):
        return self.source.registries

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
                self.out(f'/* embedding file "{file_at}" */')
                self.output.write(file.read())
                self.out(f'/* end of file "{file_at}" */')

    def include_path(self, filename=None):
        if filename is None:
            # It would be better to read this from the cache itself
            from pooch import os_cache
            return os_cache('mccode_antlr-libc')
        return self.library_path(filename)

    def out(self, value):
        if self.output is None:
            raise RuntimeError('Printing only enabled once translation has begun!')
        print(value, file=self.output)

    def info(self, msg: str):
        if self.verbose:
            log.info(f'{self.source.name}: {msg}')

    def translate(self, reprocess=True):
        if self.output is not None:
            if not reprocess:
                return self.output
            self.output.close()
        self.output = StringIO()
        self.info('visit header')
        self.visit_header()
        self.info('visit declare')
        self.visit_declare()
        self.info('set jump targets')
        self.set_jump_absolute_targets()
        self.info('determine transforms to skip')
        self.detect_skipable_transforms()
        self.info('visit initialize')
        self.visit_initialize()
        self.info('enter trace')
        self.enter_trace()
        self.info('enter uservars')
        self.enter_uservars()
        self.info('visit raytrace')
        self.visit_raytrace()
        self.info('visit raytrace funnel')
        self.visit_raytrace_funnel()
        self.info('leave uservars')
        self.leave_uservars()
        self.info('leave trace')
        self.leave_trace()
        self.info('visit save')
        self.visit_save()
        self.info('visit finally')
        self.visit_finally()
        self.info('visit display')
        self.visit_display()
        self.info('visit macros')
        self.visit_macros()
        if self.verbose and self.warnings:
            print(f"Build of instrument {self.source.name} had {self.warnings} warnings")
        return self.output

    def save(self, filename=None, close=True, reprocess=True):
        self.translate(reprocess=reprocess)
        if filename:
            with open(filename, 'w') as file:
                file.write(self.output.getvalue())
        if close:
            self.output.close()
            self.output = None

    def contents(self):
        if self.output is None:
            output = self.translate(reprocess=False)
            string = output.getvalue()
            output.close()
            self.output = None
        else:
            string = self.output.getvalue()
        return string

    def detect_skipable_transforms(self):
        def can_skip(comp):
            # Any component with a TRACE or EXTEND can not be skipped
            if any(not x.is_empty for x in comp.extend) or any(not x.is_empty for x in comp.type.trace):
                return False
            # Any component jumping elsewhere can not be skipped
            if len(comp.jump):
                return False
            return True

        can_skip_transform = [can_skip(comp) for comp in self.source.components]

        # Any component that is jumped *to* can not be skipped (set_jump_absolute_targets must be called before this)
        for jump in [j for c in self.source.components for j in c.jump]:
            can_skip_transform[jump.absolute_target] = False

        self.ok_to_skip = can_skip_transform

    def set_jump_absolute_targets(self):
        for index, jump in [(i, j) for i, c in enumerate(self.source.components) for j in c.jump]:
            # jump is a dataclass with 'target', 'index', 'iterate', 'condition', and 'actual_target_index'
            if jump.absolute_target > -1:
                # Somewhere/something already set the actual target index -- we don't have a choice but to trust it
                continue
            if jump.relative_target == 0 and jump.target.lower() != 'myself':
                # the target is another named component:
                jump.absolute_target = [i for i, c in enumerate(self.source.components) if jump.target == c.name][0]
                jump.relative_target = jump.absolute_target - index
            else:
                jump.absolute_target = index + jump.relative_target

    def enter_trace(self):
        pass
            
    def leave_trace(self):
        pass

    def visit_header(self):
        pass

    def visit_declare(self):
        pass

    def visit_initialize(self):
        # likely target dependent
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

        
        

