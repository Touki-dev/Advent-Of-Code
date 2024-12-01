from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("optimized_day18_part2.pyx", language_level="3"),
    include_dirs=[np.get_include()]
)