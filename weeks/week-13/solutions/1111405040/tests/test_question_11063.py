"""
UVA 11063 測試。
"""

from __future__ import annotations

import unittest

from question_11063 import is_b2_sequence, solve
from question_11063_easy import solve as solve_easy


class TestQuestion11063(unittest.TestCase):
    """驗證 B2-Sequence。"""

    def test_is_b2_sequence_true(self) -> None:
        """標準遞增序列且兩兩和不重複。"""
        self.assertTrue(is_b2_sequence([1, 2, 4, 8]))

    def test_is_b2_sequence_false_when_not_increasing(self) -> None:
        """不嚴格遞增時一定不是 B2-Sequence。"""
        self.assertFalse(is_b2_sequence([1, 2, 2, 4]))

    def test_is_b2_sequence_false_when_sum_repeats(self) -> None:
        """如果兩兩和重複，也不符合條件。"""
        self.assertFalse(is_b2_sequence([1, 2, 3]))

    def test_solve(self) -> None:
        """正式版與 easy 版都要通過相同案例。"""
        data = "\n".join(
            [
                "4",
                "1 2 4 8",
                "4",
                "1 2 2 4",
            ]
        )
        expected = "\n".join(
            [
                "Case #1: It is a B2-Sequence.",
                "",
                "Case #2: It is not a B2-Sequence.",
            ]
        )
        self.assertEqual(solve(data), expected)
        self.assertEqual(solve_easy(data), expected)


if __name__ == "__main__":
    unittest.main()
