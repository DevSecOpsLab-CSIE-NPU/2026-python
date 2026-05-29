# -*- coding: utf-8 -*-
"""
UVA 12019 - Doom's Day Algorithm 單元測試程式

本測試程式採用 Python 內建的 unittest 框架，對以下模組進行驗證：
1. 核心星期計算：測試手動對應與加總的 `get_weekday(month, day)` 運算是否精準符合 2011 年。
2. 整合 I/O 與完整範例比對：使用 UVA 官方提供的 8 組標準測試範例，模擬輸入並擷取輸出，
   對 `12019.hand.py` 與 `12019-easy.py` 兩版解決方案之全流程進行 100% 精準驗證。

採用 `importlib.util` 進行動態載入，以維持程式架構。
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
hand_file_path = os.path.join(current_dir, "12019.hand.py")
easy_file_path = os.path.join(current_dir, "12019-easy.py")

# 動態載入 12019.hand.py
spec_hand = importlib.util.spec_from_file_location("hand_solution_12019", hand_file_path)
hand_sol = importlib.util.module_from_spec(spec_hand)
spec_hand.loader.exec_module(hand_sol)

# 動態載入 12019-easy.py
spec_easy = importlib.util.spec_from_file_location("easy_solution_12019", easy_file_path)
easy_sol = importlib.util.module_from_spec(spec_easy)
spec_easy.loader.exec_module(easy_sol)


class TestDoomsdayAlgorithm(unittest.TestCase):
    
    def test_core_get_weekday_2011_cases(self):
        """測試單元：驗證 2011 年特定關鍵日期的星期判定"""
        # 1月1日應為星期六
        self.assertEqual(hand_sol.get_weekday(1, 1), "Saturday")
        # 2011 年的 Doomsday 為星期一，故各月 Doomsday 基準日應全為星期一
        self.assertEqual(hand_sol.get_weekday(1, 10), "Monday")
        self.assertEqual(hand_sol.get_weekday(2, 21), "Monday")
        self.assertEqual(hand_sol.get_weekday(3, 7), "Monday")
        self.assertEqual(hand_sol.get_weekday(4, 4), "Monday")
        self.assertEqual(hand_sol.get_weekday(5, 9), "Monday")
        self.assertEqual(hand_sol.get_weekday(6, 6), "Monday")
        self.assertEqual(hand_sol.get_weekday(7, 11), "Monday")
        self.assertEqual(hand_sol.get_weekday(8, 8), "Monday")
        self.assertEqual(hand_sol.get_weekday(9, 5), "Monday")
        self.assertEqual(hand_sol.get_weekday(10, 10), "Monday")
        self.assertEqual(hand_sol.get_weekday(11, 7), "Monday")
        self.assertEqual(hand_sol.get_weekday(12, 12), "Monday")

    def test_solve_hand_standard_flow(self):
        """測試單元：驗證結構化版本 12019.hand.py 的 solve() 整合測試與官方範例"""
        # UVA 官方給出的 8 組標準測試測資
        sample_input = (
            "8\n"
            "1 6\n"
            "2 28\n"
            "4 5\n"
            "5 26\n"
            "8 1\n"
            "11 1\n"
            "12 25\n"
            "12 31\n"
        )
        expected_output = (
            "Thursday\n"
            "Monday\n"
            "Tuesday\n"
            "Thursday\n"
            "Monday\n"
            "Tuesday\n"
            "Sunday\n"
            "Saturday\n"
        )
        
        buf = io.StringIO()
        with patch('sys.stdin', io.StringIO(sample_input)):
            with redirect_stdout(buf):
                hand_sol.solve()
                
        self.assertEqual(buf.getvalue(), expected_output)

    def test_solve_easy_standard_flow(self):
        """測試單元：驗證精簡版本 12019-easy.py 的 solve() 整合測試與官方範例"""
        sample_input = (
            "8\n"
            "1 6\n"
            "2 28\n"
            "4 5\n"
            "5 26\n"
            "8 1\n"
            "11 1\n"
            "12 25\n"
            "12 31\n"
        )
        expected_output = (
            "Thursday\n"
            "Monday\n"
            "Tuesday\n"
            "Thursday\n"
            "Monday\n"
            "Tuesday\n"
            "Sunday\n"
            "Saturday\n"
        )
        
        buf = io.StringIO()
        with patch('sys.stdin', io.StringIO(sample_input)):
            with redirect_stdout(buf):
                easy_sol.solve()
                
        self.assertEqual(buf.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
