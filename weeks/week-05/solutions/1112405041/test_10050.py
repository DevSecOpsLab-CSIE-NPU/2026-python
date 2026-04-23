import unittest
from io import StringIO
import sys
import importlib

problem_10050 = importlib.import_module("10050")

class TestHartals(unittest.TestCase):
    def test_sample_input(self):
        # 範例輸入
        # 2 組測資
        # 1: 14 天, 3 政黨 (3, 4, 8) -> 損失 5 天
        # 2: 100 天, 4 政黨 (12, 15, 25, 40) -> 損失 15 天
        input_str = "2\n14\n3\n3\n4\n8\n100\n4\n12\n15\n25\n40\n"
        expected_output = "5\n15\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin

        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10050.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == '__main__':
    unittest.main()
