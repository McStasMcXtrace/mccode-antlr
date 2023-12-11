import unittest


class MetadataTestCase(unittest.TestCase):
    def test_direct_creation(self):
        from mccode_antlr.common import MetaData
        md = MetaData.from_instance_tokens('instance_source', 'mimetype', 'metadata_name', 'metadata_value')
        self.assertEqual(md.source.name, 'instance_source')
        self.assertEqual(md.source.type_name, 'Instance')
        self.assertEqual(md.name, 'metadata_name')
        self.assertEqual(md.mimetype, 'mimetype')
        self.assertEqual(md.value, 'metadata_value')

    def test_parsed(self):
        from mccode_antlr.loader import parse_mcstas_instr
        from json import loads
        instr = """
        DEFINE INSTRUMENT splitRunTest(a1=0, a2=0, virtual_source_x=0.05, virtual_source_y=0.1, string newname)
        TRACE
        COMPONENT origin = Arm() AT (0, 0, 0) ABSOLUTE
        COMPONENT point = Arm() AT (0, 0, 0.8) RELATIVE origin
        METADATA "application/text" "names with spaces keep their quotes" %{
            This is some unparsed metadata that will be included as a literal string in the instrument.
        %}
        COMPONENT line = Arm() AT (0, 0, 1) RELATIVE PREVIOUS METADATA "application/json" identifier_name %{
            {"key": "value", "array": [1, 2, 3]}
        %}
        END
        """
        instr = parse_mcstas_instr(instr)
        self.assertEqual(len(instr.components), 3)
        self.assertEqual(instr.components[1].name, 'point')
        self.assertEqual(len(instr.components[1].metadata), 1)
        md = instr.components[1].metadata[0]
        self.assertEqual(md.source.name, 'point')
        self.assertEqual(md.source.type_name, 'Instance')
        self.assertEqual(md.name, '"names with spaces keep their quotes"')
        self.assertEqual(md.mimetype, 'application/text')
        self.assertEqual(md.value, """
            This is some unparsed metadata that will be included as a literal string in the instrument.
        """)
        self.assertEqual(instr.components[2].name, 'line')
        self.assertEqual(len(instr.components[2].metadata), 1)
        md = instr.components[2].metadata[0]
        self.assertEqual(md.source.name, 'line')
        self.assertEqual(md.source.type_name, 'Instance')
        self.assertEqual(md.name, 'identifier_name')
        self.assertEqual(md.mimetype, 'application/json')
        self.assertEqual(loads(md.value), {'key': 'value', 'array': [1, 2, 3]})



if __name__ == '__main__':
    unittest.main()
