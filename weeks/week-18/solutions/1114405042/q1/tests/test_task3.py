import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from task3_log_summary import summarize_logs, format_output


class TestLogSummary(unittest.TestCase):

    def setUp(self):
        self.logs = [
            "alice login",
            "bob login",
            "alice view",
            "alice logout",
            "bob view",
            "bob view",
            "chris login",
            "bob logout",
        ]

    def test_normal_case(self):
        result = summarize_logs(self.logs)
        self.assertEqual(result["user_counts"], [("bob", 4), ("alice", 3), ("chris", 1)])
        self.assertEqual(result["top_action"], ("login", 3))

    def test_empty_logs(self):
        result = summarize_logs([])
        self.assertEqual(result["user_counts"], [])
        self.assertEqual(result["top_action"], ("", 0))

    def test_single_user_single_action(self):
        result = summarize_logs(["alice login"])
        self.assertEqual(result["user_counts"], [("alice", 1)])
        self.assertEqual(result["top_action"], ("login", 1))

    def test_tie_user_counts_sorted_by_name(self):
        logs = ["bob view", "bob view", "alice view", "alice view"]
        result = summarize_logs(logs)
        self.assertEqual(result["user_counts"], [("alice", 2), ("bob", 2)])

    def test_format_output(self):
        result = {
            "user_counts": [("bob", 4), ("alice", 3)],
            "top_action": ("login", 3),
        }
        output = format_output(result)
        self.assertIn("bob 4", output)
        self.assertIn("alice 3", output)
        self.assertIn("top_action: login 3", output)


if __name__ == "__main__":
    unittest.main()
