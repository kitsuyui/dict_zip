import unittest

from dict_zip import dict_zip, dict_zip_longest


class TestDictZip(unittest.TestCase):
    def test_basis(self) -> None:
        d1 = {"a": 1, "b": 2, "c": 3}
        d2 = {"a": 4, "b": 5}

        self.assertEqual(dict_zip(d1, d2), {"a": (1, 4), "b": (2, 5)})

        self.assertEqual(
            dict_zip_longest(d1, d2),
            {"a": (1, 4), "b": (2, 5), "c": (3, None)}
        )

    def test_fill_value(self) -> None:
        d1 = {"a": 1, "b": 2, "c": 3}
        d2 = {"a": 4, "b": 5}

        self.assertEqual(
            dict_zip_longest(d1, d2, fillvalue=10),
            {"a": (1, 4), "b": (2, 5), "c": (3, 10)},
        )

    def test_key_order(self) -> None:
        d1 = {"a": 1, "b": 2}
        d2 = {"b": 4, "c": 2, "a": 5}
        self.assertEqual(
            list(dict_zip(d1, d2).keys()),
            ["a", "b"],
        )
        self.assertEqual(
            list(dict_zip_longest(d1, d2).keys()),
            ["a", "b", "c"],
        )

        self.assertEqual(
            list(dict_zip(d2, d1).keys()),
            ["b", "a"],
        )
        self.assertEqual(
            list(dict_zip_longest(d2, d1).keys()),
            ["b", "c", "a"],
        )
