"""Stage 2 — 三種搜尋正確性測試"""

import unittest
import copy

from search import linear_search, binary_search, set_search

SEARCH_FUNCTIONS = [linear_search, binary_search, set_search]


def _found(result):
    if isinstance(result, bool):
        return result
    return result >= 0


class TestSearchFunctions(unittest.TestCase):

    def test_found_cases(self):
        cases = [
            ([1, 3, 5, 7, 9], 5),
            ([1, 3, 5, 7, 9], 1),
            ([1, 3, 5, 7, 9], 9),
            ([1, 1, 2, 3], 1),
            ([42], 42),
        ]
        for data, target in cases:
            for func in SEARCH_FUNCTIONS:
                with self.subTest(func=func.__name__, data=data, target=target):
                    result = func(data, target)
                    self.assertTrue(_found(result))

    def test_not_found_cases(self):
        cases = [
            ([1, 3, 5, 7, 9], 4),
            ([], 42),
            ([1, 3, 5], 0),
            ([1, 3, 5], 10),
            ([42], 99),
        ]
        for data, target in cases:
            for func in SEARCH_FUNCTIONS:
                with self.subTest(func=func.__name__, data=data, target=target):
                    result = func(data, target)
                    self.assertFalse(_found(result))

    def test_linear_search_exact_index(self):
        data = [10, 20, 30, 40]
        self.assertEqual(linear_search(data, 10), 0)
        self.assertEqual(linear_search(data, 30), 2)
        self.assertEqual(linear_search(data, 40), 3)
        self.assertEqual(linear_search(data, 99), -1)

    def test_binary_search_exact_index(self):
        data = [10, 20, 30, 40]
        self.assertEqual(binary_search(data, 10), 0)
        self.assertEqual(binary_search(data, 30), 2)
        self.assertEqual(binary_search(data, 40), 3)
        self.assertEqual(binary_search(data, 99), -1)

    def test_input_not_mutated(self):
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                original = [3, 1, 4, 1, 5]
                expected = copy.deepcopy(original)
                func(original, 4)
                self.assertEqual(original, expected)

    def test_none_input_raises_typeerror(self):
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__, case="data is None"):
                with self.assertRaises(TypeError):
                    func(None, 42)
            with self.subTest(func=func.__name__, case="target is None"):
                with self.assertRaises(TypeError):
                    func([1, 2, 3], None)


if __name__ == "__main__":
    unittest.main()
