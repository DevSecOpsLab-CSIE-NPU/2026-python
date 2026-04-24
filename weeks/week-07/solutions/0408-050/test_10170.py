# -*- coding: utf-8 -*-
import unittest
import importlib

# 動態匯入數字命名的 Python 檔案
# 改為載入簡單易記的二分搜尋版本 10170-easy.py
try:
    sol = importlib.import_module("10170-easy")
    solve = sol.solve
except ImportError:
    solve = None

class TestUVA10170(unittest.TestCase):

    def setUp(self):
        """確保已經成功匯入解題函式"""
        if solve is None:
            self.skipTest("尚未找到 10170.py 或解題函式 solve")

    def test_simple_case(self):
        """基礎測試：從 1 開始的簡單累加"""
        # 1人(住1天) + 2人(住2天) + 3人(住3天) = 第 6 天剛好是 3 人團的最後一天
        self.assertEqual(solve(1, 6), 3)

    def test_sample_case_1(self):
        """題目範例測試 1"""
        # 3人(住3天) + 4人(住4天) = 7天 
        # 第 8~12 天是 5 人團，故第 10 天是 5 人
        self.assertEqual(solve(3, 10), 5)

    def test_sample_case_2(self):
        """題目範例測試 2"""
        # 3+4+5=12 天 (涵蓋到第 12 天)
        # 第 13~18 天是 6 人團，故第 14 天是 6 人
        self.assertEqual(solve(3, 14), 6)

    def test_minimum_input(self):
        """邊界測試：查詢非常早期的天數"""
        self.assertEqual(solve(1, 1), 1)
        self.assertEqual(solve(10000, 1), 10000)

    def test_large_input(self):
        """極端測試：極大的 D，驗證程式是否會超時 (Time Limit Exceeded)"""
        # 當 S=1, D=10^14 時，若使用 O(N) 迴圈會 TLE，必須使用公式解或二分搜尋
        self.assertEqual(solve(1, 100000000000000), 14142136)

if __name__ == '__main__':
    unittest.main()