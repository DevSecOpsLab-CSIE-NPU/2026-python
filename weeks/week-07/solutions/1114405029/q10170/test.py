import unittest
import io
import sys
from contextlib import redirect_stdout

class TestQ10170(unittest.TestCase):
    def run_test(self, solve_func, input_str):
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(input_str)
        stdout_capture = io.StringIO()
        with redirect_stdout(stdout_capture):
            solve_func()
        sys.stdin = stdin_backup
        return stdout_capture.getvalue().strip()

    def test_samples(self):
        # 測試範例 1: S=1, D=6 -> 1(1)+2(2)+3(3) = 6天，答案為 3
        # 測試範例 2: S=3, D=10 -> 3(3)+4(4)+5(5) = 12天，第10天在5人團內
        test_input = "1 6\n3 10"
        expected = "3\n5"
        
        import main
        import main_easy
        import main_handwritten
        
        for func in [main.solve, main_easy.solve, main_handwritten.solve]:
            with self.subTest(version=func.__name__):
                result = self.run_test(func, test_input)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()