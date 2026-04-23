import unittest
from io import StringIO
import sys
import importlib

problem_10193 = importlib.import_module("10193")

class TestArctan(unittest.TestCase):
    def test_sample(self):
        # a = 1 => k = 1*1+1 = 2. Factors: 1, 2. x=1, y=2.
        # b+c = 1+2 + 2*1 = 5
        input_str = "1"
        expected_output = "5\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10193.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
