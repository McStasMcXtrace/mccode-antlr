from dataclasses import dataclass, field
from ..common import Expr, unary_expr, binary_expr
from zenlog import log
from typing import TypeVar, NamedTuple, Union

VectorType = TypeVar('VectorType', bound='Vector')
MatrixType = TypeVar('MatrixType', bound='Matrix')
RotationType = TypeVar('RotationType', bound='Rotation')
SeitzType = TypeVar('SeitzType', bound='Seitz')


class Matrix(NamedTuple):
    """Any 3D matrix, not necessarily a rotation matrix"""
    xx: Expr = Expr.float(0)
    xy: Expr = Expr.float(0)
    xz: Expr = Expr.float(0)
    yx: Expr = Expr.float(0)
    yy: Expr = Expr.float(0)
    yz: Expr = Expr.float(0)
    zx: Expr = Expr.float(0)
    zy: Expr = Expr.float(0)
    zz: Expr = Expr.float(0)

    @classmethod
    def eye(cls):
        o = Expr.float(1)
        z = Expr.float(0)
        return cls(o, z, z, z, o, z, z, z, o)

    def __str__(self):
        x = [f'{x}' for x in (self.xx, self.xy, self.xz, self.yx, self.yy, self.yz, self.zx, self.zy, self.zz)]
        widths = [max(len(x[i+3*j]) for j in range(3)) for i in range(3)]
        line_fmt = [f'>{w+2:d}s' for w in widths]
        lines = '\n'.join(' '.join(f'{x[i+3*j]:{f:s}}' for i, f in zip(range(3), line_fmt)) for j in range(3))
        return lines

    def __repr__(self):
        return str(self)

    def __mul__(self, other: Union[MatrixType, VectorType, Expr]) -> Union[MatrixType, VectorType]:
        if isinstance(other, Matrix):
            return Matrix(
                self.xx * other.xx + self.xy * other.yx + self.xz * other.zx,
                self.xx * other.xy + self.xy * other.yy + self.xz * other.zy,
                self.xx * other.xz + self.xy * other.yz + self.xz * other.zz,
                self.yx * other.xx + self.yy * other.yx + self.yz * other.zx,
                self.yx * other.xy + self.yy * other.yy + self.yz * other.zy,
                self.yx * other.xz + self.yy * other.yz + self.yz * other.zz,
                self.zx * other.xx + self.zy * other.yx + self.zz * other.zx,
                self.zx * other.xy + self.zy * other.yy + self.zz * other.zy,
                self.zx * other.xz + self.zy * other.yz + self.zz * other.zz,
            )
        elif isinstance(other, Vector):
            return Vector(self.xx * other.x + self.xy * other.y + self.xz * other.z,
                          self.yx * other.x + self.yy * other.y + self.yz * other.z,
                          self.zx * other.x + self.zy * other.y + self.zz * other.z)
        else:
            return Matrix(self.xx * other, self.xy * other, self.xz * other,
                          self.yx * other, self.yy * other, self.yz * other,
                          self.zx * other, self.zy * other, self.zz * other)

    def __add__(self, other: MatrixType) -> MatrixType:
        if isinstance(other, Matrix):
            return Matrix(self.xx + other.xx, self.xy + other.xy, self.xz + other.xz,
                          self.yx + other.yx, self.yy + other.yy, self.yz + other.yz,
                          self.zx + other.zx, self.zy + other.zy, self.zz + other.zz)
        else:
            raise RuntimeError(f'No addition with {type(other)}')

    def __sub__(self, other: MatrixType) -> MatrixType:
        if isinstance(other, Matrix):
            return Matrix(self.xx - other.xx, self.xy - other.xy, self.xz - other.xz,
                          self.yx - other.yx, self.yy - other.yy, self.yz - other.yz,
                          self.zx - other.zx, self.zy - other.zy, self.zz - other.zz)
        else:
            raise RuntimeError(f'No subtraction with {type(other)}')


class Vector(NamedTuple):
    x: Expr = Expr.float(0)
    y: Expr = Expr.float(0)
    z: Expr = Expr.float(0)

    def __mul__(self, other: RotationType) -> VectorType:
        return Vector(self.x * other.xx + self.y * other.yx + self.z * other.zx,
                      self.x * other.xy + self.y * other.yy + self.z * other.zy,
                      self.x * other.xz + self.y * other.yz + self.z * other.zz)

    def cross_matrix(self) -> Matrix:
        z = Expr.float(0)
        return Matrix(z, -self.z, self.y, self.z, z, -self.x, -self.y, self.x, z)

    def length(self) -> Expr:
        from mccode.common.expression import unary_expr
        from math import sqrt
        if self.x.is_zero and self.y.is_zero:
            return abs(self.z)
        if self.y.is_zero and self.z.is_zero:
            return abs(self.x)
        if self.z.is_zero and self.x.is_zero:
            return abs(self.y)
        return unary_expr(sqrt, 'sqrt', self.x * self.x + self.y * self.y + self.z * self.z)

    def is_null(self) -> bool:
        return self.x.is_zero and self.y.is_zero and self.z.is_zero

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


class Angles(NamedTuple):
    x: Expr = Expr.float(0)
    y: Expr = Expr.float(0)
    z: Expr = Expr.float(0)

    def is_null(self) -> bool:
        return self.x.is_zero and self.y.is_zero and self.z.is_zero

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


class Rotation(NamedTuple):
    """A _valid_ 3-D rotation matrix flattened in row-order.

    Note:
        To be valid, the Rotation must have an inverse which is its (conjugate) transpose.
        This is equivalent to the matrix being Orthogonal (or Unitary, if complex-valued)
    """
    xx: Expr = Expr.float(1)
    xy: Expr = Expr.float(0)
    xz: Expr = Expr.float(0)
    yx: Expr = Expr.float(0)
    yy: Expr = Expr.float(1)
    yz: Expr = Expr.float(0)
    zx: Expr = Expr.float(0)
    zy: Expr = Expr.float(0)
    zz: Expr = Expr.float(1)

    def transpose(self) -> RotationType:
        return Rotation(self.xx, self.yx, self.zx, self.xy, self.yy, self.zy, self.xz, self.yz, self.zz)

    def inverse(self) -> RotationType:
        return self.transpose()

    def __mul__(self, other: Union[RotationType, Vector]) -> Union[RotationType, Vector]:
        if isinstance(other, Vector):
            return Vector(self.xx * other.x + self.xy * other.y + self.xz * other.z,
                          self.yx * other.x + self.yy * other.y + self.yz * other.z,
                          self.zx * other.x + self.zy * other.y + self.zz * other.z)
        elif isinstance(other, Rotation):
            return Rotation(
                self.xx * other.xx + self.xy * other.yx + self.xz * other.zx,
                self.xx * other.xy + self.xy * other.yy + self.xz * other.zy,
                self.xx * other.xz + self.xy * other.yz + self.xz * other.zz,
                self.yx * other.xx + self.yy * other.yx + self.yz * other.zx,
                self.yx * other.xy + self.yy * other.yy + self.yz * other.zy,
                self.yx * other.xz + self.yy * other.yz + self.yz * other.zz,
                self.zx * other.xx + self.zy * other.yx + self.zz * other.zx,
                self.zx * other.xy + self.zy * other.yy + self.zz * other.zy,
                self.zx * other.xz + self.zy * other.yz + self.zz * other.zz,
            )
        raise RuntimeError(f'No multiplication with {type(other)}')

    def __sub__(self, other: RotationType) -> Matrix:
        return Matrix(self.xx - other.xx, self.xy - other.xy, self.xz - other.xz,
                      self.yx - other.yx, self.yy - other.yy, self.yz - other.yz,
                      self.zx - other.zx, self.zy - other.zy, self.zz - other.zz)


class Seitz(NamedTuple):
    xx: Expr = Expr.float(1)
    xy: Expr = Expr.float(0)
    xz: Expr = Expr.float(0)
    xt: Expr = Expr.float(0)
    yx: Expr = Expr.float(0)
    yy: Expr = Expr.float(1)
    yz: Expr = Expr.float(0)
    yt: Expr = Expr.float(0)
    zx: Expr = Expr.float(0)
    zy: Expr = Expr.float(0)
    zz: Expr = Expr.float(1)
    zt: Expr = Expr.float(0)

    def rotation(self) -> Rotation:
        return Rotation(self.xx, self.xy, self.xz, self.yx, self.yy, self.yz, self.zx, self.zy, self.zz)

    def vector(self) -> Vector:
        return Vector(self.xt, self.yt, self.zt)

    def inverse(self) -> SeitzType:
        """
        Special 4x3 (flat, row-ordered) matrix inverse.

        For the special case of a _projective transformation matrix_ and acts on augmented vectors,
        where the omitted last row would be [0, 0, 0, 1]. In this special case, we can express the matrix as
            |R T|
            |0 1|
        where R is a 3x3 (rotation) matrix and T a 3-vector translation. Then we need only find the inverse of R, R^-1,
        and note that T^-1 = - R^-1 T to find the inverse of the affine projective transformation matrix.
        """
        inv_r = self.rotation().inverse()
        neg_inv_t = inv_r * self.vector()
        return Seitz(inv_r.xx, inv_r.xy, inv_r.xz, -neg_inv_t.x,
                     inv_r.yx, inv_r.yy, inv_r.yz, -neg_inv_t.y,
                     inv_r.zx, inv_r.zy, inv_r.zz, -neg_inv_t.z)

    def trace(self) -> Expr:
        """Abuse this to be the trace of the rotation part"""
        return self.xx + self.yy + self.zz

    def __mul__(self, other: SeitzType) -> SeitzType:
        """
        Multiplication in the special case of two _projective transformation matrices_ with omitted last row [0, 0, 0, 1].
        In this special case, we can express the matrix multiplication as
            |A t| |B s|  =  | AB  As+t |
            |0 1| |0 1|     |  0    1  |
        where A and B are 3x3 (rotation) matrices and t and s 3-vector translations.
        """
        so = self.rotation() * other.rotation()
        st = self.rotation() * other.vector()
        s = self.vector()
        return Seitz(so.xx, so.xy, so.xz, st.x + s.x,
                     so.yx, so.yy, so.yz, st.y + s.y,
                     so.zx, so.zy, so.zz, st.z + s.z)


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
    return Angles(rx, ry, rz)


OrientationPartType = TypeVar('OrientationPartType', bound='OrientationPart')


@dataclass
class OrientationPart:
    """The Seitz matrix part of any arbitrary projective affine transformation"""
    _axes: Seitz = field(default_factory=Seitz)
    _coordinates: Seitz = field(default_factory=Seitz)

    @property
    def is_translation(self):
        return any(not p.is_zero for p in (self._axes[3], self._axes[7], self._axes[11]))

    @property
    def is_rotation(self):
        return (self._axes.inverse() * self._axes).trace() == Expr.float(3.)

    @property
    def rotation_axis_angle(self) -> tuple[Vector, Expr, str]:
        from numpy.linalg import eig
        from numpy import array, argmin, sqrt, real, imag, conj, sum
        if not self.is_rotation or not self.is_constant:
            raise RuntimeError('Not possible to determine the rotation axis and angle of a variable general transform')
        # For the matrix A in cross(axis, v) = A v,
        # If flat is _axes, then R = 1 - A sin(angle) + A^2 (1-cos(angle))
        #  if _coordinates, then R = 1 + A sin(angle) * A^2 (1-cos(angle))
        # where the difference in sign is due to _coordinates rotating points and _axes rotating the axes instead.
        flat = self._coordinates.rotation()
        matrix = [[flat.xx.value, flat.xy.value, flat.xz.value],
                  [flat.yx.value, flat.yy.value, flat.yz.value],
                  [flat.zx.value, flat.zy.value, flat.zz.value]]
        dd, vv = eig(array(matrix))
        # The eigenvalues, dd, are (1+0j, a+bj, a-bj) of which we want 1+0j.
        axis = vv[:, argmin(sqrt(real(conj(dd-1) * (dd-1))))]
        if sum(imag(axis)) != 0:
            log.warn(f'Imaginary rotation axis {real(axis)} + j {imag(axis)}')
        axis = real(axis)
        cos_angle = (matrix[0][0] + matrix[1][1] + matrix[2][2] - 1) / 2
        if abs(cos_angle) > 1:
            log.warn(f'Invalid cos(angle) {cos_angle} for {self}')
        angle = Expr.float(acos_degree(cos_angle))
        axis = Vector(Expr.float(axis[0]), Expr.float(axis[1]), Expr.float(axis[2]))

        # Check that the rotation matrix signs all match:
        a = axis.cross_matrix()
        r = Matrix.eye() + a * sin_value(angle, True) + (a * a) * (Expr.float(1) - cos_value(angle, True))
        # and flip the sign of angle if not:
        return axis, -angle if any(flat[index] * r[index] < Expr.float(0) for index in range(9)) else angle, 'degrees'

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
        return self.axes if which is None or 'axes' in which else self.coordinates

    def position(self, which=None) -> Vector:
        return self.seitz(which).vector()

    def angles(self, which=None, degrees=True) -> Angles:
        return axes_euler_angles(self.seitz('axes').rotation(), degrees)

    @property
    def all_values(self) -> bool:
        return all(x.has_value for x in self._axes) and all(x.has_value for x in self._coordinates)

    @property
    def is_constant(self) -> bool:
        return all(x.is_constant for x in self._axes) and all(x.is_constant for x in self._coordinates)

    def inverse(self: OrientationPartType) -> OrientationPartType:
        return OrientationPart(self._axes.inverse(), self._coordinates.inverse())

    def __mul__(self: OrientationPartType, other: OrientationPartType) -> OrientationPartType:
        if not isinstance(other, OrientationPart):
            raise RuntimeError('Multiplication only defined for two orientation parts')
        if not self.is_constant or not other.is_constant:
            raise ValueError('Multiplication only defined for two *constant* orientation parts')
        return OrientationPart(self.axes * other.axes, self.coordinates * other.coordinates)


@dataclass
class TranslationPart(OrientationPart):
    """A specialization to the translation-only part of a projective affine transformation"""
    v: Vector = field(default_factory=Vector)

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
        self._axes = Seitz(o, z, z, self.v[0], z, o, z, self.v[1], z, z, o, self.v[2])
        self._coords = self._axes

    def inverse(self):
        return TranslationPart(v=Vector(-self.v[0], -self.v[1], -self.v[2]))

    def position(self, which=None) -> Vector:
        return self.v

    def angles(self, which=None, degrees=True) -> Angles:
        z = Expr.float(0)
        return Angles(z, z, z)


@dataclass
class RotationPart(OrientationPart):
    """A specialization to the rotation-only part of a projective affine transformation"""
    v: Expr = Expr.float(0)
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
        return Vector(Expr.float(0), Expr.float(0),  Expr.float(0))

    @property
    def rotation_axis_angle(self) -> tuple[Vector, Expr, str]:
        return self.rotation_axis, self.v, 'degrees' if self.degrees else 'radian'

    def _cos_sin_one_zero(self):
        r = self.v if self.degrees else degree_to_radian(self.v)
        return cos_value(r), sin_value(r), Expr.float(1), Expr.float(0)

    def position(self, which=None) -> Vector:
        z = Expr.float(0)
        return Vector(z, z, z)


class RotationX(RotationPart):
    """A specialization to the rotation-around-X part of a projective affine transformation"""
    def __post_init__(self):
        c, s, o, z = self._cos_sin_one_zero()
        self._axes = Seitz(o, z, z, z, z, c, -s, z, z, s, c, z)
        self._coordinates = Seitz(o, z, z, z, z, c, s, z, z, -s, c, z)

    def inverse(self):
        return RotationX(v=-self.v, degrees=self.degrees)

    def angles(self, which=None, degrees=True) -> Angles:
        z = Expr.float(0)
        return Angles(self.v, z, z)

    def __str__(self):
        return f'(0, 0, 0) [{self.v}, 0, 0]'

    @property
    def rotation_axis(self) -> Vector:
        return Vector(Expr.float(1), Expr.float(0), Expr.float(0))


class RotationY(RotationPart):
    """A specialization to the rotation-around-Y part of a projective affine transformation"""
    def __post_init__(self):
        c, s, o, z = self._cos_sin_one_zero()
        self._axes = Seitz(c, z, s, z, z, o, z, z, -s, z, c, z)
        self._coordinates = Seitz(c, z, -s, z, z, o, z, z, s, z, c, z)

    def inverse(self):
        return RotationY(v=-self.v, degrees=self.degrees)

    def angles(self, which=None, degrees=True) -> Angles:
        z = Expr.float(0)
        return Angles(z, self.v, z)

    def __str__(self):
        return f'(0, 0, 0) [0, {self.v}, 0]'

    @property
    def rotation_axis(self) -> Vector:
        return Vector(Expr.float(0), Expr.float(1), Expr.float(0))


class RotationZ(RotationPart):
    """A specialization to the rotation-around-Z part of a projective affine transformation"""
    def __post_init__(self):
        c, s, o, z = self._cos_sin_one_zero()
        self._axes = Seitz(c, -s, z, z, s, c, z, z, z, z, o, z)
        self._coordinates = Seitz(c, s, z, z, -s, c, z, z, z, z, o, z)

    def inverse(self):
        return RotationZ(v=-self.v, degrees=self.degrees)

    def angles(self, which=None, degrees=True) -> Angles:
        z = Expr.float(0)
        return Angles(z, z, self.v)

    def __str__(self):
        return f'(0, 0, 0) [0, 0, {self.v}]'

    @property
    def rotation_axis(self) -> Vector:
        return Vector(Expr.float(0), Expr.float(0), Expr.float(1))


OrientationPartsType = TypeVar('OrientationPartsType', bound='OrientationParts')


@dataclass
class OrientationParts:
    """A list of unresolved or partially resolved successive projective affine transformation(s)"""
    _stack: tuple[OrientationPart] = field(default_factory=tuple)

    def __str__(self):
        return f'OrientationParts<{len(self._stack)}>'

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
        if not len(self._stack):
            return OrientationParts()

        reduced = [self._stack[0]]
        for top in self._stack[1:]:
            if reduced[-1].is_constant and top.is_constant:
                reduced[-1] = top * reduced[-1]
            else:
                reduced.append(top)
        return OrientationParts(tuple(reduced))

    def resolve(self):
        """Fully combine all parts of the chain, may raise an error if such a proceedure is disallowed"""
        if not len(self._stack):
            return OrientationPart()

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

    def __str__(self):
        return f'DependentOrientation<{self._position}, {self._rotation}>'

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
        resolved_at_dep = None if dep_at is None else dep_at.combine().reduce()
        resolved_rot_dep = None if dep_angles is None else dep_angles._rotation.reduce()
        pos = OrientationParts.from_dependent_chain(resolved_at_dep, at, Angles(*zero), degrees=degrees, copy=copy)
        rot = OrientationParts.from_dependent_chain(resolved_rot_dep, Vector(*zero), angles, degrees=degrees, copy=copy)
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



