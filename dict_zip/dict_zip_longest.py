"""Zip dictionaries by the union of their keys.

Example:
    >>> from dict_zip import dict_zip_longest
    >>> dict_zip_longest({'a': 1, 'b': 2, 'c': 4}, {'a': 3, 'b': 4})
    {'a': (1, 3), 'b': (2, 4), 'c': (4, None)}
"""

from __future__ import annotations

from collections.abc import Iterable
from itertools import chain
from typing import TypeVar, overload

_K = TypeVar("_K")
_Fill = TypeVar("_Fill")
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
def dict_zip_longest(dict1: dict[_K, _T1]) -> dict[_K, tuple[_T1 | None]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    *,
    fillvalue: _Fill | None = None,
) -> dict[_K, tuple[_T1 | _Fill]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
) -> dict[_K, tuple[_T1 | None, _T2 | None]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    *,
    fillvalue: _Fill | None = None,
) -> dict[_K, tuple[_T1 | _Fill, _T2 | _Fill]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
) -> dict[_K, tuple[_T1 | None, _T2 | None, _T3 | None]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    *,
    fillvalue: _Fill | None = None,
) -> dict[_K, tuple[_T1 | _Fill, _T2 | _Fill, _T3 | _Fill]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
) -> dict[_K, tuple[_T1 | None, _T2 | None, _T3 | None, _T4 | None]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    *,
    fillvalue: _Fill | None = None,
) -> dict[_K, tuple[_T1 | _Fill, _T2 | _Fill, _T3 | _Fill, _T4 | _Fill]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
) -> dict[
    _K,
    tuple[_T1 | None, _T2 | None, _T3 | None, _T4 | None, _T5 | None],
]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    *,
    fillvalue: _Fill | None = None,
) -> dict[
    _K,
    tuple[_T1 | _Fill, _T2 | _Fill, _T3 | _Fill, _T4 | _Fill, _T5 | _Fill],
]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
) -> dict[
    _K,
    tuple[
        _T1 | None,
        _T2 | None,
        _T3 | None,
        _T4 | None,
        _T5 | None,
        _T6 | None,
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    *,
    fillvalue: _Fill | None = None,
) -> dict[
    _K,
    tuple[
        _T1 | _Fill,
        _T2 | _Fill,
        _T3 | _Fill,
        _T4 | _Fill,
        _T5 | _Fill,
        _T6 | _Fill,
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    dict7: dict[_K, _T7],
) -> dict[
    _K,
    tuple[
        _T1 | None,
        _T2 | None,
        _T3 | None,
        _T4 | None,
        _T5 | None,
        _T6 | None,
        _T7 | None,
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    dict7: dict[_K, _T7],
    *,
    fillvalue: _Fill | None = None,
) -> dict[
    _K,
    tuple[
        _T1 | _Fill,
        _T2 | _Fill,
        _T3 | _Fill,
        _T4 | _Fill,
        _T5 | _Fill,
        _T6 | _Fill,
        _T7 | _Fill,
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    dict7: dict[_K, _T7],
    dict8: dict[_K, _T8],
) -> dict[
    _K,
    tuple[
        _T1 | None,
        _T2 | None,
        _T3 | None,
        _T4 | None,
        _T5 | None,
        _T6 | None,
        _T7 | None,
        _T8 | None,
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    dict7: dict[_K, _T7],
    dict8: dict[_K, _T8],
    *,
    fillvalue: _Fill | None = None,
) -> dict[
    _K,
    tuple[
        _T1 | _Fill,
        _T2 | _Fill,
        _T3 | _Fill,
        _T4 | _Fill,
        _T5 | _Fill,
        _T6 | _Fill,
        _T7 | _Fill,
        _T8 | _Fill,
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    dict7: dict[_K, _T7],
    dict8: dict[_K, _T8],
    dict9: dict[_K, _T9],
) -> dict[
    _K,
    tuple[
        _T1 | None,
        _T2 | None,
        _T3 | None,
        _T4 | None,
        _T5 | None,
        _T6 | None,
        _T7 | None,
        _T8 | None,
        _T9 | None,
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1],
    dict2: dict[_K, _T2],
    dict3: dict[_K, _T3],
    dict4: dict[_K, _T4],
    dict5: dict[_K, _T5],
    dict6: dict[_K, _T6],
    dict7: dict[_K, _T7],
    dict8: dict[_K, _T8],
    dict9: dict[_K, _T9],
    *,
    fillvalue: _Fill | None = None,
) -> dict[
    _K,
    tuple[
        _T1 | _Fill,
        _T2 | _Fill,
        _T3 | _Fill,
        _T4 | _Fill,
        _T5 | _Fill,
        _T6 | _Fill,
        _T7 | _Fill,
        _T8 | _Fill,
        _T9 | _Fill,
    ],
]: ...


def dict_zip_longest(*dictionaries, fillvalue=None):  # type: ignore[no-untyped-def]
    """Return a dictionary zipped by the union of keys.

    The keys are the union set of the dictionaries.
    The value is a tuple with one value from each dictionary.
    Missing keys are filled with ``fillvalue`` (default: ``None``).

    .. note::
        When dictionary values can legitimately be ``None``, the default
        ``fillvalue=None`` makes it impossible to distinguish a missing key
        from a real ``None`` value in the output tuple.  Use a sentinel
        object as ``fillvalue`` to tell them apart::

            _MISSING = object()
            result = dict_zip_longest(d1, d2, fillvalue=_MISSING)
            # value is _MISSING  →  key was absent
            # value is None      →  key was present with value None

        This matches the behaviour of :func:`itertools.zip_longest`.

    >>> dict_zip_longest({'a': 1, 'b': 2, 'c': 4}, {'a': 3, 'b': 4})
    {'a': (1, 3), 'b': (2, 4), 'c': (4, None)}
    """
    all_keys = __all_keys(d.keys() for d in dictionaries)
    return {
        key: tuple(
            dictionary.get(key, fillvalue) for dictionary in dictionaries
        )
        for key in all_keys
    }


def __all_keys(iterables: Iterable[Iterable[_K]]) -> list[_K]:
    return list(dict.fromkeys(chain.from_iterable(iterables)))


__all__ = ["dict_zip_longest"]
