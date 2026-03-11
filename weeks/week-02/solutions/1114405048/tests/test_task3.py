import unittest
import sys
sys.path.insert(0, '..')
from task3_log_summary import count_user_actions, find_top_action, process_logs


class TestLogSummary(unittest.TestCase):
    """Task 3: Log Summary - 3個測試案例 x 3個測試"""
    
    def test_count_user_actions_normal(self):
        """正常情況：多個使用者多個事件"""
        logs = [
            "alice login",
            "bob login",
            "alice view",
            "alice logout",
            "bob view",
            "bob view",
            "chris login",
            "bob logout",
        ]
        result = count_user_actions(logs)
        self.assertEqual(result["alice"], 3)
        self.assertEqual(result["bob"], 4)
        self.assertEqual(result["chris"], 1)
    
    def test_count_user_actions_edge_empty(self):
        """邊界情況：空日誌"""
        result = count_user_actions([])
        self.assertEqual(len(result), 0)
    
    def test_count_user_actions_single_user(self):
        """反例：只有一個使用者"""
        logs = ["alice login", "alice view", "alice logout"]
        result = count_user_actions(logs)
        self.assertEqual(result["alice"], 3)
        self.assertEqual(len(result), 1)
    
    def test_find_top_action_normal(self):
        """正常情況：多個事件"""
        logs = [
            "alice login",
            "bob login",
            "alice view",
            "bob view",
            "bob view",
            "chris login",
        ]
        action, count = find_top_action(logs)
        self.assertEqual(action, "login")
        self.assertEqual(count, 3)
    
    def test_find_top_action_edge_empty(self):
        """邊界情況：空日誌"""
        action, count = find_top_action([])
        self.assertIsNone(action)
        self.assertEqual(count, 0)
    
    def test_find_top_action_tie(self):
        """反例：多個事件頻率相同"""
        logs = [
            "alice login",
            "bob logout",
        ]
        action, count = find_top_action(logs)
        # 當有平手時，應該返回其中一個（題目沒有明確說)
        self.assertIn(action, ["login", "logout"])
        self.assertEqual(count, 1)
    
    def test_process_logs_normal(self):
        """正常情況：完整日誌處理"""
        logs = [
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
        result = process_logs(logs)
        # 結果應該包含排序的使用者和最常見的action
        self.assertIn("bob 4", result)
        self.assertIn("alice 3", result)
        self.assertIn("chris 1", result)
        self.assertIn("top_action:", result)
    
    def test_process_logs_edge_zero(self):
        """邊界情況：0筆日誌"""
        logs = ["0"]
        result = process_logs(logs)
        # 應該只有top_action行或空結果
        self.assertIsNotNone(result)
    
    def test_process_logs_ranking_order(self):
        """反例：驗證使用者排序（由多到少，同數則名稱由小到大）"""
        logs = [
            "4",
            "zoe action1",
            "bob action1",
            "alice action1",
            "alice action1",
        ]
        result = process_logs(logs)
        lines = result.strip().split('\n')
        # alice應該排在最前（2個事件）
        self.assertEqual(lines[0].split()[0], "alice")
        # bob和zoe各1個，應按名字字母序
        if len(lines) >= 3:
            self.assertEqual(lines[2].split()[0], "zoe")


if __name__ == '__main__':
    unittest.main()
