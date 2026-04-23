import unittest
from io import StringIO
import sys
import importlib

problem_10062 = importlib.import_module("10062")

class TestCowSorting(unittest.TestCase):
    def test_sample(self):
        # 3 頭牛
        # 第 2 個位置前面有 1 個比它小 (1)
        # 第 3 個位置前面有 1 個比它小 (1)
        # 順序推算: 1, 2, 3 ->
        # 最後一個 (pos 3) 前面有 1 個比它小，剩下 {1,2,3} 中選第 2 小的是 2
        # 第二個 (pos 2) 前面有 1 個比它小，剩下 {1,3} 中選第 2 小的是 3
        # 第一個 (pos 1) 剩下 1
        # 結果應為 1, 3, 2
        input_str = "3\n1\n1\n"
        expected_output = "1\n3\n2\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10062.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
