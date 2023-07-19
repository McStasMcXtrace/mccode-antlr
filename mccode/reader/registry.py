import pooch
from pathlib import Path
from importlib.resources import files, as_file
from mccode import __version__


class Registry:
    name = None
    root = None
    pooch = None

    def known(self, name: str):
        pass

    def unique(self, name: str):
        pass

    def fullname(self, name: str):
        pass

    def is_available(self, name: str):
        pass

    def path(self, name: str):
        pass



class RemoteRegistry(Registry):
    def __init__(self, name: str, url: str, filename=None):
        self.name = name
        self.pooch = pooch.create(
            path=pooch.os_cache(f'mccode-{name}'),
            base_url=url,
            version=__version__,
            version_dev="main",
            registry=None,
        )
        if isinstance(filename, Path):
            self.pooch.load_registry(filename)
        elif files('mccode').joinpath(filename).is_file():
            with as_file(files('mccode').joinpath(filename)) as path:
                self.pooch.load_registry(path)
        else:
            raise RuntimeError(f"The provided filename {filename} is not a path or file packaged with this module")

    def known(self, name: str):
        return any(name in x for x in self.pooch.registry_files)

    def unique(self, name: str):
        return sum(name in x for x in self.pooch.registry_files) == 1

    def fullname(self, name: str):
        return list(filter(lambda x: name in x, self.pooch.registry_files))[0]

    def is_available(self, name: str):
        return self.pooch.registry_files(self.fullname(name))

    def path(self, name: str):
        return Path(self.pooch.fetch(self.fullname(name)))

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


class LocalRegistry(Registry):
    def __init__(self, name: str, root: str):
        self.name = name
        self.root = Path(root)

    def _filetype_iterator(self, filetype: str):
        return self.root.glob(f'**/*.{filetype}')

    def _file_iterator(self, name: str):
        return self.root.glob(f'**/{name}')

    def known(self, name: str):
        return len(list(self._file_iterator(name))) > 0

    def unique(self, name: str):
        return len(list(self._file_iterator(name))) == 1

    def fullname(self, name: str):
        return list(self._file_iterator(name))[0]

    def is_available(self, name: str):
        return self.known(name)

    def path(self, name: str):
        return self.root.joinpath(self.fullname(name))

    def __eq__(self, other):
        if not isinstance(other, Registry):
            return False
        if other.name != self.name:
            return False
        if other.root != self.root:
            return False
        return True


MCSTAS_REGISTRY = RemoteRegistry('mcstas', 'https://github.com/g5t/mccode-mcstas-files/raw/main', 'mcstas-registry.txt')


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

    The first two variants make a LocalRegistry, which searches the provided directory for files.
    The last makes a RemoteRegistry using pooch. The resolvable file path should point at a  Pooch registry file.

    Note:
        At present, no check is performed on the Pooch URL before attempting to locate a file.
        This could lead to delayed runtime errors.
    """
    if isinstance(spec, Registry):
        return spec
    parts = spec.split()
    if len(parts) == 0:
        return None
    elif len(parts) == 1:
        p1, p2, p3 = parts, parts, None
    else:
        p1, p2, p3 = parts[0], parts[1], None if len(parts) < 3 else parts[2]
    if Path(p2).exists() and Path(p2).is_dir():
        return LocalRegistry(p1, str(Path(p2).resolve()))
    if Path(p3).exists() and Path(p3).is_file():
        return RemoteRegistry(p1, p2, Path(p3).resolve())
    return None



