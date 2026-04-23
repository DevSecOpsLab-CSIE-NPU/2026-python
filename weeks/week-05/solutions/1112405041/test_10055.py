import unittest
from io import StringIO
import sys
import importlib

problem_10055 = importlib.import_module("10055")

class TestCompositeFunction(unittest.TestCase):
    def test_sample_input(self):
        # 測試輸入：
        # 3 個函數，5 次操作
        # 一開始: f1, f2, f3 = 增, 增, 增 (0, 0, 0)
        # 1. 查詢 1~3 -> 0^0^0 = 0
        # 2. 反轉 f2 -> f2 變 1 (減)
        # 3. 查詢 1~3 -> 0^1^0 = 1
        # 4. 反轉 f2 -> f2 變 0 (增)
        # 5. 查詢 1~3 -> 0^0^0 = 0
        input_str = "3 5\n2 1 3\n1 2\n2 1 3\n1 2\n2 1 3\n"
        expected_output = "0\n1\n0\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin

        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10055.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == '__main__':
    unittest.main()
