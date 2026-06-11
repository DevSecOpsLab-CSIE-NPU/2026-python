"""Stage 2 & 3 — 排序正確性測試（基本版 + 加速版共用同一組測試）"""
import random
import unittest

from sorts import bubble_sort, merge_sort, quick_sort
from sorts_fast import bubble_sort_fast, merge_sort_fast, quick_sort_fast

SORT_FUNCTIONS = [
    bubble_sort,
    quick_sort,
    merge_sort,
    bubble_sort_fast,
    quick_sort_fast,
    merge_sort_fast,
]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
            ([5, 4, 3, 2, 1],           [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5],           [1, 2, 3, 4, 5]),
            ([2, 2, 2, 2],              [2, 2, 2, 2]),
            ([-5, -1, -10, 0, 3, -2],   [-10, -5, -2, -1, 0, 3]),
        ]
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                for data, expected in cases:
                    self.assertEqual(fn(list(data)), expected)

    def test_random_data_matches_builtin(self):
        random.seed(42)
        data = [random.randint(-1000, 1000) for _ in range(300)]
        expected = sorted(data)
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn(list(data)), expected)

    def test_input_not_mutated(self):
        original = [5, 3, 8, 1, 9, 2, 7, 4]
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                data = original.copy()
                fn(data)
                self.assertEqual(data, original)

    def test_single_element(self):
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn([42]), [42])

    def test_empty_list(self):
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn([]), [])

    def test_duplicates(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = sorted(data)
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn(list(data)), expected)


if __name__ == "__main__":
    unittest.main()
