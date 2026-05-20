"""
UVA 11321 測試。
"""

from __future__ import annotations

import unittest

from question_11321 import c_style_mod, solve, sort_numbers
from question_11321_easy import solve as solve_easy
from question_11321_hand import solve as solve_hand


class TestQuestion11321(unittest.TestCase):
    """驗證排序規則。"""

    def test_c_style_mod_for_negative_values(self) -> None:
        """負數餘數要和 C / C++ 一致。"""
        self.assertEqual(c_style_mod(-1, 3), -1)
        self.assertEqual(c_style_mod(-4, 3), -1)
        self.assertEqual(c_style_mod(4, 3), 1)

    def test_sort_numbers(self) -> None:
        """驗證題目的主要排序邏輯。"""
        numbers = list(range(1, 16))
        expected = [15, 9, 3, 6, 12, 13, 7, 1, 4, 10, 11, 5, 2, 8, 14]
        self.assertEqual(sort_numbers(numbers, 3), expected)

    def test_solve(self) -> None:
        """正式版、easy 版與 hand 版都要得到相同排序結果。"""
        data = "\n".join(
            [
                "15 3",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "0 0",
            ]
        )
        expected = "\n".join(
            [
                "15 3",
                "15",
                "9",
                "3",
                "6",
                "12",
                "13",
                "7",
                "1",
                "4",
                "10",
                "11",
                "5",
                "2",
                "8",
                "14",
                "0 0",
            ]
        )
        self.assertEqual(solve(data), expected)
        self.assertEqual(solve_easy(data), expected)
        self.assertEqual(solve_hand(data), expected)


if __name__ == "__main__":
    unittest.main()
