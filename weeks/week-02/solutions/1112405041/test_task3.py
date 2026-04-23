# test_task3.py
import unittest
from task3 import summarize_logs

class TestTask3(unittest.TestCase):
    def test_log_summary(self):
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("bob", "view"),
            ("bob", "view")
        ]
        sorted_users, top_action = summarize_logs(logs)
        # bob: 3, alice: 2
        self.assertEqual(sorted_users[0], ("bob", 3))
        self.assertEqual(sorted_users[1], ("alice", 2))
        # top_action: (login, 2) or (view, 3) -> view: 3
        self.assertEqual(top_action, ("view", 3))

    def test_empty_logs(self):
        sorted_users, top_action = summarize_logs([])
        self.assertEqual(sorted_users, {})
        self.assertEqual(top_action[1], 0)

if __name__ == "__main__":
    unittest.main()
