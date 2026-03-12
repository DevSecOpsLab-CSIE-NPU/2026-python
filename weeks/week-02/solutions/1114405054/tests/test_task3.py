import unittest
from task3_log_summary import summarize_logs

class TestTask3(unittest.TestCase):
    def test_summary(self):
        logs = [("alice", "login"), ("bob", "login"), ("alice", "view")]
        users, action, count = summarize_logs(logs)
        self.assertEqual(users[0], ("alice", 2))
        self.assertEqual(action, "login")
    def test_empty(self):
        users, action, count = summarize_logs([])
        self.assertEqual(len(users), 0)
    def test_user_order(self):
        logs = [("bob", "login"), ("alice", "login")]
        users, _, _ = summarize_logs(logs)
        self.assertEqual(users[0][0], "alice")