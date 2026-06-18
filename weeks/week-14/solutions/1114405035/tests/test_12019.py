import unittest
import io
import sys
import importlib.util
import os

# 動態匯入上一層目錄的 12019.py 模組
module_name = "12019"
parent_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(parent_dir, f"{module_name}.py")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = module.solve

class Test12019(unittest.TestCase):
    def test_sample_case(self):
        input_text = """8
1 6
2 28
4 5
5 26
8 1
11 1
12 25
12 31
"""
        expected_output = """Thursday
Monday
Tuesday
Thursday
Monday
Tuesday
Sunday
Saturday
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
