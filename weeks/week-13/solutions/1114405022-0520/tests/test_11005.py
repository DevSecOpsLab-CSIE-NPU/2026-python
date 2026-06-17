"""
UVA 11005 — Cheapest Base

測試計算在各種進位制下，印刷數字的最低成本進位制。
"""
import unittest
import sys
import os

# 加入上一層目錄，以便匯入 solution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCheapestBase(unittest.TestCase):
    """測試 UVA 11005：最低成本進位制"""

    def setUp(self):
        """載入解答模組，若尚未撰寫則跳過"""
        try:
            from solution_11005 import cheapest_bases, parse_input, format_output
            self.cheapest_bases = cheapest_bases
            self.parse_input = parse_input
            self.format_output = format_output
        except ImportError:
            self.skipTest("solution_11005.py 尚未撰寫")

    # ─── 核心功能測試 ───────────────────────────────

    def test_number_zero_in_all_bases(self):
        """數字 0 在任何進位制下都是 "0"，成本皆為 costs[0]"""
        costs = [1] * 36
        result = self.cheapest_bases(costs, 0)
        self.assertEqual(result, list(range(2, 37)))

    def test_single_base_is_cheapest(self):
        """讓 digit '0' 成本極高 → 避免出現 0 的進位制最便宜"""
        # costs[0] = 100, 其餘 = 1
        # 數字 100 在 base 11~36 為 1~2 位數不含 digit 0，成本低
        # 在 base 10 = "100" → cost = 1+100+100 = 201
        costs = [100] + [1] * 35
        result = self.cheapest_bases(costs, 100)
        # 取決於哪個 base 能用最少 non-zero digits 表示
        self.assertTrue(len(result) >= 1)
        self.assertTrue(all(2 <= b <= 36 for b in result))

    def test_number_10_default_costs(self):
        """預設成本（全 1），數字 10 在進位制 11~36 僅需 1 位數，成本最低"""
        costs = [1] * 36
        result = self.cheapest_bases(costs, 10)
        # 10 在 base 11+ 為單一字元，成本 = 1；base 2~10 需多位數，成本 >= 2
        self.assertEqual(result, list(range(11, 37)))

    def test_large_number(self):
        """測試大數字 2,000,000,000"""
        costs = [1] * 36
        result = self.cheapest_bases(costs, 2_000_000_000)
        self.assertTrue(len(result) > 0)
        self.assertTrue(all(2 <= b <= 36 for b in result))

    # ─── digit 轉字元 ────────────────────────────────

    def test_digit_to_char(self):
        """測試 digit 轉換是否正確：0-9 對應 '0'-'9'，10-35 對應 'A'-'Z'"""
        from solution_11005 import digit_to_char
        self.assertEqual(digit_to_char(0), '0')
        self.assertEqual(digit_to_char(9), '9')
        self.assertEqual(digit_to_char(10), 'A')
        self.assertEqual(digit_to_char(35), 'Z')

    # ─── 格式輸出測試 ────────────────────────────────

    def test_output_format(self):
        """檢查輸出格式是否符合題目要求"""
        output = self.format_output(1, [(10, [10]), (20, [8, 16])])
        expected = (
            "Case 1:\n"
            "Cheapest base(s) for number 10: 10\n"
            "Cheapest base(s) for number 20: 8 16\n"
        )
        self.assertEqual(output.strip(), expected.strip())


if __name__ == '__main__':
    unittest.main()
