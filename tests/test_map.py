import pytest

from dict_zip import (
    map_keys,
    map_values,
    map_items,
)


def test_map_keys() -> None:
    d = {"a": 1, "b": 2}
    assert map_keys(d, str.upper) == {"A": 1, "B": 2}
    assert map_keys(d, lambda x: x + "!") == {"a!": 1, "b!": 2}
    assert map_keys({("a", "b"): 1, ("c", "d"): 2}, lambda x: "".join(x)) == {
        "ab": 1,
        "cd": 2,
    }

    # empty dictionary
    d2: dict[str, int] = {}
    assert map_keys(d2, str.upper) == {}
    assert map_keys(d2, lambda x: x + "!") == {}

    # duplicate keys
    with pytest.raises(KeyError):
        map_keys({"a1": 1, "a2": 2}, lambda x: x[0])


def test_map_values() -> None:
    d = {"a": 1, "b": 2}
    assert map_values(d, str) == {"a": "1", "b": "2"}
    assert map_values(d, lambda x: x + 1) == {"a": 2, "b": 3}
    assert map_values({("a", "b"): 1, ("c", "d"): 2}, lambda x: x * 2) == {
        ("a", "b"): 2,
        ("c", "d"): 4,
    }

    # empty dictionary
    d2: dict[str, int] = {}
    assert map_values(d2, str) == {}
    assert map_values(d2, lambda x: x + 1) == {}


def test_map_items() -> None:
    d = {"a": 1, "b": 2}
    assert map_items(d, str.upper, str) == {"A": "1", "B": "2"}
    assert map_items(d, lambda x: x + "!", lambda x: x * 2) == {
        "a!": 2,
        "b!": 4,
    }
    assert map_items(
        {("a", "b"): 1, ("c", "d"): 2}, lambda x: "".join(x), lambda x: x * 2
    ) == {"ab": 2, "cd": 4}

    # empty dictionary
    d2: dict[str, int] = {}
    assert map_items(d2, str.upper, str) == {}
    assert map_items(d2, lambda x: x + "!", lambda x: x * 2) == {}

    # duplicate keys
    with pytest.raises(KeyError):
        map_items({"a1": 1, "a2": 2}, lambda x: x[0], lambda x: x * 2)
