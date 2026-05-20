"""
UVA 11150 測試。
"""

from __future__ import annotations

import unittest

from question_11150 import max_colas, solve
from question_11150_easy import solve as solve_easy


class TestQuestion11150(unittest.TestCase):
    """驗證 Cola。"""

    def test_max_colas_small_values(self) -> None:
        """驗證幾個小範圍已知答案。"""
        self.assertEqual(max_colas(1), 1)
        self.assertEqual(max_colas(2), 3)
        self.assertEqual(max_colas(8), 12)

    def test_solve(self) -> None:
        """正式版與 easy 版都應逐行輸出答案。"""
        data = "1\n2\n8\n"
        expected = "1\n3\n12"
        self.assertEqual(solve(data), expected)
        self.assertEqual(solve_easy(data), expected)


if __name__ == "__main__":
    unittest.main()
