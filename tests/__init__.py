import unittest

from dict_zip import dict_zip, dict_zip_longest


class TestDictZip(unittest.TestCase):

    def test_basis(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': 4, 'b': 5}

        self.assertEqual(dict(dict_zip(d1, d2)),
                         {'a': (1, 4), 'b': (2, 5)})

        self.assertEqual(dict(dict_zip_longest(d1, d2)),
                         {'a': (1, 4), 'b': (2, 5), 'c': (3, None)})
