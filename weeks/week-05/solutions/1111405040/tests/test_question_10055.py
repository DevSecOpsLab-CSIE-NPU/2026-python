"""
UVA 10055 測試。
"""

from __future__ import annotations

import unittest

from question_10055 import absolute_difference, solve


class TestQuestion10055(unittest.TestCase):
    """測試絕對差。"""

    def test_absolute_difference_basic(self) -> None:
        self.assertEqual(absolute_difference(10, 12), 2)

    def test_absolute_difference_large_numbers(self) -> None:
        self.assertEqual(absolute_difference(10000000000, 1), 9999999999)

    def test_absolute_difference_same_number(self) -> None:
        self.assertEqual(absolute_difference(5, 5), 0)

    def test_solve_multiple_lines(self) -> None:
        sample_input = "10 12\n10 10\n1 10000000000\n"
        self.assertEqual(solve(sample_input), "2\n0\n9999999999")


if __name__ == "__main__":
    unittest.main()
