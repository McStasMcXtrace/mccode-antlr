import pooch
from pathlib import Path
from importlib.resources import files, as_file

class Registry:
    def __init__(self, name: str, url: str, version, dev, filename=None):
        self.pooch = pooch.create(
            path=pooch.os_cache(name),
            base_url=url,
            version=version,
            version_dev=dev,
            registry=None,
        )
        if isinstance(filename, Path):
            self.pooch.load_registry(filename)
        elif files('mccode').joinpath(filename).is_file():
            with as_file(files('mccode').joinpath(filename)) as path:
                self.pooch.load_registry(path)
        else:
            raise RuntimeError(f"The provided filename {filename} is not a path or file packaged with this module")

