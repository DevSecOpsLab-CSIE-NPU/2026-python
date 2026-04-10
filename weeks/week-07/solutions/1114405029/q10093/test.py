import unittest
import io
import sys
from contextlib import redirect_stdout

class TestQ10093(unittest.TestCase):
    def run_test(self, solve_func, input_str):
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(input_str)
        stdout_capture = io.StringIO()
        with redirect_stdout(stdout_capture):
            solve_func()
        sys.stdin = stdin_backup
        return stdout_capture.getvalue().strip()

    def test_sample(self):
        # 範例測試用例
        test_input = "5 4\nPHPP\nPPHH\nPPPP\nPHPP\nPHHP"
        expected = "6"
        
        # 引入模組
        import main
        import main_easy
        import main_handwritten
        
        for func in [main.solve, main_easy.solve, main_handwritten.solve]:
            with self.subTest(version=func.__name__):
                result = self.run_test(func, test_input)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()