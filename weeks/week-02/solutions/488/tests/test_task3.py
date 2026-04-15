import pathlib
import sys
import unittest

BASE_DIR = pathlib.Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from task3_log_summary import summarize_logs


class TestTask3LogSummary(unittest.TestCase):
    def test_normal_case(self):
        records = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("alice", "logout"),
            ("bob", "view"),
            ("bob", "view"),
            ("chris", "login"),
            ("bob", "logout"),
        ]
        user_counts, top_action = summarize_logs(records)
        self.assertEqual(user_counts, [("bob", 4), ("alice", 3), ("chris", 1)])
        self.assertEqual(top_action, ("login", 3))

    def test_empty_records(self):
        user_counts, top_action = summarize_logs([])
        self.assertEqual(user_counts, [])
        self.assertIsNone(top_action)

    def test_action_tie_uses_name_asc(self):
        records = [("u1", "b"), ("u2", "a")]
        _, top_action = summarize_logs(records)
        self.assertEqual(top_action, ("a", 1))


if __name__ == "__main__":
    unittest.main()
