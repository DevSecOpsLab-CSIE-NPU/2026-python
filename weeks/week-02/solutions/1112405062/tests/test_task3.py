import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task3_log_summary import summarize_logs


class TestTask3LogSummary(unittest.TestCase):
    """Task 3: Log Summary 測試類別"""

    def test_normal_case(self):
        """一般情況：正常統計"""
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("alice", "logout"),
            ("bob", "view"),
            ("bob", "view"),
            ("chris", "login"),
            ("bob", "logout"),
        ]
        user_counts, top_action = summarize_logs(logs)
        self.assertEqual(user_counts[0], ("bob", 4))
        self.assertEqual(user_counts[1], ("alice", 3))
        self.assertEqual(user_counts[2], ("chris", 1))
        self.assertEqual(top_action, ("login", 3))

    def test_empty_logs(self):
        """邊界情況：空日誌"""
        user_counts, top_action = summarize_logs([])
        self.assertEqual(user_counts, [])
        self.assertIsNone(top_action)

    def test_single_user(self):
        """邊界情況：只有一個使用者"""
        logs = [
            ("alice", "login"),
            ("alice", "view"),
        ]
        user_counts, top_action = summarize_logs(logs)
        self.assertEqual(user_counts[0], ("alice", 2))
        self.assertEqual(top_action, ("login", 1))

    def test_tie_users_by_count(self):
        """同計數時按 name 字母序排序"""
        logs = [
            ("bob", "login"),
            ("alice", "login"),
            ("chris", "view"),
        ]
        user_counts, _ = summarize_logs(logs)
        self.assertEqual(user_counts[0][0], "alice")
        self.assertEqual(user_counts[1][0], "bob")
        self.assertEqual(user_counts[2][0], "chris")

    def test_tie_actions(self):
        """多個 action 計數相同時，取第一個出現的"""
        logs = [
            ("alice", "login"),
            ("bob", "view"),
            ("chris", "logout"),
        ]
        _, top_action = summarize_logs(logs)
        self.assertEqual(top_action[1], 1)

    def test_single_action_multiple_users(self):
        """全部相同 action"""
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("chris", "login"),
        ]
        _, top_action = summarize_logs(logs)
        self.assertEqual(top_action, ("login", 3))


if __name__ == "__main__":
    unittest.main()
