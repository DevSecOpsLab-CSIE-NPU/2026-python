"""Stage 2 - search function tests."""

import unittest

from search import binary_search, linear_search, set_search


SEARCH_FUNCTIONS = [
    ("linear_search", linear_search, lambda result: result != -1),
    ("binary_search", binary_search, lambda result: result != -1),
    ("set_search", set_search, bool),
]


class TestSearchFunctions(unittest.TestCase):
    def test_found_cases(self):
        cases = [
            ([1, 2, 2, 4], 2),
            ([7], 7),
        ]

        for function_name, search_function, normalize in SEARCH_FUNCTIONS:
            for data, target in cases:
                with self.subTest(function=function_name, data=data, target=target):
                    result = search_function(data, target)
                    self.assertTrue(normalize(result))

    def test_not_found_cases(self):
        cases = [
            ([], 1),
            ([1, 3, 5], 4),
        ]

        for function_name, search_function, normalize in SEARCH_FUNCTIONS:
            for data, target in cases:
                with self.subTest(function=function_name, data=data, target=target):
                    result = search_function(data, target)
                    self.assertFalse(normalize(result))

    def test_input_not_mutated(self):
        original = [1, 2, 3, 4]

        for function_name, search_function, _ in SEARCH_FUNCTIONS:
            with self.subTest(function=function_name):
                data = original.copy()
                search_function(data, 3)
                self.assertEqual(data, original)

    def test_binary_search_returns_minus_one_for_unsorted_data(self):
        data = [3, 1, 2]

        self.assertEqual(binary_search(data, 2), -1)
        self.assertEqual(data, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()