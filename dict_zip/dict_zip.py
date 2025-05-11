"""
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
def dict_zip(dict1: dict[_K, _T1]) -> dict[_K, tuple[_T1]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1], dict2: dict[_K, _T2]
) -> dict[_K, tuple[_T1, _T2]]: ...
@overload
def dict_zip(
    dict1: dict[_K, _T1], dict2: dict[_K, _T2], dict3: dict[_K, _T3]
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
    """Returns a new dictionary \
concatenated with the dictionaries specified in the argument.

    The key is a common key that each dictionary has.
    The value is a tuple of the values of the dictionaries.

    >>> dict_zip({'a': 1, 'b': 2}, {'a': 3, 'b': 4})
    {'a': (1, 3), 'b': (2, 4)}
    """
    common_keys = functools.reduce(
        lambda x, y: x & y, (set(d.keys()) for d in dictionaries)
    )
    return_dic = {}  # type: ignore[var-annotated]
    for dic in dictionaries:
        for key, val in dic.items():
            if key in common_keys:
                return_dic.setdefault(key, []).append(val)

    return {key: tuple(val) for key, val in return_dic.items()}


__all__ = ["dict_zip"]
