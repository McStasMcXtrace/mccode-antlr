"""Monte Carlo Particle Ray Tracing compiler, Volume 4"""
__author__ = "Gregory Tucker"
__affiliation__ = "European Spallation Source ERIC"
import sys
if sys.version_info[0] == 3 and sys.version_info[1] < 8:
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata
try:
    __version__ = importlib_metadata.version("mccode")
except importlib_metadata.PackageNotFoundError:
    __version__ = "dev"

import mccode.grammar
