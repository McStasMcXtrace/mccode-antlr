from unittest import TestCase


def _make_seitz_list(tx, ty, tz, degrees=False):
    from mccode.common import Expr
    from mccode.instr.orientation import Seitz, cos_value, sin_value
    o, z = Expr.float(1), Expr.float(0)
    cx, sx = cos_value(tx, degrees), sin_value(tx, degrees)
    cy, sy = cos_value(ty, degrees), sin_value(ty, degrees)
    cz, sz = cos_value(tz, degrees), sin_value(tz, degrees)
    rx = Seitz(o, z, z, z, z, cx, sx, z, z, -sx, cx, z)
    ry = Seitz(cy, z, -sy, z, z, o, z, z, sy, z, cy, z)
    rz = Seitz(cz, sz, z, z, -sz, cz, z, z, z, z, o, z)
    return rx, ry, rz


def _random_angles_radian():
    from numpy import random, pi
    from mccode.common import Expr
    return [Expr.float(random.rand() * 2 * pi - pi) for _ in range(3)]


def _random_angles_degrees():
    from numpy import random
    from mccode.common import Expr
    return [Expr.float(random.rand() * 360 - 180) for _ in range(3)]


class TestOrientation(TestCase):
    def test_seitz_multiply_identity(self):
        from numpy import random
        from mccode.common import Expr
        from mccode.instr.orientation import Seitz
        o, z = Expr.float(1), Expr.float(0)
        a = Seitz(o, z, z, z, z, o, z, z, z, z, o, z)
        b = a * a
        self.assertEqual(a, b)

        c = Seitz(*[Expr.float(random.rand()) for _ in range(12)])
        b = a * c
        self.assertEqual(b, c)

    def test_seitz_inverse(self):
        from numpy import random, pi
        from mccode.common import Expr
        from mccode.instr.orientation import Seitz, cos_value, sin_value
        o, z = Expr.float(1), Expr.float(0)
        a = Seitz(o, z, z, z, z, o, z, z, z, z, o, z)
        # Construct a matrix that *has* an inverse (use rotations to make life easier)
        ts = ([Expr.float(30/180*pi) for _ in range(3)], _random_angles_radian(),)
        for tx, ty, tz in ts:
            rx, ry, rz = _make_seitz_list(tx, ty, tz)
            b = rz * (ry * rx)
            c = b.inverse()
            d = c * b

            for i, j in zip(d, a):
                self.assertAlmostEqual(i, j)

            for i, j in zip(b, c.inverse()):
                self.assertAlmostEqual(i, j)

    def test_OrientationPart(self):
        from mccode.common import Expr
        from mccode.instr.orientation import OrientationPart, Vector
        op = OrientationPart()
        self.assertFalse(op.is_translation)
        self.assertTrue(op.is_rotation)
        self.assertTrue(op.all_values)
        self.assertTrue(op.is_constant)

        axis, angle, unit = op.rotation_axis_angle
        self.assertEqual(unit, 'degrees')
        self.assertEqual(angle, Expr.float(0))
        # Since the angle is zero, the axis is degenerate and the returned value depends on details of the eigenvalue
        # solver, which we are not testing here.

        tx, ty, tz = _random_angles_degrees()
        rx, ry, rz = _make_seitz_list(tx, ty, tz, degrees=True)

        # for individual rotations, it's easy to prove that axes and coordinates rotate opposite each other:
        opx = OrientationPart(rx, rx.inverse())
        opy = OrientationPart(ry, ry.inverse())
        opz = OrientationPart(rz, rz.inverse())

        vx = Vector(Expr.float(1), Expr.float(0), Expr.float(0))
        vy = Vector(Expr.float(0), Expr.float(1), Expr.float(0))
        vz = Vector(Expr.float(0), Expr.float(0), Expr.float(1))

        for o, t, v in [(opx, tx, vx), (opy, ty, vy), (opz, tz, vz)]:
            axis, angle, unit = o.rotation_axis_angle
            if (angle * t) < Expr.float(0):
                # this shouldn't happen since we've selected all vectors to be positive
                angle *= Expr.float(-1)
                axis = Vector(-axis.x, -axis.y, -axis.z)
            self.assertEqual(unit, 'degrees')
            self.assertAlmostEqual(angle, t)
            self.assertEqual(axis, v)

    def test_RotationParts(self):
        from mccode.common import Expr
        from mccode.instr.orientation import RotationPart, RotationX, RotationY, RotationZ, Angles, Vector

        rp = RotationPart()
        self.assertTrue(rp.is_constant)
        self.assertFalse(rp.is_translation)
        self.assertTrue(rp.is_rotation)
        self.assertEqual(rp.rotation_axis, Vector(Expr.float(0), Expr.float(0), Expr.float(0)))
        self.assertEqual(rp.position(), Vector(Expr.float(0), Expr.float(0), Expr.float(0)))

        tx, ty, tz = _random_angles_degrees()

        # for individual rotations, it's easy to prove that axes and coordinates rotate opposite each other:
        rpx = RotationX(v=tx, degrees=True)
        self.assertTrue(rpx.is_constant)
        self.assertFalse(rpx.is_translation)
        self.assertTrue(rpx.is_rotation)
        self.assertEqual(rpx.rotation_axis, Vector(Expr.float(1), Expr.float(0), Expr.float(0)))
        self.assertEqual(rpx.angles(), Angles(tx, Expr.float(0), Expr.float(0)))

        rpy = RotationY(v=ty, degrees=True)
        self.assertTrue(rpy.is_constant)
        self.assertFalse(rpy.is_translation)
        self.assertTrue(rpy.is_rotation)
        self.assertEqual(rpy.rotation_axis, Vector(Expr.float(0), Expr.float(1), Expr.float(0)))
        self.assertEqual(rpy.angles(), Angles(Expr.float(0), ty, Expr.float(0)))

        rpz = RotationZ(v=tz, degrees=True)
        self.assertTrue(rpz.is_constant)
        self.assertFalse(rpz.is_translation)
        self.assertTrue(rpz.is_rotation)
        self.assertEqual(rpz.rotation_axis, Vector(Expr.float(0), Expr.float(0), Expr.float(1)))
        self.assertEqual(rpz.angles(), Angles(Expr.float(0), Expr.float(0), tz))

