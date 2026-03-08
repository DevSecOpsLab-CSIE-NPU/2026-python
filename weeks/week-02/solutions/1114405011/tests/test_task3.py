import pathlib
import sys
import unittest

p = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(p.parent.parent))

from task3_log_summary import format_output, parse_input, summarize


class MyTask3Test(unittest.TestCase):
    def test_case1_sample(self):
        lines = [
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
        arr = parse_input(lines)
        users, top = summarize(arr)
        self.assertEqual(users, [("bob", 4), ("alice", 3), ("chris", 1)])
        self.assertEqual(top, ("login", 3))

    def test_case2_empty(self):
        arr = parse_input(["0"])
        users, top = summarize(arr)
        self.assertEqual(users, [])
        self.assertEqual(top, ("None", 0))

    def test_case3_tie(self):
        arr = [
            ("u1", "view"),
            ("u2", "login"),
            ("u3", "view"),
            ("u4", "login"),
        ]
        _, top = summarize(arr)
        self.assertEqual(top, ("login", 2))

    def test_case4_text(self):
        s = format_output([("bob", 2), ("amy", 1)], ("view", 2))
        self.assertTrue("top_action: view 2" in s)


if __name__ == "__main__":
    unittest.main()
