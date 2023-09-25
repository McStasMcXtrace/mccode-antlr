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
        self.assertFalse(op.is_rotation)
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

    def test_OrientationParts(self):
        from mccode.common import Expr
        from mccode.instr.orientation import TranslationPart, Vector
        from mccode.instr.orientation import RotationX, RotationY, RotationZ
        from mccode.instr.orientation import OrientationParts

        tx = TranslationPart(v=Vector(Expr.float(0.1), Expr.float(0), Expr.float(0)))
        ty = TranslationPart(v=Vector(Expr.float(0.), Expr.float(0.2), Expr.float(0)))
        tz = TranslationPart(v=Vector(Expr.float(0.), Expr.float(0), Expr.float(0.3)))

        op = OrientationParts((tx, ty, tz)).reduce()
        self.assertEqual(len(op.stack()), 1)
        t = op.stack()[0]
        self.assertEqual(t, TranslationPart(v=Vector(Expr.float(0.1), Expr.float(0.2), Expr.float(0.3))))

        rx = RotationX(v=Expr.float(30), degrees=True)
        ry = RotationY(v=Expr.float(45), degrees=True)
        rz = RotationZ(v=Expr.float(60), degrees=True)

        rx2 = OrientationParts((rx, rx)).reduce()
        self.assertEqual(len(rx2.stack()), 1)
        rx2 = rx2.stack()[0]
        rx60 = RotationX(v=Expr.float(60), degrees=True)
        for a, b in zip(rx2.seitz(), rx60.seitz()):
            self.assertAlmostEqual(a, b)

        for a, b in zip((OrientationParts((rx,)) + OrientationParts((rx,))).reduce().stack()[0].seitz(), rx2.seitz()):
            self.assertEqual(a, b)

        ry2 = OrientationParts((ry, ry)).reduce()
        self.assertEqual(len(ry2.stack()), 1)
        ry2 = ry2.stack()[0]
        ry90 = RotationY(v=Expr.float(90), degrees=True)
        for a, b in zip(ry2.seitz(), ry90.seitz()):
            self.assertAlmostEqual(a, b)

        rz2 = OrientationParts((rz, rz)).reduce()
        self.assertEqual(len(rz2.stack()), 1)
        rz2 = rz2.stack()[0]
        rz120 = RotationZ(v=Expr.float(120), degrees=True)
        for a, b in zip(rz2.seitz(), rz120.seitz()):
            self.assertAlmostEqual(a, b)

        rxy = OrientationParts((rx, ry)).reduce().stack()[0]
        ryx = OrientationParts((ry, rx)).reduce().stack()[0]
        for j in ('xx', 'yy', 'zz'):
            self.assertAlmostEqual(getattr(rxy.seitz(), j), getattr(ryx.seitz(), j))
        for i, j in [('xy', 'yx')]:
            self.assertAlmostEqual(getattr(rxy.seitz(), i), getattr(ryx.seitz(), j))
        for i, j in [('xz', 'zx'), ('yz', 'zy')]:
            self.assertAlmostEqual(getattr(rxy.seitz(), i), -getattr(ryx.seitz(), j))

        trx = OrientationParts((t, rx)).reduce().stack()[0]
        rxt = OrientationParts((rx, t)).reduce().stack()[0]
        for j in ('xx', 'yy', 'zz', 'xy', 'yx', 'xz', 'zx', 'yz', 'zy', 'xt'):
            self.assertAlmostEqual(getattr(trx.seitz(), j), getattr(rxt.seitz(), j))
        for j in ('yt', 'zt'):
            self.assertNotAlmostEqual(getattr(trx.seitz(), j), getattr(rxt.seitz(), j))

        trz = OrientationParts((t, rz)).reduce().stack()[0]
        rzt = OrientationParts((rz, t)).reduce().stack()[0]
        for j in ('xx', 'yy', 'zz', 'xy', 'yx', 'xz', 'zx', 'yz', 'zy', 'zt'):
            self.assertAlmostEqual(getattr(trz.seitz(), j), getattr(rzt.seitz(), j))
        for j in ('xt', 'yt'):
            self.assertNotAlmostEqual(getattr(trz.seitz(), j), getattr(rzt.seitz(), j))

    def test_DependentOrientation(self):
        from mccode.common import Expr
        from mccode.instr.orientation import TranslationPart, Vector, Angles
        from mccode.instr.orientation import RotationX, RotationY, RotationZ
        from mccode.instr.orientation import OrientationParts, DependentOrientation

        v123 = Vector(Expr.float(0.1), Expr.float(0.2), Expr.float(0.3))
        v321 = Vector(Expr.float(0.3), Expr.float(0.2), Expr.float(0.1))
        t123 = TranslationPart(v=v123)
        t321 = TranslationPart(v=v321)

        a000 = Angles(Expr.float(0), Expr.float(0), Expr.float(0))

        dop = DependentOrientation.from_dependent_orientation(None, v123, a000)
        self.assertEqual(dop.position(), v123)

        d2 = DependentOrientation.from_dependent_orientation(dop, v321, a000)
        t444 = OrientationParts((t123, t321)).reduce().stack()[0]
        self.assertEqual(d2.position(), t444.position())
        self.assertEqual(d2.angles(), a000)