import unittest
from io import StringIO
import sys

def run_script(file_name, input_str):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(input_str)
    sys.stdout = StringIO()
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            exec(f.read(), {'__name__': '__main__'})
        return sys.stdout.getvalue()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

class TestFalseCoin(unittest.TestCase):
    def test_standard_case(self):
        # 模擬題目敘述中的範例數據
        sample_input = "1\n5 3\n2 1 2 3 4\n<\n1 1 4\n=\n1 2 5\n=\n"
        expected_output = "3\n"
        
        for script in ["main.py", "main-easy.py", "main-handwritten.py"]:
            with self.subTest(script=script):
                output = run_script(script, sample_input)
                self.assertEqual(output.strip(), expected_output.strip())

if __name__ == "__main__":
    unittest.main()