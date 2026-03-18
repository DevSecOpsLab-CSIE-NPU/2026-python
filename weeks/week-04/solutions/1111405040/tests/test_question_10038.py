"""
UVA 10038 測試。
"""

from __future__ import annotations

import unittest

from question_10038 import is_jolly, solve


class TestQuestion10038(unittest.TestCase):
    """測試 Jolly Jumper 判定。"""

    def test_single_value_is_jolly(self) -> None:
        self.assertTrue(is_jolly([1]))

    def test_known_jolly_sequence(self) -> None:
        self.assertTrue(is_jolly([1, 4, 2, 3]))

    def test_known_not_jolly_sequence(self) -> None:
        self.assertFalse(is_jolly([1, 4, 2, -1, 6]))

    def test_repeated_difference_is_not_jolly(self) -> None:
        self.assertFalse(is_jolly([1, 2, 3, 4]))

    def test_solve_multiple_lines(self) -> None:
        sample_input = "4 1 4 2 3\n5 1 4 2 -1 6\n"
        expected = "Jolly\nNot jolly"
        self.assertEqual(solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
