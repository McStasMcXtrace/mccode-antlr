import pooch
from pathlib import Path
from importlib.resources import files, as_file
from mccode import __version__


class Registry:
    name = None

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


MCSTAS_REGISTRY = RemoteRegistry('mcstas', 'https://github.com/g5t/mccode-mcstas-files/raw/main', 'mcstas-registry.txt')
