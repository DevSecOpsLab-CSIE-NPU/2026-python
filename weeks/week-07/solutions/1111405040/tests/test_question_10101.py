"""
UVA 10101 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10101 as standard
import question_10101_easy as easy

MODULES = {
    "正式版": standard,
    "簡單版": easy,
}


class TestQuestion10101(unittest.TestCase):
    """驗證 Bangla 數字格式。"""

    def test_format_bangla_examples(self) -> None:
        self.assertEqual(standard.format_bangla(23764), "23 hajar 7 shata 64")
        self.assertEqual(
            standard.format_bangla(45897458973958),
            "45 lakh 89 hajar 7 shata 45 kuti 89 lakh 73 hajar 9 shata 58",
        )

    def test_zero_is_output_directly(self) -> None:
        for name, module in MODULES.items():
            formatter = standard.format_bangla if name == "正式版" else module.format_number
            with self.subTest(module=name):
                self.assertEqual(formatter(0), "0")

    def test_single_kuti_case(self) -> None:
        for name, module in MODULES.items():
            formatter = standard.format_bangla if name == "正式版" else module.format_number
            with self.subTest(module=name):
                self.assertEqual(formatter(10_000_000), "1 kuti")

    def test_solve_adds_case_numbers(self) -> None:
        text = "23764\n45897458973958\n0\n"
        expected = (
            "   1. 23 hajar 7 shata 64\n"
            "   2. 45 lakh 89 hajar 7 shata 45 kuti 89 lakh 73 hajar 9 shata 58\n"
            "   3. 0"
        )

        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve(text), expected)


if __name__ == "__main__":
    unittest.main()
