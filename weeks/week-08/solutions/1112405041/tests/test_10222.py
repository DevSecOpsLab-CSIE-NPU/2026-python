import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
import sys
import importlib

# ?´æ–°æ¸¬è©¦ä»¥ç¬¦?ˆé??¹å??„ã€Œå„ªè³ªå­¸?Ÿåˆ¤?·ã€é?æ±?
problem_10222 = importlib.import_module("10222")

class TestQualityStudent(unittest.TestCase):
    def test_quality_id(self):
        # è¼¸å…¥ 1112405041 ?‰è©²è¼¸å‡º yes
        input_str = "1112405041"
        expected_output = "yes"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10222.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

    def test_invalid_id(self):
        # ?æ•¸å­—è¼¸??
        input_str = "abc"
        expected_output = "no"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10222.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()

