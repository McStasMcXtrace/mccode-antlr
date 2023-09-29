from unittest import TestCase
from zenlog import log

def parse_instr_string(instr_source: str):
    from antlr4 import CommonTokenStream, InputStream
    from mccode.grammar import McInstrParser, McInstrLexer
    from mccode.instr import InstrVisitor
    from mccode.reader import MCSTAS_REGISTRY, Reader
    parser = McInstrParser(CommonTokenStream(McInstrLexer(InputStream(instr_source))))
    visitor = InstrVisitor(Reader(registries=[MCSTAS_REGISTRY]), None)
    return visitor.visitProg(parser.prog())


def make_mcstas_assembler(name: str):
    from mccode.assembler import Assembler
    from mccode.reader import MCSTAS_REGISTRY
    return Assembler(name, registries=[MCSTAS_REGISTRY])


class TestInstr(TestCase):
    def test_parse_empty_trace(self):
        from mccode.instr import Instr
        from mccode.common import InstrumentParameter, Expr, Value, DataType
        instr_source = """
        DEFINE INSTRUMENT test_parse(par0=3.14159, double par1 = 49, int par2 =     1010110
            , string par3="this is a long string with spaces", 
            
            string par4, int par5, double par6, par7)
        TRACE
        END
        """
        instr = parse_instr_string(instr_source)
        self.assertTrue(isinstance(instr, Instr))
        self.assertEqual(instr.name, 'test_parse')
        self.assertEqual(len(instr.parameters), 8)
        self.assertEqual(len(instr.components), 0)
        for i, (d_type, val) in enumerate([('double', 3.14159), ('double', 49), ('int', 1010110),
                                           ('string', '"this is a long string with spaces"'),
                                           ('string', None), ('int', None), ('double', None), ('double', None)]):
            p = instr.parameters[i]
            self.assertTrue(isinstance(p, InstrumentParameter))
            self.assertEqual(p.name, f'par{i}')
            self.assertTrue(isinstance(p.value, Expr))
            self.assertEqual(p.value, Value(val, data_type=DataType.from_name(d_type)))

    def test_assemble_empty_trace(self):
        from mccode.instr import Instr
        from mccode.common import InstrumentParameter, Expr, Value, DataType

        assembler = make_mcstas_assembler('test_assemble')

        # There are multiple ways to specify instrument parameters:
        # 1. specify a single parameter object to add:
        assembler.parameter(InstrumentParameter('par0', '', Expr.float(3.14159)))
        # 2. specify a single parameter as a string to be parsed:
        assembler.parameter('double par1 = 49')
        # 3. Using the parameters method, specify any number of parameter objects or strings to be parsed (as above)
        #    and/or specify keyword value pairs, where each value can be
        #      a. a two-element list or tuple of 'value', 'unit'
        #      b. a dict with entries 'unit' and 'value'
        #      c. a plain value
        #    in each of these cases, Expr.best converts the provided value if it is not already an Expr object
        assembler.parameters(InstrumentParameter('par2', '', Expr.int(1010110)),
                             'string par3 = "this is a long string with spaces"',
                             InstrumentParameter('par4', '', Expr.str('"the-fourth_parameter"')),
                             'int par5=-9', par6=[Expr.float(None), ''], par7=191, par8=dict(unit='', value='"whoa!"'))

        instr = assembler.instrument
        self.assertTrue(isinstance(instr, Instr))
        self.assertEqual(instr.name, 'test_assemble')
        self.assertEqual(len(instr.parameters), 9)
        self.assertEqual(len(instr.components), 0)
        d_type_vals = [('double', 3.14159), ('double', 49), ('int', 1010110),
                       ('string', '"this is a long string with spaces"'), ('string', '"the-fourth_parameter"'),
                       ('int', -9), ('float', None), ('int', 191), ('string', '"whoa!"')]
        for i, (par, (d_type, val)) in enumerate(zip(instr.parameters, d_type_vals)):
            self.assertTrue(isinstance(par, InstrumentParameter))
            self.assertEqual(par.name, f'par{i}')
            self.assertTrue(isinstance(par.value, Expr))
            self.assertEqual(par.value, Value(val, data_type=DataType.from_name(d_type)))

    def test_assemble_identifier_instance_parameter(self):
        assembler = make_mcstas_assembler('fake_bifrost')

        parameters = [
            'ps1speed/"Hz" = 196', 'ps2speed/"Hz" = 196',
            'fo1speed/"Hz" = 14', 'fo2speed/"Hz" = 14',
            'bw1speed/"Hz" = 14', 'bw2speed/"Hz" = -14',
            'ps1phase/"Hz" = 0', 'ps2phase/"Hz" = 0',
            'fo1phase/"Hz" = 0', 'fo2phase/"Hz" = 0',
            'bw1phase/"Hz" = 0', 'bw2phase/"Hz" = 0',
            'blade0l/"m" = -0.05', 'blade0r/"m" = 0.05',
            'blade1l/"m" = -0.05', 'blade1r/"m" = 0.05',
            'blade2l/"m" = -0.05', 'blade2r/"m" = 0.05',
            'blade3l/"m" = -0.05', 'blade3r/"m" = 0.05',
            'int pulses = 1', 'power/"MW" = 2',
            'source_lambda_min/"angstrom" = 0.75', 'source_lambda_max/"angstrom" = 30',
        ]
        assembler.parameters(*parameters)

        # Mix of initialization temporary variables and calculated instrument parameters.
        pulse_length = 2.86E-3
        assembler.declare(f"""
        double lambda_0;
        double lambda_1;
        double tf_d=1;
        double tf_t={pulse_length / 2};
        double tf_w={pulse_length};
        double tf_tau={1 / 14.0};
        double ps_disk_open_angle=170.0;
        double ps_distance={4.41 + 0.032 + 2.0 - 0.1};
        double bw_disk_open_angle=161.0;
        double bw_distance=78.0;
        """)

        # Chopper-based wavelength calculations can only be done at runtime since they depend on instrument parameters
        new_chopper_calculations = """
        chopper_parameters * pars = calloc(6, sizeof(chopper_parameters));
        pars[0].speed = ps1speed; // Pulse shaping disk 1
        pars[0].phase = ps1phase;
        pars[0].angle = 170.0;
        pars[0].path = ps_distance;
        pars[1].speed = ps2speed; // Pulse shaping disk 2
        pars[1].phase = ps2phase;
        pars[1].angle = pars[0].angle;
        pars[1].path = pars[0].path + 0.02;
        pars[2].speed = fo1speed; // Frame overlap 1
        pars[2].phase = fo1phase;
        pars[2].angle = 38.26;
        pars[2].path = 8.530;
        pars[3].speed = fo2speed; // Frame overlap 2
        pars[3].phase = fo2phase;
        pars[3].angle = 52.01;
        pars[3].path = 14.973;
        pars[4].speed = bw1speed; // Bandwidth disk 1
        pars[4].phase = bw1phase;
        pars[4].angle = 161.0;
        pars[4].path = bw_distance;
        pars[5].speed = bw2speed; // Bandwidth disk 2
        pars[5].phase = bw2phase;
        pars[5].angle = pars[4].angle;
        pars[5].path = pars[4].path + 0.02;

        lambda_0 = source_lambda_min;
        lambda_1 = source_lambda_max;
        double pulse_delay = 2.0e-4; // time to peak brightness after proton pulse T0
        double pulse_width = 2.86e-3; // duration of high flux plateau
        double latest = pulse_delay + pulse_width + 2e-3; // extra for good measure?
        unsigned windows = chopper_wavelength_limits(&source_lambda_min, &source_lambda_max, 6, pars, lambda_0, lambda_1, latest);

        // free the memory used by pars
        if (pars) free(pars);

        if (windows == 0) {
          printf("Chopper train will not pass wavelengths between %f and %f angstrom!\\n", lambda_0, lambda_1);
          printf("Examine the provided chopper speeds and phases.\\n");
        }
        if (windows > 1) {
          printf("Chopper train will pass %u wavelength ranges between %f and %f angstrom\\n", windows, lambda_0, lambda_1);
          printf("but only their envelope between %f and %f angstrom is considered!\\n", source_lambda_min, source_lambda_max);   
        }
        printf("Using source lambda limits %f to %f\\n", source_lambda_min, source_lambda_max);

        // Now calculate the time-focusing window on the first chopper given the wavelength band:
        // ...

        """
        assembler.initialize(new_chopper_calculations)

        # Start the actual instrument:
        assembler.component("Origin", "Progress_bar", at=[0, 0, 0])

        # Elliptic guide gravity initialization and declaration
        def declare_line(name, vec):
            initializer = '{' + ','.join(f'{x}' for x in vec) + '}'
            return f'double {name}[] = {initializer};'

        # Neutron Beam Optical Assembly (NBOA) in-monolith guide:
        nboa = dict()
        nboa['nboa_lens'] = [
            0.48844444, 0.48844444, 0.48844444, 0.48844444, 0.48844444, 0.48844444, 0.48844444, 0.06121889, 0.02349,
            0.40373556, 0.07626444, 0.015, 0.39671
        ]
        nboa['nboa_vert'] = [3.5, 3.5, 3.0, 3.0, 2.5, 2.5, 2.5, 2.5, 0.0, 2.0, 2.0, 0.0, 2.0]
        nboa['nboa_horz'] = [3.0, 3.0, 2.5, 2.5, 2.5, 2.0, 1.5, 1.5, 0.0, 1.5, 1.5, 0.0, 1.5]

        assembler.declare('\n'.join([declare_line(n, v) for n, v in nboa.items()]), source=__file__)

        el6_lens = nboa['nboa_lens']

        guide = assembler.component("NBOA", 'Elliptic_guide_gravity', at=([0, 0, 1e-5], "PREVIOUS"))
        # make sure that array-valued parameters can be set:
        guide.set_parameters(dimensionsAt="\"mid\"", R0=0.99, Qc=0.0217, alpha=3.1, W=0.003, xwidth=0.069634,
                             yheight=0.04862, linxw=3.4578, loutxw=0.415155, linyh=1.36, loutyh=3.487681,
                             seglength="nboa_lens", mvaluesright="nboa_horz", mvaluesleft="nboa_horz",
                             mvaluestop="nboa_vert", mvaluesbottom="nboa_vert", nSegments=len(el6_lens),
                             l=sum(el6_lens))

        # Bandwidth chopper
        bw_upstream_gap = 0.1
        bwc1 = assembler.component("BWC1", "DiskChopper", at=([0, 0, bw_upstream_gap], "PREVIOUS"))
        bwc1.set_parameters(theta_0="bw_disk_open_angle", radius='1+2+3+4', nslit='(2+4)/(1+2)', yheight=0.1,
                            nu="bw1speed", phase="bw1phase/2")

        for par in ('theta_0', 'nslit', 'nu', 'phase'):
            self.assertFalse(bwc1.get_parameter(par).value.is_constant)
        for par in ('radius', 'yheight'):
            self.assertTrue(bwc1.get_parameter(par).value.is_constant)

        # nslit is not a constant parameter because the expression parsing does not simplify grouped expressions
        nslit = bwc1.get_parameter('nslit').value.simplify()
        # But explicitly simplifying the expression is possible (in this simple case) and yields a constant value
        self.assertTrue(nslit.simplify().is_constant)

        phase = bwc1.get_parameter('phase').value  # == bw1phase / 2
        # In contrast, phase is Expr(BinaryOp('/', Expr.id('bw1phase'), Expr.int(2))) which can't be simplified
        self.assertFalse(phase.simplify().is_constant)

        # But we can attempt to parse the declarations and instantiation blocks from the instrument
        from mccode.translators.c_listener import extract_c_declared_expressions, evaluate_c_defined_expressions
        variables = {x.name:  x.value for x in assembler.instrument.parameters}
        for dec in assembler.instrument.declare:
            variables.update(extract_c_declared_expressions(dec.source))

        # defined as
        # TODO this does not work because the simple "C"-style expression parser doesn't know about pointers
        try:
            for init in assembler.instrument.initialize:
                variables = evaluate_c_defined_expressions(variables, init.source)
        except AttributeError:
            log.warn('Evaluating INITIALIZE section failed; see preceding errors for hints for why. '
                     'This is not a test failure condition (for now). Continuing')

        evaluated_phase = phase.evaluate(variables)
        self.assertTrue(evaluated_phase.is_constant)

        theta_0 = bwc1.get_parameter('theta_0').value
        self.assertTrue(theta_0.evaluate(variables).is_constant)

        # We want to know whether an expression involves any instrument parameters
        # -- which phase and nu do, but others do not:
        for x in ('phase', 'nu'):
            par = bwc1.get_parameter(x).value
            dep = any(par.depends_on(inst_par.name) for inst_par in assembler.instrument.parameters)
            self.assertTrue(dep)
        for x in ('theta_0', 'radius', 'nslit', 'yheight'):
            par = bwc1.get_parameter(x).value
            self.assertFalse(any(par.depends_on(inst_par.name) for inst_par in assembler.instrument.parameters))

    def assertRotationsEqual(self, r1, r2):
        from mccode.instr.orientation import Rotation, Matrix
        self.assertTrue(isinstance(r1, Rotation))
        self.assertTrue(isinstance(r2, Rotation))
        d = r1 - r2
        self.assertTrue(isinstance(d, Matrix))
        self.assertEqual(round(abs(d), 14), Matrix())

    def test_assemble_positioning(self):
        from mccode.common import Expr
        from mccode.instr.orientation import Vector, Rotation
        z, o = Expr.float(0), Expr.float(1)

        assembler = make_mcstas_assembler('orientation_test')
        # Start the actual instrument:
        assembler.component("origin", "Progress_bar", at=[0, 0, 0])
        # 'Fun' Positioning stuff
        left = assembler.component('left', 'Arm', at=([0, 0, 1], "origin"), rotate=[0, 90, 0])
        v3 = Vector(z, z, o)
        self.assertEqual(v3, left.orientation.position())
        self.assertEqual(Rotation(z, z, -o, z, o, z, o, z, z), left.orientation.rotation())
        self.assertEqual(left.orientation.rotation(), left.orientation.rotation('coordinates').inverse())

        up = assembler.component("up", 'Arm', at=([0, 0, 1], "left"), rotate=[-90, 0, 0])
        v4 = Vector(o, z, z)
        self.assertEqual(v4, up.orientation.position() - left.orientation.position())
        up_orientation = Rotation(z, z, -o, -o, z, z, z, o, z)
        self.assertRotationsEqual(up_orientation, up.orientation.rotation())
        self.assertEqual(Vector(o, z, o), up.orientation.position())
        self.assertRotationsEqual(up_orientation, up.orientation.rotation('coordinates').inverse())

        last = assembler.component("last", 'Arm', at=([0, 0, 1], "up"), rotate=[0, 0, 0])
        v5 = Vector(z, o, z)
        self.assertRotationsEqual(up_orientation, last.orientation.rotation())
        print(last.orientation.position())
        print(up.orientation.position())
        self.assertEqual(v5, last.orientation.position() - up.orientation.position())

    def test_read_positioning(self):
        instr_source = """
        DEFINE INSTRUMENT orientation_test()
        TRACE
        COMPONENT origin = Arm() AT (0, 0, 0) ABSOLUTE
        COMPONENT left = Arm() AT (0, 0, 1) RELATIVE PREVIOUS ROTATED (0, 90, 0) RELATIVE origin
        COMPONENT up = Arm() AT (0, 0, 1) RELATIVE left ROTATED (-90, 0, 0) RELATIVE left
        COMPONENT last = Arm() AT (0, 0, 1) RELATIVE up
        END
        """
        instr = parse_instr_string(instr_source)