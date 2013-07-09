#!/usr/bin/env python3

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# Note that (unlike normal python) the name of the extension
# is not necessarily the name of the .pyx file (e.g. it is possible,
# but not recommend, to set extension_name to 'something_else'
# which would mean that, after compilation, you would import the 
# module via 'import something_else', even though the source file is 'example.pyx')
#
# In normal python, you would *always* import example.py by 'import example'

extension_name = "example"
sourcefiles = ["example.pyx"]

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension(extension_name, sourcefiles)]
)