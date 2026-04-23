import unittest
from io import StringIO
import sys
import importlib

problem_10190 = importlib.import_module("10190")

class TestAutomaticUmbrella(unittest.TestCase):
    def test_sample(self):
        # 1 傘, 寬 10, 時間 10, 雨率 1
        # 傘: x=0, l=5, v=1
        # 總雨量 = 10 * 10 * 1 = 100
        # 吸收 = 5 * 10 * 1 = 50
        # 剩餘 = 50.00
        input_str = "1 10 10 1\n0 5 1\n"
        expected_output = "50.00\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10190.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
