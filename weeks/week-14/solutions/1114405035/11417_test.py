# -*- coding: utf-8 -*-
"""
UVA 11417 - GCD 單元測試程式

本測試程式使用 Python 內建的 unittest 框架，對以下模組進行驗證：
1. 核心最大公因數計算：測試手寫的 `gcd(a, b)` 是否正確。
2. 核心 GCD 總和算法：測試 `compute_gcd_sum(n)` 在關鍵輸入下（如 N=10, 100, 500）的計算結果。
3. 整合 I/O 驗證：模擬標準輸入並擷取輸出，驗證結構化與精簡版的 solve()。

同樣採用 `importlib.util` 進行動態載入，以避免 Python 在導入含有點/數字/減號之檔名時所發生的語法問題。
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
hand_file_path = os.path.join(current_dir, "11417.hand.py")
easy_file_path = os.path.join(current_dir, "11417-easy.py")

# 動態載入 11417.hand.py
spec_hand = importlib.util.spec_from_file_location("hand_solution_11417", hand_file_path)
hand_sol = importlib.util.module_from_spec(spec_hand)
spec_hand.loader.exec_module(hand_sol)

# 動態載入 11417-easy.py
spec_easy = importlib.util.spec_from_file_location("easy_solution_11417", easy_file_path)
easy_sol = importlib.util.module_from_spec(spec_easy)
spec_easy.loader.exec_module(easy_sol)


class TestGCDSum(unittest.TestCase):
    
    def test_core_gcd_function(self):
        """測試單元：驗證自訂的 gcd(a, b) 函式之正確性"""
        self.assertEqual(hand_sol.gcd(10, 5), 5)
        self.assertEqual(hand_sol.gcd(17, 3), 1)
        self.assertEqual(hand_sol.gcd(100, 40), 20)
        self.assertEqual(hand_sol.gcd(1, 1), 1)
        self.assertEqual(hand_sol.gcd(12, 18), 6)

    def test_core_compute_gcd_sum(self):
        """測試單元：驗證 compute_gcd_sum 在題目指定測資下的數值答案"""
        # 題目測資 1：N = 10，答案應為 67
        self.assertEqual(hand_sol.compute_gcd_sum(10), 67)
        # 題目測資 2：N = 100，答案應為 13015
        self.assertEqual(hand_sol.compute_gcd_sum(100), 13015)
        # 題目測資 3：N = 500，答案應為 442011
        self.assertEqual(hand_sol.compute_gcd_sum(500), 442011)

    def test_solve_hand_io_flow(self):
        """測試單元：驗證結構化版本 11417.hand.py 的 solve() 整合測試"""
        sample_input = "10\n100\n500\n0\n"
        expected_output = "67\n13015\n442011\n"
        
        buf = io.StringIO()
        with patch('sys.stdin', io.StringIO(sample_input)):
            with redirect_stdout(buf):
                hand_sol.solve()
                
        self.assertEqual(buf.getvalue(), expected_output)

    def test_solve_easy_io_flow(self):
        """測試單元：驗證精簡版本 11417-easy.py 的 solve() 整合測試"""
        sample_input = "10\n100\n500\n0\n"
        expected_output = "67\n13015\n442011\n"
        
        buf = io.StringIO()
        with patch('sys.stdin', io.StringIO(sample_input)):
            with redirect_stdout(buf):
                easy_sol.solve()
                
        self.assertEqual(buf.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
