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

    def is_leader(self, index: int):
        return len(self.ids) and self.ids[0] == index

    @property
    def first_id(self):
        return min(self.ids)

    @property
    def last_id(self):
        return max(self.ids)

    @property
    def first(self):
        fid = self.first_id
        return [m for i, m in zip(self.ids, self.members) if i == fid][0]

    @property
    def last(self):
        lid = self.last_id
        return [m for i, m in zip(self.ids, self.members) if i == lid][0]

    def copy(self):
        return Group(self.name, self.index, self.ids.copy(), self.members.copy())
