"""
UVA 490 測試。
"""

from __future__ import annotations

import unittest

from question_490 import rotate_clockwise, solve


class TestRotateClockwise(unittest.TestCase):
    """旋轉邏輯測試。"""

    def test_hello_world(self) -> None:
        lines = ["HELLO", "WORLD"]
        expected = ["WH", "OE", "RL", "LL", "DO"]
        self.assertEqual(rotate_clockwise(lines), expected)

    def test_different_lengths(self) -> None:
        lines = ["ABC", "DE", "F"]
        expected = ["FDA", " EB", "  C"]
        self.assertEqual(rotate_clockwise(lines), expected)

    def test_empty_input(self) -> None:
        self.assertEqual(rotate_clockwise([]), [])
        self.assertEqual(solve(""), "")


if __name__ == "__main__":
    unittest.main()
