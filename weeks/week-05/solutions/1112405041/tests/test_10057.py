import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
import sys
import importlib

problem_10057 = importlib.import_module("10057")

class TestMidSummerNightDream(unittest.TestCase):
    def test_sample_input(self):
        # æ¸¬è©¦è¼¸å…¥
        input_str = "2\n10\n10\n4\n1\n2\n2\n4\n"
        # ç¬¬ä?çµ? n=2, nums=[10, 10] -> ?’å? [10, 10], m1=10, m2=10, count=2, diff=1
        # ç¬¬ä?çµ? n=4, nums=[1, 2, 2, 4] -> ?’å? [1, 2, 2, 4], m1=2, m2=2, count=2, diff=1
        expected_output = "10 2 1\n2 2 1\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin

        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10057.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == '__main__':
    unittest.main()

