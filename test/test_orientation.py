from unittest import TestCase


class TestOrientation(TestCase):
    def test_seitz_multiply_identity(self):
        from numpy import random
        from mccode.common import Expr
        from mccode.instr.orientation import seitz_multiply
        o, z = Expr.float(1), Expr.float(0)
        a = o, z, z, z, z, o, z, z, z, z, o, z
        b = seitz_multiply(a, a)
        self.assertEqual(a, b)

        c = tuple(Expr.float(random.rand()) for _ in range(12))
        b = seitz_multiply(a, c)
        self.assertEqual(b, c)

    def test_seitz_inverse(self):
        from numpy import random, pi
        from mccode.common import Expr
        from mccode.instr.orientation import seitz_multiply, seitz_inverse, cos_value, sin_value
        o, z = Expr.float(1), Expr.float(0)
        a = o, z, z, z, z, o, z, z, z, z, o, z
        # Construct a matrix that *has* an inverse (use rotations to make life easier)
        tx, ty, tz = [Expr.float(random.rand() * 2 * pi - pi) for _ in range(3)]
        tx, ty, tz = [Expr.float(30/180*pi) for _ in range(3)]
        cx, sx = cos_value(tx, False), sin_value(tx, False)
        cy, sy = cos_value(ty, False), sin_value(ty, False)
        cz, sz = cos_value(tz, False), sin_value(tz, False)
        rx = o, z, z, z, z, cx, sx, z, z, -sx, cx, z
        ry = cy, z, -sy, z, z, o, z, z, sy, z, cy, z
        rz = cz, sz, z, z, -sz, cz, z, z, z, z, o, z
        b = seitz_multiply(rz, seitz_multiply(ry, rx))
        c = seitz_inverse(b)
        d = seitz_multiply(c, b)

        for i, j in zip(d, a):
            self.assertAlmostEqual(i, j)

        for i, j in zip(b, seitz_inverse(c)):
            self.assertAlmostEqual(i, j)
