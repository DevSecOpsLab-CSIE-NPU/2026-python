"""
UVA 10071 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10071 as standard
import question_10071_easy as easy

MODULES = {
    "正式版": standard,
    "簡單版": easy,
}


class TestQuestion10071(unittest.TestCase):
    """驗證位移計算。"""

    def test_compute_displacement_function(self) -> None:
        self.assertEqual(standard.compute_displacement(5, 12), 120)

    def test_zero_velocity_and_time(self) -> None:
        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve("0 0\n"), "0")

    def test_multiple_cases_until_eof(self) -> None:
        text = "0 0\n5 12\n10 10\n"
        expected = "0\n120\n200"

        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve(text), expected)

    def test_negative_velocity_is_supported(self) -> None:
        for name, module in MODULES.items():
            with self.subTest(module=name):
                self.assertEqual(module.solve("-3 5\n"), "-30")


if __name__ == "__main__":
    unittest.main()
