"""Stage 2 — 排序正確性測試

規格:sorts.py 的 bubble_sort / quick_sort / merge_sort 必須
   1. 回傳新的排序後 list,不可修改傳入的 list
   2. 禁用內建 sorted() / list.sort()
"""

import unittest

from sorts import bubble_sort, quick_sort, merge_sort

SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    def _assert_sort_functions_defined(self):
        self.assertGreater(len(SORT_FUNCTIONS), 0, "No sort functions defined")

    def test_basic_cases(self):
        self._assert_sort_functions_defined()
        cases = [
            ([], []),
            ([5], [5]),
            ([1, 2, 3, 4], [1, 2, 3, 4]),
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),
            ([0, -1, -5, 3], [-5, -1, 0, 3]),
            ([1.5, 0.5, 2.0], [0.5, 1.5, 2.0]),
            (["b", "a", "c"], ["a", "b", "c"]),
        ]
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(func=sort_func.__name__):
                for data, expected in cases:
                    result = sort_func(data[:])
                    self.assertEqual(result, expected)

    def test_random_data_matches_builtin(self):
        self._assert_sort_functions_defined()
        import random

        random.seed(42)
        for _ in range(5):
            data = random.sample(range(-1000, 1000), 100)
            for sort_func in SORT_FUNCTIONS:
                with self.subTest(func=sort_func.__name__):
                    result = sort_func(data[:])
                    self.assertEqual(result, sorted(data))

    def test_input_not_mutated(self):
        self._assert_sort_functions_defined()
        data = [3, 1, 4, 1, 5]
        original = data[:]
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(func=sort_func.__name__):
                sort_func(data)
                self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
