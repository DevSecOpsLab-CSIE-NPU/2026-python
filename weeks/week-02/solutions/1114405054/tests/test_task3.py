from __future__ import annotations

import pathlib
import sys
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from task3_log_summary import solve, summarize  # noqa: E402


class TestTask3LogSummary(unittest.TestCase):
    def test_sample_case(self) -> None:
        raw_input = (
            "8\n"
            "alice login\n"
            "bob login\n"
            "alice view\n"
            "alice logout\n"
            "bob view\n"
            "bob view\n"
            "chris login\n"
            "bob logout\n"
        )
        expected = "bob 4\nalice 3\nchris 1\ntop_action: login 3"
        self.assertEqual(solve(raw_input), expected)

    def test_empty_logs(self) -> None:
        self.assertEqual(solve("0\n"), "top_action: none 0")

    def test_action_tie_uses_lexicographical_order(self) -> None:
        users, top_action = summarize([("u1", "view"), ("u2", "login")])
        self.assertEqual(users, [("u1", 1), ("u2", 1)])
        self.assertEqual(top_action, ("login", 1))


if __name__ == "__main__":
    unittest.main()