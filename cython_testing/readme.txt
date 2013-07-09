Requirements:
Python
GCC
Cython (see getting_cython.txt)
---

How to cython stuff:

Note that cython does *not* create a c code that gets compiled into an application.
It creates c code that gets compiled into a python extension that can imported into a python script.

The 'normal' python way:

some_module.py ===[imported as 'some_module']===> main.py

The cython way:

some_module.pyx =[cython]=> some_module.c =[gcc]=> some_module.dll ===[imported as 'some_module']===> main.py

Fortunately, cython is a strict *superset* of python. Most development can (and should) be done with normal python.
Only use cython once you've decided you like the way your code is written and are trying to squeeze out extra performance.

---

Automated builds:

Compiling some_module.pyx with cython by hand is painful. Python's distutils makes this easier.

setup.py ends up being the equivalent of 'make'. I've already created a setup.py to handle example.pyx.

To build, excute the following at the command line:

$ python setup.py build_ext --inplace

This will generate a python extension. Open a python interpreter and type:

>> import example

And you will have access to all of the functions in the example module, (but they will probably be faster then pure python.)

---

Performance:

example.pyx has the function primes(kmax) which lists the first k primes
pure_python_example.py also has the function primes(kmax)

Results:

$ time benchmark_python.py

real    0m12.381s
user    0m12.214s
sys     0m0.171s

$ time benchmark_cython.py

real    0m0.435s
user    0m0.250s

In this case, cython is about 50 times faster.

Additional reading:
http://en.wikipedia.org/wiki/Cython
http://docs.cython.org/src/userguide/source_files_and_compilation.html#compilation