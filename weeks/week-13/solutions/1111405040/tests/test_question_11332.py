"""
UVA 11332 測試。
"""

from __future__ import annotations

import unittest

from question_11332 import digital_root, solve
from question_11332_easy import solve as solve_easy


class TestQuestion11332(unittest.TestCase):
    """驗證 Summing Digits。"""

    def test_digital_root(self) -> None:
        """驗證反覆加總後的一位數結果。"""
        self.assertEqual(digital_root(24), 6)
        self.assertEqual(digital_root(39), 3)
        self.assertEqual(digital_root(999999999), 9)

    def test_solve(self) -> None:
        """正式版與 easy 版都應在 0 前停止。"""
        data = "24\n39\n999999999\n0\n"
        expected = "6\n3\n9"
        self.assertEqual(solve(data), expected)
        self.assertEqual(solve_easy(data), expected)


if __name__ == "__main__":
    unittest.main()
