from __future__ import annotations

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

# type stubs for dict_zip
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

# type stubs for dict_zip_longest
@overload
def dict_zip_longest(dict1: dict[_K, _T1]) -> dict[_K, tuple[_T1 | None]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1], *, fillvalue: _Fill | None = None
) -> dict[_K, tuple[_T1 | _Fill]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1], dict2: dict[_K, _T2]
) -> dict[_K, tuple[_T1 | None, _T2 | None]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1], dict2: dict[_K, _T2], *, fillvalue: _Fill | None = None
) -> dict[_K, tuple[_T1 | _Fill, _T2 | _Fill]]: ...
@overload
def dict_zip_longest(
    dict1: dict[_K, _T1], dict2: dict[_K, _T2], dict3: dict[_K, _T3]
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
) -> dict[_K, tuple[_T1 | None, _T2 | None, _T3 | None, _T4 | None, _T5 | None]]: ...
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
    _K, tuple[_T1 | _Fill, _T2 | _Fill, _T3 | _Fill, _T4 | _Fill, _T5 | _Fill]
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
    _K, tuple[_T1 | None, _T2 | None, _T3 | None, _T4 | None, _T5 | None, _T6 | None]
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
    tuple[_T1 | _Fill, _T2 | _Fill, _T3 | _Fill, _T4 | _Fill, _T5 | _Fill, _T6 | _Fill],
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
