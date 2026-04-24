# -*- coding: utf-8 -*-
import unittest
import importlib

# 動態匯入數字命名的 Python 檔案
# 假設解題程式名為 10222.py，且裡面實作了 solve(text) 函式
try:
    # 改為載入簡單易記版 10222-easy.py
    sol = importlib.import_module("10222-easy")
    solve = sol.solve
except ImportError:
    solve = None

class TestUVA10222(unittest.TestCase):

    def setUp(self):
        """在每個測試開始前，檢查解題函式是否已成功匯入"""
        if solve is None:
            self.skipTest("尚未找到 10222.py 或其解題函式 solve")

    def test_standard_decode(self):
        """
        基礎測試：測試標準字元的解碼。
        在 QWERTY 鍵盤上向左移 2 位。
        'k' -> 'h', '[' -> 'o', 'r' -> 'w'
        """
        self.assertEqual(solve("k[r"), "how")

    def test_decode_with_spaces(self):
        """空白字元測試：解碼過程中，空白鍵不應該被偏移，需保持原樣"""
        self.assertEqual(solve("k[r v"), "how x")

    def test_case_insensitive(self):
        """
        大小寫測試：UVA 10222 規定輸入若包含大寫字母，
        應視為小寫並輸出小寫解碼結果。
        """
        self.assertEqual(solve("K[R"), "how")

    def test_numbers_and_symbols(self):
        """
        標點符號與數字測試：
        '2' 的左邊 2 格是 '`'
        'e' 的左邊 2 格是 'q'
        """
        self.assertEqual(solve("2"), "`")
        self.assertEqual(solve("e"), "q")
        self.assertEqual(solve("]"), "p")

if __name__ == '__main__':
    unittest.main()