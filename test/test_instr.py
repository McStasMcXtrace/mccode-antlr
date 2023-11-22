from unittest import TestCase
from zenlog import log


def parse_instr_string(instr_source: str):
    from mccode_antlr.loader import parse_mcstas_instr
    return parse_mcstas_instr(instr_source)


def make_mcstas_assembler(name: str):
    from mccode_antlr.assembler import Assembler
    from mccode_antlr.reader import MCSTAS_REGISTRY
    return Assembler(name, registries=[MCSTAS_REGISTRY])


class TestInstr(TestCase):
    def test_parse_empty_trace(self):
        from mccode_antlr.instr import Instr
        from mccode_antlr.common import InstrumentParameter, Expr, Value, DataType
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
        from mccode_antlr.instr import Instr
        from mccode_antlr.common import InstrumentParameter, Expr, Value, DataType

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
        from mccode_antlr.translators.c_listener import extract_c_declared_expressions, evaluate_c_defined_expressions
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
        from mccode_antlr.instr.orientation import Rotation, Matrix
        self.assertTrue(isinstance(r1, Rotation))
        self.assertTrue(isinstance(r2, Rotation))
        d = r1 - r2
        self.assertTrue(isinstance(d, Matrix))
        self.assertEqual(round(abs(d), 14), Matrix())

    def _positioning_evaluator(self, instr):
        """Common positioning checks for `test_read_positioning` and `test_assemble_positioning`"""
        from mccode_antlr.common import Expr
        from mccode_antlr.instr.orientation import Vector, Rotation
        z, o = Expr.float(0), Expr.float(1)

        left = instr.get_component('left')
        v3 = Vector(z, z, o)
        self.assertEqual(v3, left.orientation.position())
        self.assertEqual(Rotation(z, z, -o, z, o, z, o, z, z), left.orientation.rotation())
        self.assertEqual(left.orientation.rotation(), left.orientation.rotation('coordinates').inverse())

        up = instr.get_component('up')
        v4 = Vector(o, z, z)
        self.assertEqual(v4, up.orientation.position() - left.orientation.position())
        up_orientation = Rotation(z, z, -o, -o, z, z, z, o, z)
        self.assertRotationsEqual(up_orientation, up.orientation.rotation())
        self.assertEqual(Vector(o, z, o), up.orientation.position())
        self.assertRotationsEqual(up_orientation, up.orientation.rotation('coordinates').inverse())

        last = instr.get_component('last')
        v5 = Vector(z, o, z)
        self.assertRotationsEqual(up_orientation, last.orientation.rotation())
        self.assertEqual(v5, last.orientation.position() - up.orientation.position())

    def test_assemble_positioning(self):
        """Equivalent test to `test_read_positioning` but using an assembled instrument"""
        assembler = make_mcstas_assembler('orientation_test')
        origin = assembler.component("origin", "Progress_bar", at=[0, 0, 0])
        left = assembler.component('left', 'Arm', at=([0, 0, 1], origin), rotate=[0, 90, 0])
        up = assembler.component("up", 'Arm', at=([0, 0, 1], left), rotate=[-90, 0, 0])
        assembler.component("last", 'Arm', at=([0, 0, 1], up), rotate=[0, 0, 0])
        self._positioning_evaluator(assembler.instrument)

    def test_read_positioning(self):
        """Equivalent test to `test_assemble_positioning` but using a parsed instrument"""
        instr_source = """DEFINE INSTRUMENT orientation_test() TRACE
        COMPONENT origin = Arm() AT (0, 0, 0) ABSOLUTE
        COMPONENT left = Arm() AT (0, 0, 1) RELATIVE PREVIOUS ROTATED (0, 90, 0) RELATIVE origin
        COMPONENT up = Arm() AT (0, 0, 1) RELATIVE left ROTATED (-90, 0, 0) RELATIVE left
        COMPONENT last = Arm() AT (0, 0, 1) RELATIVE up
        END """
        self._positioning_evaluator(parse_instr_string(instr_source))

    def _simple_position_tests(self, instr, positions: dict):
        from mccode_antlr.common import Expr
        from mccode_antlr.instr.orientation import Vector
        positions = {k: Vector(*[Expr.float(x) for x in v]) for k, v in positions.items()}
        for instance in instr.components:
            self.assertEqual(positions[instance.name], instance.orientation.position())
            self.assertEqual(positions[instance.name], instance.orientation.position('axes'))
            self.assertEqual(positions[instance.name], instance.orientation.position('coordinates'))

    def test_simple_positioning(self):

        from math import pi, cos, sin
        instr_source = """DEFINE INSTRUMENT simple_test() TRACE
        COMPONENT origin = Arm() AT (0, 0, 0) ABSOLUTE
        COMPONENT slit = Arm() at (0, 0, 10) RELATIVE origin
        COMPONENT sample = Arm() at (0, 0, 10) RELATIVE slit
        END"""
        instr = parse_instr_string(instr_source)
        positions = {'origin': (0, 0, 0), 'slit': (0, 0, 10), 'sample': (0, 0, 20)}
        self._simple_position_tests(instr, positions)

        instr_source = """DEFINE INSTRUMENT slightly_more_complex() TRACE
        COMPONENT origin = Arm() AT (0, 0, 0) ABSOLUTE
        COMPONENT guide_start = Arm() AT (0.01277, 0, 1.930338) RELATIVE origin ROTATED (0, -0.56, 0) RELATIVE origin
        COMPONENT guide = Arm() AT (0, 0, 0) RELATIVE guide_start
        COMPONENT guide_end = Arm() AT (0, 0, 4.33) RELATIVE guide
        END
        """
        instr = parse_instr_string(instr_source)
        positions = {'origin': (0, 0, 0), 'guide_start': (0.01277, 0, 1.930338), 'guide': (0.01277, 0, 1.930338),
                     'guide_end': (0.01277 - 4.33*sin(pi/180*0.56), 0, 1.930338 + 4.33*cos(pi/180*0.56))}
        self._simple_position_tests(instr, positions)
        pos_hat = (0.006615, 0, 0.999978)
        pos = instr.components[2].orientation.position()
        distance = pos.length()
        vector = pos / distance
        self.assertAlmostEqual(vector.x, pos_hat[0], 6)
        self.assertAlmostEqual(vector.y, pos_hat[1], 6)
        self.assertAlmostEqual(vector.z, pos_hat[2], 6)
        self.assertAlmostEqual(distance, 1.930380239005777, 6)

        # Combining the position and rotation (reduced) operations should yield the same position
        comb = instr.components[2].orientation.combine().reduce()
        self.assertEqual(pos, comb.position())

    def test_copy(self):
        from mccode_antlr.instr import Instr
        from mccode_antlr.common import InstrumentParameter, Expr, Value, DataType
        instr_source = """
        DEFINE INSTRUMENT test_copy(par0=3.14159, double par1 = 49, int par2 =     1010110
            , string par3="this is a long string with spaces", 
            
            string par4, int par5, double par6, par7)
        TRACE
        COMPONENT first = Arm() AT (0, 0, 0) ABSOLUTE
        COMPONENT second = Arm() AT (0, 0, 1) RELATIVE first ROTATED (0, 90, 0) RELATIVE first
        END
        """
        instr = parse_instr_string(instr_source)
        instr_copy = instr.copy()
        self.assertTrue(isinstance(instr_copy, Instr))
        self.assertEqual(instr.name, instr_copy.name)
        self.assertEqual(len(instr.parameters), len(instr_copy.parameters))
        self.assertEqual(len(instr.components), len(instr_copy.components))
        for p, p_copy in zip(instr.parameters, instr_copy.parameters):
            self.assertTrue(isinstance(p_copy, InstrumentParameter))
            self.assertEqual(p.name, p_copy.name)
            self.assertEqual(p.value, p_copy.value)

        instr_copy.add_parameter(InstrumentParameter('par8', '', Expr.float(1.6189)))
        self.assertEqual(len(instr.parameters), len(instr_copy.parameters) - 1)

    def test_mcpl_split(self):
        from mccode_antlr.instr import Instr
        instr_source = """
        DEFINE INSTRUMENT test_copy(par0=3.14159, double par1 = 49, int par2 =     1010110
            , string par3="this is a long string with spaces", 

            string par4, int par5, double par6, par7)
        TRACE
        COMPONENT first = Arm() AT (0, 0, 0) ABSOLUTE
        COMPONENT second = Arm() AT (0, 0, 1) RELATIVE first ROTATED (0, 90, 0) RELATIVE first
        END
        """
        instr = parse_instr_string(instr_source)
        before, after = instr.mcpl_split('first', filename='test_mcpl_split')
        self.assertTrue(isinstance(before, Instr))
        self.assertTrue(isinstance(after, Instr))
        self.assertEqual(len(before.components), 1)
        self.assertEqual(len(after.components), 2)
        self.assertEqual(before.components[0].name, 'first')
        self.assertEqual(after.components[0].name, 'first')
        self.assertEqual(after.components[1].name, 'second')
        self.assertEqual(before.components[0].type.name, 'MCPL_output')
        self.assertEqual(after.components[0].type.name, 'MCPL_input')

    def test_tas1_c1(self):
        from mccode_antlr.loader.loader import parse_mccode_instr_parameters
        contents = """ DEFINE INSTRUMENT tas(PHM=-37.077,TTM=-74,C1=30) TRACE END"""
        instr_parameters = parse_mccode_instr_parameters(contents)
        self.assertEqual(len(instr_parameters), 3)
        self.assertEqual(instr_parameters[0].name, 'PHM')
        self.assertEqual(instr_parameters[1].name, 'TTM')
        self.assertEqual(instr_parameters[2].name, 'C1')
        self.assertEqual(instr_parameters[0].value, -37.077)
        self.assertEqual(instr_parameters[1].value, -74)
        self.assertEqual(instr_parameters[2].value, 30)


class CompiledTest(TestCase):
    def setUp(self):
        import subprocess
        from mccode_antlr.config import config
        try:
            subprocess.run([config['cc'].get(str), '--version'], check=True)
        except FileNotFoundError:
            log.info(f'Provide alternate C compiler via MCCODE_ANTLR_CC environment variable')
            self.skipTest(f"C compiler {config['cc']} not found")


class CompiledInstr(CompiledTest):
    def _compile_and_run(self, instr, parameters, run=True):
        from mccode_antlr.compiler.c import compile_instrument, CBinaryTarget, run_compiled_instrument
        from mccode_antlr.translators.target import MCSTAS_GENERATOR
        from mccode_antlr.loader import read_mccode_dat
        from mccode_antlr.config import config as module_config
        from tempfile import TemporaryDirectory
        from os import R_OK, access
        from pathlib import Path

        target = CBinaryTarget(mpi=False, acc=False, count=1, nexus=False)
        config = dict(default_main=True, enable_trace=False, portable=False, include_runtime=True,
                      embed_instrument_file=False, verbose=False)

        with TemporaryDirectory() as directory:
            try:
                compile_instrument(instr, target, directory, generator=MCSTAS_GENERATOR, config=config, dump_source=True)
            except RuntimeError as e:
                log.error(f'Failed to compile instrument: {e}')
                raise e
            binary = Path(directory).joinpath(f'{instr.name}{module_config["ext"].get(str)}')
            self.assertTrue(binary.exists())
            self.assertTrue(binary.is_file())
            self.assertTrue(access(binary, R_OK))
            if run:
                run_compiled_instrument(binary, target, f"--dir {directory}/instr {parameters}")
                sim_files = list(Path(directory).glob('**/*.dat'))
                dats = {file.stem: read_mccode_dat(file) for file in sim_files}
                return dats
            return None

    def test_one_axis(self):
        from math import pi, asin, sqrt
        from mccode_antlr.loader import parse_mcstas_instr
        d_spacing = 3.355  # (002) for Highly-ordered Pyrolytic Graphite
        mean_energy = 5.0
        energy_width = 0.5
        mean_ki = sqrt(mean_energy / 2.0722)
        instr = f"""
        DEFINE INSTRUMENT splitRunTest(a1=0, a2=0, virtual_source_x=0.05, virtual_source_y=0.1, string newname)
        TRACE
        COMPONENT origin = Arm() AT (0, 0, 0) ABSOLUTE
        COMPONENT source = Source_simple(yheight=2*virtual_source_y, xwidth=0.2, dist=1.5, focus_xw=0.06, focus_yh=0.12,
                                         E0={mean_energy}, dE={energy_width})
                           AT (0, 0, 0) RELATIVE origin
        COMPONENT m0 = PSD_monitor(xwidth=0.1, yheight=0.15, nx=100, ny=160, restore_neutron=1) AT (0, 0, 0.01) RELATIVE PREVIOUS
        COMPONENT guide = Guide_gravity(w1 = 0.06, h1 = 0.12, w2 = 0.05, h2 = 0.1, l = 30, m = 4) 
                          AT (0, 0, 1.5) RELATIVE  PREVIOUS
        COMPONENT guide_end = Arm() AT (0, 0, 30) RELATIVE PREVIOUS
        COMPONENT m1 = PSD_monitor(xwidth=0.1, yheight=0.15, nx=100, ny=160, restore_neutron=1) AT (0, 0, 0.01) RELATIVE PREVIOUS
        COMPONENT aperture = Slit(xwidth=virtual_source_x, yheight=virtual_source_y) AT (0, 0, 0.01) RELATIVE PREVIOUS
        COMPONENT split_at = Arm() AT (0, 0, 0.0001) RELATIVE PREVIOUS
        COMPONENT m3 = PSD_monitor(xwidth=0.1, yheight=0.15, nx=100, ny=160, restore_neutron=1) AT (0, 0, 0.01) RELATIVE PREVIOUS
        COMPONENT mono_point = Arm() AT (0, 0, 0.8) RELATIVE split_at
        METADATA "txt" "something" %{{
            This is some unparsed metadata that will be included as a literal string in the instrument.
        %}}
        COMPONENT mono = Monochromator_curved(zwidth = 0.02, yheight = 0.02, NH = 13, NV = 7, DM={d_spacing}) 
                         AT (0, 0, 0) RELATIVE  mono_point ROTATED (0, a1, 0) RELATIVE mono_point
        COMPONENT sample_arm = Arm() AT (0, 0, 0) RELATIVE mono_point ROTATED (0, a2, 0) RELATIVE mono_point
        COMPONENT detector = Monitor(xwidth=0.1, yheight=0.15, restore_neutron=1) AT (0, 0, 0.8) RELATIVE sample_arm
        COMPONENT lmon = L_monitor(filename=newname) AT (0, 0, 0.001) RELATIVE PREVIOUS
        END
        """
        instr = parse_mcstas_instr(instr)

        a1 = asin(pi / d_spacing / mean_ki) * 180 / pi
        self.assertAlmostEqual(a1, 37.0722, 4)
        parameters = f'a1={a1} a2={2 * a1} -n 1000000'

        dats = self._compile_and_run(instr, parameters)
        self.assertEqual(len(dats), 5)
        self.assertEqual(dats['m0'].data.shape, (3, 160, 100))
        self.assertEqual(dats['m1'].data.shape, (3, 160, 100))
        self.assertEqual(dats['m3'].data.shape, (3, 160, 100))
        self.assertEqual(dats['detector'].data.shape, (3, ))

        # Moving farther from the source means less (but finite) intensity in equivalent monitors
        self.assertTrue(sum(sum(dats['m0']['I'])) > sum(sum(dats['m1']['I'])) > sum(sum(dats['m3']['I'])) > 0)
        # The detector has been positioned correctly to collect intensity
        self.assertTrue(dats['detector']['I'] > 0)

    def test_assembled_parameters(self):
        """Check that setting an instance parameter to a value that is an instrument parameter name works"""
        assembler = make_mcstas_assembler('assembled_parameters_test_instr')
        assembler.parameter("double par0 = 3.14159")
        origin = assembler.component("origin", "Progress_bar", at=[0, 0, 0])
        left = assembler.component('left', 'Slit', at=([0, 0, 1], origin), rotate=[0, 90, 0],
                                   parameters=dict(xwidth='par0', yheight='2*fmod(par0, 0.1)'))

        self._compile_and_run(assembler.instrument, None, run=False)

    def test_vector_component_parameter(self):
        """Some components can use vector parameters, which must be initialized by initializer lists"""
        from mccode_antlr.common import Value
        # TODO Update the registry with the new Conics_* components, then update this test (if necessary)
        instr = """
        DEFINE INSTRUMENT test_vector_component_parameter() TRACE
        COMPONENT cEH = Conics_EH(R0=0.99, alpha=6.07, W=0.003, m=3, nshells=4, focal_length_u=10, focal_length_d=10,
                                  radii={0.05236, 0.03, 0.01, 0.0031416}, le=0.25, lh=0.25, disk=1)
        AT (0,0,0) ABSOLUTE
        COMPONENT cEH2 = Conics_EH(R0=0.99, alpha=6.07, W=0.003, m=3, nshells=0, focal_length_u=10, focal_length_d=10,
                                   le=0.25, lh=0.25, disk=0)
        AT (0,0,1) ABSOLUTE
        END
        """
        instr = parse_instr_string(instr)
        self.assertEqual(instr.components[0].get_parameter('radii').value, Value([0.05236, 0.03, 0.01, 0.0031416]))

        try:
            self._compile_and_run(instr, '-n 1000', run=True)
        except RuntimeError as e:
            log.error(f'Failed to compile instrument: {e}')
            self.fail(f'Failed to compile instrument {e}')



class CompiledMCPL(CompiledTest):
    def setUp(self):
        import subprocess
        try:
            subprocess.run(['mcpl-config', '--version'], check=True)
        except FileNotFoundError:
            self.skipTest('mcpl-config not found')

    def test_mcpl_split_run(self):
        # Adapted from Test_MCPL_*.instr in ${MCCODE}/mcstas-comps/examples
        from mccode_antlr.instr import Instr
        from mccode_antlr.common import ComponentParameter, Expr
        from mccode_antlr.compiler.c import compile_instrument, run_compiled_instrument, CBinaryTarget
        from mccode_antlr.translators.target import MCSTAS_GENERATOR
        from mccode_antlr.loader import read_mccode_dat
        from tempfile import TemporaryDirectory
        from os import R_OK, access
        from pathlib import Path
        from random import randint
        from numpy import allclose

        instr_source = """
        DEFINE INSTRUMENT Test_MCPL_output()
        USERVARS %{ double flag; %}
        TRACE
        COMPONENT Origin = Progress_bar() AT (0, 0, 0) ABSOLUTE
        COMPONENT sa = Source_Maxwell_3( /* flux in n/s/cm2/st/AA */
                                        Lmin=1, Lmax=11, dist=1, focus_xw=0.1, focus_yh=0.1, xwidth=0.01, yheight=0.01,
                                        T1=216.8,I1=1.24e+13,T2=33.9,I2=1.02e+13, T3=16.7 ,I3=3.0423e+12)
        AT (0,0,0) ABSOLUTE
        EXTEND %{
            t=1e-3*rand01();
            flag=(double)mcget_run_num();
        %}
        COMPONENT split_point = Arm() AT(0,0,0) RELATIVE PREVIOUS
        COMPONENT m1 = Monitor_nD(filename="o1", xwidth=0.2, yheight=0.2,
                                  options="lambda limits=[1 11] bins=100 parallel", bins=40)
        AT (0,0,0) ABSOLUTE
        COMPONENT m2 = Monitor_nD(filename="o2", xwidth=0.2, yheight=0.2, options="x y, parallel", bins=40)
        AT (0,0,0) ABSOLUTE
        COMPONENT m3 = Monitor_nD(filename="o3", xwidth=0.2, yheight=0.2, options="t limits=[0 1e-3]parallel", bins=40)
        AT (0,0,0) ABSOLUTE
        COMPONENT m4 = Monitor_nD(filename="o4", xwidth=0.2, yheight=0.2, options="E limits=[0 82] parallel", bins=40)
        AT (0,0,0) ABSOLUTE
        END
        """
        instr = parse_instr_string(instr_source)
        self.assertEqual(instr.name, 'Test_MCPL_output')

        flag_params = tuple(ComponentParameter(k, Expr.str(v)) for k, v in [
            ('userflag', '"flag"'), ('userflagcomment', '"Neutron Id"')])
        before, after = instr.mcpl_split('split_point', filename='test_mcpl_split', output_parameters=flag_params)
        self.assertEqual(before.name, 'Test_MCPL_output_first')
        self.assertEqual(after.name, 'Test_MCPL_output_second')
        self.assertTrue(isinstance(before, Instr))
        self.assertTrue(isinstance(after, Instr))
        self.assertEqual(len(before.components), 3)
        self.assertEqual(len(after.components), 5)
        for i, name in enumerate(('Origin', 'sa', 'split_point')):
            self.assertEqual(before.components[i].name, name)
        for i, name in enumerate(('split_point', 'm1', 'm2', 'm3', 'm4')):
            self.assertEqual(after.components[i].name, name)

        # If we compile and run the parsed instrument, or the split instrument parts, we should get the same results
        target = CBinaryTarget(mpi=False, acc=False, count=1, nexus=False)
        config = dict(default_main=True, enable_trace=False, portable=False, include_runtime=True,
                      embed_instrument_file=False, verbose=False)
        with TemporaryDirectory() as directory:
            expected_binaries = [Path(directory).joinpath(f'{x.name}.out') for x in (instr, before, after)]
            for obj in (instr, before, after):
                try:
                    compile_instrument(obj, target, directory, generator=MCSTAS_GENERATOR, config=config)
                except RuntimeError as e:
                    log.error(f'Failed to compile instrument: {e}')
                    raise e

            for binary in expected_binaries:
                self.assertTrue(binary.exists())
                self.assertTrue(binary.is_file())
                self.assertTrue(access(binary, R_OK))

            # Run the instrument and check that the output is the same
            seed = randint(1000, 2**32 - 1)
            common = f'--seed {seed} -n 10000'
            run_compiled_instrument(expected_binaries[0], target, f"--dir {directory}/instr {common}")
            mcpl_file = Path(directory).joinpath('instr.mcpl')
            run_compiled_instrument(expected_binaries[1], target, f"--dir {directory}/before {common} mcpl_filename={mcpl_file}")
            # Depending on how MCPL was built, it might have gzipped the output file
            if not mcpl_file.exists():
                mcpl_file = Path(directory).joinpath('instr.mcpl.gz')
            self.assertTrue(mcpl_file.exists())
            run_compiled_instrument(expected_binaries[2], target,
                                    f"--dir {directory}/after {common} mcpl_filename={mcpl_file}")

            # Now check that the instr and after outputs are the same
            instr_files = list(Path(directory).joinpath('instr').glob('o*'))
            after_files = list(Path(directory).joinpath('after').glob('o*'))
            self.assertEqual(len(instr_files), len(after_files))
            for file in instr_files:
                self.assertEqual(len([x for x in after_files if x.name == file.name]), 1)
            for file in after_files:
                self.assertEqual(len([x for x in instr_files if x.name == file.name]), 1)
            instr_files = [[x for x in instr_files if x.name == file.name][0] for file in after_files]
            for instr_file, after_file in zip(instr_files, after_files):
                # The files must be the same except for any header information:
                instr_data = read_mccode_dat(instr_file)
                after_data = read_mccode_dat(after_file)
                self.assertTrue(allclose(instr_data.data, after_data.data))
