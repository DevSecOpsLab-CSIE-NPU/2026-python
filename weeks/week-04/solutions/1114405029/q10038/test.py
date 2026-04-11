import unittest
from io import StringIO
import sys

def run_script(file_name, input_str):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(input_str)
    sys.stdout = StringIO()
    try:
        # 使用 exec 執行外部檔案
        with open(file_name, "r", encoding="utf-8") as f:
            exec(f.read(), {'__name__': '__main__'})
        return sys.stdout.getvalue()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

class TestJolly(unittest.TestCase):
    def test_all_versions(self):
        sample_input = "4 1 4 2 3\n5 1 4 2 -1 6\n"
        expected_output = "Jolly\nNot jolly\n"
        
        # 驗證三個檔案
        for script in ["main.py", "main-easy.py", "main-handwritten.py"]:
            with self.subTest(script=script):
                output = run_script(script, sample_input)
                self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()