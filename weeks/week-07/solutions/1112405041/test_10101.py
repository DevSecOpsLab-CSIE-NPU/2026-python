import unittest
from io import StringIO
import sys
import importlib

# 由於檔案名稱以數字開頭，我們使用 importlib 來動態匯入
problem_10101 = importlib.import_module("10101-easy")

class TestMatchstick(unittest.TestCase):
    def test_no_solution(self):
        # 測試無解的情況
        input_str = "1+1=1#"
        expected_output = "No\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            # 這裡呼叫 easy 版的 main
            problem_10101.main()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
