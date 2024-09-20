import sys
import os
import fnmatch
import setuptools

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


def all_files(pattern):
    directory = 'src/grammar/Cpp'
    return list(get_files(directory, pattern))


def run_setup(with_binary):
    if with_binary:
        ext_modules = [
            setuptools.Extension(
                name=f'mccode_antlr.grammar.sa_{name.lower()}_cpp_parser',
                include_dirs=['lib/antlr4-cpp-runtime'],
                sources=all_files(f'{name}*.cpp') + all_files(f'sa_{name.lower()}*.cpp') + all_files('speedy*.cpp'),
                depends=all_files(f'{name}*.h') + all_files(f'sa_{name.lower()}*.h') + all_files('speedy*.h'),
                extra_compile_args=get_target_args()
            )
            for name in ('McComp', 'McInstr')
        ]
    else:
        ext_modules = []

    setuptools.setup(
        name='mccode-antlr',
        packages=setuptools.find_packages('mccode_antlr'),
        package_dir={'': 'src'},
        ext_modules=ext_modules,
        python_requires='>=3.8',
        install_requires=[
            'antlr4-python3-runtime==4.9.2',
            'speedy-antlr-tool==0.1.0'
        ],
        entry_points={
            'console_scripts': [
                'mccode-antlr-build = grammar.builder:main'
            ]
        }
    )

