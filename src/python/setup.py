from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# absolute path to RDL root
RDL_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

extensions = [
    Extension(
        name='py_rdl.wrapper.DataInternal',
        sources=['py_rdl/wrapper/DataInternal.pyx'],
        include_dirs=[os.path.join(RDL_ROOT, 'src', 'RingDecomposerLib')],
        extra_objects=[os.path.join(RDL_ROOT, 'build', 'src', 'RingDecomposerLib', 'libRingDecomposerLibStatic.a')],
        language='c++'
    )
]

setup(
    name='py_rdl',
    packages=['py_rdl', 'py_rdl.wrapper'],
    package_dir={'py_rdl': '.'},
    package_data={'py_rdl.wrapper': ['*.pyx', '*.pxd']},
    ext_modules=cythonize(extensions, language_level=3),
    zip_safe=False
)
