"""
UVA 10170 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10170 as standard
import question_10170_easy as easy

MODULES = {
    "正式版": standard,
    "簡單版": easy,
}


class TestQuestion10170(unittest.TestCase):
    """驗證第 D 天所屬旅行團。"""

    def test_total_days_helper(self) -> None:
        self.assertEqual(standard.total_days(3, 5), 12)

    def test_small_examples(self) -> None:
        cases = {
            "1 1\n": "1",
            "1 6\n": "3",
            "3 10\n": "5",
            "3 14\n": "6",
        }

        for raw_text, expected in cases.items():
            for name, module in MODULES.items():
                with self.subTest(case=raw_text.strip(), module=name):
                    self.assertEqual(module.solve(raw_text), expected)

    def test_multiple_cases_are_processed(self) -> None:
        text = "1 6\n3 10\n3 14\n"
        expected = "3\n5\n6"

        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve(text), expected)

    def test_large_day_value(self) -> None:
        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve("10000 1000000000000\n"), "1414249")


if __name__ == "__main__":
    unittest.main()
