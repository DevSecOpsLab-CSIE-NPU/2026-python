import unittest
from io import StringIO
import sys

# 模擬輸入與獲取輸出的輔助函式
def run_main(script_func, input_str):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(input_str)
    sys.stdout = StringIO()
    
    try:
        script_func()
        return sys.stdout.getvalue()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

class TestPrimaryArithmetic(unittest.TestCase):
    def setUp(self):
        self.sample_input = "123 456\n555 555\n123 594\n0 0\n"
        self.expected_output = (
            "No carry operation.\n"
            "3 carry operations.\n"
            "1 carry operation.\n"
        )

    def test_main(self):
        import main
        output = run_main(main.solve, self.sample_input)
        self.assertEqual(output, self.expected_output)

    def test_main_easy(self):
        # 由於 main-easy 是腳本形式，這裡可以用 exec 執行
        def wrapper():
            with open("main-easy.py", encoding="utf-8") as f:
                exec(f.read(), {})
        output = run_main(wrapper, self.sample_input)
        self.assertEqual(output, self.expected_output)

    def test_main_handwritten(self):
        def wrapper():
            with open("main-handwritten.py", encoding="utf-8") as f:
                exec(f.read(), {})
        output = run_main(wrapper, self.sample_input)
        self.assertEqual(output, self.expected_output)

if __name__ == "__main__":
    unittest.main()