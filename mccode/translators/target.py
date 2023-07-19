from io import StringIO
from ..instr import Instr, Instance
from ..comp import Comp

MCSTAS_GENERATOR = dict(project=1, name="mcstas", fancy="McStas", url='http://www.mcstas.org')
MCXTRACE_GENERATOR = dict(project=2, name='mcxtrace', fancy='McXtrace', url='http://www.mcxtrace.org')


# Follow the logic of codegen.c(.in) from McCode-3, but make use of visitor semantics for possible alternate runtimes
class TargetVisitor:
    def __init__(self, instr: Instr, generate: dict = None, verbose=False):
        self.runtime = MCSTAS_GENERATOR if generate is None else generate
        self.source = instr
        self.sink = None
        self.output = None
        self.verbose = verbose
        self.warnings = 0

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
        # TODO implement this here
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

        
        

