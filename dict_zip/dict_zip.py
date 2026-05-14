"""Zip dictionaries by their shared keys.

Example:
    >>> from dict_zip import dict_zip
    >>> dict_zip({'a': 1, 'b': 2}, {'a': 3, 'b': 4})
    {'a': (1, 3), 'b': (2, 4)}
"""

from __future__ import annotations

import functools
from typing import TypeVar, overload

_K = TypeVar("_K")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_T6 = TypeVar("_T6")
_T7 = TypeVar("_T7")
_T8 = TypeVar("_T8")
_T9 = TypeVar("_T9")


@overload
def dict_zip() -> dict[object, tuple[()]]: ...
@overload
def dict_zip(dict1: dict[_K, _T1]) -> dict[_K, tuple[_T1]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
) -> dict[_K, tuple[_T1, _T2]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
) -> dict[_K, tuple[_T1, _T2, _T3]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
) -> dict[_K, tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
) -> dict[_K, tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
) -> dict[_K, tuple[_T1, _T2, _T3, _T4, _T5, _T6]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    dict7: dict[_K, _T7],
) -> dict[_K, tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    dict7: dict[_K, _T7],
    dict8: dict[_K, _T8],
) -> dict[_K, tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    dict7: dict[_K, _T7],
    dict8: dict[_K, _T8],
    dict9: dict[_K, _T9],
) -> dict[_K, tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]]: ...


def dict_zip(*dictionaries):  # type: ignore[no-untyped-def]
    """Return a dictionary zipped by the common keys.

    The key is a common key shared by every dictionary.
    The value is a tuple with one value from each dictionary.

    >>> dict_zip({'a': 1, 'b': 2}, {'a': 3, 'b': 4})
    {'a': (1, 3), 'b': (2, 4)}
    """
    if not dictionaries:
        return {}

    common_keys = functools.reduce(
        lambda x, y: x & y,
        (set(d.keys()) for d in dictionaries),
    )
    ordered_common_keys = [
        key for key in dictionaries[0] if key in common_keys
    ]
    return {
        key: tuple(dictionary[key] for dictionary in dictionaries)
        for key in ordered_common_keys
    }


__all__ = ["dict_zip"]
