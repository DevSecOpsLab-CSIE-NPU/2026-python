import unittest
from io import StringIO
import sys
import importlib

problem_10189 = importlib.import_module("10189")

class TestMinesweeper(unittest.TestCase):
    def test_sample_input(self):
        # 測試範例輸入
        input_str = "4 4\n*...\n....\n.*..\n....\n3 5\n**...\n.....\n.*...\n0 0\n"
        expected_output = "Field #1:\n*100\n2210\n1*10\n1110\n\nField #2:\n**100\n33200\n1*100\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10189.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
