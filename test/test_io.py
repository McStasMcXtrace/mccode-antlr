import unittest


class HDFIOTestCase(unittest.TestCase):
    def setUp(self):
        from pathlib import Path
        from tempfile import mkdtemp
        from importlib.util import find_spec
        if not find_spec('h5py'):
            self.skipTest("h5py not found -- skipping HDF5 tests")
        self.td = Path(mkdtemp())

    def tearDown(self):
        from shutil import rmtree
        rmtree(self.td)

    def test_one_axis(self):
        from mccode_antlr.io import load_hdf5, save_hdf5
        from mccode_antlr.loader import parse_mcstas_instr
        d_spacing = 3.355  # (002) for Highly-ordered Pyrolytic Graphite
        mean_energy = 5.0
        energy_width = 0.1
        instr = f"""
        DEFINE INSTRUMENT splitRunTest(a1=0, a2=0, virtual_source_x=0.05, virtual_source_y=0.1)
        TRACE
        COMPONENT origin = Arm() AT (0, 0, 0) ABSOLUTE
        COMPONENT source = Source_simple(yheight=0.25, xwidth=0.2, dist=1.5, focus_xw=0.06, focus_yh=0.12,
                                         E0={mean_energy}, dE={energy_width})
                           AT (0, 0, 0) RELATIVE origin
        COMPONENT guide = Guide_gravity(w1 = 0.06, h1 = 0.12, w2 = 0.05, h2 = 0.1, l = 30, m = 4) 
                          AT (0, 0, 1.5) RELATIVE  PREVIOUS
        COMPONENT guide_end = Arm() WHEN (a1 == 1) AT (0, 0, 30) RELATIVE PREVIOUS
        COMPONENT aperture = Slit(xwidth=virtual_source_x, yheight=virtual_source_y) AT (0, 0, 0.01) RELATIVE PREVIOUS
        METADATA "txt" "something" %{{
            This is some unparsed metadata that will be included as a literal string in the instrument.
        %}}
        COMPONENT split_at = Arm() AT (0, 0, 0.0001) RELATIVE PREVIOUS
        SPLIT 10 COMPONENT mono_point = Arm() AT (0, 0, 0.8) RELATIVE split_at
        COMPONENT mono = Monochromator_curved(zwidth = 0.02, yheight = 0.02, NH = 13, NV = 7, DM={d_spacing}) 
                         AT (0, 0, 0) RELATIVE  mono_point ROTATED (0, a1, 0) RELATIVE mono_point
        COMPONENT sample_arm = Arm() AT (0, 0, 0) RELATIVE mono_point ROTATED (0, a2, 0) RELATIVE mono_point
        COMPONENT detector = Monitor(xwidth=0.01, yheight=0.05) AT (0, 0, 0.8) RELATIVE sample_arm
        END
        """
        instr = parse_mcstas_instr(instr)
        filename = 'test.h5'
        save_hdf5(instr, self.td.joinpath(filename))

        read_instr = load_hdf5(self.td.joinpath(filename))
        self.assertEqual(instr.name, read_instr.name)
        instance_names = [c.name for c in instr.components]
        read_instance_names = [c.name for c in read_instr.components]
        self.assertEqual(instance_names, read_instance_names)


if __name__ == '__main__':
    unittest.main()
