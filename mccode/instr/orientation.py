from dataclasses import dataclass, field
from ..common import Expr, unary_expr, binary_expr
from enum import Enum

def _value_float_tuple(n, v=0.):
    return tuple(Expr.float(v) for _ in range(n))


def cos_value(v: Expr):
    from math import cos
    return unary_expr(cos, 'cos', v)


def sin_value(v: Expr):
    from math import sin
    return unary_expr(sin, 'sin', v)


def atan2_value(va: Expr, vb: Expr):
    from math import atan2
    return binary_expr(atan2, 'atan2', va, vb)


def degree_to_radian(v: Expr):
    from math import pi
    if v.is_id:
        return v * (Expr.float('PI') / Expr.float(180))
    return v * Expr.float(pi / 180)


@dataclass
class Orientation:
    class Type(Enum):
        axes = 1
        coordinates = 2

    position: tuple[Expr, Expr, Expr] = field(default_factory=lambda: _value_float_tuple(3))
    _axes: tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr] \
        = field(default_factory=lambda: _value_float_tuple(9))
    _coordinates: tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr] \
        = field(default_factory=lambda: _value_float_tuple(9))

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

    @property
    def angles(self):
        from zenlog import log
        def abs_ch(a, b):
            # v = abs(a) > abs(b)
            # return v.value == 1 if isinstance(v, Value) else v
            return abs(a) > abs(b)

        # Inspired by eniius get_euler_angles
        x = atan2_value(-self._axes[7], self._axes[8])  # tan(x) = sin(x) / cos(x) = -(-sx*cy)/(cx*cy)
        z = atan2_value(-self._axes[3], self._axes[0])  # tan(z) = sin(z) / cos(z) = -(-cy*sz)/(cy*cz)
        # Ensure we know the sign of cos(y), not just its magnitude:
        cos_x, cos_z = [cos_value(a) for a in (x, z)]
        # if not x.is_a(Value.Type.str) and not z.is_a(Value.Type.str):
        # elif not x.is_a(Value.Type.str):
        # elif not z.is_a(Value.Type.str):
        if not x.is_id and not z.is_id:
            if abs_ch(cos_x, cos_z):
                cos_a, sin_a, cos_y_cos_a, sin_y_sin_a = cos_x, sin_value(x), self._axes[8], -self._axes[7]
            else:
                cos_a, sin_a, cos_y_cos_a, sin_y_sin_a = cos_z, sin_value(z), self._axes[0], -self._axes[3]
        elif not x.is_id:
            cos_a, sin_a, cos_y_cos_a, sin_y_sin_a = cos_x, sin_value(x), self._axes[8], -self._axes[7]
        elif not z.is_id:
            cos_a, sin_a, cos_y_cos_a, sin_y_sin_a = cos_z, sin_value(z), self._axes[0], -self._axes[3]
        else:
            log.debug(self)
            raise RuntimeError("How do we prevent division by zero when both x and z are strings?")
        y = atan2_value(self._axes[6], cos_y_cos_a / cos_a if abs_ch(cos_a, sin_a) else sin_y_sin_a / sin_a)
        return x, y, z

    @staticmethod
    def from_at_rotated(at, rotated):
        cx, cy, cz = [cos_value(degree_to_radian(r)) for r in rotated]
        sx, sy, sz = [sin_value(degree_to_radian(r)) for r in rotated]
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
        # The 3 vector part:
        v = at[0], at[1], at[2]
        return Orientation(v, axes, coordinates)


def from_at_rotated(at: tuple[Expr, Expr, Expr], rotated: tuple[Expr, Expr, Expr]):
    return Orientation.from_at_rotated(at, rotated)


def matrix_det_2(m: tuple[Expr, Expr, Expr, Expr]):
    """Determinant of a (flat, row ordered) 2x2 matrix"""
    return m[0] * m[3] - m[1] * m[2]


def matrix_det_3(m: tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr]):
    """Determinant of a (flat, row ordered) 3x3 matrix"""
    def d(i, j, k, l):
        return matrix_det_2((m[i], m[j], m[k], m[l]))
    return m[0] * d(4, 5, 7, 8) - m[1] * d(3, 5, 6, 8) + m[2] * d(3, 4, 6, 7)


def matrix_inverse_3(m: tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr]):
    """Inverse of a (flat, row ordered) 3x3 matrix"""
    det = abs(matrix_det_3(m))

    def d(i, j, k, n):
        return matrix_det_2((m[i], m[j], m[k], m[n])) / det

    return (d(4, 5, 7, 8), d(2, 1, 8, 7), d(1, 2, 4, 5),
            d(5, 3, 8, 6), d(0, 2, 6, 8), d(2, 0, 5, 3),
            d(3, 4, 6, 7), d(1, 0, 7, 6), d(0, 1, 3, 4))


def matrix_matrix_multiply_3(a: tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr],
                             b: tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr]):
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


def matrix_matrix_multiply_4(a: tuple[Expr, ...], b: tuple[Expr, ...]):
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


def matrix_vector_multiply_3(m: tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr],
                             v: tuple[Expr, Expr, Expr]):
    """Multiplication of a (flat, row-ordered) 3x3 matrix with a column 3-vector"""
    x0 = m[0] * v[0] + m[1] * v[1] + m[2] * v[2]
    x1 = m[3] * v[0] + m[4] * v[1] + m[4] * v[2]
    x2 = m[6] * v[0] + m[7] * v[1] + m[8] * v[2]
    return x0, x1, x2


def vector_matrix_multiply_3(v: tuple[Expr, Expr, Expr],
                             m: tuple[Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr, Expr]):
    """Multiplication of a row 3-vector with a (flat, row-ordered) 3x3 matrix"""
    x0 = v[0] * m[0] + v[1] * m[3] + v[2] * m[6]
    x1 = v[0] * m[1] + v[1] * m[4] + v[2] * m[7]
    x2 = v[0] * m[2] + v[1] * m[5] + v[2] * m[8]
    return x0, x1, x2


def affine_inverse(a: tuple[Expr, ...]):
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
