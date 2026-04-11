import unittest
from task3_log_summary import summarize_logs

class TestTask3(unittest.TestCase):

    def test_basic_summary(self):
        """測試基本的統計與排序功能"""
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("bob", "view"),
            ("bob", "view"),
            ("bob", "logout")
        ]
        # bob 4 次, alice 2 次
        sorted_users, top_action = summarize_logs(logs)
        
        self.assertEqual(sorted_users[0], ("bob", 4))
        self.assertEqual(sorted_users[1], ("alice", 2))
        self.assertEqual(top_action, ("view", 3))

    def test_user_tie_break(self):
        """測試當次數相同時，使用者名稱按字母序排列 (加分項)"""
        logs = [
            ("chris", "login"),
            ("alice", "login"),
            ("bob", "login")
        ]
        # 三人都是 1 次，應按 alice, bob, chris 排序
        sorted_users, _ = summarize_logs(logs)
        expected = [("alice", 1), ("bob", 1), ("chris", 1)]
        self.assertEqual(sorted_users, expected)

    def test_empty_logs(self):
        """邊界測試：處理空輸入 (m = 0)"""
        logs = []
        sorted_users, top_action = summarize_logs(logs)
        
        self.assertEqual(sorted_users, [])
        self.assertIsNone(top_action)

    def test_single_log(self):
        """邊界測試：只有一筆紀錄"""
        logs = [("admin", "delete")]
        sorted_users, top_action = summarize_logs(logs)
        
        self.assertEqual(sorted_users, [("admin", 1)])
        self.assertEqual(top_action, ("delete", 1))

    def test_multiple_top_actions(self):
        """測試當多個動作次數相同時的行為 (穩定性測試)"""
        logs = [
            ("user1", "login"),
            ("user2", "logout")
        ]
        # login 和 logout 各 1 次，確認不會當機
        _, top_action = summarize_logs(logs)
        self.assertIn(top_action[0], ["login", "logout"])
        self.assertEqual(top_action[1], 1)

if __name__ == '__main__':
    unittest.main()