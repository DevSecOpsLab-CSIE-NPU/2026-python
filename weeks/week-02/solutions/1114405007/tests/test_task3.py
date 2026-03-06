import unittest

from task3_log_summary import summarize_logs


class TestTask3(unittest.TestCase):
    def test_summarize_logs_example_case(self) -> None:
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
        users, top_action = summarize_logs(records)
        self.assertEqual(users, [("bob", 4), ("alice", 3), ("chris", 1)])
        self.assertEqual(top_action, ("login", 3))

    def test_summarize_logs_empty_input(self) -> None:
        users, top_action = summarize_logs([])
        self.assertEqual(users, [])
        self.assertIsNone(top_action)

    def test_summarize_logs_user_tie_break_by_name(self) -> None:
        records = [("zoe", "x"), ("amy", "y")]
        users, _ = summarize_logs(records)
        self.assertEqual(users, [("amy", 1), ("zoe", 1)])

    def test_summarize_logs_action_tie_break_by_action_name(self) -> None:
        records = [("amy", "view"), ("bob", "login")]
        _, top_action = summarize_logs(records)
        self.assertEqual(top_action, ("login", 1))


if __name__ == "__main__":
    unittest.main()
