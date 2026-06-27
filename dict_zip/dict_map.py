"""Helpers for transforming dictionary keys and values."""

from __future__ import annotations

from collections.abc import Callable
from typing import NoReturn, TypeVar, cast, overload

K = TypeVar("K")
V = TypeVar("V")
U = TypeVar("U")
T = TypeVar("T")


_MISSING = object()
_MISSING_VALUE_FUNC = cast("Callable[[object], NoReturn]", _MISSING)


def _require_callable(mapper: object, argument_name: str) -> None:
    if not callable(mapper):
        raise TypeError(
            f"map_items() argument '{argument_name}' must be callable",
        )


def _resolve_key_mapper(
    key_func: Callable[[K], U] | None,
    func: Callable[[K], U] | None,
) -> Callable[[K], U]:
    mappers = tuple(
        (argument_name, mapper)
        for argument_name, mapper in (("key_func", key_func), ("func", func))
        if mapper is not None
    )
    if len(mappers) == 1:
        argument_name, mapper = mappers[0]
        _require_callable(mapper, argument_name)
        return mapper
    raise TypeError(
        "map_items() missing required argument: 'key_func'"
        if not mappers
        else "map_items() got both 'key_func' and 'func'",
    )


def _resolve_value_mapper(
    value_func: Callable[[V], T],
) -> Callable[[V], T]:
    if value_func is _MISSING:
        raise TypeError("map_items() missing required argument: 'value_func'")
    _require_callable(value_func, "value_func")
    return value_func


def map_keys(dic: dict[K, V], func: Callable[[K], U]) -> dict[U, V]:
    """Apply a function to the keys of a dictionary.

    Args:
        dic: The dictionary to map.
        func: The function to apply to the keys.

    Returns:
        A new dictionary with the same values and transformed keys.

    Raises:
        ValueError: If two different keys in ``dic`` are mapped to the same key
            by ``func``.

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
        A new dictionary with the same keys and transformed values.

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


@overload
def map_items(
    dic: dict[K, V],
    key_func: Callable[[K], U],
    value_func: Callable[[V], T],
) -> dict[U, T]: ...


@overload
def map_items(
    dic: dict[K, V],
    key_func: None = None,
    value_func: Callable[[V], T] = ...,
    *,
    func: Callable[[K], U],
) -> dict[U, T]: ...


def map_items(
    dic: dict[K, V],
    key_func: Callable[[K], U] | None = None,
    value_func: Callable[[V], T] = _MISSING_VALUE_FUNC,
    *,
    func: Callable[[K], U] | None = None,
) -> dict[U, T]:
    """Apply a function to the keys and values of a dictionary.

    Args:
        dic: The dictionary to map.
        key_func: The function to apply to the keys. Prefer this positional
            argument for new code.
        value_func: The function to apply to the values.
        func: Backward-compatible keyword-only alias for ``key_func``.

    Returns:
        A new dictionary with the keys and values transformed by the functions.

    Raises:
        ValueError: If ``key_func`` maps two different keys in ``dic`` to the
            same key.
        TypeError: If a mapper is missing, ambiguous, or not callable.

    Example:
        >>> from dict_zip import map_items
        >>> map_items({'a': 1, 'b': 2}, str.upper, str)
        {'A': '1', 'B': '2'}
        >>> map_items({'a': 1, 'b': 2}, func=str.upper, value_func=str)
        {'A': '1', 'B': '2'}
    """
    key_mapper = _resolve_key_mapper(key_func, func)
    value_mapper: Callable[[V], T] = _resolve_value_mapper(value_func)
    key_origins: dict[U, K] = {}
    result: dict[U, T] = {}
    for original_key, value in dic.items():
        new_key = key_mapper(original_key)
        if new_key in key_origins:
            first_key = key_origins[new_key]
            raise ValueError(
                f"Duplicate mapped key: {new_key}"
                f" from original keys: {first_key!r}"
                f" and {original_key!r}",
            )
        key_origins[new_key] = original_key
        result[new_key] = value_mapper(value)
    return result


__all__ = [
    "map_items",
    "map_keys",
    "map_values",
]
