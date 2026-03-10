import unittest
from task3_log_summary import summarize_logs

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
        user_counts, top_action = summarize_logs(logs)
        expected_users = [('bob', 4), ('alice', 3), ('chris', 1)]
        self.assertEqual(user_counts, expected_users)
        self.assertEqual(top_action, ('login', 3))

    def test_single_user(self):
        logs = [
            ('user1', 'action1'),
            ('user1', 'action2'),
            ('user1', 'action1')
        ]
        user_counts, top_action = summarize_logs(logs)
        expected_users = [('user1', 3)]
        self.assertEqual(user_counts, expected_users)
        self.assertEqual(top_action, ('action1', 2))

    def test_tie_in_actions(self):
        logs = [
            ('a', 'x'),
            ('a', 'y'),
            ('b', 'x'),
            ('b', 'y')
        ]
        user_counts, top_action = summarize_logs(logs)
        expected_users = [('a', 2), ('b', 2)]
        self.assertEqual(user_counts, expected_users)
        # Since tie, it should pick one of the max, but test assumes 'x' or 'y'
        self.assertIn(top_action[0], ['x', 'y'])
        self.assertEqual(top_action[1], 2)

    def test_empty_logs(self):
        logs = []
        user_counts, top_action = summarize_logs(logs)
        self.assertEqual(user_counts, [])
        self.assertIsNone(top_action)

    def test_one_log(self):
        logs = [('user', 'act')]
        user_counts, top_action = summarize_logs(logs)
        expected_users = [('user', 1)]
        self.assertEqual(user_counts, expected_users)
        self.assertEqual(top_action, ('act', 1))

if __name__ == '__main__':
    unittest.main()