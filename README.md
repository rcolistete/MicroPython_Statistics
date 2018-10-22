# MicroPython Statistics module

Statistics module for MicroPython, based on statistics module for Python 3 (>= 3.4) :
- [documentation of Python 3 statistics module](https://docs.python.org/3/library/statistics.html)
- [PEP 0450 about Python 3 statistics module](https://www.python.org/dev/peps/pep-0450/)
- [source code of Python 3 statistics module](https://github.com/python/cpython/blob/3.7/Lib/statistics.py)

All Python 3 statistics functions are implemented on MicroPython version, with the same syntax :

| Function | Description |
| -------- | ----------- |
| mean()   | Arithmetic mean (“average”) of data |
| harmonic_mean()	| Harmonic mean of data |
| median() | Median (middle value) of data |
| median_low()	| Low median of data |
| median_high()	| High median of data |
| median_grouped()	| Median, or 50th percentile, of grouped data |
| mode() |	Mode (most common value) of discrete data |
| pstdev() | Population standard deviation of data |
| pvariance()	| Population variance of data |
| stdev()	| Sample standard deviation of data |
| variance() | Sample variance of data |

The MicroPython version of statistics module has some limitations :
- less precision on mean due to the lack of fraction numbers and 'float.as_integer_ratio()' on MicroPython;
- Fraction (from fraction module) and Decimal (from decimal module) are not accepted numbers because the fraction and decimal modules are not implemented on MicroPython;
- no error messages;
- no documentation and examples for each function inside the module.

Many MicroPython modules are optimised to save RAM memory because many microcontrollers only have tens of KBytes.
