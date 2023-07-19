from dataclasses import dataclass
from ..common import Value


@dataclass
class Jump:
    target: str
    target_index: int
    iterate: bool
    condition: Value
