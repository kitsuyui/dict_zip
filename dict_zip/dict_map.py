from __future__ import annotations
from typing import TypeVar, Callable

K = TypeVar("K")
V = TypeVar("V")
U = TypeVar("U")
T = TypeVar("T")


def map_keys(dic: dict[K, V], func: Callable[[K], U]) -> dict[U, V]:
    """Apply a function to the keys of a dictionary.
    Args:
        dic: The dictionary to map.
        func: The function to apply to the keys.
    Returns:
        A new dictionary with the same values but with the keys transformed by the function.
    Example:
        >>> from dict_zip import map_keys
        >>> map_keys({'a': 1, 'b': 2}, str.upper)
        {'A': 1, 'B': 2}
        >>> map_keys({'a': 1, 'b': 2}, lambda x: x + '!')
        {'a!': 1, 'b!': 2}
        >>> map_keys({('a', 'b'): 1, ('c', 'd'): 2}, lambda x: ''.join(x))
        {'ab': 1, 'cd': 2}
    """
    return map_items(dic, func, lambda v: v)


def map_values(dic: dict[K, V], func: Callable[[V], U]) -> dict[K, U]:
    """Apply a function to the values of a dictionary.
    Args:
        dic: The dictionary to map.
        func: The function to apply to the values.
    Returns:
        A new dictionary with the same keys but with the values transformed by the function.
    Example:
        >>> from dict_zip import map_values
        >>> map_values({'a': 1, 'b': 2}, str)
        {'a': '1', 'b': '2'}
        >>> map_values({'a': 1, 'b': 2}, lambda x: x + 1)
        {'a': 2, 'b': 3}
        >>> map_values({('a', 'b'): 1, ('c', 'd'): 2}, lambda x: x * 2)
        {('a', 'b'): 2, ('c', 'd'): 4}
    """
    return map_items(dic, lambda k: k, func)


def map_items(
    dic: dict[K, V],
    key_func: Callable[[K], U],
    value_func: Callable[[V], T],
) -> dict[U, T]:
    """Apply a function to the keys and values of a dictionary.
    Args:
        dic: The dictionary to map.
        key_func: The function to apply to the keys.
        value_func: The function to apply to the values.
    Returns:
        A new dictionary with the keys and values transformed by the functions.
    Example:
        >>> from dict_zip import map_items
        >>> map_items({'a': 1, 'b': 2}, str.upper, str)
        {'A': '1', 'B': '2'}
    """
    items = [
        (original_key, key_func(original_key), value_func(value))
        for original_key, value in dic.items()
    ]
    # duplicate keys are not allowed in a dictionary
    keys = set()
    for original_key, new_key, _ in items:
        if new_key in keys:
            raise KeyError(
                f"Duplicate mapped key: {new_key} from original key: {original_key}"
            )
        keys.add(new_key)
    return {new_key: value for _, new_key, value in items}


__all__ = [
    "map_keys",
    "map_values",
    "map_items",
]
