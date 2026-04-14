"""
UVA 10189 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10189


class TestQuestion10189(unittest.TestCase):
    """測試 Minesweeper。"""

    def test_count_adjacent_mines(self) -> None:
        field = ["*.", ".*"]
        self.assertEqual(question_10189.count_adjacent_mines(field, 0, 1), 2)

    def test_solve_single_field(self) -> None:
        text = "4 4\n*...\n....\n.*..\n....\n0 0\n"
        expected = "Field #1:\n*100\n2210\n1*10\n1110"
        self.assertEqual(question_10189.solve(text), expected)

    def test_solve_multiple_fields_with_blank_line(self) -> None:
        text = (
            "4 4\n*...\n....\n.*..\n....\n"
            "3 5\n**...\n.....\n.*...\n0 0\n"
        )
        expected = (
            "Field #1:\n*100\n2210\n1*10\n1110\n\n"
            "Field #2:\n**100\n33200\n1*100"
        )
        self.assertEqual(question_10189.solve(text), expected)

    def test_empty_field_without_mines(self) -> None:
        text = "2 2\n..\n..\n0 0\n"
        expected = "Field #1:\n00\n00"
        self.assertEqual(question_10189.solve(text), expected)


if __name__ == "__main__":
    unittest.main()
