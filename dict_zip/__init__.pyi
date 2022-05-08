from typing import Any, Dict, Optional, Tuple, TypeVar, Union, overload

K = TypeVar("K")
Fill = TypeVar("Fill")
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
def dict_zip(dict1: Dict[K, _T1]) -> Dict[K, Tuple[_T1]]: ...
@overload
def dict_zip(dict1: Dict[K, _T1], dict2: Dict[K, _T2]) -> Dict[K, Tuple[_T1, _T2]]: ...
@overload
def dict_zip(
    dict1: Dict[K, _T1], dict2: Dict[K, _T2], dict3: Dict[K, _T3]
) -> Dict[K, Tuple[_T1, _T2, _T3]]: ...
@overload
def dict_zip(
    dict1: Dict[K, _T1], dict2: Dict[K, _T2], dict3: Dict[K, _T3], dict4: Dict[K, _T4]
) -> Dict[K, Tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def dict_zip(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
) -> Dict[K, Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def dict_zip(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
) -> Dict[K, Tuple[_T1, _T2, _T3, _T4, _T5, _T6]]: ...
@overload
def dict_zip(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    dict7: Dict[K, _T7],
) -> Dict[K, Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7]]: ...
@overload
def dict_zip(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    dict7: Dict[K, _T7],
    dict8: Dict[K, _T8],
) -> Dict[K, Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]]: ...
@overload
def dict_zip(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    dict7: Dict[K, _T7],
    dict8: Dict[K, _T8],
    dict9: Dict[K, _T9],
) -> Dict[K, Tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]]: ...

# type stubs for dict_zip_longest
@overload
def dict_zip_longest(dict1: Dict[K, _T1]) -> Dict[K, Tuple[Optional[_T1]]]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1], *, fillvalue: Fill = ...
) -> Dict[K, Tuple[Union[_T1, Fill]]]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1], dict2: Dict[K, _T2]
) -> Dict[K, Tuple[Optional[_T1], Optional[_T2]]]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1], dict2: Dict[K, _T2], *, fillvalue: Fill = ...
) -> Dict[K, Tuple[Union[_T1, Fill], Union[_T2, Fill]]]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1], dict2: Dict[K, _T2], dict3: Dict[K, _T3]
) -> Dict[K, Tuple[Optional[_T1], Optional[_T2], Optional[_T3]]]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    *,
    fillvalue: Fill = ...
) -> Dict[K, Tuple[Union[_T1, Fill], Union[_T2, Fill], Union[_T3, Fill]]]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1], dict2: Dict[K, _T2], dict3: Dict[K, _T3], dict4: Dict[K, _T4]
) -> Dict[K, Tuple[Optional[_T1], Optional[_T2], Optional[_T3], Optional[_T4]]]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    *,
    fillvalue: Fill = ...
) -> Dict[
    K, Tuple[Union[_T1, Fill], Union[_T2, Fill], Union[_T3, Fill], Union[_T4, Fill]]
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
) -> Dict[
    K, Tuple[Optional[_T1], Optional[_T2], Optional[_T3], Optional[_T4], Optional[_T5]]
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    *,
    fillvalue: Fill = ...
) -> Dict[
    K,
    Tuple[
        Union[_T1, Fill],
        Union[_T2, Fill],
        Union[_T3, Fill],
        Union[_T4, Fill],
        Union[_T5, Fill],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
) -> Dict[
    K,
    Tuple[
        Optional[_T1],
        Optional[_T2],
        Optional[_T3],
        Optional[_T4],
        Optional[_T5],
        Optional[_T6],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    *,
    fillvalue: Fill = ...
) -> Dict[
    K,
    Tuple[
        Union[_T1, Fill],
        Union[_T2, Fill],
        Union[_T3, Fill],
        Union[_T4, Fill],
        Union[_T5, Fill],
        Union[_T6, Fill],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    dict7: Dict[K, _T7],
) -> Dict[
    K,
    Tuple[
        Optional[_T1],
        Optional[_T2],
        Optional[_T3],
        Optional[_T4],
        Optional[_T5],
        Optional[_T6],
        Optional[_T7],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    dict7: Dict[K, _T7],
    *,
    fillvalue: Fill = ...
) -> Dict[
    K,
    Tuple[
        Union[_T1, Fill],
        Union[_T2, Fill],
        Union[_T3, Fill],
        Union[_T4, Fill],
        Union[_T5, Fill],
        Union[_T6, Fill],
        Union[_T7, Fill],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    dict7: Dict[K, _T7],
    dict8: Dict[K, _T8],
) -> Dict[
    K,
    Tuple[
        Optional[_T1],
        Optional[_T2],
        Optional[_T3],
        Optional[_T4],
        Optional[_T5],
        Optional[_T6],
        Optional[_T7],
        Optional[_T8],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    dict7: Dict[K, _T7],
    dict8: Dict[K, _T8],
    *,
    fillvalue: Fill = ...
) -> Dict[
    K,
    Tuple[
        Union[_T1, Fill],
        Union[_T2, Fill],
        Union[_T3, Fill],
        Union[_T4, Fill],
        Union[_T5, Fill],
        Union[_T6, Fill],
        Union[_T7, Fill],
        Union[_T8, Fill],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    dict7: Dict[K, _T7],
    dict8: Dict[K, _T8],
    dict9: Dict[K, _T9],
) -> Dict[
    K,
    Tuple[
        Optional[_T1],
        Optional[_T2],
        Optional[_T3],
        Optional[_T4],
        Optional[_T5],
        Optional[_T6],
        Optional[_T7],
        Optional[_T8],
        Optional[_T9],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    dict6: Dict[K, _T6],
    dict7: Dict[K, _T7],
    dict8: Dict[K, _T8],
    dict9: Dict[K, _T9],
    *,
    fillvalue: Fill = ...
) -> Dict[
    K,
    Tuple[
        Union[_T1, Fill],
        Union[_T2, Fill],
        Union[_T3, Fill],
        Union[_T4, Fill],
        Union[_T5, Fill],
        Union[_T6, Fill],
        Union[_T7, Fill],
        Union[_T8, Fill],
        Union[_T9, Fill],
    ],
]: ...
