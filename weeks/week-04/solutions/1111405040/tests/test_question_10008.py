"""
UVA 10008 測試。
"""

from __future__ import annotations

import unittest

from question_10008 import count_letters, solve


class TestQuestion10008(unittest.TestCase):
    """測試字母頻率統計。"""

    def test_count_letters_ignores_case(self) -> None:
        self.assertEqual(count_letters(["AaBb"]), [("A", 2), ("B", 2)])

    def test_count_letters_ignores_non_letters(self) -> None:
        self.assertEqual(count_letters(["A1! a?"]), [("A", 2)])

    def test_sort_by_frequency_then_alphabet(self) -> None:
        self.assertEqual(count_letters(["CCAAAB"]), [("A", 3), ("C", 2), ("B", 1)])

    def test_solve_matches_expected_format(self) -> None:
        sample_input = "3\nThis is a test.\nCount me in.\nAAB!\n"
        expected = "T 4\nA 3\nI 3\nS 3\nE 2\nN 2\nB 1\nC 1\nH 1\nM 1\nO 1\nU 1"
        self.assertEqual(solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
