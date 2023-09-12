from unittest import TestCase


class TestExpression(TestCase):
    def test_ObjectType(self):
        from mccode.common.expression import ObjectType as OT

        for ot in (OT.value, OT.initializer_list):
            self.assertFalse(ot.is_id)
            self.assertFalse(ot.is_parameter)
            self.assertFalse(ot.is_function)

        ot = OT.identifier
        self.assertTrue(ot.is_id)
        self.assertFalse(ot.is_parameter)
        self.assertFalse(ot.is_function)

        ot = OT.function
        self.assertFalse(ot.is_id)
        self.assertFalse(ot.is_parameter)
        self.assertTrue(ot.is_function)

        ot = OT.parameter
        self.assertFalse(ot.is_id)
        self.assertTrue(ot.is_parameter)
        self.assertFalse(ot.is_function)

        types = OT.value, OT.initializer_list, OT.identifier, OT.function, OT.parameter
        for ot in types:
            self.assertEqual(ot, ot)

        for i in range(len(types)):
            for j in range(len(types)):
                if i != j:
                    self.assertNotEqual(types[i], types[j])

    def test_ShapeType(self):
        from mccode.common.expression import ShapeType as ST
        st = ST.scalar
        vt = ST.vector
        self.assertFalse(st.compatible(vt))
        self.assertFalse(vt.compatible(st))
        self.assertTrue(st.compatible(st))
        self.assertTrue(vt.compatible(vt))
        self.assertTrue(st.is_scalar)
        self.assertFalse(st.is_vector)
        self.assertTrue(vt.is_vector)
        self.assertFalse(vt.is_scalar)
        self.assertEqual(st.mccode_c_type, '')
        self.assertEqual(vt.mccode_c_type, '*')

    def test_DataType(self):
        from mccode.common.expression import DataType as DT
        u, f, i, s = DT.undefined, DT.float, DT.int, DT.str
        for x in (u, f, i, s):
            self.assertTrue(x.compatible(x))
            self.assertTrue(u.compatible(x))
            self.assertTrue(x.compatible(u))
        for x in (f, i):
            self.assertFalse(s.compatible(x))
            self.assertFalse(x.compatible(s))
        self.assertTrue(f.compatible(i))
        self.assertTrue(i.compatible(f))

        for x in (u, f, i, s):
            self.assertEqual(x + x, x)
            self.assertEqual(x - x, x)
            self.assertEqual(x * x, x)
            self.assertEqual(x / x, x)

        for x in (f, i, s):
            self.assertEqual(x + u, x)
            self.assertEqual(x - u, x)
            self.assertEqual(x * u, x)
            self.assertEqual(x / u, x)
            self.assertEqual(u + x, x)
            self.assertEqual(u - x, x)
            self.assertEqual(u * x, x)
            self.assertEqual(u / x, x)

        for x in (u, f, i):
            self.assertEqual(x + s, s)
            self.assertEqual(x - s, s)
            self.assertEqual(x * s, s)
            self.assertEqual(x / s, s)
            self.assertEqual(s + x, s)
            self.assertEqual(s - x, s)
            self.assertEqual(s * x, s)
            self.assertEqual(s / x, s)

        self.assertEqual(i + f, i)
        self.assertEqual(i - f, i)
        self.assertEqual(i * f, i)
        self.assertEqual(i / f, i)

        self.assertEqual(i.mccode_c_type, 'int')
        self.assertEqual(f.mccode_c_type, 'double')
        self.assertEqual(s.mccode_c_type, 'char *')

    def test_Value(self):
        from mccode.common.expression import Value, ObjectType, ShapeType
        float_value = Value.float(1)
        int_value = Value.int(1)
        str_value = Value.str('1')
        id_value = Value.id('one')
        array_value = Value.array([1])
        function_value = Value.function('ones')

        for x in (float_value, int_value, str_value, id_value, array_value, function_value):
            self.assertFalse(x.is_op)
            self.assertFalse(x.is_zero)

        self.assertEqual(float_value.object_type, ObjectType.value)
        self.assertEqual(int_value.object_type, ObjectType.value)
        self.assertEqual(str_value.object_type, ObjectType.value)
        self.assertEqual(id_value.object_type, ObjectType.identifier)
        self.assertEqual(array_value.object_type, ObjectType.value)
        self.assertEqual(function_value.object_type, ObjectType.function)

        for x, y in ((float_value, ShapeType.scalar), (int_value, ShapeType.scalar), (str_value, ShapeType.scalar),
                     (id_value, ShapeType.scalar), (array_value, ShapeType.vector), (function_value, ShapeType.scalar)):
            self.assertEqual(x.shape_type, y)

        for x in (float_value, int_value, id_value, array_value, function_value):
            self.assertFalse(x.is_str)
        self.assertTrue(str_value.is_str)

        for x in (float_value, int_value, str_value, array_value, function_value):
            self.assertTrue(x.is_value(x._value))

        # Identifiers are not values:
        self.assertTrue(id_value.is_id)
        self.assertFalse(id_value.is_value(id_value._value))

        for x in (float_value, int_value, str_value, id_value, function_value):
            self.assertTrue(x.is_scalar)
            self.assertFalse(x.is_vector)
        self.assertFalse(array_value.is_scalar)
        self.assertTrue(array_value.is_vector)

    def test_float_Value(self):
        from mccode.common.expression import Value
        one = Value.float(1)
        two = Value.float(2)
        self.assertEqual(one, one)
        self.assertEqual(one + one, two)
        self.assertEqual(two - one, one)
        self.assertEqual(one * one, one)
        self.assertEqual(two / two, one)
        self.assertEqual(one - two, -one)
        self.assertEqual(abs(one - two), one)
        self.assertTrue(one < two)
        self.assertTrue(one <= two)
        self.assertTrue(two > one)
        self.assertTrue(two >= one)
        self.assertEqual(one.mccode_c_type, 'double')
        self.assertEqual(one.mccode_c_type_name, 'instr_type_double')

    def test_int_Value(self):
        from mccode.common.expression import Value
        one = Value.int(1)
        two = Value.int(2)
        self.assertEqual(one, one)
        self.assertEqual(one + one, two)
        self.assertEqual(two - one, one)
        self.assertEqual(one * one, one)
        self.assertEqual(two / two, one)
        self.assertEqual(one - two, -one)
        self.assertEqual(abs(one - two), one)
        self.assertTrue(one < two)
        self.assertTrue(one <= two)
        self.assertTrue(two > one)
        self.assertTrue(two >= one)
        self.assertEqual(one.mccode_c_type, 'int')
        self.assertEqual(one.mccode_c_type_name, 'instr_type_int')

    def test_str_Value(self):
        from mccode.common.expression import Value, BinaryOp
        one = Value.str('one')
        two = Value.str('two')
        self.assertEqual(one, one)
        self.assertEqual(one + one, BinaryOp('+', one, one))
        self.assertEqual(two - one, BinaryOp('-', two, one))
        self.assertEqual(one * one, BinaryOp('*', one, one))
        self.assertEqual(two / two, BinaryOp('/', two, two))
        self.assertEqual(one - two, BinaryOp('-', one, two))
        self.assertEqual(one.mccode_c_type, 'char *')
        self.assertEqual(one.mccode_c_type_name, 'instr_type_string')