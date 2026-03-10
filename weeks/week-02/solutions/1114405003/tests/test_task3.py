import unittest
from task3_log_summary import log_summary

class TestTask3LogSummary(unittest.TestCase):
    def test_normal_case(self):
        lines = [
            '8',
            'alice login',
            'bob login',
            'alice view',
            'alice logout',
            'bob view',
            'bob view',
            'chris login',
            'bob logout',
        ]
        users, top_action = log_summary(lines)
        self.assertEqual(users, ['bob 4', 'alice 3', 'chris 1'])
        self.assertEqual(top_action, 'top_action: login 3')

    def test_no_records(self):
        users, top_action = log_summary(['0'])
        self.assertEqual(users, [])
        self.assertEqual(top_action, 'top_action:  0')

    def test_tie_top_action(self):
        lines = [
            '4',
            'u1 a',
            'u2 b',
            'u1 b',
            'u3 a',
        ]
        users, top_action = log_summary(lines)
        self.assertEqual(users, ['u1 2', 'u2 1', 'u3 1'])
        self.assertEqual(top_action, 'top_action: a 2')
