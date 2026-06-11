"""Stage 2 — 排序正確性測試（共用測試集）"""

import unittest
from sorts import bubble_sort, quick_sort, merge_sort
from sorts_fast import (
    bubble_sort_opt,
    quick_sort_opt,
    merge_sort_opt,
)

SORT_FUNCTIONS = [
    bubble_sort,
    quick_sort,
    merge_sort,
    bubble_sort_opt,
    quick_sort_opt,
    merge_sort_opt,
]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                self.assertEqual(sort_fn([3, 1, 2]), [1, 2, 3])
                self.assertEqual(sort_fn([1]), [1])
                self.assertEqual(sort_fn([]), [])

    def test_duplicates(self):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                self.assertEqual(sort_fn([4, 2, 4, 1, 2]), [1, 2, 2, 4, 4])

    def test_already_sorted(self):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                self.assertEqual(sort_fn([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                self.assertEqual(sort_fn([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_data_matches_builtin(self):
        import random

        random.seed(42)
        data = [random.randint(0, 1000) for _ in range(100)]
        expected = sorted(data)
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                self.assertEqual(sort_fn(data), expected)

    def test_input_not_mutated(self):
        original = [3, 1, 4, 1, 5]
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                data_copy = original[:]
                sort_fn(data_copy)
                self.assertEqual(data_copy, original)

    def test_negative_numbers(self):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                self.assertEqual(sort_fn([-3, 0, -1, 2]), [-3, -1, 0, 2])


if __name__ == "__main__":
    unittest.main()
