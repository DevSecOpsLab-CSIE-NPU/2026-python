"""Stage 3 — 加速版排序共用正確性測試"""

import unittest
import random

from sorts_fast import quick_sort_fast


class TestSortsFast(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            ([], []),
            ([5], [5]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([4, 2, 2, 5], [2, 2, 4, 5]),
        ]
        for data, expected in cases:
            with self.subTest(data=data):
                result = quick_sort_fast(data)
                self.assertEqual(result, expected)

    def test_random_data_matches_builtin(self):
        random.seed(123)
        for n in [10, 50, 200]:
            data = [random.randint(-10000, 10000) for _ in range(n)]
            with self.subTest(n=n):
                self.assertEqual(quick_sort_fast(data), sorted(data))

    def test_input_not_mutated(self):
        original = [5, 3, 8, 1, 9, 2]
        data = list(original)
        quick_sort_fast(data)
        self.assertEqual(data, original)

    def test_edge_case_duplicates_and_sorted(self):
        data = [7, 7, 7, 7]
        self.assertEqual(quick_sort_fast(data), [7, 7, 7, 7])
        data2 = [1, 2, 3, 4, 5]
        self.assertEqual(quick_sort_fast(data2), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
