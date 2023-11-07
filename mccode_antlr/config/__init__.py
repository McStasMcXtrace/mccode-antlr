import confuse
# Try and simplify handling configuration values need for, e.g., compiling different versions of the runtimes
# under different operating systems, while allowing a user to 'easily' override defaults if necessary.
#
# Any platform independent configuration settings can go in 'config_default.yaml'
config = confuse.LazyConfig('mccode_antlr', __name__)

# use environment variables specified as 'MCCODE_XYZ' as configuration entries 'xyz'
config.set_env()


# Add platform specific values from the local config_platforms.yaml
def _platform_defaults():
    import platform
    import yaml
    from importlib.resources import files, as_file

    platforms_file = files(__name__).joinpath('platforms.yaml')
    if not platforms_file.is_file():
        raise RuntimeError(f"Can not locate platforms.yaml in module files (looking for {platforms_file}")

    with as_file(platforms_file) as file:
        with open(file, 'r') as data:
            platform_configs = yaml.safe_load(data)

    system = platform.system()  # "Linux", "Darwin", "Windows", ...
    if system not in platform_configs:
        raise RuntimeError(f"Unknown system '{system}' for default configuration")

    return platform_configs[system]


# By using the 'add' method, we set these as the *lowest* priority. Any user/system files will override:
config.add(_platform_defaults())
