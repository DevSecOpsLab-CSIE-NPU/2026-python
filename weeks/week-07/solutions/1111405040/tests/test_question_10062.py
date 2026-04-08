"""
UVA 10062 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10062 as standard
import question_10062_easy as easy

MODULES = {
    "正式版": standard,
    "簡單版": easy,
}


class TestQuestion10062(unittest.TestCase):
    """驗證 ASCII 頻率排序邏輯。"""

    def test_frequency_pairs_are_sorted_by_count_then_ascii_desc(self) -> None:
        expected = [(67, 1), (66, 2), (65, 3)]

        self.assertEqual(standard.frequency_pairs("AAABBC"), expected)

    def test_single_line_output_matches_expected_order(self) -> None:
        expected = "67 1\n66 2\n65 3"

        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve("AAABBC\n"), expected)

    def test_blank_line_is_inserted_between_cases(self) -> None:
        expected = "66 1\n65 1\n\n67 2"

        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve("AB\nCC\n"), expected)

    def test_space_is_also_counted(self) -> None:
        expected = "32 1\n65 2"

        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve("A A\n"), expected)

    def test_same_frequency_uses_larger_ascii_first(self) -> None:
        expected = "97 1\n65 1\n33 1"

        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve("aA!\n"), expected)


if __name__ == "__main__":
    unittest.main()
