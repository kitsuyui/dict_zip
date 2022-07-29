# dict_zip

zip and zip_longest for dict.

[![Python](https://img.shields.io/pypi/pyversions/dict-zip.svg)](https://badge.fury.io/py/dict-zip)
[![codecov](https://codecov.io/gh/kitsuyui/dict_zip/branch/master/graph/badge.svg?token=LiuhQeZsnc)](https://codecov.io/gh/kitsuyui/dict_zip)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI version shields.io](https://img.shields.io/pypi/v/dict-zip.svg)](https://pypi.python.org/pypi/dict-zip/)

# Installation

```sh
$ pip install dict-zip
```

# Usage

## dict_zip

`dict_zip` is `zip` for dict.

```python
>>> from dict_zip import dict_zip
>>> dict_zip({'a': 1, 'b': 2}, {'a': 3, 'b': 4})
{'a': (1, 3), 'b': (2, 4)}
```

## dict_zip_longest

`dict_zip_longest` is `zip_longest` for dict.
It fills with fillvalue (default: `None`) when argument dict doesn't have match key.

```python
>>> from dict_zip import dict_zip_longest
>>> dict_zip_longest({'a': 1, 'b': 2, 'c': 4}, {'a': 3, 'b': 4})
{'a': (1, 3), 'b': (2, 4), 'c': (4, None)}
```

# LICENSE

The 3-Clause BSD License. See also LICENSE file.
