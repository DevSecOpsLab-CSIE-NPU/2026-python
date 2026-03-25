"""
UVA 10050 測試。
"""

from __future__ import annotations

import unittest

from question_10050 import count_lost_days, solve


class TestQuestion10050(unittest.TestCase):
    """測試 Hartals。"""

    def test_single_party(self) -> None:
        self.assertEqual(count_lost_days(14, [3]), 3)

    def test_multiple_parties(self) -> None:
        self.assertEqual(count_lost_days(14, [3, 4]), 5)

    def test_ignore_friday_and_saturday(self) -> None:
        self.assertEqual(count_lost_days(7, [1]), 5)

    def test_solve_multiple_cases(self) -> None:
        sample_input = "2\n14\n2\n3\n4\n7\n1\n1\n"
        self.assertEqual(solve(sample_input), "5\n5")


if __name__ == "__main__":
    unittest.main()
