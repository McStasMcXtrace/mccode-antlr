from dataclasses import dataclass, field
from ..common import Expr, unary_expr, binary_expr
from enum import Enum
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


OrientationType = TypeVar('OrientationType', bound='Orientation')


@dataclass
class Orientation:

    degrees: bool
    _axes: Seitz = field(default_factory=lambda: _value_float_tuple(12))
    _coordinates: Seitz = field(default_factory=lambda: _value_float_tuple(12))

    @property
    def all_values(self):
        for x in self._axes:
            if not x.has_value:
                return False
        for x in self._coordinates:
            if not x.has_value:
                return False
        return True

    @staticmethod
    def from_at_rotated(at: Vector, rotated: Angles, degrees=True):
        a, c = _rotation_angles_to_axes_coordinates(rotated, degrees=degrees)
        axes = a[0], a[1], a[2], at[0], a[3], a[4], a[5], at[1], a[6], a[7], a[8], at[2]
        coordinates = c[0], c[1], c[2], at[0], c[3], c[4], c[5], at[1], c[6], c[7], c[8], at[2]
        return Orientation(degrees, axes, coordinates)

    @staticmethod
    def from_affine(degrees: bool, axes: Affine, coordinates: Affine):
        def a2s(a: Affine) -> Seitz:
            return a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11]

        return Orientation(degrees, a2s(axes), a2s(coordinates))

    def seitz(self, which=None) -> Seitz:
        return self._axes if 'axes' in which else self._coordinates

    def position(self, which=None) -> Vector:
        t = self.seitz(which)
        return t[3], t[7], t[11]

    def angles(self, which=None) -> Angles:
        t = self.seitz('axes')
        return axes_euler_angles((t[0], t[1], t[2], t[4], t[5], t[6], t[8], t[9], t[10]), self.degrees)

    # @angles.setter
    # def angles(self, rotated: Angles, degrees=True):
    #     self._axes, self._coordinates = _rotation_angles_to_axes_coordinates(rotated, degrees=degrees)

    def __str__(self):
        x = [f'{x}' for x in self._axes]
        widths = [max(len(x[i+4*j]) for j in range(3)) for i in range(4)]
        line_fmt = [f'>{w+2:d}s' for w in widths]
        lines = '\n'.join(' '.join(f'{x[i+4*j]:{f:s}}' for i, f in zip(range(4), line_fmt)) for j in range(3))
        return lines

    def affine(self, which) -> Affine:
        t = self._axes if 'axes' in which else self._coordinates
        m = (t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11],
             Expr.float(0), Expr.float(0), Expr.float(0), Expr.float(1))
        return m

    def __mul__(self, other: OrientationType) -> OrientationType:
        if not isinstance(other, Orientation):
            raise RuntimeError('Orientation multiplication only defined between class objects')
        if self.degrees != other.degrees:
            raise RuntimeError('Inconsistent degree use between orientations')
        axes = seitz_multiply(self.seitz('axes'), other.seitz('axes'))
        coords = seitz_multiply(self.seitz('coords'), other.seitz('coords'))
        return Orientation(self.degrees, axes, coords)

    def inverse(self):
        return Orientation(self.degrees, seitz_inverse(self.seitz('axes')), seitz_inverse(self.seitz('coords')))


OrientationChainType = TypeVar('OrientationChainType', bound='OrientationChain')
DependentOrientationType = TypeVar('DependentOrientationType', bound='DependentOrientation')


@dataclass
class OrientationChain:
    _chain: tuple[Orientation] = field(default_factory=tuple)

    @property
    def degrees(self) -> bool:
        deg = set(x.degrees for x in self._chain)
        if len(deg) < 2:
            deg = list(deg)[0] if len(deg) else True
        else:
            raise RuntimeError("Inconsistent degree use in OrientationChain")
        return deg

    def _copy(self, deep: bool = True) -> tuple[Orientation]:
        if deep:
            from copy import deepcopy
            return tuple([deepcopy(x) for x in self._chain])
        return tuple(x for x in self._chain)

    def resolve(self, origin: Orientation = None) -> Orientation:
        deg = self.degrees
        if origin is None:
            zero = Expr.float(0), Expr.float(0), Expr.float(0)
            origin = Orientation.from_at_rotated(zero, zero, degrees=deg)

        resolved = origin
        for orientation in self._chain:
            resolved *= orientation
        return resolved

    @classmethod
    def from_dependent_chain(cls, dep: OrientationChainType, final: Orientation, copy=True):
        chain = () if dep is None else dep._copy(deep=copy)
        chain += (final,)
        return cls(chain)

    @classmethod
    def from_dependent_at_rotate(cls, dep: OrientationChainType, position: Vector, angles: Angles, degrees=True, copy=True):
        return cls.from_dependent_chain(dep, Orientation.from_at_rotated(position, angles, degrees=degrees), copy=copy)

    def inverse(self):
        return OrientationChain(tuple(x.inverse() for x in reversed(self._chain)))

    def reduce(self):
        """Combine successive chained orientations which are fully determined -- i.e., have no unknown values"""
        reduced = []
        group = self._chain[0]
        for ort in self._chain[1:]:
            if group.all_values:
                # successive chained orientations multiply from the left
                group = ort * group
            else:
                reduced.append(group)
                group = ort

        reduced.append(group)

        return OrientationChain(tuple(reduced))

    def __add__(self, other):
        chain = self._copy()
        if isinstance(other, OrientationChain):
            chain += other._chain
        elif isinstance(other, Orientation):
            chain += (other,)
        return OrientationChain(chain)


@dataclass
class DependentOrientation:
    _position: OrientationChain = field(default_factory=OrientationChain)
    _rotation: OrientationChain = field(default_factory=OrientationChain)

    @property
    def degrees(self):
        return self._rotation.degrees

    @classmethod
    def from_dependent_orientations(cls,
                                    dep_at: DependentOrientationType,
                                    at: Vector,
                                    dep_angles: DependentOrientationType,
                                    angles: Angles,
                                    degrees=True, copy=True):
        zero = Expr.float(0), Expr.float(0), Expr.float(0)
        pos = OrientationChain.from_dependent_at_rotate(dep_at, at, zero, degrees=degrees, copy=copy)
        rot = OrientationChain.from_dependent_at_rotate(dep_rot, zero, angles, degrees=degrees, copy=copy)
        return cls(pos, rot)

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

    def __add__(self, other):
        if isinstance(other, DependentOrientation):
            return DependentOrientation(self._position + other._position, self._rotation + other._rotation)
        elif isinstance(other, Orientation):
            return DependentOrientation(self._position + other, self._rotation + other)
        else:
            raise ValueError(f"__add__ undefined for DependentOrientation and {type(other)}")


def from_at_rotated(at: Vector, rotated: Angles):
    return Orientation.from_at_rotated(at, rotated)


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
