# MicroPython_Statistics

Statistics module for MicroPython, based on statistics module for Python 3 (>= 3.4) :
- [documentation of Python 3 statistics module](https://docs.python.org/3/library/statistics.html)
- [PEP 0450 about Python 3 statistics module](https://www.python.org/dev/peps/pep-0450/)
- [source code of Python 3 statistics module](https://github.com/python/cpython/blob/3.7/Lib/statistics.py)

There are some differences between MicroPython version and Python 3 version of statistics module :
- less precision on mean due to lack of fraction numbers on MicroPython;
- no error messages.
