from typing import Any, Dict, Optional, overload, Tuple, TypeVar, Union

K = TypeVar("K")
Fill = TypeVar("Fill")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
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
def dict_zip_longest(
    dict1: Dict[K, _T1], fillvalue: Optional[Fill] = None
) -> Dict[K, Tuple[Union[_T1, Optional[Fill]]]]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1], dict2: Dict[K, _T2], fillvalue: Optional[Fill] = None
) -> Dict[K, Tuple[Union[_T1, Optional[Fill]], Union[_T2, Optional[Fill]]]]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    fillvalue: Optional[Fill] = None,
) -> Dict[
    K,
    Tuple[
        Union[_T1, Optional[Fill]],
        Union[_T2, Optional[Fill]],
        Union[_T3, Optional[Fill]],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    fillvalue: Optional[Fill] = None,
) -> Dict[
    K,
    Tuple[
        Union[_T1, Optional[Fill]],
        Union[_T2, Optional[Fill]],
        Union[_T3, Optional[Fill]],
        Union[_T4, Optional[Fill]],
    ],
]: ...
@overload
def dict_zip_longest(
    dict1: Dict[K, _T1],
    dict2: Dict[K, _T2],
    dict3: Dict[K, _T3],
    dict4: Dict[K, _T4],
    dict5: Dict[K, _T5],
    fillvalue: Optional[Fill] = None,
) -> Dict[
    K,
    Tuple[
        Union[_T1, Optional[Fill]],
        Union[_T2, Optional[Fill]],
        Union[_T3, Optional[Fill]],
        Union[_T4, Optional[Fill]],
        Union[_T5, Optional[Fill]],
    ],
]: ...
