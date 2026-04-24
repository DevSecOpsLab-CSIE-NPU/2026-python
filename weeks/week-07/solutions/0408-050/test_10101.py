# -*- coding: utf-8 -*-
import unittest
import importlib

# 動態匯入數字命名的 Python 檔案
sol = importlib.import_module("10101")
solve = sol.solve

class TestUVA10101(unittest.TestCase):

    def test_move_within_digit_lhs(self):
        """
        測試在等號左側、單一數字內移動火柴。
        範例：1+1=3 -> 1+1=2 (3 變成 2)
        """
        self.assertEqual(solve("1+1=3#"), "1+1=2#")

    def test_move_within_digit_rhs(self):
        """
        測試在等號右側、單一數字內移動火柴。
        範例：3+3=0 -> 3+3=6 (0 變成 6)
        """
        self.assertEqual(solve("3+3=0#"), "3+3=6#")

    def test_move_between_digits(self):
        """
        測試在不同數字間移動火柴（一增一減）。
        範例：8-1=1 -> 9-1=8 (8 移除一根變 9，1 新增一根變 8)
        """
        self.assertEqual(solve("8-1=1#"), "9-1=8#")

    def test_no_solution(self):
        """測試確定無解的情況。"""
        self.assertEqual(solve("1+1=4#"), "No")

    def test_negative_numbers(self):
        """測試包含負數的情況。"""
        self.assertEqual(solve("-1-1=-3#"), "-1-1=-2#")

    def test_larger_numbers(self):
        """測試較大數字的轉換。"""
        self.assertEqual(solve("16-0=10#"), "10-0=10#")

if __name__ == '__main__':
    unittest.main()