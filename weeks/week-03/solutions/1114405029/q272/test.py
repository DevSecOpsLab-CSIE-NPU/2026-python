import unittest
import io
import sys
from contextlib import redirect_stdout

class TestQ272(unittest.TestCase):
    def run_test(self, solve_func, input_str):
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(input_str)
        output_capture = io.StringIO()
        with redirect_stdout(output_capture):
            solve_func()
        sys.stdin = stdin_backup
        return output_capture.getvalue()

    def test_sample(self):
        # 官方範例測試
        test_input = '"To be or not to be," quoth the bard, "that is the question."'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        
        import main
        import main_easy
        import main_handwritten
        
        for func in [main.solve, main_easy.solve, main_handwritten.solve]:
            with self.subTest(version=func.__name__):
                result = self.run_test(func, test_input)
                # 注意：因為 main-easy 用 print(end="")，所以要比對完整內容
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()