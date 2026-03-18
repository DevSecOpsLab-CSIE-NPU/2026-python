"""
UVA 948 測試。
"""

from __future__ import annotations

import unittest

from question_948 import build_fib_numbers, fibonaccimal_representation, solve


class TestQuestion948(unittest.TestCase):
    """測試 Fibonaccimal Base 轉換。"""

    def test_build_fib_numbers_up_to_ten(self) -> None:
        self.assertEqual(build_fib_numbers(10), [1, 2, 3, 5, 8])

    def test_one_is_single_one(self) -> None:
        self.assertEqual(fibonaccimal_representation(1), "1")

    def test_two_is_ten(self) -> None:
        self.assertEqual(fibonaccimal_representation(2), "10")

    def test_ten_is_10010(self) -> None:
        self.assertEqual(fibonaccimal_representation(10), "10010")

    def test_solve_multiple_cases(self) -> None:
        sample_input = "3\n1\n2\n10\n"
        expected = "1 = 1 (fib)\n2 = 10 (fib)\n10 = 10010 (fib)"
        self.assertEqual(solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
