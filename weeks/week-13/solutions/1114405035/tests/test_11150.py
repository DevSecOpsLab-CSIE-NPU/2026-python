import unittest
import io
import sys
import importlib.util
import os

# 動態匯入上一層目錄的 11150.py 模組
module_name = "11150"
parent_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(parent_dir, f"{module_name}.py")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = module.solve

class Test11150(unittest.TestCase):
    def test_sample_case(self):
        input_text = """10
2 3 5
2 3 5 6 7
"""
        expected_output = "2\n"
        
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
