import unittest
from io import StringIO
import sys
import importlib

problem_10221 = importlib.import_module("10221")

class TestSatellites(unittest.TestCase):
    def test_sample(self):
        input_str = "500 30 deg\n700 60 min\n200 45 deg\n"
        expected_output = "3633.775503 3592.408346\n124.616509 124.614927\n5215.043805 5082.035982\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10221.solve()
            # 使用 split() 檢查數字，避免浮點數微小差異導致斷言失敗
            actual_lines = sys.stdout.getvalue().strip().split('\n')
            expected_lines = expected_output.strip().split('\n')
            for a, e in zip(actual_lines, expected_lines):
                a_parts = list(map(float, a.split()))
                e_parts = list(map(float, e.split()))
                for ap, ep in zip(a_parts, e_parts):
                    self.assertAlmostEqual(ap, ep, places=6)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
