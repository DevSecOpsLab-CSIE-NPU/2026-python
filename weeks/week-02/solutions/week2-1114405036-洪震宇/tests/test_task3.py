"""
Test Suite for Task 3: Log Summary
測試統計和排序功能
"""

import unittest
from task3_log_summary import (
    parse_logs, count_user_events, get_top_action, 
    rank_users, process_logs
)


class TestParseLogs(unittest.TestCase):
    """日誌解析測試"""
    
    def test_parse_valid_logs(self):
        """測試解析有效的日誌"""
        lines = ["alice login", "bob view", "charlie logout"]
        logs = parse_logs(lines)
        
        self.assertEqual(len(logs), 3)
        self.assertEqual(logs[0], ("alice", "login"))
        self.assertEqual(logs[2][1], "logout")
    
    def test_parse_invalid_format(self):
        """測試無效格式的日誌"""
        lines = ["alice"]  # 缺少 action
        with self.assertRaises(ValueError):
            parse_logs(lines)
    
    def test_parse_empty_list(self):
        """測試空日誌列表"""
        lines = []
        logs = parse_logs(lines)
        self.assertEqual(len(logs), 0)


class TestCountUserEvents(unittest.TestCase):
    """使用者事件計數測試"""
    
    def test_count_user_events(self):
        """測試計算使用者事件數"""
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
        counts = count_user_events(logs)
        
        self.assertEqual(counts["alice"], 3)
        self.assertEqual(counts["bob"], 4)
        self.assertEqual(counts["chris"], 1)
    
    def test_count_single_user(self):
        """測試單一使用者的計數"""
        logs = [("alice", "login"), ("alice", "logout")]
        counts = count_user_events(logs)
        
        self.assertEqual(counts["alice"], 2)
    
    def test_count_empty_logs(self):
        """測試空日誌的計數"""
        logs = []
        counts = count_user_events(logs)
        
        self.assertEqual(len(counts), 0)


class TestGetTopAction(unittest.TestCase):
    """最常見行為測試"""
    
    def test_get_top_action(self):
        """測試找出最常見的行為"""
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
        action, count = get_top_action(logs)
        
        # login 出現 3 次，是最常見的
        self.assertEqual(action, "login")
        self.assertEqual(count, 3)
    
    def test_get_top_action_single_action(self):
        """測試只有一種行為的情況"""
        logs = [("alice", "login"), ("bob", "login")]
        action, count = get_top_action(logs)
        
        self.assertEqual(action, "login")
        self.assertEqual(count, 2)
    
    def test_get_top_action_empty_logs(self):
        """測試空日誌"""
        logs = []
        action, count = get_top_action(logs)
        
        self.assertIsNone(action)
        self.assertEqual(count, 0)


class TestRankUsers(unittest.TestCase):
    """使用者排名測試"""
    
    def test_rank_users_primary_sort(self):
        """測試主排列：依總數由大到小"""
        user_count = {"alice": 3, "bob": 4, "chris": 1}
        ranked = rank_users(user_count)
        
        # 應按事件數由大到小
        self.assertEqual(ranked[0][0], "bob")
        self.assertEqual(ranked[1][0], "alice")
        self.assertEqual(ranked[2][0], "chris")
    
    def test_rank_users_tie_break_by_name(self):
        """測試同數時按名字由小到大排序"""
        user_count = {"zoe": 2, "alice": 2, "bob": 2}
        ranked = rank_users(user_count)
        
        # 同數時應按名字排序：alice, bob, zoe
        names = [r[0] for r in ranked]
        self.assertEqual(names, ["alice", "bob", "zoe"])
    
    def test_rank_users_single_user(self):
        """測試單一使用者"""
        user_count = {"alice": 5}
        ranked = rank_users(user_count)
        
        self.assertEqual(len(ranked), 1)
        self.assertEqual(ranked[0][0], "alice")
        self.assertEqual(ranked[0][1], 5)


class TestProcessLogs(unittest.TestCase):
    """完整日誌統計流程測試"""
    
    def test_process_logs_example(self):
        """測試作業範例"""
        m = 8
        lines = [
            "alice login",
            "bob login",
            "alice view",
            "alice logout",
            "bob view",
            "bob view",
            "chris login",
            "bob logout",
        ]
        result = process_logs(m, lines)
        
        # 驗證使用者排名
        user_ranking = result['user_ranking']
        self.assertEqual(len(user_ranking), 3)
        self.assertEqual(user_ranking[0], ("bob", 4))
        self.assertEqual(user_ranking[1], ("alice", 3))
        self.assertEqual(user_ranking[2], ("chris", 1))
        
        # 驗證最常見的行為
        self.assertEqual(result['top_action'], "login")
        self.assertEqual(result['top_action_count'], 3)
    
    def test_process_logs_empty(self):
        """測試空輸入（m = 0）"""
        m = 0
        lines = []
        result = process_logs(m, lines)
        
        self.assertEqual(len(result['user_ranking']), 0)
        self.assertIsNone(result['top_action'])
        self.assertEqual(result['top_action_count'], 0)
    
    def test_process_logs_single_entry(self):
        """測試只有一筆記錄的邊界情況"""
        m = 1
        lines = ["alice login"]
        result = process_logs(m, lines)
        
        self.assertEqual(len(result['user_ranking']), 1)
        self.assertEqual(result['user_ranking'][0], ("alice", 1))
        self.assertEqual(result['top_action'], "login")
        self.assertEqual(result['top_action_count'], 1)
    
    def test_process_logs_mismatched_count(self):
        """測試 m 與實際行數不匹配"""
        m = 3
        lines = ["alice login", "bob view"]  # 只有 2 行，不是 3 行
        
        with self.assertRaises(ValueError):
            process_logs(m, lines)


if __name__ == '__main__':
    unittest.main()
