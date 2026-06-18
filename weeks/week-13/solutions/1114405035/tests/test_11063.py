import unittest
import io
import sys
import importlib.util
import os

# 動態匯入上一層目錄的 11063.py 模組
module_name = "11063"
parent_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(parent_dir, f"{module_name}.py")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = module.solve

class Test11063(unittest.TestCase):
    def test_sample_case(self):
        input_text = """2
255 3 192 254 16 171
224 51 167 160 34 8
"""
        expected_output = """163.1271 82.0146 169.9752
163.4547 89.1162 153.7144
158.7189 104.3614 153.9368
94.6992 65.7712 15.0144
The average of Y is 85.3159
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
