import unittest
import io
import sys
import importlib.util
import os

# 動態匯入上一層目錄的 11321.py 模組
module_name = "11321"
parent_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(parent_dir, f"{module_name}.py")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = module.solve

class Test11321(unittest.TestCase):
    def test_sample_case(self):
        # 測試 3x3 的路徑與陷阱設置
        input_text = """3 3 3
2 0
0 2
1 1
"""
        expected_output = """<(_ _)>
<(_ _)>
>_<
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

    def test_sample_case_2(self):
        # 測試 3x3 另一個情況，前三個可以放，第四個會堵死
        input_text = """3 3 4
2 0
0 2
1 0
1 1
"""
        expected_output = """<(_ _)>
<(_ _)>
<(_ _)>
>_<
"""
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
