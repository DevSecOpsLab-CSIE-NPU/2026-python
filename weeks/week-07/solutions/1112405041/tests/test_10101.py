import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
import sys
import importlib

# ?±æ–¼æª”æ??ç¨±ä»¥æ•¸å­—é??­ï??‘å€‘ä½¿??importlib ä¾†å??‹åŒ¯??
problem_10101 = importlib.import_module("10101-easy")

class TestMatchstick(unittest.TestCase):
    def test_no_solution(self):
        # æ¸¬è©¦?¡è§£?„æ?æ³?
        input_str = "1+1=1#"
        expected_output = "No\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            # ?™è£¡?¼å« easy ?ˆç? main
            problem_10101.main()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()

