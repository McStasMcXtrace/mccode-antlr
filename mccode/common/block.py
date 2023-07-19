from dataclasses import dataclass


@dataclass
class RawC:
    filename: str
    line: int
    source: str

    @staticmethod
    def from_tuple(p: tuple):
        if isinstance(p, tuple) and len(p) == 3 and \
                isinstance(p[0], str) and isinstance(p[1], int) and isinstance(p[2], str):
            return RawC(*p)
        if isinstance(p, tuple) and len(p) == 2 and isinstance(p[0], int) and isinstance(p[1], str):
            return RawC("", *p)
        if isinstance(p, str):
            return RawC("", -1, p)
        raise RuntimeError(f"No conversion to RawC from\n{p}")

    def to_c(self):
        """Use the preprocessor #line directive to aid in debugging produced C source code."""
        return f'#line {self.line} "{self.filename}"\n{self.source}'


def blocks_to_raw_c(*args):
    return tuple(x if isinstance(x, RawC) else RawC.from_tuple(x) for x in args)
