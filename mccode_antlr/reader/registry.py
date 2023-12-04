from __future__ import annotations

import pooch
from pathlib import Path
from re import Pattern
from mccode_antlr.version import version as mccode_antlr_version


def ensure_regex_pattern(pattern):
    import re
    if not isinstance(pattern, Pattern) and isinstance(pattern, str):
        pattern = re.compile(pattern)
    if not isinstance(pattern, Pattern):
        raise RuntimeError("No valid regex pattern from input")
    return pattern


def simple_url_validator(url: str, file_ok=False):
    from urllib.parse import urlparse

    if not isinstance(url, str):
        return False
    try:
        result = urlparse(url)
    except AttributeError:
        return False
    if not result.scheme:
        return False
    if file_ok:
        if result.scheme == 'file':
            print("Constructing a RemoteRegistry for a file:// URL will likely duplicate files!")
        if result.scheme != 'file' and not result.netloc:
            return False
    elif not result.netloc:
        return False
    return True


class Registry:
    name = None
    root = None
    pooch = None

    def __str__(self):
        from mccode_antlr.common import TextWrapper
        return self.to_string(TextWrapper())

    def to_string(self, wrapper):
        from io import StringIO
        output = StringIO()
        self.to_file(output, wrapper)
        return output.getvalue()

    def to_file(self, output, wrapper):
        print('Registry<>', file=output)

    def known(self, name: str, ext: str = None):
        pass

    def unique(self, name: str):
        pass

    def fullname(self, name: str, ext: str = None):
        pass

    def is_available(self, name: str, ext: str = None):
        pass

    def path(self, name: str, ext: str = None):
        pass

    def filenames(self) -> list[str]:
        pass

    def search(self, regex: Pattern):
        """Return filenames containing the regex pattern, uses regex search"""
        regex = ensure_regex_pattern(regex)
        return [x for x in self.filenames() if regex.search(x) is not None]

    def match(self, regex: Pattern):
        """Return regex *matching* registered file names -- which *start* with the regex pattern"""
        regex = ensure_regex_pattern(regex)
        return [x for x in self.filenames() if regex.match(x) is not None]


def _name_plus_suffix(name: str, suffix: str = None):
    path = Path(name)
    if suffix is not None and path.suffix != suffix:
        return path.with_suffix(f'{path.suffix}{suffix}').as_posix()
    return path.as_posix()


def find_registry_file(name: str):
    """Find a registry file in the mccode_antlr package"""
    from importlib.resources import files
    from importlib.metadata import distribution
    from json import loads
    if isinstance(name, Path):
        name = name.as_posix()
    if files('mccode_antlr').joinpath(name).is_file():
        return files('mccode_antlr').joinpath(name)
    info = loads(distribution('mccode_antlr').read_text('direct_url.json'))
    if 'dir_info' in info and 'editable' in info['dir_info'] and info['dir_info']['editable'] and 'url' in info:
        path = Path(info['url'].split('file://')[1]).joinpath('mccode_antlr', name)
        return path if path.is_file() else None
    return None


class RemoteRegistry(Registry):
    def __init__(self, name: str, url: str | None, version: str | None, filename: str | None):
        self.name = name
        self.url = url
        self.version = version
        self.filename = filename
        self.pooch = None

    @classmethod
    def file_keys(cls) -> tuple[str, ...]:
        return 'name', 'url', 'version', 'filename'

    def file_contents(self) -> dict[str, str]:
        return {key: getattr(self, key) or '' for key in self.file_keys()}

    def to_file(self, output, wrapper):
        wp = wrapper.parameter
        wv = wrapper.value
        contents = '(' + ', '.join([wp(n) + '=' + wv(v) for n, v in self.file_contents().items()]) + ')'
        print(wrapper.line(self.__class__.__name__, [contents], ''), file=output)

    def known(self, name: str, ext: str = None):
        compare = _name_plus_suffix(name, ext)
        # the files *in* the registry are already posix paths, so that makes life easier
        if any(x.endswith(compare) for x in self.pooch.registry_files):
            return True
        # fall back to matching without the extension:
        if any(Path(x).with_suffix('').as_posix().endswith(compare) for x in self.pooch.registry_files):
            return True
        # Or matching *any* file that contains name
        return any(name in x for x in self.pooch.registry_files)

    def unique(self, name: str):
        return sum(name in x for x in self.pooch.registry_files) == 1

    def fullname(self, name: str, ext: str = None, exact: bool = True):
        compare = _name_plus_suffix(name, ext)
        # the files *in* the registry are already posix paths, so that makes life easier
        # first step, exact match:
        for registry_file in self.pooch.registry_files:
            if registry_file == compare:
                return registry_file
        # second step, exact match to filename:
        for registry_file in self.pooch.registry_files:
            if Path(registry_file).parts[-1] == compare:
                return registry_file
        # fall back to matching without the extension:
        if not exact:
            for registry_file in self.pooch.registry_files:
                if Path(registry_file).with_suffix('').as_posix() == compare:
                    return registry_file
            # nearly-giving-up match filename without extension against the comparison
            for registry_file in self.pooch.registry_files:
                if Path(registry_file).with_suffix('').parts[-1] == compare:
                    return registry_file
        # Or matching *any* file that contains name
        matches = list(filter(lambda x: name in x, self.pooch.registry_files))
        if len(matches) != 1:
            raise RuntimeError(f'More than one match for {name}:{ext}, which is required of:\n{matches}')
        return matches[0]

    def is_available(self, name: str, ext: str = None, exact: bool = True):
        return self.pooch.registry_files(self.fullname(name, ext, exact))

    def path(self, name: str, ext: str = None, exact: bool = True):
        return Path(self.pooch.fetch(self.fullname(name, ext, exact)))

    def filenames(self) -> list[str]:
        return [x for x in self.pooch.registry_files]

    def __eq__(self, other):
        if not isinstance(other, Registry):
            return False
        if other.name != self.name:
            return False
        if other.pooch is None:
            return False
        if other.pooch.path != self.pooch.path:
            return False
        if other.pooch.base_url != self.pooch.base_url:
            return False
        return True


class ModuleRemoteRegistry(RemoteRegistry):
    def __init__(self, name: str, url: str, filename=None, version=None):
        super().__init__(name, url, version, filename)
        self.pooch = pooch.create(
            path=pooch.os_cache(f'mccode_antlr-{self.name}'),
            base_url=self.url,
            version=self.version or mccode_antlr_version(),
            version_dev="main",
            registry=None,
        )
        if isinstance(self.filename, Path):
            self.pooch.load_registry(self.filename)
        else:
            filepath = find_registry_file(self.filename)
            if filepath is None:
                raise RuntimeError(f"Provided filename {self.filename} is not a path or file packaged with this module")
            self.pooch.load_registry(filepath)


class GitHubRegistry(RemoteRegistry):
    def __init__(self, name: str, url: str, version: str, filename: str | None = None,
                 registry: str | dict | None = None):
        if filename is None:
            filename = f'{name}-registry.txt'
        super().__init__(name, url, version, filename)
        import requests
        base_url = f'{self.url}/raw/{self.version}/'
        # If registry is a string url, we expect the registry file to be available from _that_ url
        self._stashed_registry = None
        if isinstance(registry, str) and simple_url_validator(registry, file_ok=True):
            self._stashed_registry = registry
            registry = f'{registry}/raw/{self.version}/'
        # We allow a full-dictionary to be provided, otherwise we expect the registry file to be available from the
        # base_url where all subsequent files are also expected to be available
        if not isinstance(registry, dict):
            r = requests.get((registry or base_url) + (self.filename or 'pooch-registry.txt'))
            if not r.ok:
                raise RuntimeError(f"Could not retrieve {r.url} because {r.reason}")
            registry = {k: v for k, v in [x.split(maxsplit=1) for x in r.text.split('\n') if len(x)]}

        self.pooch = pooch.create(
            path=pooch.os_cache(self.name),
            base_url=base_url,
            version=version,
            version_dev="main",
            registry=registry,
        )

    @property
    def registry(self):
        return self._stashed_registry

    def file_contents(self) -> dict[str, str]:
        fc = super().file_contents()
        fc['registry'] = self._stashed_registry or ''
        return fc

    @classmethod
    def file_keys(cls) -> tuple[str, ...]:
        return super().file_keys() + ('registry',)


class LocalRegistry(Registry):
    def __init__(self, name: str, root: str):
        self.name = name
        self.root = Path(root)

    def to_file(self, output, wrapper):
        contents = '(' + ', '.join([
            wrapper.parameter('name') + '=' + wrapper.value(self.name),
            wrapper.parameter('root') + '=' + wrapper.url(self.root.as_posix()),
        ]) + ')'
        print(wrapper.line('LocalRegistry', [contents], ''), file=output)

    def _filetype_iterator(self, filetype: str):
        return self.root.glob(f'**/*.{filetype}')

    def _file_iterator(self, name: str):
        return self.root.glob(f'**/{name}')

    def _exact_file_iterator(self, name: str):
        return self.root.glob(name)

    def known(self, name: str, ext: str = None):
        compare = _name_plus_suffix(name, ext)
        return len(list(self._file_iterator(compare))) > 0

    def unique(self, name: str):
        return len(list(self._file_iterator(name))) == 1

    def fullname(self, name: str, ext: str = None, exact: bool = True):
        compare = _name_plus_suffix(name, ext)
        # Complete match
        is_compare = list(self._exact_file_iterator(compare))
        if len(is_compare) == 1:
            return is_compare[0]
        # Complete match if name happens to be missing the extension
        is_name = list(self._exact_file_iterator(name))
        if len(is_name) == 1:
            return is_name[0]
        if not exact:
            ends_with_compare = list(self._file_iterator(compare))
            if len(ends_with_compare) == 1:
                return ends_with_compare[0]
            # Complete match if name happens to be missing the extension
            ends_with_name = list(self._file_iterator(name))
            if len(ends_with_name) == 1:
                return ends_with_name[0]
        # Or matching *any* file that contains name
        matches = list(self._file_iterator(name))
        if len(matches) != 1:
            raise RuntimeError(f'More than one match for {name}:{ext}, which is required of:\n{matches}')
        return matches[0]

    def is_available(self, name: str, ext: str = None):
        return self.known(name, ext)

    def path(self, name: str, ext: str = None, exact: bool = True):
        return self.root.joinpath(self.fullname(name, ext, exact))

    def filenames(self) -> list[str]:
        return [str(x) for x in self.root.glob('**')]

    def __eq__(self, other):
        if not isinstance(other, Registry):
            return False
        if other.name != self.name:
            return False
        if other.root != self.root:
            return False
        return True


def registries_match(registry: Registry, spec):
    if isinstance(spec, Registry):
        return registry == spec
    parts = spec.split()
    path = Path(parts[1] if len(parts) == 2 else parts[0])
    if path.exists() and registry.root == path.resolve():
        return True
    url = parts[1] if len(parts) >= 2 else parts[0]
    if registry.pooch is not None and registry.pooch.base_url == url:
        return True
    return False


def registry_from_specification(spec: str):
    """Construct a Local or Remote Registry instance from a specification string

    Expected specifications are:

    1. {resolvable folder path}
    2. {name} {resolvable folder path}
    3. {name} {resolvable url} {resolvable file path}
    4. {name} {resolvable url} {version} {registry file name}

    The first two variants make a LocalRegistry, which searches the provided directory for files.
    The third makes a ModuleRemoteRegistry using pooch. The resolvable file path should point at a Pooch registry file.
    The fourth makes a GitHubRegistry, which uses the specific folder structure of GitHub
    """
    if isinstance(spec, Registry):
        return spec
    parts = spec.split()
    if len(parts) == 0:
        return None
    elif len(parts) == 1:
        p1, p2, p3, p4 = parts[0], parts[0], None, None
    elif len(parts) < 4:
        p1, p2, p3, p4 = parts[0], parts[1], None if len(parts) < 3 else parts[2], None
    else:
        p1, p2, p3, p4 = parts[0], parts[1], parts[2], parts[3]
    print(f"Constructing registry from {p1=} {p2=} {p3=} {p4=}  [{type(p1)=} {type(p2)=} {type(p3)=} {type(p4)=}]")
    # convert string literals to strings:
    p1 = p1[1:-1] if p1.startswith('"') and p1.endswith('"') else p1
    p2 = p2[1:-1] if p2.startswith('"') and p2.endswith('"') else p2
    p3 = p3[1:-1] if p3 is not None and p3.startswith('"') and p3.endswith('"') else p3
    p4 = p4[1:-1] if p4 is not None and p4.startswith('"') and p4.endswith('"') else p4

    if Path(p2).exists() and Path(p2).is_dir():
        return LocalRegistry(p1, str(Path(p2).resolve()))

    # (simple) URL validation:
    if not simple_url_validator(p2, file_ok=True):
        return None

    if Path(p3).exists() and Path(p3).is_file():
        return ModuleRemoteRegistry(p1, p2, Path(p3).resolve().as_posix())

    if p4 is not None:
        return GitHubRegistry(p1, p2, p3, p4)

    return None


def _m_reg(name):
    m_url = "https://github.com/McStasMcXtrace/McCode"
    r_url = "https://github.com/g5t/mccode-pooch"
    # TODO update this version with new McStasMcXtrace releases
    return GitHubRegistry(name, m_url, 'v3.4.0', registry=r_url)


# TODO remove this registry once mcstas-d.h and mcxtrace-d.h are in the mccode repo; plus mccode-r.h is not configured
FIXED_LIBC_REGISTRY = ModuleRemoteRegistry(
    'fixed-libc',
    'https://github.com/g5t/mccode-files/raw/main/runtime/libc',
    'libc-registry.txt'
)

MCSTAS_REGISTRY, MCXTRACE_REGISTRY, LIBC_REGISTRY = [_m_reg(name) for name in ('mcstas', 'mcxtrace', 'libc')]
del _m_reg
