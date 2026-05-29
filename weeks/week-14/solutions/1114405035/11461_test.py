# -*- coding: utf-8 -*-
"""
UVA 11461 - Square Numbers 單元測試程式

本測試程式採用 Python 內建的 unittest 框架，對以下模組進行驗證：
1. 核心區間平方數數量計算：測試 `count_squares(a, b)` 是否在一般與極端邊界下表現正確。
2. 整合 I/O 驗證：模擬標準輸入並擷取輸出，驗證結構化與精簡版的 solve() 是否產出完全符合範例答案的格式。

採用 `importlib.util` 進行動態載入，以維持測試的可靠度。
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
hand_file_path = os.path.join(current_dir, "11461.hand.py")
easy_file_path = os.path.join(current_dir, "11461-easy.py")

# 動態載入 11461.hand.py
spec_hand = importlib.util.spec_from_file_location("hand_solution_11461", hand_file_path)
hand_sol = importlib.util.module_from_spec(spec_hand)
spec_hand.loader.exec_module(hand_sol)

# 動態載入 11461-easy.py
spec_easy = importlib.util.spec_from_file_location("easy_solution_11461", easy_file_path)
easy_sol = importlib.util.module_from_spec(spec_easy)
spec_easy.loader.exec_module(easy_sol)


class TestSquareNumbers(unittest.TestCase):
    
    def test_core_count_squares_examples(self):
        """測試單元：驗證題目範例測資"""
        # 範例 1: [1, 4] 應有 2 個平方數 (1, 4)
        self.assertEqual(hand_sol.count_squares(1, 4), 2)
        # 範例 2: [1, 10] 應有 3 個平方數 (1, 4, 9)
        self.assertEqual(hand_sol.count_squares(1, 10), 3)
        # 範例 3: [1, 100000] 應有 316 個平方數
        self.assertEqual(hand_sol.count_squares(1, 100000), 316)

    def test_core_count_squares_no_squares(self):
        """測試單元：區間內沒有完全平方數"""
        # 區間 [17, 24] 沒有完全平方數
        self.assertEqual(hand_sol.count_squares(17, 24), 0)

    def test_core_count_squares_single_elements(self):
        """測試單元：邊界條件單一元素區間 [a, a]"""
        # [16, 16] 為平方數，應為 1
        self.assertEqual(hand_sol.count_squares(16, 16), 1)
        # [15, 15] 非平方數，應為 0
        self.assertEqual(hand_sol.count_squares(15, 15), 0)

    def test_core_count_squares_invalid_input(self):
        """測試單元：無效的輸入區間"""
        # 起點大於終點
        self.assertEqual(hand_sol.count_squares(10, 5), 0)
        # 包含 0 或負數
        self.assertEqual(hand_sol.count_squares(-5, 5), 0)

    def test_solve_hand_io_flow(self):
        """測試單元：驗證結構化版本 11461.hand.py 的 solve() 整合測試"""
        sample_input = "1 4\n1 10\n1 100000\n0 0\n"
        expected_output = "2\n3\n316\n"
        
        buf = io.StringIO()
        with patch('sys.stdin', io.StringIO(sample_input)):
            with redirect_stdout(buf):
                hand_sol.solve()
                
        self.assertEqual(buf.getvalue(), expected_output)

    def test_solve_easy_io_flow(self):
        """測試單元：驗證精簡版本 11461-easy.py 的 solve() 整合測試"""
        sample_input = "1 4\n1 10\n1 100000\n0 0\n"
        expected_output = "2\n3\n316\n"
        
        buf = io.StringIO()
        with patch('sys.stdin', io.StringIO(sample_input)):
            with redirect_stdout(buf):
                easy_sol.solve()
                
        self.assertEqual(buf.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
