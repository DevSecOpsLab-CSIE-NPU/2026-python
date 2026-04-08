"""
UVA 10093 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10093 as standard
import question_10093_easy as easy

MODULES = {
    "正式版": standard,
    "簡單版": easy,
}


class TestQuestion10093(unittest.TestCase):
    """驗證最小進位判斷。"""

    def test_char_value_mapping(self) -> None:
        self.assertEqual(standard.char_value("0"), 0)
        self.assertEqual(standard.char_value("A"), 10)
        self.assertEqual(standard.char_value("a"), 36)

    def test_known_sample_values(self) -> None:
        cases = {
            "3\n": "4",
            "+5\n": "6",
            "-A\n": "11",
            "1\n": "2",
            "0\n": "2",
        }

        for raw_text, expected in cases.items():
            for name, module in MODULES.items():
                with self.subTest(case=raw_text.strip(), module=name):
                    self.assertEqual(module.solve(raw_text), expected)

    def test_impossible_case(self) -> None:
        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve("q12345\n"), "such number is impossible!")

    def test_multiple_lines_are_processed(self) -> None:
        text = "3\n+5\n-A\nq12345\n"
        expected = "4\n6\n11\nsuch number is impossible!"

        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve(text), expected)


if __name__ == "__main__":
    unittest.main()
