from typing import Dict, Optional, Tuple, Union

from dict_zip import dict_zip, dict_zip_longest

d1: Dict[str, int] = {"a": 1, "b": 2, "c": 3}
d2: Dict[str, int] = {"a": 4, "b": 5}
d3: Dict[str, int] = {"b": 6, "c": 7}
d4: Dict[str, float] = {"b": 6.0, "c": 7.0}
d5: Dict[str, float] = {"b": 6.0, "c": 7.0, "d": 8.0}

t1 = dict_zip(d1, d2)
t1_: Dict[str, Tuple[int, int]] = t1

t2 = dict_zip(d1, d2, d3)
t2_: Dict[str, Tuple[int, int, int]] = t2

t3 = dict_zip(d3, d4)
t3_: Dict[str, Tuple[int, float]] = t3

t4 = dict_zip(d1, d2, d3, d4)
t4_: Dict[str, Tuple[int, int, int, float]] = t4

t5 = dict_zip_longest(d1, d2)
t5_: Dict[str, Tuple[Optional[int], Optional[int]]] = t5

t6 = dict_zip_longest(d1, d2, fillvalue=4)
t6_: Dict[str, Tuple[int, int]] = t6

t7 = dict_zip_longest(d1, d4)
t7_: Dict[str, Tuple[Optional[int], Optional[float]]] = t7

t8 = dict_zip_longest(d1, d4, fillvalue=4)
t8_: Dict[str, Tuple[int, Union[float, int]]] = t8

t9 = dict_zip_longest(d1, d4, fillvalue=4.0)
t9_: Dict[str, Tuple[Union[int, float], float]] = t9
