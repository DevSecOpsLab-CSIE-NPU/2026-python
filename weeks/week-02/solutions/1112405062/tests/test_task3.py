"""
================================================================================
Task 3: Log Summary 測試程式
================================================================================

題目說明：
    給定多行事件紀錄（user action），統計每位使用者行為次數，並輸出：
    1. 每位使用者總事件數（依總數由大到小，若同數則使用者名稱由小到大）
    2. 全域最常見 action 及其次數

================================================================================
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task3_log_summary import log_summary



class TestLogSummary(unittest.TestCase):
    """測試日誌統計功能"""

    def test_basic_case(self):
        """測試基本情況"""
        input_data = [
            "8",
            "alice login",
            "bob login",
            "alice view",
            "alice logout",
            "bob view",
            "bob view",
            "chris login",
            "bob logout",
        ]
        result = log_summary(input_data)
        expected_user = ["bob 4", "alice 3", "chris 1"]
        self.assertEqual(result["users"], expected_user)
        self.assertEqual(result["top_action"], "login 3")

    def test_empty_input(self):
        """測試空輸入 (m=0)"""
        input_data = ["0"]
        result = log_summary(input_data)
        self.assertEqual(result["users"], [])
        self.assertEqual(result["top_action"], "")

    def test_single_user(self):
        """測試單一使用者"""
        input_data = ["3", "alice login", "alice view", "alice logout"]
        result = log_summary(input_data)
        self.assertEqual(result["users"], ["alice 3"])
        self.assertEqual(result["top_action"], "login 1")

    def test_same_count_different_name(self):
        """測試同數不同名稱"""
        input_data = ["4", "alice login", "bob login", "chris login", "dave login"]
        result = log_summary(input_data)
        self.assertEqual(result["users"], ["alice 1", "bob 1", "chris 1", "dave 1"])

    def test_all_same_action(self):
        """測試全部相同 action"""
        input_data = [
            "5",
            "alice view",
            "bob view",
            "carol view",
            "dave view",
            "eve view",
        ]
        result = log_summary(input_data)
        self.assertEqual(result["top_action"], "view 5")

    def test_tie_top_action(self):
        """測試多個 action 次數相同"""
        input_data = [
            "6",
            "alice login",
            "bob login",
            "alice view",
            "bob view",
            "carol login",
            "carol view",
        ]
        result = log_summary(input_data)
        self.assertIn(result["top_action"], ["login 3", "view 3"])


if __name__ == "__main__":
    unittest.main()
