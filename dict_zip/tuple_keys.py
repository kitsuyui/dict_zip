from __future__ import annotations
from typing import TypeVar

from .dict_map import map_keys


T = TypeVar("T")
S = TypeVar("S")


def tuple_keys(dic: dict[T, S]) -> dict[tuple[T], S]:
    """Convert the keys of a dictionary to tuples.
    Args:
        dic: The dictionary to convert.
    Returns:
        A new dictionary with the keys converted to tuples.
    Example:
        >>> from dict_zip import tuple_keys
        >>> tuple_keys({'a': 1, 'b': 2})
        {('a',): 1, ('b',): 2}
    """
    return map_keys(dic, lambda k: (k,))
