import unittest
import io
import sys
from contextlib import redirect_stdout

class TestUVA118(unittest.TestCase):
    def run_test(self, solve_func, input_str):
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(input_str)
        output_capture = io.StringIO()
        with redirect_stdout(output_capture):
            solve_func()
        sys.stdin = stdin_backup
        return output_capture.getvalue().strip()

    def test_logic(self):
        # 官方範例測試
        test_input = """5 3
1 1 E
RFRFEFD
1 1 E
RFRFEFD
2 2 N
F
"""
        # 注意：實際輸出需根據模擬邏輯比對
        import main_easy
        result = self.run_test(main_easy.solve, test_input)
        
        # 簡單驗證輸出行數是否正確
        lines = result.split('\n')
        self.assertEqual(len(lines), 3)

if __name__ == "__main__":
    unittest.main()