import unittest
import io
import sys
from contextlib import redirect_stdout

class TestQ490(unittest.TestCase):
    def run_test(self, solve_func, input_str):
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(input_str)
        output_capture = io.StringIO()
        with redirect_stdout(output_capture):
            solve_func()
        sys.stdin = stdin_backup
        return output_capture.getvalue()

    def test_basic_rotation(self):
        # 使用簡單範例：
        # ABC
        # DEF
        # 旋轉 90 度後應為：
        # DA
        # EB
        # FC
        test_input = "ABC\nDEF"
        expected = "DA\nEB\nFC\n"
        
        import main_easy
        result = self.run_test(main_easy.solve, test_input)
        self.assertEqual(result, expected)

    def test_uneven_lines(self):
        # 測試長短不一的行
        test_input = "HELLO\nWORLD!!"
        # 最長是 WORLD!! (7字)
        # 預期第 6, 7 個字位置只有 WORLD!! 有字，第一行要補空白
        import main
        result = self.run_test(main.solve, test_input)
        self.assertTrue(result.startswith("WH"))

if __name__ == "__main__":
    unittest.main()