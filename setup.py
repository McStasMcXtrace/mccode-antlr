import sys
import os
import fnmatch
import setuptools
from setuptools.command.build_ext import build_ext


def get_target():
    from platform import system
    target = system().lower()
    platforms = {'windows', 'linux', 'darwin', 'cygwin'}
    for known in platforms:
        if target.startswith(known):
            return known
    raise ValueError(f'Unknown platform {target}')


def get_target_args():
    extra_compile_args = {
        'windows': ['/DANTLR4CPP_STATIC', '/Zc:__cplusplus', '/std:c++17'],
        'linux': ['-std=c++17'],
        'darwin': ['-std=c++17'],
        'cygwin': ['-std=c++17']
    }
    return extra_compile_args.get(get_target(), [])


def get_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(root, filename)


def all_files(name, ext):
    src = 'src/grammar/Cpp'
    lib = 'lib/antlr4-cpp-runtime'
    antlr_src = list(get_files(lib, f"*.{ext}"))
    antlr_gen = list(get_files(src, f"{name}*.{ext}"))
    speed_gen = list(get_files(src, f"sa_{name.lower()}*.{ext}"))
    speed_src = list(get_files(src, f"speedy*.{ext}"))
    return antlr_src + antlr_gen + speed_gen + speed_src


def run_setup(with_binary):
    if with_binary:
        ext_modules = [
            setuptools.Extension(
                name=f'mccode_antlr.grammar.sa_{name.lower()}_cpp_parser',
                include_dirs=['lib/antlr4-cpp-runtime'],
                sources=all_files(name, 'cpp'),
                depends=all_files(name, 'h'),
                extra_compile_args=get_target_args()
            )
            for name in ('McComp', 'McInstr')
        ]
    else:
        ext_modules = []

    setuptools.setup(
        ext_modules=ext_modules,
        cmdclass={"build_ext": build_ext},
    )



#===============================================================================


# Detect if an alternate interpreter is being used
is_jython = "java" in sys.platform
is_pypy = hasattr(sys, "pypy_version_info")

# Force using fallback if using an alternate interpreter
using_fallback = is_jython or is_pypy

if not using_fallback:
    try:
        run_setup(with_binary=True)
    except Exception:
        using_fallback = True

if using_fallback:
    run_setup(with_binary=False)