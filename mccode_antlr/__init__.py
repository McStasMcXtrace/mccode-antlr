"""Monte Carlo Particle Ray Tracing compiler, Volume 4"""
import mccode_antlr.grammar
__author__ = "Gregory Tucker"
__affiliation__ = "European Spallation Source ERIC"


def version():
    import sys
    if sys.version_info[0] == 3 and sys.version_info[1] < 8:
        import importlib_metadata
    else:
        import importlib.metadata as importlib_metadata
    try:
        return importlib_metadata.version("mccode_antlr")
    except importlib_metadata.PackageNotFoundError:
        return "dev"


__version__ = version()

__all__ = ["__author__", "__affiliation__", "__version__", "version"]
