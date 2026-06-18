import unittest
import io
import sys
import importlib.util
import os

# 動態匯入上一層目錄的 11332.py 模組
module_name = "11332"
parent_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(parent_dir, f"{module_name}.py")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = module.solve

class Test11332(unittest.TestCase):
    def test_sample_case_1(self):
        # 兩個鏡子，一個在 x=1 (y從-1到1)，另一個在 x=2 (y從-2到2)
        # 第一個會把第二個完全擋住，所以只有第一個可見
        input_text = """2
1 -1 1 1
2 -2 2 2
"""
        expected_output = "1 0\n"
        
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

    def test_sample_case_2(self):
        # 第一個鏡子在 (1,0) 到 (1,2)
        # 第二個鏡子在 (2,-2) 到 (2,2)
        # 兩個都可見，因為第二個鏡子在下方 (2,-2) 到 (2,0) 的部分不會被擋住
        input_text = """2
1 0 1 2
2 -2 2 2
"""
        expected_output = "1 1\n"
        
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
