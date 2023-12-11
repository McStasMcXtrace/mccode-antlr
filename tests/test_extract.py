from unittest import TestCase

class TestExtract(TestCase):
    def test_runtime_parameter(self):
        from antlr4 import CommonTokenStream, InputStream
        from mccode_antlr.grammar import McInstrParser, McInstrLexer
        from mccode_antlr.instr import InstrVisitor
        from mccode_antlr.reader import MCSTAS_REGISTRY, Reader
        from mccode_antlr.common.expression import Value, ObjectType
        from mccode_antlr.translators.c_listener import extract_c_declared_variables, evaluate_c_defined_variables
        instr_source = """
        DEFINE INSTRUMENT blah()
        DECLARE %{
            double par;
        %}
        INITIALIZE %{
            par = (1 + 2 + 3) / (7 + 8 - 9);
        %}
        TRACE
        COMPONENT origin = Progress_bar() AT (0, 0, 0) RELATIVE ABSOLUTE
        COMPONENT source = Source_gen(T1=413.5, I1=10.22e12, T2=145.8, I2=3.44e13, T3=40.1, I3=2.78e13, dist=2,
                                      radius=0.06, focus_xw=0.1, focus_yh=0.1, lambda0=1.0, dlambda=0.5)
                           AT (0, 0, 0) RELATIVE PREVIOUS
        COMPONENT monitor = PSD_monitor(nx=par, ny=par, xwidth=0.1, yheight=0.1) AT (0, 0, 10.1) RELATIVE PREVIOUS
        END
        """
        parser = McInstrParser(CommonTokenStream(McInstrLexer(InputStream(instr_source))))
        visitor = InstrVisitor(Reader(registries=[MCSTAS_REGISTRY, ]), __file__)
        # Parse the instrument definition and return an Instr object
        instr = visitor.visitProg(parser.prog())
        nx = instr.components[-1].get_parameter('nx')

        self.assertFalse(nx.value.is_parameter)
        self.assertTrue(nx.value.is_id)

        # parse the declare block(s) to find parameter declarations
        variables = {}
        for dec in instr.declare:
            variables.update({k: t for k, (t, _) in extract_c_declared_variables(dec.source).items()})
        # Then parse and evaluate initialize to set their value(s).
        values = {}
        for init in instr.initialize:
            values.update(evaluate_c_defined_variables(variables, init.source, verbose=False))

        self.assertEqual(values['par'], Value.float(1))

