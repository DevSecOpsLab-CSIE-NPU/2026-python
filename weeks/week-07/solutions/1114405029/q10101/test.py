import unittest
import io
import sys
from contextlib import redirect_stdout

class TestQ10101(unittest.TestCase):
    def run_test(self, solve_func, input_str):
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(input_str + "\n#") # 加上終止符號
        stdout_capture = io.StringIO()
        with redirect_stdout(stdout_capture):
            solve_func()
        sys.stdin = stdin_backup
        return stdout_capture.getvalue().strip()

    def test_simple_move(self):
        # 1+1=3 移動 3 的一根木棒變成 2
        test_input = "1+1=3"
        # 注意：正確答案可能是 1+1=2 或其他成立的等式
        import main_easy
        result = self.run_test(main_easy.solve, test_input)
        
        # 驗證輸出的等式是否真的成立
        left, right = result.split('=')
        self.assertEqual(eval(left), eval(right))

if __name__ == "__main__":
    unittest.main()