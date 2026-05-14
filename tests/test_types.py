from dict_zip import dict_zip, dict_zip_longest

d1: dict[str, int] = {"a": 1, "b": 2, "c": 3}
d2: dict[str, int] = {"a": 4, "b": 5}
d3: dict[str, int] = {"b": 6, "c": 7}
d4: dict[str, float] = {"b": 6.0, "c": 7.0}
d5: dict[str, float] = {"b": 6.0, "c": 7.0, "d": 8.0}

t1 = dict_zip(d1, d2)
t1_: dict[str, tuple[int, int]] = t1

t2 = dict_zip(d1, d2, d3)
t2_: dict[str, tuple[int, int, int]] = t2

t3 = dict_zip(d3, d4)
t3_: dict[str, tuple[int, float]] = t3

t4 = dict_zip(d1, d2, d3, d4)
t4_: dict[str, tuple[int, int, int, float]] = t4

t5 = dict_zip_longest(d1, d2)
t5_: dict[str, tuple[int | None, int | None]] = t5

t6 = dict_zip_longest(d1, d2, fillvalue=4)
t6_: dict[str, tuple[int, int]] = t6

t7 = dict_zip_longest(d1, d4)
t7_: dict[str, tuple[int | None, float | None]] = t7

t8 = dict_zip_longest(d1, d4, fillvalue=4)
t8_: dict[str, tuple[int, float | int]] = t8

t9 = dict_zip_longest(d1, d4, fillvalue=4.0)
t9_: dict[str, tuple[int | float, float]] = t9
