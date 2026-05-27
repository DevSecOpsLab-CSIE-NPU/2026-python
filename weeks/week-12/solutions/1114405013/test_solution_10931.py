"""
UVA 10931 — Parity 之單元測試
==========================================
測試涵蓋範圍：
  • 題目範例（1, 2, 10, 21）
  • 典型邊界（最小值 1、最大值 2³¹−1、2 的冪次）
  • 特殊數字（全 1、0 結尾不處理）
詳細繁體中文說明
"""

import io
import unittest
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from solution_10931 import solve


class TestUVA10931(unittest.TestCase):
    """測試 UVA 10931：Parity"""

    def run_cases(self, test_input, expected_lines):
        in_stream = io.StringIO(test_input)
        out_stream = io.StringIO()
        solve(in_stream, out_stream)
        output = out_stream.getvalue().strip().splitlines()
        self.assertEqual(output, expected_lines)

    # ================================================================
    # 測試一：題目給的範例
    # ================================================================
    def test_sample(self):
        """4 筆官方範例"""
        self.run_cases(
            "1\n2\n10\n21\n0\n",
            [
                "The parity of 1 is 1 (mod 2).",
                "The parity of 10 is 1 (mod 2).",
                "The parity of 1010 is 2 (mod 2).",
                "The parity of 10101 is 3 (mod 2).",
            ]
        )

    # ================================================================
    # 測試二：邊界值
    # ================================================================
    def test_boundaries(self):
        """最小值 1、2 的冪次（只有一個 1）"""
        self.run_cases(
            "1\n2\n4\n8\n16\n32\n0\n",
            [
                "The parity of 1 is 1 (mod 2).",
                "The parity of 10 is 1 (mod 2).",
                "The parity of 100 is 1 (mod 2).",
                "The parity of 1000 is 1 (mod 2).",
                "The parity of 10000 is 1 (mod 2).",
                "The parity of 100000 is 1 (mod 2).",
            ]
        )

    # ================================================================
    # 測試三：最大值與全 1 數字
    # ================================================================
    def test_max_and_all_ones(self):
        """最大值 2147483647（全 1 共 31 位）、Mersenne 數"""
        max_int = 2147483647      # 2³¹−1，二進位 31 個 1
        self.run_cases(
            f"{max_int}\n0\n",
            [f"The parity of {'1'*31} is 31 (mod 2)."]
        )

    # ================================================================
    # 測試四：隨機一般數字
    # ================================================================
    def test_misc(self):
        """一般常見數字"""
        self.run_cases(
            "7\n15\n100\n255\n0\n",
            [
                "The parity of 111 is 3 (mod 2).",
                "The parity of 1111 is 4 (mod 2).",
                "The parity of 1100100 is 3 (mod 2).",
                "The parity of 11111111 is 8 (mod 2).",
            ]
        )


if __name__ == "__main__":
    unittest.main()
