import unittest

from task3_log_summary import format_summary, summarize_logs


class TestTask3LogSummary(unittest.TestCase):
    def test_example_summary(self):
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
        users, top_action = summarize_logs(lines)
        self.assertEqual(users, [("bob", 4), ("alice", 3), ("chris", 1)])
        self.assertEqual(top_action, ("login", 3))

    def test_tie_top_action(self):
        lines = [
            "u1 a",
            "u2 b",
            "u3 a",
            "u4 b",
        ]
        users, top_action = summarize_logs(lines)
        # Both a and b appear 2 times; choose lexicographically smaller
        self.assertEqual(top_action, ("a", 2))

    def test_empty_logs(self):
        users, top_action = summarize_logs([])
        self.assertEqual(users, [])
        self.assertEqual(top_action, ("", 0))

    def test_format_summary(self):
        out = format_summary([("bob", 4), ("alice", 3)], ("login", 4))
        expected = "bob 4\nalice 3\ntop_action: login 4"
        self.assertEqual(out, expected)


if __name__ == "__main__":
    unittest.main()
