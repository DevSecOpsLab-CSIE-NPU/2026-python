"""
UVA 10041 測試。
"""

from __future__ import annotations

import unittest

from question_10041 import min_total_distance, solve


class TestQuestion10041(unittest.TestCase):
    """測試 Vito's Family。"""

    def test_min_total_distance_basic(self) -> None:
        self.assertEqual(min_total_distance([2, 4, 6]), 4)

    def test_min_total_distance_even_count(self) -> None:
        self.assertEqual(min_total_distance([2, 4, 6, 8]), 8)

    def test_min_total_distance_unsorted_input(self) -> None:
        self.assertEqual(min_total_distance([10, 2, 4, 6]), 10)

    def test_solve_multiple_cases(self) -> None:
        sample_input = "2\n2 2 4\n3 2 4 6\n"
        self.assertEqual(solve(sample_input), "2\n4")


if __name__ == "__main__":
    unittest.main()
