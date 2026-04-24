# -*- coding: utf-8 -*-
import unittest
import importlib
import math

# 動態匯入數字命名的 Python 檔案
# 假設解題程式名為 10221.py，且裡面實作了 solve(s, a, unit) 函式
try:
    # 改為載入簡單易記版 10221-easy.py
    sol = importlib.import_module("10221-easy")
    # 預期 solve 函式會回傳一個包含 (弧長, 弦長) 的元組 (tuple)
    solve = sol.solve
except (ImportError, AttributeError):
    solve = None

class TestUVA10221(unittest.TestCase):

    def setUp(self):
        """在每個測試開始前，檢查解題函式是否已成功匯入"""
        if solve is None:
            self.skipTest("尚未找到 10221.py 或其解題函式 solve")

    def test_sample_case_1(self):
        """測試題目範例 1：角度單位為 'deg'"""
        # 輸入: s=500, a=30, unit='deg'
        arc, chord = solve(500, 30, 'deg')
        self.assertAlmostEqual(arc, 3633.775503, places=6)
        self.assertAlmostEqual(chord, 3592.408346, places=6)

    def test_sample_case_2(self):
        """測試題目範例 2：角度單位為 'min'"""
        # 輸入: s=700, a=60, unit='min'
        arc, chord = solve(700, 60, 'min')
        self.assertAlmostEqual(arc, 124.616509, places=6)
        self.assertAlmostEqual(chord, 124.614927, places=6)

    def test_sample_case_3(self):
        """測試題目範例 3"""
        # 輸入: s=200, a=45, unit='deg'
        arc, chord = solve(200, 45, 'deg')
        self.assertAlmostEqual(arc, 5215.043805, places=6)
        self.assertAlmostEqual(chord, 5082.035982, places=6)

    def test_180_degrees(self):
        """邊界測試：角度為 180 度"""
        # 當角度為 180 度時，弧長應為半圓周，弦長應為直徑 2*r
        arc, chord = solve(1000, 180, 'deg')
        r = 6440 + 1000
        expected_arc = r * math.pi
        expected_chord = 2 * r
        self.assertAlmostEqual(arc, expected_arc, places=6)
        self.assertAlmostEqual(chord, expected_chord, places=6)

    def test_zero_angle(self):
        """邊界測試：角度為 0"""
        # 當角度為 0 時，弧長和弦長都應為 0
        arc, chord = solve(1000, 0, 'deg')
        self.assertAlmostEqual(arc, 0.0, places=6)
        self.assertAlmostEqual(chord, 0.0, places=6)

if __name__ == '__main__':
    unittest.main()