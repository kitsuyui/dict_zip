from dict_zip import tuple_keys


def test_tuple_keys() -> None:
    d = {"a": 1, "b": 2}
    assert tuple_keys(d) == {("a",): 1, ("b",): 2}
