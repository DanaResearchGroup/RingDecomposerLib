from setuptools import setup, Extension
from Cython.Build import cythonize
import os

RDL_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

extensions = [
    Extension(
        name='py_rdl.wrapper.DataInternal',
        sources=['py_rdl/wrapper/DataInternal.pyx'],
        include_dirs=[
            os.path.join(RDL_ROOT, 'src', 'RingDecomposerLib'),
            os.path.join(RDL_ROOT, 'build', 'src', 'RingDecomposerLib'),
            os.path.join(os.path.dirname(__file__), 'py_rdl', 'wrapper'),  # crucial for .pxd
        ],
        extra_objects=[
            os.path.join(RDL_ROOT, 'build', 'src', 'RingDecomposerLib', 'libRingDecomposerLibStatic.a')
        ],
        language='c++',
    )
]

setup(
    name='py_rdl',
    packages=['py_rdl', 'py_rdl.wrapper'],
    package_data={'py_rdl.wrapper': ['*.pyx', '*.pxd']},
    ext_modules=cythonize(extensions, language_level=3),
    zip_safe=False
)
