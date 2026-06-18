import unittest
from search import linear_search, binary_search, set_search


def _found(result):
    if isinstance(result, bool):
        return result
    return result >= 0


def _not_found(result):
    if isinstance(result, bool):
        return not result
    return result == -1


SEARCH_FUNCTIONS = [
    ("linear", linear_search),
    ("binary", binary_search),
    ("set", set_search),
]


class TestSearchFunctions(unittest.TestCase):

    def test_found_cases(self):
        data = [1, 3, 4, 7, 9]
        for name, func in SEARCH_FUNCTIONS:
            with self.subTest(func=name):
                result = func(data, 7)
                self.assertTrue(_found(result))

    def test_not_found_cases(self):
        data = [1, 3, 4, 7, 9]
        for name, func in SEARCH_FUNCTIONS:
            with self.subTest(func=name):
                result = func(data, 5)
                self.assertTrue(_not_found(result))

    def test_empty_list(self):
        for name, func in SEARCH_FUNCTIONS:
            with self.subTest(func=name):
                result = func([], 1)
                self.assertTrue(_not_found(result))

    def test_input_not_mutated(self):
        data = [3, 7, 1, 9, 4]
        original = data.copy()
        for name, func in SEARCH_FUNCTIONS:
            with self.subTest(func=name):
                func(data, 9)
                self.assertEqual(data, original)

    def test_duplicate_values(self):
        data = [1, 3, 3, 3, 7]
        for name, func in SEARCH_FUNCTIONS:
            with self.subTest(func=name):
                result = func(data, 3)
                self.assertTrue(_found(result))

    def test_binary_unsorted_returns_minus1(self):
        data = [1, 3, 7, 9, 4]
        result = binary_search(data, 4)
        self.assertEqual(result, -1)
