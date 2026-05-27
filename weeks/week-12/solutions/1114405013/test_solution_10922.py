"""
UVA 10922 — 2 the 9s 之單元測試
==========================================
測試涵蓋範圍：
  • 題目範例：9, 999999, 123456789, 18, 81, 162, 987654321, 22, 111111111
  • 邊界情境：個位數（非 9）、極長 20 位數
  • 極端大數：1 + 50 個 8（非倍數）、30 個連續 9（degree 2）
詳細繁體中文說明
"""

import io
import unittest
import sys, os

# 讓 Python 能找到同資料夾下的 solution_10922.py
sys.path.insert(0, os.path.dirname(__file__))
from solution_10922 import solve


class TestUVA10922(unittest.TestCase):
    """測試 UVA 10922：2 the 9s"""

    def run_sample(self, test_input, expected_lines):
        """輔助方法：餵入測試字串，比對輸出每一行是否與預期完全相同"""
        in_stream = io.StringIO(test_input)
        out_stream = io.StringIO()
        solve(in_stream, out_stream)
        output = out_stream.getvalue().strip().splitlines()
        self.assertEqual(output, expected_lines)

    # ------------------------------------------------------------------
    # 測試一：基本範例
    # ------------------------------------------------------------------
    def test_examples(self):
        """包含 9 的倍數（各種 degree）與非倍數"""
        self.run_sample(
            "9\n999999\n123456789\n18\n81\n162\n987654321\n22\n111111111\n0\n",
            [
                "9-degree of 9 is 1.",          # 本身就是 9
                "9-degree of 999999 is 2.",      # →54→9
                "9-degree of 123456789 is 2.",   # →45→9
                "9-degree of 18 is 1.",          # →9 （1 次加總）
                "9-degree of 81 is 1.",          # →9
                "9-degree of 162 is 1.",         # →9
                "9-degree of 987654321 is 2.",   # →45→9
                "22 is not a multiple of 9.",
                "9-degree of 111111111 is 1.",   # 九個 1 → 9
            ]
        )

    # ------------------------------------------------------------------
    # 測試二：邊界案例
    # ------------------------------------------------------------------
    def test_edge_cases(self):
        """個位數非 9、極長 20 位數"""
        # (a) 個位數 1, 8, 5 → 都不是 9 的倍數
        self.run_sample("1\n8\n5\n0\n", [
            "1 is not a multiple of 9.",
            "8 is not a multiple of 9.",
            "5 is not a multiple of 9.",
        ])

        # (b) 20 個連續 9 → 9*20=180 → 1+8+0=9，degree = 2
        self.run_sample(
            "99999999999999999999\n0\n",
            ["9-degree of 99999999999999999999 is 2."]
        )

    # ------------------------------------------------------------------
    # 測試三：極端大數
    # ------------------------------------------------------------------
    def test_huge_number(self):
        """超長字串（超過 50 位），混合非倍數與超大倍數"""
        bad = "1" + "8" * 50          # 1 後面接 50 個 8，總和 401 → 5 ≠ 9
        good = "9" * 30              # 30 個 9 → 270 → 9，degree = 2
        self.run_sample(f"{bad}\n{good}\n0\n", [
            f"{bad} is not a multiple of 9.",
            f"9-degree of {good} is 2.",
        ])


if __name__ == "__main__":
    unittest.main()
