"""
UVA 10057 測試。
"""

from __future__ import annotations

import unittest

from question_10057 import analyze_numbers, solve


class TestQuestion10057(unittest.TestCase):
    """測試 A mid-summer night's dream。"""

    def test_odd_count_numbers(self) -> None:
        self.assertEqual(analyze_numbers([1, 2, 3]), (2, 1, 1))

    def test_even_count_same_middle_value(self) -> None:
        self.assertEqual(analyze_numbers([1, 2, 2, 4]), (2, 2, 1))

    def test_even_count_middle_range(self) -> None:
        self.assertEqual(analyze_numbers([1, 2, 4, 6]), (2, 2, 3))

    def test_solve_multiple_cases(self) -> None:
        sample_input = "3\n1\n2\n3\n4\n1\n2\n4\n6\n"
        self.assertEqual(solve(sample_input), "2 1 1\n2 2 3")


if __name__ == "__main__":
    unittest.main()
