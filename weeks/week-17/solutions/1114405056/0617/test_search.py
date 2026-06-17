import unittest

from search import binary_search, linear_search


class TestSearchFunctions(unittest.TestCase):
    def test_found_items_return_index(self):
        cases = [
            ("linear", linear_search, [2, 4, 6, 8], 6, 2),
            ("binary", binary_search, [2, 4, 6, 8], 6, 2),
        ]

        for name, func, data, target, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(func(data, target), expected)

    def test_missing_items_return_minus_one(self):
        cases = [
            ("linear", linear_search, [2, 4, 6, 8], 5),
            ("binary", binary_search, [2, 4, 6, 8], 5),
            ("linear_empty", linear_search, [], 5),
            ("binary_empty", binary_search, [], 5),
        ]

        for name, func, data, target in cases:
            with self.subTest(name=name):
                self.assertEqual(func(data, target), -1)

    def test_duplicate_items_return_first_matching_index(self):
        cases = [
            ("linear", linear_search, [1, 2, 2, 2, 3], 2, 1),
            ("binary", binary_search, [1, 2, 2, 2, 3], 2, 1),
        ]

        for name, func, data, target, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(func(data, target), expected)

    def test_search_does_not_mutate_input(self):
        cases = [
            ("linear", linear_search, [3, 1, 2], 1),
            ("binary", binary_search, [1, 2, 3], 2),
        ]

        for name, func, data, target in cases:
            with self.subTest(name=name):
                original = data.copy()
                func(data, target)
                self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
