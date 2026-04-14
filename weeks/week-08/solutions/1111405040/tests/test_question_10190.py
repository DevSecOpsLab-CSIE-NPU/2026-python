"""
UVA 10190 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10190


class TestQuestion10190(unittest.TestCase):
    """測試 Divide, But Not Quite Conquer!。"""

    def test_valid_sequence(self) -> None:
        self.assertEqual(question_10190.divide_sequence(125, 5), [125, 25, 5, 1])

    def test_invalid_when_not_divisible_to_one(self) -> None:
        self.assertIsNone(question_10190.divide_sequence(120, 3))

    def test_invalid_divisor_one(self) -> None:
        self.assertIsNone(question_10190.divide_sequence(10, 1))

    def test_solve_multiple_lines(self) -> None:
        text = "125 5\n30 3\n1 2\n"
        expected = "125 25 5 1\nBoring!\nBoring!"
        self.assertEqual(question_10190.solve(text), expected)


if __name__ == "__main__":
    unittest.main()
