import unittest

from task3_log_summary import solve


class TestTask3LogSummary(unittest.TestCase):
    def test_summary_matches_example(self):
        raw = "\n".join(
            [
                "8",
                "alice login",
                "bob login",
                "alice view",
                "alice logout",
                "bob view",
                "bob view",
                "chris login",
                "bob logout",
            ]
        )
        expected = "\n".join(
            [
                "bob 4",
                "alice 3",
                "chris 1",
                "top_action: login 3",
            ]
        )
        self.assertEqual(solve(raw), expected)

    def test_user_sort_tie_break_by_name(self):
        raw = "\n".join(
            [
                "4",
                "bob login",
                "alice view",
                "bob logout",
                "alice login",
            ]
        )
        expected = "\n".join(
            [
                "alice 2",
                "bob 2",
                "top_action: login 2",
            ]
        )
        self.assertEqual(solve(raw), expected)

    def test_empty_log_input(self):
        self.assertEqual(solve("0"), "top_action: none 0")


if __name__ == "__main__":
    unittest.main()
