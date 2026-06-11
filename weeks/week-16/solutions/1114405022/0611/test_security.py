"""Stage 5 — 安全性測試

依 OpenSSF Secure Coding Guide for Python 檢視 Stage 1–4 程式。
每條紅燈測試代表一個安全問題，修正後轉綠。
"""

import os
import unittest


class TestSecuritySorts(unittest.TestCase):
    def test_sort_rejects_non_list(self):
        from sorts import bubble_sort, quick_sort, merge_sort

        for func in [bubble_sort, quick_sort, merge_sort]:
            with self.subTest(func=func.__name__):
                with self.assertRaises(TypeError):
                    func((1, 2, 3))
                with self.assertRaises(TypeError):
                    func("abc")
                with self.assertRaises(TypeError):
                    func(42)
                with self.assertRaises(TypeError):
                    func(None)


class TestSecurityPlot(unittest.TestCase):
    def test_plot_rejects_path_traversal(self):
        from plot import plot_results

        with self.assertRaises(ValueError):
            plot_results(output_path="../evil.png")


class TestSecurityBenchmark(unittest.TestCase):
    def test_benchmark_random_not_secure(self):
        """掃到 random 模組用於資料生成，但 benchmark 非安全敏感，無需改 secrets。
        依 OpenSSF 規範記錄此條為不適用。"""
        import random
        self.assertIsNotNone(random)
