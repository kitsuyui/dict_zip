# dict_zip

zip and zip_longest for dict.

[![CircleCI](https://circleci.com/gh/kitsuyui/dict_zip.svg?style=svg)](https://circleci.com/gh/kitsuyui/dict_zip)

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# Usage

## dict_zip

`dict_zip` is `zip` for dict.

```python
>>> from dict_zip import dict_zip
>>> dict_zip({'a': 1, 'b': 2}, {'a': 3, 'b': 4})
{'b': (2, 4), 'a': (1, 3)}
```

## dict_zip_longest

`dict_zip_longest` is `zip_longest` for dict.
It fills with fillvalue (default: `None`) when argument dict doesn't have match key.

```python
>>> from dict_zip import dict_zip_longest
>>> dict_zip_longest({'a': 1, 'b': 2, 'c': 4}, {'a': 3, 'b': 4})
{'b': (2, 4), 'a': (1, 3), 'c': (4, None)}
```

# LICENSE

The 3-Clause BSD License. See also LICENSE file.
