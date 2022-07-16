from dict_zip import dict_zip, dict_zip_longest


def test_basis() -> None:
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"a": 4, "b": 5}

    assert dict_zip(d1, d2) == {"a": (1, 4), "b": (2, 5)}
    assert dict_zip_longest(d1, d2) == {
        "a": (1, 4),
        "b": (2, 5),
        "c": (3, None),
    }


def test_fill_value() -> None:
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"a": 4, "b": 5}

    assert dict_zip_longest(d1, d2, fillvalue=10) == {
        "a": (1, 4),
        "b": (2, 5),
        "c": (3, 10),
    }


def test_key_order() -> None:
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 4, "c": 2, "a": 5}

    assert list(dict_zip(d1, d2).keys()) == ["a", "b"]
    assert list(dict_zip_longest(d1, d2).keys()) == ["a", "b", "c"]
    assert list(dict_zip(d2, d1).keys()) == ["b", "a"]
    assert list(dict_zip_longest(d2, d1).keys()) == ["b", "c", "a"]
