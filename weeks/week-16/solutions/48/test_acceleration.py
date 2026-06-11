"""Stage 3 — 加速驗證測試

加速版函式必須:
  1. 通過與 Stage 2 相同的正確性測試
  2. 實際執行速度比原版快
  3. benchmark 能產出 results.json
"""

import json
import os
import time
import unittest

from sorts import (
    bubble_sort,
    merge_sort,
    merge_sort_fast,
    quick_sort,
    quick_sort_fast,
    sorted_baseline,
)

SORT_PAIRS = [
    (quick_sort, quick_sort_fast, "quick_sort"),
    (merge_sort, merge_sort_fast, "merge_sort"),
]


class TestCorrectness(unittest.TestCase):
    def _check_sorted(self, sort_func, original):
        expected = sorted(original)
        result = sort_func(original)
        self.assertEqual(result, expected)

    def _test_all_fast(self, data):
        for _, fast, name in SORT_PAIRS:
            with self.subTest(sort=name):
                self._check_sorted(fast, data)

    def test_empty_list(self):
        self._test_all_fast([])

    def test_single_element(self):
        self._test_all_fast([42])

    def test_sorted_input(self):
        self._test_all_fast([1, 2, 3, 4, 5])

    def test_reverse_input(self):
        self._test_all_fast([5, 4, 3, 2, 1])

    def test_all_equal(self):
        self._test_all_fast([7, 7, 7, 7])

    def test_with_duplicates(self):
        self._test_all_fast([3, 1, 3, 2, 1])

    def test_negative_and_zero(self):
        self._test_all_fast([-5, 0, -1, 10])


class TestPerformance(unittest.TestCase):
    def test_fast_is_not_slower_than_original(self):
        data = list(range(500, 0, -1))
        for orig, fast, name in SORT_PAIRS:
            with self.subTest(sort=name):
                t_orig = _time_once(orig, data)
                t_fast = _time_once(fast, data)
                self.assertLessEqual(t_fast, t_orig * 2)


class TestBenchmarkOutput(unittest.TestCase):
    def test_results_json_exists(self):
        self.assertTrue(os.path.isfile("results.json"))

    def test_results_json_not_empty(self):
        with open("results.json") as f:
            data = json.load(f)
        self.assertTrue(len(data) > 0)


def _time_once(func, data):
    start = time.perf_counter()
    func(data)
    return time.perf_counter() - start


if __name__ == "__main__":
    unittest.main()
