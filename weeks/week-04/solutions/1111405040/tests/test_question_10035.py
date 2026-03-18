"""
UVA 10035 測試。
"""

from __future__ import annotations

import unittest

from question_10035 import count_carries, format_carry_result, solve


class TestQuestion10035(unittest.TestCase):
    """測試進位次數計算。"""

    def test_no_carry(self) -> None:
        self.assertEqual(count_carries(123, 456), 0)

    def test_single_carry(self) -> None:
        self.assertEqual(count_carries(555, 555), 3)

    def test_multiple_carries(self) -> None:
        self.assertEqual(count_carries(123, 594), 1)

    def test_format_carry_result(self) -> None:
        self.assertEqual(format_carry_result(2), "2 carry operations.")

    def test_solve_stops_at_zero_zero(self) -> None:
        sample_input = "123 456\n555 555\n123 594\n0 0\n1 1\n"
        expected = "No carry operation.\n3 carry operations.\n1 carry operation."
        self.assertEqual(solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
