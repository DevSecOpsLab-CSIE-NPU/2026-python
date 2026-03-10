import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task3_log_summary import summarize_logs

class TestTask3(unittest.TestCase):
    def test_normal_summary(self):
       
        logs = [("alice", "login"), ("bob", "login"), ("alice", "view")]
        users, top = summarize_logs(logs)
        self.assertEqual(users[0], ("alice", 2)) # alice 次數最多
        self.assertEqual(top, ("login", 2))

    def test_empty_log(self):
       
        users, top = summarize_logs([])
        self.assertEqual(users, [])
        self.assertIsNone(top)

    def test_user_alphabetical_tie(self):
        
        logs = [("zed", "login"), ("apple", "login")]
        users, _ = summarize_logs(logs)
        self.assertEqual(users[0][0], "apple") # a 比 z 優先