import unittest

from task3_log_summary import format_summary, parse_events, solve, summarize_events


class Task3LogSummaryTests(unittest.TestCase):
    def test_summarize_events_counts_users_and_actions(self):
        events = [("alice", "login"), ("bob", "login"), ("alice", "view"), ("bob", "view")]
        user_totals, top_action = summarize_events(events)
        self.assertEqual(user_totals, [("alice", 2), ("bob", 2)])
        self.assertEqual(top_action, ("login", 2))

    def test_parse_events_handles_empty_input(self):
        self.assertEqual(parse_events("0\n"), [])

    def test_format_summary_renders_expected_text(self):
        result = format_summary([("bob", 4), ("alice", 3)], ("login", 3))
        self.assertEqual(result, "bob 4\nalice 3\ntop_action: login 3")

    def test_solve_handles_sample_input(self):
        text = "8\nalice login\nbob login\nalice view\nalice logout\nbob view\nbob view\nchris login\nbob logout\n"
        expected = "bob 4\nalice 3\nchris 1\ntop_action: login 3"
        self.assertEqual(solve(text), expected)

    def test_solve_handles_zero_events(self):
        self.assertEqual(solve("0\n"), "top_action: none 0")


if __name__ == "__main__":
    unittest.main()