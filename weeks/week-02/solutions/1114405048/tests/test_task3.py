"""
Task 3 Unit Tests: Log Summary
測試日誌統計功能
"""

import unittest
from task3_log_summary import (
    parse_logs,
    rank_users,
    get_top_action,
    format_output,
    process_logs
)


class TestParseLogs(unittest.TestCase):
    """測試日誌解析"""
    
    def test_parse_normal(self):
        """正常解析"""
        m = 2
        lines = ["alice login", "bob logout"]
        user_actions, all_actions = parse_logs(m, lines)
        self.assertEqual(user_actions["alice"], 1)
        self.assertEqual(user_actions["bob"], 1)
        self.assertIn("login", all_actions)
        self.assertIn("logout", all_actions)
    
    def test_parse_same_user(self):
        """同一使用者多行"""
        m = 2
        lines = ["alice login", "alice view"]
        user_actions, all_actions = parse_logs(m, lines)
        self.assertEqual(user_actions["alice"], 2)
    
    def test_parse_empty(self):
        """空日誌"""
        m = 0
        lines = []
        user_actions, all_actions = parse_logs(m, lines)
        self.assertEqual(len(user_actions), 0)
        self.assertEqual(len(all_actions), 0)


class TestRankUsers(unittest.TestCase):
    """測試使用者排名"""
    
    def test_rank_by_count(self):
        """按事件數由高到低排名"""
        user_actions = {"alice": 3, "bob": 4, "chris": 1}
        ranked = rank_users(user_actions)
        self.assertEqual(ranked[0][0], "bob")     # 4
        self.assertEqual(ranked[1][0], "alice")   # 3
        self.assertEqual(ranked[2][0], "chris")   # 1
    
    def test_rank_tie_by_name(self):
        """同數時按名稱字母序"""
        user_actions = {"zoe": 2, "alice": 2, "bob": 2}
        ranked = rank_users(user_actions)
        # 都是 2，按名字排
        self.assertEqual(ranked[0][0], "alice")
        self.assertEqual(ranked[1][0], "bob")
        self.assertEqual(ranked[2][0], "zoe")
    
    def test_rank_single_user(self):
        """單個使用者"""
        user_actions = {"alice": 5}
        ranked = rank_users(user_actions)
        self.assertEqual(len(ranked), 1)
        self.assertEqual(ranked[0], ("alice", 5))


class TestGetTopAction(unittest.TestCase):
    """測試最常見動作"""
    
    def test_top_action_normal(self):
        """正常情況"""
        all_actions = ["login", "login", "logout", "view"]
        action, count = get_top_action(all_actions)
        self.assertEqual(action, "login")
        self.assertEqual(count, 2)
    
    def test_top_action_tie(self):
        """並列最多"""
        all_actions = ["login", "logout", "login", "logout"]
        action, count = get_top_action(all_actions)
        # 兩個都出現 2 次，Counter 會取第一個遇到的
        self.assertEqual(count, 2)
    
    def test_top_action_empty(self):
        """無動作"""
        all_actions = []
        action, count = get_top_action(all_actions)
        self.assertIsNone(action)
        self.assertEqual(count, 0)


class TestFormatOutput(unittest.TestCase):
    """測試輸出格式"""
    
    def test_format_single_user(self):
        """單個使用者"""
        ranked_users = [("alice", 3)]
        output = format_output(ranked_users, "login", 2)
        self.assertEqual(output[0], "alice 3")
        self.assertEqual(output[1], "top_action: login 2")
    
    def test_format_multiple_users(self):
        """多個使用者"""
        ranked_users = [("bob", 4), ("alice", 3)]
        output = format_output(ranked_users, "login", 3)
        self.assertEqual(len(output), 3)
        self.assertEqual(output[0], "bob 4")
        self.assertEqual(output[1], "alice 3")
        self.assertEqual(output[2], "top_action: login 3")
    
    def test_format_no_action(self):
        """無動作"""
        ranked_users = [("alice", 1)]
        output = format_output(ranked_users, None, 0)
        self.assertEqual(len(output), 1)  # 不輸出 top_action


class TestProcessLogs(unittest.TestCase):
    """測試完整日誌處理"""
    
    def test_process_logs_example(self):
        """題目範例"""
        m = 8
        lines = [
            "alice login",
            "bob login",
            "alice view",
            "alice logout",
            "bob view",
            "bob view",
            "chris login",
            "bob logout"
        ]
        output = process_logs(m, lines)
        self.assertIn("bob 4", output)
        self.assertIn("alice 3", output)
        self.assertIn("chris 1", output)
        self.assertIn("top_action: login 3", output)
    
    def test_process_logs_single_user(self):
        """單個使用者"""
        m = 2
        lines = ["alice login", "alice logout"]
        output = process_logs(m, lines)
        self.assertEqual(output[0], "alice 2")
    
    def test_process_logs_empty(self):
        """空日誌"""
        m = 0
        lines = []
        output = process_logs(m, lines)
        self.assertEqual(len(output), 0)


if __name__ == "__main__":
    unittest.main()
