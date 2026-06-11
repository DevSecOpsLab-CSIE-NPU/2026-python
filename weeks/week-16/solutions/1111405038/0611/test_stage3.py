"""Stage 3 red tests — baseline + 加速版排序

目標:
1. benchmark 必須包含內建 sorted() (timsort) baseline
2. 必須有至少一個加速版排序函式,且通過正確性與不改動輸入的測試

說明:
- 本檔為 red test。若 benchmark.py / sorts_fast.py 尚未實作,測試應失敗。
"""

import unittest

from benchmark import run_benchmark
from sorts_fast import quick_sort_fast


class TestStage3Acceleration(unittest.TestCase):
    def test_fast_sort_matches_builtin(self):
        """加速版排序在一般與 edge cases 都要等同內建 sorted()。"""
        cases = [
            [],
            [1],
            [3, 1, 2],
            [5, 3, 8, 1, 9, 2, 7, 4, 6],
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
            [9, 8, 7, 6, 5, 4, 3, 2, 1],
        ]
        for data in cases:
            with self.subTest(data=data):
                self.assertEqual(quick_sort_fast(data), sorted(data))

    def test_fast_sort_does_not_mutate_input(self):
        """加速版排序必須回傳新 list,不可修改傳入資料。"""
        data = [4, 2, 7, 1, 5]
        before = data[:]
        _ = quick_sort_fast(data)
        self.assertEqual(data, before)

    def test_benchmark_includes_timsort_baseline(self):
        """run_benchmark 輸出必須包含 timsort baseline。"""
        results = run_benchmark(sizes=(50,), repeats=1)
        self.assertIn("timsort", results)
        self.assertIn(50, results["timsort"])
        self.assertIsInstance(results["timsort"][50], float)

    def test_benchmark_includes_fast_variant(self):
        """run_benchmark 輸出必須包含加速版排序欄位。"""
        results = run_benchmark(sizes=(50,), repeats=1)
        self.assertIn("quick_sort_fast", results)
        self.assertIn(50, results["quick_sort_fast"])
        self.assertIsInstance(results["quick_sort_fast"][50], float)


if __name__ == "__main__":
    unittest.main()
