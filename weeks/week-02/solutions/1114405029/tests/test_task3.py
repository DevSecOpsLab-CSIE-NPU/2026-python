import unittest
from task3_log_summary import summarize_logs


class TestLogSummary(unittest.TestCase):

    def test_normal_logs(self):
        records = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("alice", "logout"),
            ("bob", "view"),
            ("bob", "view"),
            ("chris", "login"),
            ("bob", "logout")
        ]

        users, top = summarize_logs(records)

        self.assertEqual(users[0], ("bob", 4))
        self.assertEqual(users[1], ("alice", 3))
        self.assertEqual(users[2], ("chris", 1))

        self.assertEqual(top, ("login", 3))

    def test_empty_input(self):
        records = []
        users, top = summarize_logs(records)

        self.assertEqual(users, [])
        self.assertEqual(top, (None, 0))

    def test_single_record(self):
        records = [("alice", "login")]

        users, top = summarize_logs(records)

        self.assertEqual(users, [("alice", 1)])
        self.assertEqual(top, ("login", 1))

    def test_tie_user_sorting(self):
        records = [
            ("alice", "login"),
            ("bob", "view")
        ]

        users, top = summarize_logs(records)

        # same count → alphabetical order
        self.assertEqual(users[0][0], "alice")
        self.assertEqual(users[1][0], "bob")

    def test_action_count(self):
        records = [
            ("alice", "login"),
            ("bob", "login"),
            ("chris", "view"),
            ("david", "login")
        ]

        users, top = summarize_logs(records)

        self.assertEqual(top, ("login", 3))


if __name__ == "__main__":
    unittest.main()