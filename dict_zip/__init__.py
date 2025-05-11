"""dict_zip

This module provides a function that concatenates dictionaries.
Like the zip function for lists, it concatenates dictionaries.

Example:
    >>> from dict_zip import dict_zip
    >>> dict_zip({'a': 1, 'b': 2}, {'a': 3, 'b': 4})
    {'a': (1, 3), 'b': (2, 4)}

    >>> from dict_zip import dict_zip_longest
    >>> dict_zip_longest({'a': 1, 'b': 2, 'c': 4}, {'a': 3, 'b': 4})
    {'a': (1, 3), 'b': (2, 4), 'c': (4, None)}
"""

# https://packaging-guide.openastronomy.org/en/latest/advanced/versioning.html
from ._version import __version__
from .dict_zip import dict_zip
from .dict_zip_longest import dict_zip_longest
from .dict_map import (
    map_keys,
    map_values,
    map_items,
)
from .tuple_keys import tuple_keys


__all__ = [
    "dict_zip",
    "dict_zip_longest",
    "map_keys",
    "map_values",
    "map_items",
    "map_keys_first",
    "map_keys_last",
    "tuple_keys",
    "__version__",
]
