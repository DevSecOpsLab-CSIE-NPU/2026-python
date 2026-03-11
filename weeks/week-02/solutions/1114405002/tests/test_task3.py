import unittest
from task3 import log_summary

class TestLogSummary(unittest.TestCase):
    def test_normal_case(self):
        logs = [
            ('alice', 'login'),
            ('bob', 'login'),
            ('alice', 'view'),
            ('alice', 'logout'),
            ('bob', 'view'),
            ('bob', 'view'),
            ('chris', 'login'),
            ('bob', 'logout')
        ]
        expected_users = [('bob', 4), ('alice', 3), ('chris', 1)]
        expected_top_action = ('login', 3)
        users, top_action = log_summary(logs)
        self.assertEqual(users, expected_users)
        self.assertEqual(top_action, expected_top_action)

    def test_empty_logs(self):
        logs = []
        expected_users = []
        expected_top_action = (None, 0)
        users, top_action = log_summary(logs)
        self.assertEqual(users, expected_users)
        self.assertEqual(top_action, expected_top_action)

    def test_single_user_multiple_actions(self):
        logs = [
            ('alice', 'login'),
            ('alice', 'view'),
            ('alice', 'logout')
        ]
        expected_users = [('alice', 3)]
        expected_top_action = ('login', 1)  # assuming tie, pick first
        users, top_action = log_summary(logs)
        self.assertEqual(users, expected_users)
        self.assertEqual(top_action, expected_top_action)

if __name__ == '__main__':
    unittest.main()
