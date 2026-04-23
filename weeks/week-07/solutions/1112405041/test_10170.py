import unittest
from io import StringIO
import sys
import importlib

problem_10170 = importlib.import_module("10170")

class TestInfiniteRooms(unittest.TestCase):
    def test_sample(self):
        # 1 6 => 1(day1), 2(day2-3), 3(day4-6). 第 6 天應該是 3 人團
        # 3 10 => 3(day1-3), 4(day4-7), 5(day8-12). 第 10 天應該是 5 人團
        input_str = "1 6\n3 10\n"
        expected_output = "3\n5\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10170.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
