"""
UVA 10221 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10221


class TestQuestion10221(unittest.TestCase):
    """測試 Satellites。"""

    def test_min_unit_is_converted_to_degrees(self) -> None:
        self.assertAlmostEqual(question_10221.normalize_angle_degrees(60, "min"), 1.0)

    def test_angle_uses_shorter_side(self) -> None:
        self.assertAlmostEqual(question_10221.normalize_angle_degrees(300, "deg"), 60.0)

    def test_sample_cases(self) -> None:
        text = "500 30 deg\n700 60 min\n200 45 deg\n"
        expected = (
            "3633.775503 3592.408346\n"
            "124.616509 124.614927\n"
            "5215.043805 5082.035982"
        )
        self.assertEqual(question_10221.solve(text), expected)


if __name__ == "__main__":
    unittest.main()
