"""
UVA 10929 — You can say 11 之單元測試
==========================================
測試涵蓋範圍：
  • ZeroJudge 官方樣例（6 筆測資）
  • 極端情境：個位數（0 除外）、極大位數、臨界值
  • 化簡版測試（少數筆數）
詳細繁體中文說明
"""

import io
import unittest
import sys, os

# 確保能找到同目錄下的 solution_10929
sys.path.insert(0, os.path.dirname(__file__))
from solution_10929 import solve


class TestUVA10929(unittest.TestCase):
    """測試 UVA 10929：You can say 11"""

    # ===== 輔助方法 =====
    def run_cases(self, test_input, expected_lines):
        """餵入多行輸入，逐一比對輸出"""
        in_stream = io.StringIO(test_input)
        out_stream = io.StringIO()
        solve(in_stream, out_stream)
        output = out_stream.getvalue().strip().splitlines()
        self.assertEqual(output, expected_lines)

    # ================================================================
    # 測試一：ZeroJudge 官方範例
    # ================================================================
    def test_official_samples(self):
        """來自 ZeroJudge d235 的 6 筆樣例"""
        self.run_cases(
            "112233\n30800\n2937\n323455693\n5038297\n112234\n0\n",
            [
                "112233 is a multiple of 11.",
                "30800 is a multiple of 11.",
                "2937 is a multiple of 11.",
                "323455693 is a multiple of 11.",
                "5038297 is a multiple of 11.",
                "112234 is not a multiple of 11.",
            ]
        )

    # ================================================================
    # 測試二：單位數與零邊界
    # ================================================================
    def test_single_digit(self):
        """單位數：0 不算、1~9 都不是 11 倍數、11 本身是"""
        self.run_cases(
            "1\n9\n11\n0\n",
            [
                "1 is not a multiple of 11.",
                "9 is not a multiple of 11.",
                "11 is a multiple of 11.",
            ]
        )

    # ================================================================
    # 測試三：11 的典型倍數
    # ================================================================
    def test_typical_multiples(self):
        """常見 11 倍數：121, 999999, 1000000001"""
        self.run_cases(
            "121\n999999\n1000000001\n0\n",
            [
                "121 is a multiple of 11.",
                "999999 is a multiple of 11.",
                "1000000001 is a multiple of 11.",
            ]
        )

    # ================================================================
    # 測試四：超大位數（接近 1000 位）
    # ================================================================
    def test_large_number(self):
        """極長字串：全是 1 共 1000 位 → 奇偶差 0 → 11 倍數"""
        thousand_ones = "1" * 1000
        # 1000位全1：奇數位500個1，偶數位500個1，差=0
        self.run_cases(
            f"{thousand_ones}\n0\n",
            [f"{thousand_ones} is a multiple of 11."]
        )


if __name__ == "__main__":
    unittest.main()
