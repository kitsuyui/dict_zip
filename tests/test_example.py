import pytest


def test_addition():
    assert 1 + 1 == 2, "1 + 1 == 2 is always true"


def test_exception():
    with pytest.raises(ValueError):
        raise ValueError('Hello Error!')
