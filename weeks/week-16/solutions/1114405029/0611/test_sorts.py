"""Stage 2 tests for sorting functions.

These tests are written before sorts.py exists, so the first run should be red.
The three sorting functions must share the same behavior contract.
"""

import builtins
import random
import unittest

from sorts import (
    bubble_sort,
    merge_sort,
    optimized_bubble_sort,
    optimized_quick_sort,
    quick_sort,
)


SORT_FUNCTIONS = [
    bubble_sort,
    quick_sort,
    merge_sort,
    optimized_bubble_sort,
    optimized_quick_sort,
]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            [3, 1, 2],
            [5, -1, 0, 5, 3],
            [1, 1, 1],
        ]

        for sort_func in SORT_FUNCTIONS:
            for data in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
                    self.assertEqual(sort_func(data), sorted(data))

    def test_edge_cases(self):
        cases = [
            [],
            [42],
            [-3, -10, -1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
        ]

        for sort_func in SORT_FUNCTIONS:
            for data in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
                    self.assertEqual(sort_func(data), sorted(data))

    def test_random_data_matches_builtin(self):
        rng = random.Random(42)
        cases = [[rng.randint(-100, 100) for _ in range(30)] for _ in range(5)]

        for sort_func in SORT_FUNCTIONS:
            for data in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
                    self.assertEqual(sort_func(data), sorted(data))

    def test_input_not_mutated_and_returns_new_list(self):
        for sort_func in SORT_FUNCTIONS:
            data = [3, 1, 2, 1]
            original = data[:]

            with self.subTest(sort_func=sort_func.__name__):
                result = sort_func(data)
                self.assertEqual(data, original)
                self.assertEqual(result, [1, 1, 2, 3])
                self.assertIsNot(result, data)

    def test_does_not_use_builtin_sorting_helpers(self):
        original_sorted = builtins.sorted
        original_list_sort = list.sort

        def blocked_sorted(*args, **kwargs):
            raise AssertionError("sorted() is not allowed in Stage 2")

        builtins.sorted = blocked_sorted
        try:
            for sort_func in SORT_FUNCTIONS:
                with self.subTest(sort_func=sort_func.__name__):
                    self.assertEqual(sort_func([3, 2, 1]), [1, 2, 3])
        finally:
            builtins.sorted = original_sorted
            self.assertIs(list.sort, original_list_sort)


if __name__ == "__main__":
    unittest.main()
