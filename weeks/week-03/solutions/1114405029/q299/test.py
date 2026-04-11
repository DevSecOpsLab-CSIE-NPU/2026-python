import unittest
import io
import sys
from contextlib import redirect_stdout

class TestQ299(unittest.TestCase):
    def run_test(self, solve_func, input_str):
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(input_str)
        output_capture = io.StringIO()
        with redirect_stdout(output_capture):
            solve_func()
        sys.stdin = stdin_backup
        return output_capture.getvalue().strip()

    def test_sample_cases(self):
        # 題目提供的測試範例
        test_input = "3\n3\n1 3 2\n4\n4 3 2 1\n2\n2 1"
        expected = (
            "Optimal train swapping takes 1 swaps.\n"
            "Optimal train swapping takes 6 swaps.\n"
            "Optimal train swapping takes 1 swaps."
        )
        
        import main
        import main_easy
        import main_handwritten
        
        # 驗證三個版本是否都正確
        for func in [main.solve, main_easy.solve, main_handwritten.solve]:
            with self.subTest(version=func.__name__):
                result = self.run_test(func, test_input)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()