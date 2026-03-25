import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from task3_log_summary import summarize_logs


class TestTask3LogSummary(unittest.TestCase):
    """Test suite for log summary with counting and grouping"""

    def test_normal_case(self):
        """Test normal case from problem description"""
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
        
        # user_counts should be sorted by count (desc), then name (asc)
        self.assertEqual(len(user_counts), 3)
        self.assertEqual(user_counts[0], ("bob", 4))
        self.assertEqual(user_counts[1], ("alice", 3))
        self.assertEqual(user_counts[2], ("chris", 1))
        
        # top_action should be ("login", 3)
        self.assertEqual(top_action, ("login", 3))

    def test_empty_logs(self):
        """Test boundary case with no logs"""
        logs = []
        user_counts, top_action = summarize_logs(logs)
        
        self.assertEqual(len(user_counts), 0)
        self.assertEqual(top_action, (None, 0))

    def test_single_log(self):
        """Test boundary case with single log entry"""
        logs = [("alice", "login")]
        user_counts, top_action = summarize_logs(logs)
        
        self.assertEqual(len(user_counts), 1)
        self.assertEqual(user_counts[0], ("alice", 1))
        self.assertEqual(top_action, ("login", 1))

    def test_single_user(self):
        """Test with only one user multiple actions"""
        logs = [
            ("alice", "login"),
            ("alice", "view"),
            ("alice", "logout"),
        ]
        user_counts, top_action = summarize_logs(logs)
        
        self.assertEqual(len(user_counts), 1)
        self.assertEqual(user_counts[0], ("alice", 3))
        self.assertEqual(top_action[1], 1)  # Each action appears once

    def test_same_user_count_sorted_by_name(self):
        """Test that users with same count are sorted by name"""
        logs = [
            ("zoe", "login"),
            ("alice", "login"),
            ("bob", "view"),
        ]
        user_counts, top_action = summarize_logs(logs)
        
        # All have count 1, should be sorted alphabetically: alice, bob, zoe
        self.assertEqual(len(user_counts), 3)
        self.assertEqual(user_counts[0][0], "alice")
        self.assertEqual(user_counts[1][0], "bob")
        self.assertEqual(user_counts[2][0], "zoe")

    def test_top_action_with_tie(self):
        """Test top action count when there's a tie (should return any with highest count)"""
        logs = [
            ("alice", "login"),
            ("bob", "logout"),
            ("alice", "view"),
            ("bob", "view"),
        ]
        user_counts, top_action = summarize_logs(logs)
        
        # All actions appear twice, top_action should have count 2
        self.assertEqual(top_action[1], 2)

    def test_many_actions_one_most_common(self):
        """Test clearly identifiable top action"""
        logs = [
            ("alice", "login"),
            ("alice", "login"),
            ("alice", "login"),
            ("bob", "logout"),
            ("bob", "logout"),
            ("charlie", "view"),
        ]
        user_counts, top_action = summarize_logs(logs)
        
        # login appears 3 times, logout 2 times, view 1 time
        self.assertEqual(top_action, ("login", 3))
        
        # user counts: alice 3, bob 2, charlie 1
        self.assertEqual(user_counts[0], ("alice", 3))
        self.assertEqual(user_counts[1], ("bob", 2))
        self.assertEqual(user_counts[2], ("charlie", 1))

    def test_different_actions_same_user(self):
        """Test counting different action types for same user"""
        logs = [
            ("alice", "login"),
            ("alice", "view"),
            ("alice", "view"),
            ("alice", "logout"),
        ]
        user_counts, top_action = summarize_logs(logs)
        
        # alice should have count 4 (total actions)
        self.assertEqual(user_counts[0], ("alice", 4))
        
        # view appears 2 times (most common)
        self.assertEqual(top_action, ("view", 2))

    def test_case_sensitivity(self):
        """Test that user names and actions are case-sensitive"""
        logs = [
            ("Alice", "login"),
            ("alice", "login"),
            ("bob", "Login"),
        ]
        user_counts, top_action = summarize_logs(logs)
        
        # Alice, alice, and bob are different users
        self.assertEqual(len(user_counts), 3)
        # login and Login are different actions
        # login appears 2 times, Login appears 1 time
        self.assertEqual(top_action, ("login", 2))


if __name__ == '__main__':
    unittest.main()
