import unittest
import io
import sys
import importlib.util
import os

# 動態匯入以支援數字開頭的模組名稱
module_name = "10812"
file_path = os.path.join(os.path.dirname(__file__), f"{module_name}.py")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = module.solve

class Test10812(unittest.TestCase):
    def test_sample_case(self):
        # 測試範例與預期輸出
        input_text = """2
40 20
20 40
"""
        expected_output = "30 10\nimpossible\n"
        
        # 模擬標準輸入與輸出
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = io.StringIO(input_text)
        sys.stdout = io.StringIO()
        
        try:
            solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

if __name__ == "__main__":
    unittest.main()
