from distutils.core import Extension as cExtension
from pyd.support import setup, Extension

module1 = Extension("x", sources = ['xclass.c'])
module2 = Extension("y", sources = ['hello.d'], build_deimos=True, d_lump=True)

setup(
    name = "x",
    version = '1.0',
    description = "eat a taco",
    ext_modules = [
        module1,
        module2
    ]
);
