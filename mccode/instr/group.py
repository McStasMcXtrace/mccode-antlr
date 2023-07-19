from dataclasses import dataclass, field
from .instance import Instance

@dataclass
class Group:
    name: str
    index: int
    ids: list[int] = field(default_factory=list)
    members: list[Instance] = field(default_factory=list)

    def add(self, id: int, inst: Instance):
        self.ids.append(id)
        self.members.append(inst)
