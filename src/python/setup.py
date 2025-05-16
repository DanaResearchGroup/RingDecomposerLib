from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Absolute path to the RingDecomposerLib static library
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
lib_path = os.path.join(root, "build", "src", "RingDecomposerLib", "libRingDecomposerLibStatic.a")
include_path = os.path.join(root, "src", "RingDecomposerLib")

ext_modules = cythonize([
    Extension(
        name="py_rdl.wrapper.DataInternal",
        sources=["py_rdl/wrapper/DataInternal.pyx"],
        include_dirs=[include_path],
        extra_objects=[lib_path],
        language="c++"
    )
], language_level=3)

setup(
    name="py_rdl",
    packages=["py_rdl", "py_rdl.wrapper"],
    package_dir={"py_rdl": "."},
    package_data={"py_rdl.wrapper": ["*.pyx", "*.pxd"]},
    ext_modules=ext_modules,
    zip_safe=False,
)
