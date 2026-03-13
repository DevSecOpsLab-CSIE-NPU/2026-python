import unittest

from task3_log_summary import summarize_logs


class TestTask3(unittest.TestCase):
    def test_normal_log_summary(self):
        entries = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("alice", "logout"),
            ("bob", "view"),
            ("bob", "view"),
            ("chris", "login"),
            ("bob", "logout"),
        ]
        users, top_action = summarize_logs(entries)
        self.assertEqual(users, [("bob", 4), ("alice", 3), ("chris", 1)])
        self.assertEqual(top_action, ("login", 3))

    def test_empty_input(self):
        users, top_action = summarize_logs([])
        self.assertEqual(users, [])
        self.assertEqual(top_action, ("NONE", 0))

    def test_action_tie_break_by_name(self):
        entries = [
            ("u1", "view"),
            ("u2", "login"),
            ("u3", "view"),
            ("u4", "login"),
        ]
        _, top_action = summarize_logs(entries)
        self.assertEqual(top_action, ("login", 2))


if __name__ == "__main__":
    unittest.main()
