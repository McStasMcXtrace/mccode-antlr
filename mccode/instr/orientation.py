from dataclasses import dataclass, field
from ..common import Expr, unary_expr, binary_expr
from zenlog import log
from typing import TypeVar

Vector = tuple[Expr, Expr, Expr]
Angles = tuple[Expr, Expr, Expr]
Rotation = tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr]
Seitz = tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr]
Affine = tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr]


def _value_float_tuple(n, v=0.):
    return tuple(Expr.float(v) for _ in range(n))


def cos_degree(theta_degree):
    from math import pi, cos
    return cos(theta_degree / 180 * pi)


def sin_degree(theta_degree):
    from math import pi, sin
    return sin(theta_degree / 180 * pi)


def atan2_degree(y, x):
    from math import pi, atan2
    return atan2(y, x) / pi * 180


def acos_degree(v):
    from math import pi, acos
    return acos(v) / pi * 180


def acos_value(v: Expr, degrees=True):
    from math import acos
    pi = Expr.float(180) if degrees else Expr.float('PI')
    if v.is_value(1):
        return Expr.float(0)
    if v.is_value(0):
        return pi / Expr.float(2)
    if v.is_value(-1):
        return pi
    return unary_expr(acos_degree if degrees else acos, 'acos', v)


def cos_value(v: Expr, degrees=True):
    """The cosine of an angle expressed in degrees or radian"""
    from math import cos
    if v.is_value(0):
        return Expr.float(1)
    if (degrees and v.is_value(Expr.float(90))) or (not degrees and v.is_value(Expr.float('PI')/Expr.float(2))):
        return Expr.float(0)
    if (degrees and v.is_value(Expr.float(180))) or (not degrees and v.is_value(Expr.float('PI'))):
        return Expr.float(-1)
    return unary_expr(cos_degree if degrees else cos, 'cos', v)


def sin_value(v: Expr, degrees=True):
    from math import sin
    if v.is_value(0):
        return Expr.float(0)
    if (degrees and v.is_value(Expr.float(90))) or (not degrees and v.is_value(Expr.float('PI') / Expr.float(2))):
        return Expr.float(1)
    if (degrees and v.is_value(Expr.float(180))) or (not degrees and v.is_value(-Expr.float('PI') / Expr.float(2))):
        return Expr.float(-1)
    return unary_expr(sin_degree if degrees else sin, 'sin', v)


def atan2_value(va: Expr, vb: Expr, degrees=True):
    from math import atan2
    zero = Expr.float(0)
    full = Expr.float(180) if degrees else Expr.float('PI')
    half = full / Expr.float(2)
    if va.is_value(0):
        if vb.is_op:
            return [zero, full]
        return [zero if vb > zero else full]
    if vb.is_value(0):
        if va.is_op:
            return [-half, half]
        return [half if va > zero else -half]
    return [binary_expr(atan2_degree if degrees else atan2, 'atan2', va, vb)]


def cos_from_sin_value(v: Expr):
    from ..common import UnaryOp
    if v.is_value(0):
        return Expr.float(1)
    if v.is_value(1):
        return Expr.float(0)
    if v.is_op and isinstance(v.expr[0], UnaryOp):
        if '-' == v.expr[0].op:
            return cos_from_sin_value(Expr(v.expr[0].value))
        if 'sin' == v.expr[0].op:
            return Expr(UnaryOp('cos', v.expr[0].value))
    return sqrt_value(Expr.float(1) - v * v)


def sqrt_value(v: Expr):
    from math import sqrt
    return unary_expr(sqrt, 'sqrt', v)


def degree_to_radian(v: Expr):
    from math import pi
    if v.is_id:
        if v == Expr.float('PI'):
            raise RuntimeError(f'Convert {v} to radian')
        return v * (Expr.float('PI') / Expr.float(180))
    return v * Expr.float(pi / 180)


def _rotation_angles_to_axes_coordinates(rotated: Angles, degrees=True):
    cx, cy, cz = [cos_value(r if degrees else degree_to_radian(r), degrees=degrees) for r in rotated]
    sx, sy, sz = [sin_value(r if degrees else degree_to_radian(r), degrees=degrees) for r in rotated]
    # Rotation matrices following the McCode first x then y then z method of applying rotations.
    # The 3x3 rotation matrix part (which rotates the *axes* of a coordinate system):
    axes = (cy * cz, sx * sy * cz + cx * sz, sx * sz - cx * sy * cz,
            -cy * sz, cx * cz - sx * sy * sz, sx * cz + cx * sy * sz,
            sy, -sx * cy, cx * cy)
    # The coordinates of the same system rotate the opposite way, but still in the same order
    # (All sin terms gain a negative sign)
    coordinates = (cy * cz, sx * sy * cz - cx * sz, sx * sz + cx * sy * cz,
                   cy * sz, cx * cz + sx * sy * sz, -sx * cz + cx * sy * sz,
                   -sy, sx * cy, cx * cy)
    return axes, coordinates


def axes_euler_angles(m: Rotation, degrees) -> Angles:
    """Return the angles vector which could have been used to produce this 'axes' rotation matrix"""
    rxs = atan2_value(-m[8], m[7], degrees=degrees)
    rys = atan2_value(m[6], cos_from_sin_value(m[6]), degrees=degrees)
    rzs = atan2_value(-m[4], m[0], degrees=degrees)
    rx = rxs[0] if len(rxs) == 1 else rxs[0]
    ry = rys[0] if len(rys) == 1 else rys[0]
    rz = rzs[0] if len(rzs) == 1 else rzs[0]
    return rx, ry, rz


OrientationPartType = TypeVar('OrientationPartType', bound='OrientationPart')


class OrientationPart:
    """The Seitz matrix part of any arbitrary projective affine transformation"""
    _axes: Seitz = field(default_factory=lambda: _value_float_tuple(12))
    _coordinates: Seitz = field(default_factory=lambda: _value_float_tuple(12))

    @property
    def is_translation(self):
        return any(not p.is_zero for p in (self._axes[3], self._axes[7], self._axes[11]))

    @property
    def is_rotation(self):
        return (self._axes[0] + self._axes[5] + self._axes[10]) != Expr.float(3)

    @property
    def rotation_axis_angle(self) -> tuple[Vector, Expr, str]:
        from numpy.linalg import eig
        from numpy import array, argmin, sqrt, real, imag, conj, sum
        if not self.is_rotation or not self.is_constant:
            raise RuntimeError('Not possible to determine the rotation axis and angle of a variable general transform')
        matrix = [[self._axes[0].value.value, self._axes[1].value.value, self._axes[2].value.value],
                  [self._axes[4].value.value, self._axes[5].value.value, self._axes[6].value.value],
                  [self._axes[8].value.value, self._axes[9].value.value, self._axes[10].value.value]]
        dd, vv = eig(array(matrix))
        # The eigenvalues, dd, are (1+0j, a+bj, a-bj) of which we want 1+0j.
        axis = vv[:, argmin(sqrt(real(conj(dd-1) * (dd-1))))]
        if sum(imag(axis)) != 0:
            log.warn(f'Imaginary rotation axis {real(axis)} + j {imag(axis)}')
        axis = real(axis)
        cos_angle = (matrix[0][0] + matrix[1][1] + matrix[2][2] - 1) / 2
        if abs(cos_angle) > 1:
            log.warn(f'Invalid cos(angle) {cos_angle} for {self}')
        angle = acos_degree(cos_angle)
        return (Expr.float(axis[0]), Expr.float(axis[1]), Expr.float(axis[2])), Expr.float(angle), 'degrees'

    def __str__(self):
        x = [f'{x}' for x in self._axes]
        widths = [max(len(x[i+4*j]) for j in range(3)) for i in range(4)]
        line_fmt = [f'>{w+2:d}s' for w in widths]
        lines = '\n'.join(' '.join(f'{x[i+4*j]:{f:s}}' for i, f in zip(range(4), line_fmt)) for j in range(3))
        return lines

    @property
    def axes(self) -> Seitz:
        return self._axes

    @property
    def coordinates(self) -> Seitz:
        return self._coordinates

    def seitz(self, which=None) -> Seitz:
        return self.axes if 'axes' in which else self.coordinates

    def position(self, which=None) -> Vector:
        t = self.seitz(which)
        return t[3], t[7], t[11]

    def angles(self, which=None, degrees=True) -> Angles:
        t = self.seitz('axes')
        return axes_euler_angles((t[0], t[1], t[2], t[4], t[5], t[6], t[8], t[9], t[10]), degrees)

    @property
    def all_values(self) -> bool:
        return all(x.has_value for x in self._axes) and all(x.has_value for x in self._coordinates)

    @property
    def is_constant(self) -> bool:
        return all(x.is_constant for x in self._axes) and all(x.is_constant for x in self._coordinates)

    def inverse(self: OrientationPartType) -> OrientationPartType:
        return self

    def __mul__(self: OrientationPartType, other: OrientationPartType) -> OrientationPartType:
        if not isinstance(other, OrientationPart):
            raise RuntimeError('Multiplication only defined for two orientation parts')
        if not self.is_constant or not other.is_constant:
            raise ValueError('Multiplication only defined for two *constant* orientation parts')
        out = OrientationPart()
        out._axes = seitz_multiply(self.axes, other.axes)
        out._coordinates = seitz_multiply(self.coordinates, other.coordinates)
        return out


@dataclass
class TranslationPart(OrientationPart):
    """A specialization to the translation-only part of a projective affine transformation"""
    v: Vector

    def __str__(self):
        return f'({self.v[0]}, {self.v[1]}, {self.v[2]}) [0, 0, 0]'

    @property
    def is_constant(self):
        return all(x.has_value for x in self.v)

    @property
    def is_translation(self):
        return True

    @property
    def is_rotation(self):
        return False

    @property
    def rotation_axis_angle(self) -> tuple[Vector, Expr, str]:
        raise RuntimeError('Not possible to determine the rotation axis and angle of a translation')

    def __post_init__(self):
        z, o = Expr.float(0), Expr.float(1)
        self._axes = o, z, z, self.v[0], z, o, z, self.v[1], z, z, o, self.v[2]
        self._coords = self._axes

    def inverse(self):
        return TranslationPart(v=(-self.v[0], -self.v[1], -self.v[2]))

    def position(self, which=None) -> Vector:
        return self.v

    def angles(self, which=None, degrees=True) -> Angles:
        z = Expr.float(0)
        return z, z, z


@dataclass
class RotationPart(OrientationPart):
    """A specialization to the rotation-only part of a projective affine transformation"""
    v: Expr
    degrees: bool = True


    @property
    def is_constant(self):
        return self.v.has_value

    @property
    def is_translation(self):
        return False

    @property
    def is_rotation(self):
        return True

    @property
    def rotation_axis(self) -> Vector:
        return Expr.float(0), Expr.float(0),  Expr.float(0)

    @property
    def rotation_axis_angle(self) -> tuple[Vector, Expr, str]:
        return self.rotation_axis, self.v, 'degrees' if self.degrees else 'radian'

    def _cos_sin_one_zero(self):
        r = self.v if self.degrees else degree_to_radian(self.v)
        return cos_value(r), sin_value(r), Expr.float(1), Expr.float(0)

    def position(self, which=None) -> Vector:
        z = Expr.float(0)
        return z, z, z


class RotationX(RotationPart):
    """A specialization to the rotation-around-X part of a projective affine transformation"""
    def __post_init__(self):
        c, s, o, z = self._cos_sin_one_zero()
        self._axes = o, z, z, z, z, c, -s, z, z, s, c, z
        self._coordinates = o, z, z, z, z, c, s, z, z, -s, c, z

    def inverse(self):
        return RotationX(v=-self.v, degrees=self.degrees)

    def angles(self, which=None, degrees=True) -> Angles:
        z = Expr.float(0)
        return self.v, z, z

    def __str__(self):
        return f'(0, 0, 0) [{self.v}, 0, 0]'

    @property
    def rotation_axis(self) -> Vector:
        return Expr.float(1), Expr.float(0), Expr.float(0)


class RotationY(RotationPart):
    """A specialization to the rotation-around-Y part of a projective affine transformation"""
    def __post_init__(self):
        c, s, o, z = self._cos_sin_one_zero()
        self._axes = c, z, s, z, z, o, z, z, -s, z, c, z
        self._coordinates = c, z, -s, z, z, o, z, z, s, z, c, z

    def inverse(self):
        return RotationY(v=-self.v, degrees=self.degrees)

    def angles(self, which=None, degrees=True) -> Angles:
        z = Expr.float(0)
        return z, self.v, z

    def __str__(self):
        return f'(0, 0, 0) [0, {self.v}, 0]'

    @property
    def rotation_axis(self) -> Vector:
        return Expr.float(0), Expr.float(1), Expr.float(0)


class RotationZ(RotationPart):
    """A specialization to the rotation-around-Z part of a projective affine transformation"""
    def __post_init__(self):
        c, s, o, z = self._cos_sin_one_zero()
        self._axes = c, -s, z, z, s, c, z, z, z, z, o, z
        self._coordinates = c, s, z, z, -s, c, z, z, z, z, o, z

    def inverse(self):
        return RotationZ(v=-self.v, degrees=self.degrees)

    def angles(self, which=None, degrees=True) -> Angles:
        z = Expr.float(0)
        return z, z, self.v

    def __str__(self):
        return f'(0, 0, 0) [0, 0, {self.v}]'

    @property
    def rotation_axis(self) -> Vector:
        return Expr.float(0), Expr.float(0), Expr.float(1)


OrientationPartsType = TypeVar('OrientationPartsType', bound='OrientationParts')


@dataclass
class OrientationParts:
    """A list of unresolved or partially resolved successive projective affine transformation(s)"""
    _stack: tuple[OrientationPart] = field(default_factory=tuple)

    def stack(self):
        return self._stack

    def _copy(self, deep: bool = True) -> tuple[OrientationPart]:
        if deep:
            from copy import deepcopy
            return tuple([deepcopy(x) for x in self._stack])
        return tuple(x for x in self._stack)

    def copy(self, deep: bool = True) -> OrientationPartsType:
        return OrientationParts(self._copy(deep))

    def __add__(self, other) -> OrientationPartsType:
        out = self._copy()
        if isinstance(other, OrientationParts):
            out += other.stack()
        elif isinstance(other, OrientationPart):
            out += (other,)
        else:
            raise ValueError(f'__add__ undefined for OrientationParts and {type(other)}')
        return OrientationParts(out)

    @classmethod
    def from_at_rotated(cls, at: Vector, rotated: Angles, degrees=True):
        """Emulate the McCode ordered-4-part-transformation:
            1. Translate to the specified position
            2. Rotate around the current X axis
            3. Rotate around the resulting Y axis
            4. Rotate around the resulting Z axis
        Such a method can make some orientations difficult to express, and the McCode solution
        is to chain successive ordered transformations with some parts set to zero.
        """
        # The order of individual OrientationPart objects in this tuple is paramount
        s = tuple()
        if not all(x.is_zero for x in at):
            s += (TranslationPart(v=at),)
        if not rotated[0].is_zero:
            s += (RotationX(v=rotated[0], degrees=degrees), )
        if not rotated[1].is_zero:
            s += (RotationY(v=rotated[1], degrees=degrees), )
        if not rotated[2].is_zero:
            s += (RotationZ(v=rotated[2], degrees=degrees), )
        return cls(s)

    @classmethod
    def from_dependent_chain(cls, dep: OrientationPartsType, at: Vector, rotated: Angles, degrees=True, copy=True):
        """
        If it is beneficial to rotate around Z before rotating around the resulting X,
        one can have successive components which are rotated (0,0,rz) (rx,0,0).
        By using the from_dependent_chain method these two projective transformations can be combined
        in the correct order

        :param dep: The projective transformation list which proceeds the newly added one(s)
        :param at: The translational part of the new projective transformation
        :param rotated: The angles of the three successive rotational parts
        :param degrees: Whether the angles are in degrees or radian
        :param copy: Whether the proceeding list should be copied
        :return: A OrientationParts object representing the chained operations
        """
        stack = () if dep is None else dep._copy(deep=copy)
        stack += cls.from_at_rotated(at, rotated, degrees).stack()
        return cls(stack)

    def inverse(self):
        """Return the inverse transformation of the full chain
        For operations Z Y X T R, the inverse is (Z Y X T R)^-1 which has the property
            (Z Y X T R)^-1 Z Y X T R = 1
        from inspection this can only be true if the inverse applies the inverse of each
        projective-transformation-part in reverse order
            R^-1 T^-1 X^-1 Y^-1 Z^-1 Z Y X T R = 1
        """
        return OrientationParts(tuple(x.inverse() for x in reversed(self._stack)))

    def reduce(self):
        """Combine all successive constant projective-transformation parts in the chain
        If there are parts X(x), Y(y), Z(z) that functions of an unknown (runtime defined)
        parameter and any number of constant-valued parts Ci interspersed like
            C1 C2 C3 X(x) C3 C4 Y(y) C5 Z(z) C6 ... CN
        return the reduced list
            C123 X(x) C34 Y(y) C5 Z(z) C6N
        where, e.g., C123 = C1 C2 C3
        """
        reduced = [self._stack[0]]
        for top in self._stack[1:]:
            if reduced[-1].is_constant and top.is_constant:
                reduced[-1] = top * reduced[-1]
            else:
                reduced.append(top)
        return OrientationParts(tuple(reduced))

    def resolve(self):
        """Fully combine all parts of the chain, may raise an error if such a proceedure is disallowed"""
        resolved = self._stack[0]
        for work in self._stack[1:]:
            resolved = work * resolved
        return resolved


DependentOrientationType = TypeVar('DependentOrientationType', bound='DependentOrientation')


@dataclass
class DependentOrientation:
    """Un-evaluated lists of dependent operations that position and orient an object in a coordinate system"""
    _position: OrientationParts = field(default_factory=OrientationParts)
    _rotation: OrientationParts = field(default_factory=OrientationParts)
    _degrees: bool = True

    @property
    def degrees(self):
        return self._degrees

    @classmethod
    def from_dependent_orientations(cls,
                                    dep_at: DependentOrientationType,
                                    at: Vector,
                                    dep_angles: DependentOrientationType,
                                    angles: Angles,
                                    degrees=True, copy=True):
        zero = Expr.float(0), Expr.float(0), Expr.float(0)
        # if 'at' was defined RELATIVE to another component, the vector is *in that component's coordinate system*
        # include the full rotation chain to correctly position this component
        resolved_at_dep = None if dep_at is None else dep_at.combine()
        resolved_rot_dep = None if dep_angles is None else dep_angles._rotation
        pos = OrientationParts.from_dependent_chain(resolved_at_dep, at, zero, degrees=degrees, copy=copy)
        rot = OrientationParts.from_dependent_chain(resolved_rot_dep, zero, angles, degrees=degrees, copy=copy)
        return cls(pos, rot, degrees)

    @classmethod
    def from_dependent_orientation(cls,
                                   dep_on: DependentOrientationType,
                                   at: Vector,
                                   angles: Angles,
                                   degrees=True, copy=True):
        return cls.from_dependent_orientations(dep_on, at, dep_on, angles, degrees=degrees, copy=copy)

    def position(self, which=None):
        return self._position.resolve().position(which=which)

    def angles(self, which=None):
        return self._rotation.resolve().angles(which=which)

    def rotation(self, which=None):
        glob = self._rotation.resolve().seitz(which=which)
        return glob[0], glob[1], glob[2], glob[4], glob[5], glob[6], glob[8], glob[9], glob[10]

    def inverse(self):
        return DependentOrientation(self._position.inverse(), self._rotation.inverse())

    def reduce(self):
        return DependentOrientation(self._position.reduce(), self._rotation.reduce())

    def combine(self) -> OrientationParts:
        # The full positioning & orienting stack goes through all positioning operations
        # and only then goes through the orienting operations
        comb = self._position.copy().stack()
        comb += self._rotation.stack()
        return OrientationParts(comb)

    def __add__(self, other):
        if isinstance(other, DependentOrientation):
            return DependentOrientation(self._position + other._position, self._rotation + other._rotation)
        elif isinstance(other, (OrientationPart, OrientationParts)):
            return DependentOrientation(self._position + other, self._rotation + other)
        else:
            raise ValueError(f"__add__ undefined for DependentOrientation and {type(other)}")


def matrix_det_2(m: tuple[Expr, Expr, Expr, Expr]):
    """Determinant of a (flat, row ordered) 2x2 matrix"""
    return m[0] * m[3] - m[1] * m[2]


def matrix_det_3(m: Rotation):
    """Determinant of a (flat, row ordered) 3x3 matrix"""
    def d(i, j, k, l):
        return matrix_det_2((m[i], m[j], m[k], m[l]))
    return m[0] * d(4, 5, 7, 8) - m[1] * d(3, 5, 6, 8) + m[2] * d(3, 4, 6, 7)


def matrix_inverse_3(m: Rotation):
    """Inverse of a (flat, row ordered) 3x3 matrix"""
    det = abs(matrix_det_3(m))

    def d(i, j, k, n):
        return matrix_det_2((m[i], m[j], m[k], m[n])) / det

    return (d(4, 5, 7, 8), d(2, 1, 8, 7), d(1, 2, 4, 5),
            d(5, 3, 8, 6), d(0, 2, 6, 8), d(2, 0, 5, 3),
            d(3, 4, 6, 7), d(1, 0, 7, 6), d(0, 1, 3, 4))


def matrix_matrix_multiply_3(a: Rotation, b: Rotation):
    """Matrix multiplication of two (flat, row-ordered) matrices"""
    x00 = a[0] * b[0] + a[1] * b[3] + a[2] * b[6]
    x01 = a[0] * b[1] + a[1] * b[4] + a[2] * b[7]
    x02 = a[0] * b[2] + a[1] * b[5] + a[2] * b[8]
    x10 = a[3] * b[0] + a[4] * b[3] + a[5] * b[6]
    x11 = a[3] * b[1] + a[4] * b[4] + a[5] * b[7]
    x12 = a[3] * b[2] + a[4] * b[5] + a[5] * b[8]
    x20 = a[6] * b[0] + a[7] * b[3] + a[8] * b[6]
    x21 = a[6] * b[1] + a[7] * b[4] + a[8] * b[7]
    x22 = a[6] * b[2] + a[7] * b[5] + a[8] * b[8]
    return x00, x01, x02, x10, x11, x12, x20, x21, x22


def matrix_matrix_multiply_4(a: Affine, b: Affine):
    """Matrix multiplication of two (flat, row-ordered) 4x4 matrices"""
    x00 = a[0] * b[0] + a[1] * b[4] + a[2] * b[8] + a[3] * b[12]
    x01 = a[0] * b[1] + a[1] * b[5] + a[2] * b[9] + a[3] * b[13]
    x02 = a[0] * b[2] + a[1] * b[6] + a[2] * b[10] + a[3] * b[14]
    x03 = a[0] * b[3] + a[1] * b[7] + a[2] * b[11] + a[3] * b[15]
    x10 = a[4] * b[0] + a[5] * b[4] + a[6] * b[8] + a[7] * b[12]
    x11 = a[4] * b[1] + a[5] * b[5] + a[6] * b[9] + a[7] * b[13]
    x12 = a[4] * b[2] + a[5] * b[6] + a[6] * b[10] + a[7] * b[14]
    x13 = a[4] * b[3] + a[5] * b[7] + a[6] * b[11] + a[7] * b[15]
    x20 = a[8] * b[0] + a[9] * b[4] + a[10] * b[8] + a[11] * b[12]
    x21 = a[8] * b[1] + a[9] * b[5] + a[10] * b[9] + a[11] * b[13]
    x22 = a[8] * b[2] + a[9] * b[6] + a[10] * b[10] + a[11] * b[14]
    x23 = a[8] * b[3] + a[9] * b[7] + a[10] * b[11] + a[11] * b[15]
    x30 = a[12] * b[0] + a[13] * b[4] + a[14] * b[8] + a[15] * b[12]
    x31 = a[12] * b[1] + a[13] * b[5] + a[14] * b[9] + a[15] * b[13]
    x32 = a[12] * b[2] + a[13] * b[6] + a[14] * b[10] + a[15] * b[14]
    x33 = a[12] * b[3] + a[13] * b[7] + a[14] * b[11] + a[15] * b[15]
    return x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33


def matrix_vector_multiply_3(m: Rotation, v: Vector):
    """Multiplication of a (flat, row-ordered) 3x3 matrix with a column 3-vector"""
    x0 = m[0] * v[0] + m[1] * v[1] + m[2] * v[2]
    x1 = m[3] * v[0] + m[4] * v[1] + m[4] * v[2]
    x2 = m[6] * v[0] + m[7] * v[1] + m[8] * v[2]
    return x0, x1, x2


def matrix_vector_multiply_4(m: Affine, v: tuple[Expr, Expr, Expr, Expr]):
    """Multiplication of a (flat, row-ordered) 3x3 matrix with a column 3-vector"""
    x0 = m[0] * v[0] + m[1] * v[1] + m[2] * v[2] + m[3] * v[3]
    x1 = m[4] * v[0] + m[5] * v[1] + m[6] * v[2] + m[7] * v[3]
    x2 = m[8] * v[0] + m[9] * v[1] + m[10] * v[2] + m[11] * v[3]
    x3 = m[12] * v[0] + m[13] * v[1] + m[14] * v[2] + m[15] * v[3]
    return x0, x1, x2, x3


def vector_matrix_multiply_3(v: Vector, m: Rotation):
    """Multiplication of a row 3-vector with a (flat, row-ordered) 3x3 matrix"""
    x0 = v[0] * m[0] + v[1] * m[3] + v[2] * m[6]
    x1 = v[0] * m[1] + v[1] * m[4] + v[2] * m[7]
    x2 = v[0] * m[2] + v[1] * m[5] + v[2] * m[8]
    return x0, x1, x2


def seitz_inverse(a: Seitz) -> Seitz:
    """
    Special 4x3 (flat, row-ordered) matrix inverse.

    For the special case of a _projective transformation matrix_ and acts on augmented vectors,
    where the omitted last row would be [0, 0, 0, 1]. In this special case, we can express the matrix as
        |R T|
        |0 1|
    where R is a 3x3 (rotation) matrix and T a 3-vector translation. Then we need only find the inverse of R, R^-1,
    and note that T^-1 = - R^-1 T to find the inverse of the affine projective transformation matrix.

    If we were to further restrict the possible form of R to be orthogonal (or unitary, if we allow for complex-valued
    matrices), then the transpose of R is even easier to find as the (conjugate) transpose of R.
    """
    inv_r = matrix_inverse_3((a[0], a[1], a[2], a[4], a[5], a[6], a[8], a[9], a[10]))
    neg_inv_t = matrix_vector_multiply_3(inv_r, (a[3], a[7], a[11]))
    inv_a = (inv_r[0], inv_r[1], inv_r[2], -neg_inv_t[0],
             inv_r[3], inv_r[4], inv_r[5], -neg_inv_t[1],
             inv_r[6], inv_r[7], inv_r[8], -neg_inv_t[2],)
    return inv_a


def seitz_multiply(a: Seitz, b: Seitz) -> Seitz:
    """
    Multiplication in the special case of two _projective transformation matrices_ with omitted last row [0, 0, 0, 1].
    In this special case, we can express the matrix multiplication as
        |A t| |B s|  =  | AB  As+t |
        |0 1| |0 1|     |  0    1  |
    where A and B are 3x3 (rotation) matrices and t and s 3-vector translations.
    """
    def s2m(s: Seitz) -> Rotation:
        return s[0], s[1], s[2], s[4], s[5], s[6], s[8], s[9], s[10]

    def s2v(s: Seitz) -> Vector:
        return s[3], s[7], s[11]

    AB = matrix_matrix_multiply_3(s2m(a), s2m(b))
    As = matrix_vector_multiply_3(s2m(a), s2v(b))
    t = s2v(a)
    return AB[0], AB[1], AB[2], As[0]+t[0], AB[3], AB[4], AB[5], As[1]+t[1], AB[6], AB[7], AB[8], As[2]+t[2]
