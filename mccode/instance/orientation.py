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


def degree_to_radian(v: Value):
    from math import pi
    if v.is_a(Value.Type.str):
        return v * Value.str('PI/180')
    return v * (pi/180)

@dataclass
class Orientation:
    position: tuple[Value, Value, Value] = field(default_factory=lambda: _value_float_tuple(3))
    rotation: tuple[Value, Value, Value, Value, Value, Value, Value, Value, Value] \
        = field(default_factory=lambda: _value_float_tuple(9))

    @property
    def affine_matrix(self):
        m = ((self.rotation[0], self.rotation[1], self.rotation[2], self.position[0]),
             (self.rotation[3], self.rotation[4], self.rotation[5], self.position[1]),
             (self.rotation[6], self.rotation[7], self.rotation[9], self.position[2]),
             (Value.float(0), Value.float(0), Value.float(0), Value.float(1)))
        return m

    @property
    def angles(self):
        # Copied from eniius get_euler_angles?
        pass


    @staticmethod
    def from_at_rotated(at, rotated):
        cx, cy, cz = [cos_value(degree_to_radian(r)) for r in rotated]
        sx, sy, sz = [sin_value(degree_to_radian(r)) for r in rotated]
        # The 3x3 rotation matrix part:
        m = ( cy * cz, sx * sy * cz + cx * sz, sx * sz - cx * sy * cz,
             -cy * sz, cx * cz - sx * sy * sz, sx * cz + cx * sy * sz,
              sy,     -sx * cy,                cx * cy)
        # The 3 vector part:
        v = at[0], at[1], at[2]
        return Orientation(v, m)


def from_at_rotated(at: tuple[Value, Value, Value], rotated: tuple[Value, Value, Value]):
    return Orientation.from_at_rotated(at, rotated)


def from_at_relative_rotated_relative(at: tuple[float, float, float], at_relative: Orientation,
                                      rotated: tuple[float, float, float], rotated_relative: Orientation):
    rat = at_relative.position
    global_at = at[0] + rat[0], at[1] + rat[1], at[2] + rat[2]
    rrot = rotated_relative.rotation
    global_rot = rotated[0] + rrot[0], rotated[1] + rrot[1], rotated[2] + rrot[2]
    return Orientation(global_at, global_rot)
