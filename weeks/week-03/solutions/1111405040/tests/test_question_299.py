"""
UVA 299 測試。
"""

from __future__ import annotations

import unittest

from question_299 import count_swaps, solve


class TestCountSwaps(unittest.TestCase):
    """交換次數計算單元測試。"""

    def test_sorted(self) -> None:
        self.assertEqual(count_swaps([1, 2, 3, 4]), 0)

    def test_reverse(self) -> None:
        self.assertEqual(count_swaps([4, 3, 2, 1]), 6)

    def test_single_case(self) -> None:
        self.assertEqual(count_swaps([1, 3, 2]), 1)


class TestSolve(unittest.TestCase):
    """端對端解題測試。"""

    def test_multiple_cases(self) -> None:
        text = "\n".join(
            [
                "3",
                "3",
                "1 3 2",
                "4",
                "4 3 2 1",
                "2",
                "1 2",
            ]
        )
        expected = "\n".join(
            [
                "Optimal train swapping takes 1 swaps.",
                "Optimal train swapping takes 6 swaps.",
                "Optimal train swapping takes 0 swaps.",
            ]
        )
        self.assertEqual(solve(text), expected)

    def test_zero_length_train(self) -> None:
        text = "1\n0\n"
        expected = "Optimal train swapping takes 0 swaps."
        self.assertEqual(solve(text), expected)


if __name__ == "__main__":
    unittest.main()
