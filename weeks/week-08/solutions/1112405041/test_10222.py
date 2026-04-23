import unittest
from io import StringIO
import sys
import importlib

# 更新測試以符合魔改後的「優質學生判斷」需求
problem_10222 = importlib.import_module("10222")

class TestQualityStudent(unittest.TestCase):
    def test_quality_id(self):
        # 輸入 1112405041 應該輸出 yes
        input_str = "1112405041"
        expected_output = "yes"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10222.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

    def test_invalid_id(self):
        # 非數字輸入
        input_str = "abc"
        expected_output = "no"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10222.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
