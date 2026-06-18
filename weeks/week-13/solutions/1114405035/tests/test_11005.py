import unittest
import io
import sys
import importlib.util
import os

# 動態匯入上一層目錄的 11005.py 模組
module_name = "11005"
parent_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(parent_dir, f"{module_name}.py")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = module.solve

class Test11005(unittest.TestCase):
    def test_sample_case(self):
        input_text = """2
10 8 12 13 15 13 13 16 9 11 18 24 21 23 23 23 13 15 17 33 21 23 27 26 27 19 4 22 18 30 30 24 16 26 21 21
5
98329921
12345
800348
14
873645
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
4
0
1
10
100
"""
        expected_output = """Case 1:
Cheapest base(s) for number 98329921: 24
Cheapest base(s) for number 12345: 13 31
Cheapest base(s) for number 800348: 31
Cheapest base(s) for number 14: 13
Cheapest base(s) for number 873645: 22

Case 2:
Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 1: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 10: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 100: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
"""
        # 模擬標準輸入與輸出
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = io.StringIO(input_text.strip())
        sys.stdout = io.StringIO()
        
        try:
            solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

if __name__ == "__main__":
    unittest.main()
