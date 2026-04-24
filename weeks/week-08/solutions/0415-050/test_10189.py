# -*- coding: utf-8 -*-
import unittest
import importlib

# 動態匯入數字命名的 Python 檔案
# 改為載入簡單易記的外框版 10189-easy.py
try:
    sol = importlib.import_module("10189-easy")
    solve = sol.solve
except ImportError:
    solve = None

class TestUVA10189(unittest.TestCase):

    def setUp(self):
        """確保已經成功匯入解題函式"""
        if solve is None:
            self.skipTest("尚未找到 10189.py 或解題函式 solve")

    def test_sample_case_1(self):
        """測試題目範例 1：4x4 網格"""
        grid = [
            "*...",
            "....",
            ".*..",
            "...."
        ]
        expected = [
            "*100",
            "2210",
            "1*10",
            "1110"
        ]
        self.assertEqual(solve(4, 4, grid), expected)

    def test_sample_case_2(self):
        """測試題目範例 2：3x5 網格"""
        grid = [
            "**...",
            ".....",
            ".*..."
        ]
        expected = [
            "**100",
            "33200",
            "1*100"
        ]
        self.assertEqual(solve(3, 5, grid), expected)

    def test_all_mines(self):
        """邊界測試：全是地雷的極端情況"""
        grid = ["***", "***", "***"]
        expected = ["***", "***", "***"]
        self.assertEqual(solve(3, 3, grid), expected)

    def test_no_mines(self):
        """邊界測試：完全沒有地雷"""
        self.assertEqual(solve(2, 2, ["..", ".."]), ["00", "00"])

    def test_single_cell(self):
        """邊界測試：最小的 1x1 網格"""
        self.assertEqual(solve(1, 1, ["*"]), ["*"])
        self.assertEqual(solve(1, 1, ["."]), ["0"])

if __name__ == '__main__':
    unittest.main()