# -*- coding: utf-8 -*-
"""
UVA 11349 - Symmetric Matrix 單元測試程式

本測試程式採用 Python 內建的 unittest 框架，針對以下兩部分進行完整的測試：
1. 核心對稱判斷：驗證正常奇偶維度、負數邊界、單一元素等矩陣的判斷是否正確。
2. I/O 流程測試：利用 sys.stdin 模擬輸入與 redirect_stdout 擷取輸出，驗證結構化與精簡版的 solve()。

由於檔案名稱中包含數字、點與減號（如 11349.hand.py），無法使用標準的 import 語法，
本程式使用 `importlib.util` 進行動態載入，以維持程式的健壯度與架構的乾淨。
"""

import io
import os
import sys
import unittest
import importlib.util
from contextlib import redirect_stdout
from unittest.mock import patch

# 取得當前檔案所在的絕對路徑與目標檔案路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
hand_file_path = os.path.join(current_dir, "11349.hand.py")
easy_file_path = os.path.join(current_dir, "11349-easy.py")

# 動態載入 11349.hand.py
spec_hand = importlib.util.spec_from_file_location("hand_solution", hand_file_path)
hand_sol = importlib.util.module_from_spec(spec_hand)
spec_hand.loader.exec_module(hand_sol)

# 動態載入 11349-easy.py
spec_easy = importlib.util.spec_from_file_location("easy_solution", easy_file_path)
easy_sol = importlib.util.module_from_spec(spec_easy)
spec_easy.loader.exec_module(easy_sol)


class TestSymmetricMatrix(unittest.TestCase):
    
    def test_core_is_symmetric_odd(self):
        """測試單元：奇數維度 (3x3) 的對稱矩陣 (無負數，應為 True)"""
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 1, 5]
        ]
        self.assertTrue(hand_sol.is_symmetric(matrix, 3))
        
    def test_core_is_symmetric_even(self):
        """測試單元：偶數維度 (4x4) 的對稱矩陣 (無負數，應為 True)"""
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [8, 7, 6, 5],
            [4, 3, 2, 1]
        ]
        self.assertTrue(hand_sol.is_symmetric(matrix, 4))
        
    def test_core_non_symmetric_values(self):
        """測試單元：數值不對稱的矩陣 (3x3，應為 False)"""
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [0, 1, 5]  # 左下角為 0，與右上角 3 不對稱
        ]
        self.assertFalse(hand_sol.is_symmetric(matrix, 3))
        
    def test_core_has_negative_value(self):
        """測試單元：結構對稱但含有負數的矩陣 (應為 False)"""
        matrix = [
            [5, 1, -3],
            [2, 0, 2],
            [-3, 1, 5]
        ]
        self.assertFalse(hand_sol.is_symmetric(matrix, 3))
        
    def test_core_single_element_positive(self):
        """測試單元：邊界條件 n=1，正數 (應為 True)"""
        matrix = [[42]]
        self.assertTrue(hand_sol.is_symmetric(matrix, 1))
        
    def test_core_single_element_negative(self):
        """測試單元：邊界條件 n=1，負數 (應為 False)"""
        matrix = [[-42]]
        self.assertFalse(hand_sol.is_symmetric(matrix, 1))

    def test_solve_hand_standard_flow(self):
        """測試單元：標準結構化 solve() 的 I/O 整合測試"""
        sample_input = (
            "2\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "3 1 5\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "0 1 5\n"
        )
        expected_output = (
            "Test #1: Symmetric.\n"
            "Test #2: Non-symmetric.\n"
        )
        
        # 模擬 stdin 並擷取 stdout
        buf = io.StringIO()
        with patch('sys.stdin', io.StringIO(sample_input)):
            with redirect_stdout(buf):
                hand_sol.solve()
        
        # 驗證輸出是否與範例答案完全一致
        self.assertEqual(buf.getvalue(), expected_output)

    def test_solve_easy_standard_flow(self):
        """測試單元：精簡版 solve() 的 I/O 整合測試"""
        sample_input = (
            "2\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "3 1 5\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "0 1 5\n"
        )
        expected_output = (
            "Test #1: Symmetric.\n"
            "Test #2: Non-symmetric.\n"
        )
        
        # 模擬 stdin 並擷取 stdout
        buf = io.StringIO()
        with patch('sys.stdin', io.StringIO(sample_input)):
            with redirect_stdout(buf):
                easy_sol.solve()
        
        # 驗證精簡版輸出是否符合預期
        self.assertEqual(buf.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
