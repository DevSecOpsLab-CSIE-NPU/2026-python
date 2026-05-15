import unittest
import io
import sys
import importlib.util
import os

# 動態匯入數字開頭的模組
module_name = "10922"
file_path = os.path.join(os.path.dirname(__file__), f"{module_name}.py")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = module.solve

class Test10922(unittest.TestCase):
    def test_sample_case(self):
        input_text = """999
9
181
0
"""
        expected_output = "999 is a multiple of 9 and has 9-degree 2.\n9 is a multiple of 9 and has 9-degree 1.\n181 is not a multiple of 9.\n"
        
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
