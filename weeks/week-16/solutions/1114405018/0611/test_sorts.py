"""Stage 2 — 排序正確性測試"""

import unittest
import random

from sorts import bubble_sort, quick_sort, merge_sort
from sorts_fast import quick_sort_fast

SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort, quick_sort_fast]


class TestSortFunctions(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SORT_FUNCTIONS, "SORT_FUNCTIONS 為空 — 請先解除 import 註解")

    def test_basic_cases(self):
        cases = [
            ([], []),
            ([5], [5]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([4, 2, 2, 5], [2, 2, 4, 5]),
            ([9, 9, 9], [9, 9, 9]),
        ]
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                for data, expected in cases:
                    with self.subTest(data=data):
                        result = sort_func(data)
                        self.assertEqual(result, expected)

    def test_random_data_matches_builtin(self):
        random.seed(42)
        datas = [
            [random.randint(-1000, 1000) for _ in range(50)],
            [random.randint(-1000, 1000) for _ in range(100)],
        ]
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                for data in datas:
                    with self.subTest(n=len(data)):
                        expected = sorted(data)
                        result = sort_func(data)
                        self.assertEqual(result, expected)

    def test_input_not_mutated(self):
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                original = [3, 1, 4, 1, 5, 9, 2, 6]
                data = list(original)
                sort_func(data)
                self.assertEqual(data, original)

    def test_edge_case_large_values(self):
        data = [2000000000, 1, 999999999]
        expected = [1, 999999999, 2000000000]
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                result = sort_func(data)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
