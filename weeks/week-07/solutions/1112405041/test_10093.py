import unittest
from io import StringIO
import sys
import importlib

problem_10093 = importlib.import_module("10093")

class TestArtillery(unittest.TestCase):
    def test_sample(self):
        # 1x2 map, all plain
        # P P
        # Max should be 1, because putting 2 would be within range (distance 1)
        input_str = "1 2\nPP\n"
        expected_output = "1\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10093.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
