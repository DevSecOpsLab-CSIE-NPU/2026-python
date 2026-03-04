"""
Test for Task 3: Log Summary
"""

import unittest
from task3_log_summary import (
    parse_log_entry,
    count_user_events,
    find_top_action,
    sort_users_by_count,
    log_summary
)


class TestParseLogEntry(unittest.TestCase):
    """測試日誌行解析函式。"""
    
    def test_parse_log_entry_basic(self):
        """基本解析測試。"""
        line = "alice login"
        expected = ("alice", "login")
        self.assertEqual(parse_log_entry(line), expected)
    
    def test_parse_log_entry_different_actions(self):
        """不同動作測試。"""
        line = "bob view"
        expected = ("bob", "view")
        self.assertEqual(parse_log_entry(line), expected)
    
    def test_parse_log_entry_logout(self):
        """登出動作測試。"""
        line = "alice logout"
        expected = ("alice", "logout")
        self.assertEqual(parse_log_entry(line), expected)


class TestCountUserEvents(unittest.TestCase):
    """測試使用者事件計數函式。"""
    
    def test_count_user_events_basic(self):
        """基本計數測試。"""
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("alice", "logout"),
            ("bob", "view"),
            ("bob", "view"),
            ("chris", "login"),
            ("bob", "logout")
        ]
        result = count_user_events(logs)
        
        self.assertEqual(result["alice"], 3)
        self.assertEqual(result["bob"], 4)
        self.assertEqual(result["chris"], 1)
    
    def test_count_user_events_single_user(self):
        """單一使用者測試。"""
        logs = [
            ("alice", "login"),
            ("alice", "view"),
            ("alice", "logout")
        ]
        result = count_user_events(logs)
        self.assertEqual(result["alice"], 3)
        self.assertEqual(len(result), 1)
    
    def test_count_user_events_same_action(self):
        """同一動作多次測試。"""
        logs = [
            ("bob", "login"),
            ("bob", "login"),
            ("bob", "login"),
        ]
        result = count_user_events(logs)
        self.assertEqual(result["bob"], 3)


class TestFindTopAction(unittest.TestCase):
    """測試最常見動作查找函式。"""
    
    def test_find_top_action_basic(self):
        """基本測試：login 出現 3 次最多。"""
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("alice", "logout"),
            ("bob", "view"),
            ("bob", "view"),
            ("chris", "login"),
            ("bob", "logout")
        ]
        action, count = find_top_action(logs)
        self.assertEqual(action, "login")
        self.assertEqual(count, 3)
    
    def test_find_top_action_view_most_common(self):
        """view 最常見測試。"""
        logs = [
            ("alice", "view"),
            ("bob", "view"),
            ("chris", "view"),
            ("alice", "login"),
        ]
        action, count = find_top_action(logs)
        self.assertEqual(action, "view")
        self.assertEqual(count, 3)
    
    def test_find_top_action_single_log(self):
        """單一日誌測試。"""
        logs = [
            ("alice", "login"),
        ]
        action, count = find_top_action(logs)
        self.assertEqual(action, "login")
        self.assertEqual(count, 1)


class TestSortUsersByCount(unittest.TestCase):
    """測試使用者排序函式。"""
    
    def test_sort_users_by_count_descending(self):
        """測試由多到少排序。"""
        user_counts = {
            "alice": 3,
            "bob": 4,
            "chris": 1
        }
        result = sort_users_by_count(user_counts)
        
        self.assertEqual(result[0][0], "bob")
        self.assertEqual(result[0][1], 4)
        self.assertEqual(result[1][0], "alice")
        self.assertEqual(result[1][1], 3)
        self.assertEqual(result[2][0], "chris")
        self.assertEqual(result[2][1], 1)
    
    def test_sort_users_by_count_same_count_alphabetical(self):
        """測試相同計數時按名字排序。"""
        user_counts = {
            "zoe": 2,
            "alice": 2,
            "bob": 2
        }
        result = sort_users_by_count(user_counts)
        
        # 應按字母順序排列
        self.assertEqual(result[0][0], "alice")
        self.assertEqual(result[1][0], "bob")
        self.assertEqual(result[2][0], "zoe")
    
    def test_sort_users_by_count_single_user(self):
        """單一使用者測試。"""
        user_counts = {"alice": 5}
        result = sort_users_by_count(user_counts)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ("alice", 5))


class TestLogSummaryIntegration(unittest.TestCase):
    """整合測試：log_summary 函式。"""
    
    def test_log_summary_homework_example(self):
        """使用 HOMEWORK.md 範例測試。"""
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("alice", "logout"),
            ("bob", "view"),
            ("bob", "view"),
            ("chris", "login"),
            ("bob", "logout")
        ]
        result = log_summary(logs)
        
        # 檢查使用者統計
        user_events = result['user_events']
        self.assertEqual(user_events[0], ("bob", 4))
        self.assertEqual(user_events[1], ("alice", 3))
        self.assertEqual(user_events[2], ("chris", 1))
        
        # 檢查最常見動作
        top_action, count = result['top_action']
        self.assertEqual(top_action, "login")
        self.assertEqual(count, 3)
    
    def test_log_summary_single_user(self):
        """單一使用者測試。"""
        logs = [
            ("alice", "login"),
            ("alice", "view"),
            ("alice", "logout")
        ]
        result = log_summary(logs)
        
        user_events = result['user_events']
        self.assertEqual(len(user_events), 1)
        self.assertEqual(user_events[0][0], "alice")
        self.assertEqual(user_events[0][1], 3)
        
        top_action, count = result['top_action']
        # 三個動作都出現一次，most_common 會返回其中一個
        self.assertEqual(count, 1)
    
    def test_log_summary_all_same_action(self):
        """全部相同動作測試。"""
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("chris", "login")
        ]
        result = log_summary(logs)
        
        user_events = result['user_events']
        self.assertEqual(len(user_events), 3)
        
        top_action, count = result['top_action']
        self.assertEqual(top_action, "login")
        self.assertEqual(count, 3)


if __name__ == '__main__':
    unittest.main()
