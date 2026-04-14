"""
UVA 10193 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10193


class TestQuestion10193(unittest.TestCase):
    """測試 All You Need Is Love。"""

    def test_common_factor_exists(self) -> None:
        self.assertTrue(question_10193.has_common_factor("1100", "1000"))

    def test_common_factor_not_exists(self) -> None:
        self.assertFalse(question_10193.has_common_factor("101", "10"))

    def test_solve_cases(self) -> None:
        text = "3\n1100\n1000\n101\n10\n110\n100\n"
        expected = (
            "Pair #1: All you need is love!\n"
            "Pair #2: Love is not all you need!\n"
            "Pair #3: All you need is love!"
        )
        self.assertEqual(question_10193.solve(text), expected)


if __name__ == "__main__":
    unittest.main()
