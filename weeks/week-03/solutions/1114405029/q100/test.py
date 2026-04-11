import unittest
import io
import sys
from contextlib import redirect_stdout

class TestUVA100(unittest.TestCase):
    def run_test_case(self, solve_func, input_str):
        # 模擬標準輸入輸出
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(input_str)
        output_capture = io.StringIO()
        
        with redirect_stdout(output_capture):
            solve_func()
            
        sys.stdin = stdin_backup
        return output_capture.getvalue().strip()

    def test_logic(self):
        # 使用題目提供的測試用例
        test_input = "1 10\n100 200\n201 210\n900 1000"
        expected_output = "1 10 20\n100 200 125\n201 210 89\n900 1000 174"
        
        # 引入各個版本進行測試
        import main
        import main_easy
        import main_handwritten
        
        for func in [main.solve, main_easy.solve, main_handwritten.solve]:
            with self.subTest(version=func.__name__):
                result = self.run_test_case(func, test_input)
                self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()