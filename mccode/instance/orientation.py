from dataclasses import dataclass, field
from ..common import Value


def _value_float_tuple(n, v=0.):
    return tuple(Value.float(v) for _ in range(n))


def cos_value(v: Value):
    from math import cos
    return v.apply_elementwise_function(cos, 'cos')


def sin_value(v: Value):
    from math import sin
    return v.apply_elementwise_function(sin, 'sin')


def atan2_value(va: Value, vb: Value):
    from math import atan2
    return Value.apply_elementwise_binary_function(atan2, 'atan2', va, vb)


def degree_to_radian(v: Value):
    from math import pi
    if v.is_a(Value.Type.str):
        return v * Value.str('PI/180')
    return v * (pi / 180)


@dataclass
class Orientation:
    position: tuple[Value, Value, Value] = field(default_factory=lambda: _value_float_tuple(3))
    rotation: tuple[Value, Value, Value, Value, Value, Value, Value, Value, Value] \
        = field(default_factory=lambda: _value_float_tuple(9))

    @property
    def affine_matrix(self):
        m = ((self.rotation[0], self.rotation[1], self.rotation[2], self.position[0]),
             (self.rotation[3], self.rotation[4], self.rotation[5], self.position[1]),
             (self.rotation[6], self.rotation[7], self.rotation[8], self.position[2]),
             (Value.float(0), Value.float(0), Value.float(0), Value.float(1)))
        return m

    @property
    def angles(self):
        def abs_ch(a, b):
            v = abs(a) > abs(b)
            return v.value == 1 if isinstance(v, Value) else v

        # Inspired by eniius get_euler_angles
        x = atan2_value(-self.rotation[7], self.rotation[8])  # tan(x) = sin(x) / cos(x) = -(-sx*cy)/(cx*cy)
        z = atan2_value(-self.rotation[3], self.rotation[0])  # tan(z) = sin(z) / cos(z) = -(-cy*sz)/(cy*cz)
        # Ensure we know the sign of cos(y), not just its magnitude:
        cos_x, cos_z = [cos_value(a) for a in (x, z)]
        if not x.is_a(Value.Type.str) and not z.is_a(Value.Type.str):
            if abs_ch(cos_x, cos_z):
                cos_a, sin_a, cos_y_cos_a, sin_y_sin_a = cos_x, sin_value(x), self.rotation[8], -self.rotation[7]
            else:
                cos_a, sin_a, cos_y_cos_a, sin_y_sin_a = cos_z, sin_value(z), self.rotation[0], -self.rotation[3]
        elif not x.is_a(Value.Type.str):
            cos_a, sin_a, cos_y_cos_a, sin_y_sin_a = cos_x, sin_value(x), self.rotation[8], -self.rotation[7]
        elif not z.is_a(Value.Type.str):
            cos_a, sin_a, cos_y_cos_a, sin_y_sin_a = cos_z, sin_value(z), self.rotation[0], -self.rotation[3]
        else:
            raise RuntimeError("How do we prevent division by zero when both x and z are strings?")
        y = atan2_value(self.rotation[6], cos_y_cos_a / cos_a if abs_ch(cos_a, sin_a) else sin_y_sin_a / sin_a)
        return x, y, z

    @staticmethod
    def from_at_rotated(at, rotated):
        cx, cy, cz = [cos_value(degree_to_radian(r)) for r in rotated]
        sx, sy, sz = [sin_value(degree_to_radian(r)) for r in rotated]
        # The 3x3 rotation matrix part:
        m = (cy * cz, sx * sy * cz + cx * sz, sx * sz - cx * sy * cz,
             -cy * sz, cx * cz - sx * sy * sz, sx * cz + cx * sy * sz,
             sy, -sx * cy, cx * cy)
        # The 3 vector part:
        v = at[0], at[1], at[2]
        return Orientation(v, m)


def from_at_rotated(at: tuple[Value, Value, Value], rotated: tuple[Value, Value, Value]):
    return Orientation.from_at_rotated(at, rotated)


def from_at_relative_rotated_relative(at: tuple[Value, Value, Value], at_relative: Orientation,
                                      rotated: tuple[Value, Value, Value], rotated_relative: Orientation):
    rat = at_relative.position
    global_at = at[0] + rat[0], at[1] + rat[1], at[2] + rat[2]
    rot_rel = rotated_relative.angles
    global_rot = rotated[0] + rot_rel[0], rotated[1] + rot_rel[1], rotated[2] + rot_rel[2]
    return Orientation.from_at_rotated(global_at, global_rot)


def from_at_rotated_relative(at: tuple[Value, Value, Value], rotated: tuple[Value, Value, Value],
                             relative: Orientation):
    return from_at_relative_rotated_relative(at, relative, rotated, relative)
