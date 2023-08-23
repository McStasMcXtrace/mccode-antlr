from dataclasses import dataclass
from ..common import Expr


@dataclass
class Jump:
    target: str
    relative_target: int
    iterate: bool
    condition: Expr
    absolute_target: int = -1
