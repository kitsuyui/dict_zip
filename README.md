# dict_zip

zip and zip_longest for dict.

[![Python](https://img.shields.io/pypi/pyversions/dict-zip.svg)](https://badge.fury.io/py/dict-zip)
[![PyPI version](https://img.shields.io/pypi/v/dict-zip.svg)](https://pypi.python.org/pypi/dict-zip/)
[![codecov](https://codecov.io/gh/kitsuyui/dict_zip/branch/main/graph/badge.svg?token=LiuhQeZsnc)](https://codecov.io/gh/kitsuyui/dict_zip)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![dict-zip](https://snyk.io/advisor/python/dict-zip/badge.svg)](https://snyk.io/advisor/python/dict-zip)

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

## map_keys, map_values, map_items

`map_keys`, `map_values`, and `map_items` are used to map keys, values, and items of dict.

```python
>>> from dict_zip import map_keys
>>> map_keys({'a': 1, 'b': 2}, str.upper)
{'A': 1, 'B': 2}
>>> from dict_zip import map_values
>>> map_values({'a': 1, 'b': 2}, str)
{'a': '1', 'b': '2'}
>>> from dict_zip import map_items
>>> map_items({'a': 1, 'b': 2}, str.upper, str)
{'A': '1', 'B': '2'}
```

## tuple_keys

`tuple_keys` is used to convert dict keys to tuple.

```python
>>> from dict_zip import tuple_keys
>>> tuple_keys({'a': 1, 'b': 2})
{('a',): 1, ('b',): 2}
```

# Type hints

dict_zip supports for type hints.

<img width="535" alt="screen-shot-of-type-hints" src="https://user-images.githubusercontent.com/2596972/181838389-2860e45c-b366-41e4-83a1-f747b7115a5f.png">

# LICENSE

The 3-Clause BSD License. See also LICENSE file.
