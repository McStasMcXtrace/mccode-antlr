from dataclasses import dataclass, field
from ..common import Expr, unary_expr, binary_expr
from enum import Enum
from zenlog import log
from typing import Self

Vector = tuple[Expr, Expr, Expr]
Angles = tuple[Expr, Expr, Expr]
Rotation = tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr]
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


def degree_to_radian(v: Expr):
    from math import pi
    if v.is_id:
        if v == Expr.float('PI'):
            log.error(f'Convert {v} to radian')
            raise RuntimeError('What?!')
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


@dataclass
class Orientation:
    class Type(Enum):
        axes = 1
        coordinates = 2

    degrees: bool
    position: Vector = field(default_factory=lambda: _value_float_tuple(3))
    _angles: Angles = field(default_factory=lambda: _value_float_tuple(3))
    _axes: Rotation = field(default_factory=lambda: _value_float_tuple(9))
    _coordinates: Rotation = field(default_factory=lambda: _value_float_tuple(9))

    @staticmethod
    def from_at_rotated(at: Vector, rotated: Angles, degrees=True):
        axes, coordinates = _rotation_angles_to_axes_coordinates(rotated, degrees=degrees)
        # The 3 vector part:
        v = at[0], at[1], at[2]
        return Orientation(degrees, v, rotated, axes, coordinates)

    @property
    def angles(self):
        return self._angles

    @angles.setter
    def angles(self, rotated: Angles, degrees=True):
        self._axes, self._coordinates = _rotation_angles_to_axes_coordinates(rotated, degrees=degrees)
        self._angles = rotated


    def __str__(self):
        y = [self._axes[0], self._axes[1], self._axes[2], self.position[0],
             self._axes[3], self._axes[4], self._axes[5], self.position[1],
             self._axes[6], self._axes[7], self._axes[8], self.position[2]]
        x = [f'{x}' for x in y]
        widths = [max(len(x[i+4*j]) for j in range(3)) for i in range(4)]
        line_fmt = [f'>{w+2:d}s' for w in widths]
        lines = '\n'.join(' '.join(f'{x[i+4*j]:{f:s}}' for i, f in zip(range(4), line_fmt)) for j in range(3))
        return lines

    @property
    def affine_matrix(self, which=None):
        t = self._axes if which is None or not which == Orientation.Type.coordinates else self._coordinates
        m = ((t[0], t[1], t[2], self.position[0]),
             (t[3], t[4], t[5], self.position[1]),
             (t[6], t[7], t[8], self.position[2]),
             (Expr.float(0), Expr.float(0), Expr.float(0), Expr.float(1)))
        return m

    def affine(self, which):
        t = self._axes if 'axes' in which else self._coordinates
        m = (t[0], t[1], t[2], self.position[0],
             t[3], t[4], t[5], self.position[1],
             t[6], t[7], t[8], self.position[2],
             Expr.float(0), Expr.float(0), Expr.float(0), Expr.float(1))
        return m

    def __mul__(self, other):
        if not isinstance(other, Orientation):
            raise RuntimeError('Orientation multiplication only defined between class objects')
        if self.degrees != other.degrees:
            raise RuntimeError('Inconsistent degree use between orientations')
        # position and angles are *probably* wrong, how should we indicate that?
        position = tuple(s + o for s, o in zip(self.position, other.position))
        angles = tuple(s + o for s, o in zip(self.angles, other.angles))
        axes = matrix_matrix_multiply_4(self.affine('axes'), other.affine('axes'))
        coords = matrix_matrix_multiply_4(self.affine('coords'), other.affine('coords'))
        return Orientation(self.degrees, position, angles, axes, coords)

    # @property
    # def angles(self):
    #     from math import pi
    #     from zenlog import log
    #     from itertools import product
    #
    #     def abs_ch(a, b):
    #         if a.is_zero and not b.is_zero:
    #             return False
    #         if not a.is_zero and b.is_zero:
    #             return True
    #         # v = abs(a) > abs(b)
    #         # return v.value == 1 if isinstance(v, Value) else v
    #         return abs(a) > abs(b)
    #
    #     def xyz(anx, anz):
    #         cos_x, cos_z = [cos_value(ang) for ang in (anx, anz)]
    #         log.info(f'{cos_x = }, {cos_z = }')
    #         if not anx.is_id and not anz.is_id:
    #             if abs_ch(cos_x, cos_z):
    #                 cos_a, sin_a, cos_y_cos_a, cos_y_sin_a = cos_x, sin_value(anx), self._axes[8], -self._axes[7]
    #             else:
    #                 cos_a, sin_a, cos_y_cos_a, cos_y_sin_a = cos_z, sin_value(anz), self._axes[0], -self._axes[3]
    #         elif not anx.is_id:
    #             cos_a, sin_a, cos_y_cos_a, cos_y_sin_a = cos_x, sin_value(anx), self._axes[8], -self._axes[7]
    #         elif not anz.is_id:
    #             cos_a, sin_a, cos_y_cos_a, cos_y_sin_a = cos_z, sin_value(anz), self._axes[0], -self._axes[3]
    #         else:
    #             return []
    #         log.info(f'cos_y * cos_a = {cos_y_cos_a} {cos_y_cos_a.is_zero}, cos_y * sin_a = {cos_y_sin_a} {cos_y_sin_a.is_zero}')
    #         if cos_a.is_zero:
    #             cos_y = cos_y_sin_a / sin_a
    #         elif sin_a.is_zero:
    #             cos_y = cos_y_cos_a / cos_a
    #         else:
    #             cos_y = cos_y_cos_a / cos_a if abs_ch(cos_y_cos_a, cos_y_sin_a) else cos_y_sin_a / sin_a
    #         log.error(f'Find the arctan of y={self._axes[6]} and x={cos_y}')
    #         y = atan2_value(self._axes[6], cos_y, degrees=self.degrees)
    #         return [(anx, why, anz) for why in y]
    #
    #     log.info(self)
    #
    #     # Inspired by eniius get_euler_angles
    #     # tan(x) = sin(x) / cos(x) = -(-sx*cy)/(cx*cy)
    #     x = atan2_value(-self._axes[7], self._axes[8], degrees=self.degrees)
    #     log.info(f'x could be {x}')
    #     # tan(z) = sin(z) / cos(z) = -(-cy*sz)/(cy*cz)
    #     z = atan2_value(-self._axes[3], self._axes[0], degrees=self.degrees)
    #     log.info(f'z could be {z}')
    #     # Ensure we know the sign of cos(y), not just its magnitude:
    #     xyz_lists = list(xyz(x, y) for x, y in product(x, z))
    #     xyzs = [xyz for xyz_list in xyz_lists for xyz in xyz_list]
    #     if len(xyzs) == 0:
    #         raise RuntimeError('Why are there *no* solutions for the y angle?')
    #     if len(xyzs) > 1:
    #         log.critical(f'Check that all of {xyzs} are the same solution!')
    #     x, y, z = xyzs[0]
    #     log.critical(f'y is {y}')
    #     return x, y, z


def _add_to_chain(chain: tuple[Orientation], position: Vector, angles: Angles, degrees=True, copy=True):
    orientation = Orientation.from_at_rotated(position, angles, degrees=degrees)
    if copy:
        from copy import deepcopy
        chain = tuple([deepcopy(x) for x in chain])
    chain += (orientation, )
    return chain


def _resolve_chain(chain: tuple[Orientation], origin: Orientation = None):
    degree_set = set(x.degrees for x in chain)
    if len(degree_set) < 2:
        degrees = list(degree_set)[0] if len(degree_set) else True
    else:
        raise RuntimeError("Inconsistent degree use in orientation chain")

    if origin is None:
        zero = Expr.float(0), Expr.float(0), Expr.float(0)
        origin = Orientation.from_at_rotated(zero, zero, degrees=degrees)

    resolved = origin
    for orientation in chain:
        resolved *= orientation
    return resolved


@dataclass
class DependentOrientation:
    orientation: Orientation
    dep_position: tuple[Orientation] = field(default_factory=tuple)
    dep_rotation: tuple[Orientation] = field(default_factory=tuple)

    @property
    def degrees(self):
        return self.orientation.degrees

    def _resolved_position_chain(self, copy=True):
        zero = Expr.float(0), Expr.float(0), Expr.float(0)
        return _add_to_chain(self.dep_position, self.orientation.position, zero, degrees=self.degrees, copy=copy)

    def _resolved_rotation_chain(self, copy=True):
        zero = Expr.float(0), Expr.float(0), Expr.float(0)
        return _add_to_chain(self.dep_rotation, zero, self.orientation.angles, degrees=self.degrees, copy=copy)

    @classmethod
    def from_dependent_orientation(cls, dep_on: Self, at: Vector, angles: Angles, degrees=True, copy=True):
        return cls(Orientation.from_at_rotated(at, angles, degrees=degrees),
                   () if dep_on is None else dep_on._resolved_position_chain(copy=copy),
                   () if dep_on is None else dep_on._resolved_rotation_chain(copy=copy))

    @classmethod
    def from_dependent_orientations(cls, dep_at: Self, at: Vector, dep_angles: Self, angles: Angles, degrees=True, copy=True):
        dep_pos = () if dep_at is None else dep_at._resolved_position_chain(copy=copy)
        dep_ang = () if dep_angles is None else dep_angles._resolved_rotation_chain(copy=copy)
        return cls(Orientation.from_at_rotated(at, angles, degrees=degrees), dep_pos, dep_ang)

    def position(self, axes=None):
        ra = _resolve_chain(self.dep_position).affine('axes' if axes is None else axes)
        pos = self.orientation.position[0], self.orientation.position[1], self.orientation.position[2], Expr.float(1)
        pos = matrix_vector_multiply_4(ra, pos)
        return pos[0], pos[1], pos[2]

    def rotation(self, axes=None):
        ra = _resolve_chain(self.dep_rotation).affine('axes' if axes is None else axes)
        afn = self.orientation.affine('axes' if axes is None else axes)
        glob = matrix_matrix_multiply_4(afn, ra)
        return glob[0], glob[1], glob[2], glob[4], glob[5], glob[6], glob[8], glob[9], glob[10]


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


def affine_inverse(a: Affine):
    """Special 4x4 (flat, row-ordered) matrix inverse.

    The affine matrix *must* be a _projective transformation matrix_ and acts on augmented vectors,
    the last row must be (but is not verified to be) [0, 0, 0, 1].
    In this special case, we can express the matrix as
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
             inv_r[6], inv_r[7], inv_r[8], -neg_inv_t[2],
             Expr.float(0), Expr.float(0), Expr.float(0), Expr.float(1))
    return inv_a
