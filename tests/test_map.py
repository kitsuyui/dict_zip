from typing import Any, cast

import pytest

from dict_zip import (
    map_items,
    map_keys,
    map_values,
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
    with pytest.raises(ValueError, match="Duplicate mapped key: a"):
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
        {("a", "b"): 1, ("c", "d"): 2},
        lambda x: "".join(x),
        lambda x: x * 2,
    ) == {"ab": 2, "cd": 4}

    # empty dictionary
    d2: dict[str, int] = {}
    assert map_items(d2, str.upper, str) == {}
    assert map_items(d2, lambda x: x + "!", lambda x: x * 2) == {}

    # duplicate keys
    with pytest.raises(ValueError, match="Duplicate mapped key: a"):
        map_items({"a1": 1, "a2": 2}, lambda x: x[0], lambda x: x * 2)


def test_map_items_accepts_func_alias_for_key_func() -> None:
    d = {"a": 1, "b": 2}

    assert map_items(d, func=str.upper, value_func=str) == {
        "A": "1",
        "B": "2",
    }


def test_map_items_value_func_annotation_hides_internal_sentinel() -> None:
    assert "object" not in map_items.__annotations__["value_func"]


def test_map_items_rejects_ambiguous_key_function_alias() -> None:
    d = {"a": 1, "b": 2}
    unchecked_map_items = cast(Any, map_items)

    with pytest.raises(TypeError, match="both 'key_func' and 'func'"):
        unchecked_map_items(d, str.upper, str, func=str.lower)


def test_map_items_rejects_missing_key_function() -> None:
    d = {"a": 1, "b": 2}
    unchecked_map_items = cast(Any, map_items)

    with pytest.raises(
        TypeError,
        match="missing required argument: 'key_func'",
    ):
        unchecked_map_items(d, value_func=str)


def test_map_items_duplicate_key_error_includes_both_original_keys() -> None:
    with pytest.raises(ValueError, match=r"'a1'.*'a2'|'a2'.*'a1'"):
        map_keys({"a1": 1, "a2": 2}, lambda x: x[0])


def test_map_items_checks_duplicate_keys_before_mapping_values() -> None:
    mapped_values: list[int] = []

    def map_value(value: int) -> int:
        mapped_values.append(value)
        return value * 2

    with pytest.raises(ValueError, match="Duplicate mapped key: a"):
        map_items({"a1": 1, "a2": 2}, lambda key: key[0], map_value)

    assert mapped_values == [1]
