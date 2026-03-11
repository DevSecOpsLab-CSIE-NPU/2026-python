"""
UVA 100 測試。
"""

from __future__ import annotations

import unittest

from question_100 import collatz_cycle_length, max_cycle_length, solve


class TestCycleLength(unittest.TestCase):
    """cycle length 單元測試。"""

    def test_cycle_length_22(self) -> None:
        """驗證 22 的 cycle length 為 16。"""
        cache = {1: 1}
        self.assertEqual(collatz_cycle_length(22, cache), 16)

    def test_cycle_length_1(self) -> None:
        """驗證基底值 1。"""
        cache = {1: 1}
        self.assertEqual(collatz_cycle_length(1, cache), 1)


class TestRangeQuery(unittest.TestCase):
    """區間最大值測試。"""

    def test_range_1_10(self) -> None:
        cache = {1: 1}
        self.assertEqual(max_cycle_length(1, 10, cache), 20)

    def test_range_reverse_order(self) -> None:
        cache = {1: 1}
        self.assertEqual(max_cycle_length(10, 1, cache), 20)


class TestSolve(unittest.TestCase):
    """端對端解題測試。"""

    def test_sample(self) -> None:
        text = "1 10\n100 200\n201 210\n900 1000\n"
        expected = "\n".join(
            [
                "1 10 20",
                "100 200 125",
                "201 210 89",
                "900 1000 174",
            ]
        )
        self.assertEqual(solve(text), expected)


if __name__ == "__main__":
    unittest.main()
