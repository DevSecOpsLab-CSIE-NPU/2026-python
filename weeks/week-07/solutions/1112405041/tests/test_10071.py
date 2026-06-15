import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
import sys
import importlib

problem_10071 = importlib.import_module("10071")

class TestSixTuple(unittest.TestCase):
    def test_sample(self):
        # ?†å? S = {1}
        # a+b+c+d+e = f => 1+1+1+1+1 = 1 (ä¸æ?ç«?
        # ä½†å???S = {0}, ??0+0+0+0+0 = 0 (?ç?, 1ç¨?
        input_str = "1\n0\n"
        expected_output = "1\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10071.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()

