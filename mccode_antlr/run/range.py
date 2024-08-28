from __future__ import annotations

from typing import Union


class MRange:
    """A range of values for a parameter in a MATLAB style.
    The range is inclusive of the start and stop values, and the step is the difference between items in the range.
    """
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        if self.start == self.stop:
            raise ValueError(f'MRange start and stop values are equal: {self.start} '
                             f'`list(MRange)` will be empty! Use a `Singular({self.start}, 1)` range instead.')
        if self.step == 0:
            raise ZeroDivisionError('MRange step cannot be zero')

    def __eq__(self, other):
        return self.start == other.start and self.stop == other.stop and self.step == other.step

    @property
    def min(self):
        return self.start

    @property
    def max(self):
        return self.stop

    def __iter__(self):
        def range_gen(start, stop, step):
            v = start
            i = 0
            while (step > 0 and v + step <= stop) or (step < 0 and v + step >= stop):
                v = i * step + start
                i += 1
                yield v
        return range_gen(self.start, self.stop, self.step)

    def __getitem__(self, index: int):
        if index < 0 or index >= len(self):
            raise IndexError(f'Index {index} out of range')
        return index * self.step + self.start

    def __str__(self):
        return f'{self.start}:{self.step}:{self.stop}'

    def __repr__(self):
        return f'MStyleRange({self})'

    def __len__(self):
        return int((self.stop - self.start) / self.step) + 1

    @classmethod
    def from_str(cls, string):
        """Parse a string in MATLAB style into a range.
        The string should be of the form start:step:stop
        """
        def float_or_int(s):
            try:
                return int(s)
            except ValueError:
                pass
            return float(s)

        if string.count(':') > 2:
            raise ValueError(f'Range string {string} contains more than two colons')
        step = '1'
        if ':' not in string:
            start, stop = string, string
        elif string.count(':') == 1:
            start, stop = string.split(':')
        else:
            start, step, stop = string.split(':')
        return cls(float_or_int(start), float_or_int(stop), float_or_int(step))


class Singular:
    """A singular range parameter for use with other range parameters in, e.g., a zip.

    Note:
        The Singular range value will be repeated up to `maximum` times in an iterator.
        If `maximum` is None, the Singular range will be repeated forever.
        Therefore, care must be taken to ensure that the Singular range is used in a zip with a range that is
        not infinite.
    """
    def __init__(self, value, maximum=None):
        self.value = value
        self.maximum = maximum

    def __eq__(self, other):
        return self.value == other.value and self.maximum == other.maximum

    def __str__(self):
        return f'{self.value}(up to {self.maximum} times)'

    def __repr__(self):
        return f'Singular({self.value}, {self.maximum})'

    @property
    def min(self):
        return self.value

    @property
    def max(self):
        return self.value

    def __iter__(self):
        def forever():
            while True:
                yield self.value

        def until():
            i = 0
            while i < self.maximum:
                i += 1
                yield self.value

        return until() if self.maximum is not None else forever()

    def __len__(self):
        return self.maximum

    @classmethod
    def from_str(cls, string):
        def float_or_int_or_str(s):
            try:
                return int(s)
            except ValueError:
                pass
            try:
                return float(s)
            except ValueError:
                return s

        if string.count(':') > 0:
            raise ValueError(f'Singular string {string} contains a colon')
        return cls(float_or_int_or_str(string))


def parse_list(range_type, unparsed: list[str]):
    ranges = {}
    while len(unparsed):
        if '=' in unparsed[0]:
            k, v = unparsed[0].split('=', 1)
            ranges[k.lower()] = range_type.from_str(v)
        elif len(unparsed) > 1 and '=' not in unparsed[1]:
            ranges[unparsed[0].lower()] = range_type.from_str(unparsed[1])
            del unparsed[1]
        else:
            raise ValueError(f'Invalid parameter: {unparsed[0]}')
        del unparsed[0]
    return ranges


def parameters_to_scan(parameters: dict[str, Union[list, MRange, Singular]], grid: bool = False):
    """Convert a dictionary of ranged parameters to a list of parameter names and an iterable of parameter value tuples.

    The ranged parameters can be either MRange objects or lists of values. If a list of values is provided, it will be
    iterated over directly.

    :parameter parameters: A dictionary of ranged parameters.
    :parameter grid: Controls how the parameters are iterated; True implies a grid scan, False implies a linear scan.
    """
    if grid:
        for k, v in parameters.items():
            if isinstance(v, Singular):
                parameters[k] = Singular(v.value, 1)

    names = [x.lower() for x in parameters.keys()]
    values = [x if hasattr(x, '__iter__') else [x] for x in parameters.values()]
    if not len(values):
        return 0, names, []
    elif grid:
        from itertools import product
        from math import prod
        # singular MRange objects *should* stop the grid along their axis:
        n_pts = prod([len(v) for v in values])
        return n_pts, names, product(*values)
    else:
        # replace singular MRange entries with Singular iterators, to avoid stopping the zip early:
        n_max = max([len(v) for v in values])
        for i, v in enumerate(values):
            if len(v) > 1 and len(v) != n_max:
                oth = [names[i] for i, n in enumerate(values) if len(n) == n_max]
                par = 'parameters' if len(oth) > 1 else 'parameter'
                have = 'have' if len(oth) > 1 else 'has'
                raise ValueError(f'Parameter {names[i]} has {len(v)} values, but {par} {", ".join(oth)} {have} {n_max}')
        return n_max, names, zip(*[v if len(v) > 1 else Singular(v[0] if isinstance(v, MRange) else v.value, n_max) for v in values])


def _MRange_or_Singular(s: str):
    if ':' in s:
        return MRange.from_str(s)
    return Singular.from_str(s)


def parse_command_line_parameters(unparsed: list[str]) -> dict[str, Union[Singular, MRange]]:
    """Parse a list of input parameters into a dictionary of MRange objects.

    :parameter unparsed: A list of parameters.
    """
    ranges = {}
    index = 0
    while index < len(unparsed):
        if '=' in unparsed[index]:
            k, v = unparsed[index].split('=', 1)
            ranges[k.lower()] = _MRange_or_Singular(v)
        elif index + 1 < len(unparsed) and '=' not in unparsed[index + 1]:
            ranges[unparsed[index].lower()] = _MRange_or_Singular(unparsed[index + 1])
            index += 1
        else:
            raise ValueError(f'Invalid parameter: {unparsed[index]}')
        index += 1
    return ranges


def parse_scan_parameters(unparsed: list[str]) -> dict[str, MRange | Singular]:
    """Parse a list of input parameters into a dictionary of MRange or Singular objects.

    :parameter unparsed: A list of parameters.
    :return: A dictionary of MRange or Singular objects. The Singular objects have their maximum length set to the
             maximum iterations of all the ranges to avoid infinite iterations.
    """
    ranges = parse_command_line_parameters(unparsed)
    max_length = max(len(v) if isinstance(v, MRange) else 1 for v in ranges.values())
    for k, v in ranges.items():
        if isinstance(v, Singular) and v.maximum is None:
            ranges[k] = Singular(v.value, max_length)
    return ranges