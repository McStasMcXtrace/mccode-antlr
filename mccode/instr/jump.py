from dataclasses import dataclass
from ..common import Value


@dataclass
class Jump:
    target: str
    relative_target: int
    iterate: bool
    condition: Value
    absolute_target: int = -1
