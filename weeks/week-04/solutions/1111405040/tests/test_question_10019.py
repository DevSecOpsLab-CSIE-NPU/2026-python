"""
UVA 10019 測試。
"""

from __future__ import annotations

import unittest

from question_10019 import count_bits, popcount, solve


class TestQuestion10019(unittest.TestCase):
    """測試 bit count 計算。"""

    def test_popcount_basic_value(self) -> None:
        self.assertEqual(popcount(5), 2)

    def test_count_bits_for_twenty_six(self) -> None:
        self.assertEqual(count_bits(26), (3, 3))

    def test_count_bits_for_ten(self) -> None:
        self.assertEqual(count_bits(10), (2, 1))

    def test_count_bits_for_two_hundred_sixty_five(self) -> None:
        self.assertEqual(count_bits(265), (3, 5))

    def test_solve_multiple_cases(self) -> None:
        sample_input = "3\n10\n26\n265\n"
        expected = "2 1\n3 3\n3 5"
        self.assertEqual(solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
