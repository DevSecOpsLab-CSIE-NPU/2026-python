import unittest
from task3_log_summary import summarize_logs

class TestTask3(unittest.TestCase):
    def test_normal_logs(self):
        logs = ['INFO', 'ERROR', 'INFO', 'WARN']
        expected = {'INFO': 2, 'ERROR': 1, 'WARN': 1}
        self.assertEqual(dict(summarize_logs(logs)), expected)

    def test_empty_logs(self):
        self.assertEqual(dict(summarize_logs([])), {})

    def test_single_log_type(self):
        logs = ['DEBUG', 'DEBUG', 'DEBUG']
        expected = {'DEBUG': 3}
        self.assertEqual(dict(summarize_logs(logs)), expected)

    def test_mixed_logs(self):
        logs = ['INFO', 'ERROR', 'INFO', 'ERROR', 'WARN', 'WARN', 'WARN']
        expected = {'INFO': 2, 'ERROR': 2, 'WARN': 3}
        self.assertEqual(dict(summarize_logs(logs)), expected)

if __name__ == '__main__':
    unittest.main()