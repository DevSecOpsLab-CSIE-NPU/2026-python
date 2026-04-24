# -*- coding: utf-8 -*-
import unittest
import importlib

# 動態匯入數字命名的 Python 檔案
# 改為載入簡單易記版 10190-easy.py
try:
    sol = importlib.import_module("10190-easy")
    solve = sol.solve
except ImportError:
    solve = None

class TestUVA10190(unittest.TestCase):

    def setUp(self):
        """確保已經成功匯入解題函式"""
        if solve is None:
            self.skipTest("尚未找到 10190.py 或解題函式 solve")

    def test_no_umbrellas(self):
        """邊界測試：完全沒有自動傘"""
        # N=0, W=10, T=5, V=2
        # 沒有傘遮蔽，總雨量 = 寬度(10) * 時間(5) * 單位體積(2) = 100
        self.assertEqual(solve(0, 10, 5, 2, []), "100.00")

    def test_full_cover(self):
        """邊界測試：一把傘完全遮住整條馬路"""
        # 傘長度等於馬路寬度，完美遮蔽，無雨水落到馬路
        # umbrellas 格式: (x, l, v) -> 初始位置 0, 長度 10, 速度 0
        self.assertEqual(solve(1, 10, 5, 2, [(0, 10, 0)]), "0.00")

    def test_partial_static(self):
        """基礎測試：一把靜止的傘遮住一半馬路"""
        # 馬路寬 10，傘長 5，剩下 5 的長度暴露在雨中。
        # 總雨量 = 5(暴露寬) * 5(秒) * 2(體積率) = 50
        self.assertEqual(solve(1, 10, 5, 2, [(0, 5, 0)]), "50.00")

    def test_overlapping_static(self):
        """進階測試：多把傘重疊，靜止不動"""
        # 傘1覆蓋: 0~5, 傘2覆蓋: 4~9。
        # 聯集覆蓋範圍為 0~9，因此只有 9~10 (長度 1) 暴露在雨中。
        # 總雨量 = 1(暴露寬) * 5(秒) * 2(體積率) = 10
        self.assertEqual(solve(2, 10, 5, 2, [
            (0, 5, 0),
            (4, 5, 0)
        ]), "10.00")

if __name__ == '__main__':
    unittest.main()