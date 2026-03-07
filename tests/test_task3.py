import unittest
from task3_log_summary import summarize_logs
class TestTask3(unittest.TestCase):
    def test_sum(self):
        u, a, c = summarize_logs([("a", "l"), ("b", "l"), ("a", "v")])
        self.assertEqual(u[0][0], "a")
    def test_empty(self):
        u, a, c = summarize_logs([])
        self.assertEqual(len(u), 0)
    def test_tie(self):
        u, a, c = summarize_logs([("b", "l"), ("a", "l")])
        self.assertEqual(u[0][0], "a")
