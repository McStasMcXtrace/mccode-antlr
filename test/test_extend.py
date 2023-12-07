import unittest
from zenlog import log

class ExtendTestCase(unittest.TestCase):
    def setUp(self):
        import subprocess
        from mccode_antlr.config import config
        try:
            subprocess.run([config['cc'].get(str), '--version'], check=True)
        except FileNotFoundError:
            log.info(f'Provide alternate C compiler via MCCODE_ANTLR_CC environment variable')
            self.skipTest(f"C compiler {config['cc']} not found")

    def _compile_and_run(self, instr, parameters, run=True, experimental_extend=False):
        from mccode_antlr.compiler.c import compile_instrument, CBinaryTarget, run_compiled_instrument
        from mccode_antlr.translators.target import MCSTAS_GENERATOR
        from mccode_antlr.loader import read_mccode_dat
        from mccode_antlr.config import config as module_config
        from tempfile import TemporaryDirectory
        from os import R_OK, access
        from pathlib import Path

        target = CBinaryTarget(mpi=False, acc=False, count=1, nexus=False)
        config = dict(default_main=True, enable_trace=False, portable=False, include_runtime=True,
                      embed_instrument_file=False, verbose=False, experimental_extend=experimental_extend)

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

    def test_repeated_extends_compiles(self):
        from mccode_antlr.loader import parse_mcstas_instr
        from math import cos, sin, pi
        from textwrap import dedent
        instr = dedent("""\
        DEFINE INSTRUMENT test_repeated_extends_compiles(phase, ang)
        USERVARS %{
        int who;
        int what;
        %}
        TRACE
        COMPONENT Origin = Progress_bar() AT (0, 0, 0) ABSOLUTE 
        COMPONENT ESS_source = ESS_butterfly(
            sector="W", beamline=4, yheight=0.03, cold_frac=0.5, dist=1, focus_xw=0.01, focus_yh=0.01, 
            c_performance=1.0, t_performance=1.0, Lmin=1, Lmax=2, tmax_multiplier=1.5, n_pulses=1, acc_power=2.0
        ) AT (0, 0, 0) ABSOLUTE 
        COMPONENT guide = Guide_gravity(w1=0.01, w2=0.05, h1=0.01, h2=0.05, l=8.0, m=3.5, G=-9.82) AT (0, 0, 1) ABSOLUTE 
        COMPONENT guide_end = Arm() AT (0, 0, 8.0) RELATIVE guide
        COMPONENT chopper = DiskChopper(radius=0.35, nu=14, phase=phase, theta_0=115) AT (0, 0, 0.01) RELATIVE guide_end
        COMPONENT rotate = Arm() AT (0, 0, 0) RELATIVE chopper ROTATED (0, ang, 0) RELATIVE chopper
        COMPONENT aperture = Slit(xwidth=0.05, yheight=0.05) AT (0, 0, 1) RELATIVE rotate
        COMPONENT split_at = Arm() AT (0, 0, 1e-08) RELATIVE rotate
        COMPONENT sample = Incoherent(
            radius=0.005, yheight=0.02, thickness=0.001, focus_ah=2.0, focus_aw=2.0, target_x=1.0, target_y=0.0, 
            target_z=0.0, Etrans=0.0, deltaE=0.2
        ) AT (0, 0, 1) RELATIVE aperture
        """)
        for i in range(100):
            instr += f"COMPONENT slit_{i} = Slit(xwidth=0.01, yheight=1)\n"
            instr += f"          AT ({sin(i/180 * pi)}, 0, {cos(i/180 * pi)}) RELATIVE sample\n"
            instr += f"          EXTEND %{{ who = (SCATTERED) ? {i}: 0; %}}\n"
            instr += f"COMPONENT detector_{i} = Arm() WHEN ({i} == who) AT (0, 0, 1) RELATIVE slit_{i}\n"
            instr += f"          EXTEND %{{ what = (SCATTERED) ? 1: 0; %}}\n"
        instr += "END"
        instr = parse_mcstas_instr(instr)

        for experimental_extend in (False, True):
            try:
                self._compile_and_run(instr, '-n 1000 phase=10 ang=10', run=True,
                                      experimental_extend=experimental_extend)
            except RuntimeError as e:
                self.fail(f'Failed to compile instrument with {experimental_extend=}: {e}')


if __name__ == '__main__':
    unittest.main()
