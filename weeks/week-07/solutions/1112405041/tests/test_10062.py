import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
import sys
import importlib

problem_10062 = importlib.import_module("10062")

class TestCowSorting(unittest.TestCase):
    def test_sample(self):
        # 3 ?­ç?
        # ç¬?2 ?‹ä?ç½®å??¢æ? 1 ?‹æ?å®ƒå? (1)
        # ç¬?3 ?‹ä?ç½®å??¢æ? 1 ?‹æ?å®ƒå? (1)
        # ?†å??¨ç?: 1, 2, 3 ->
        # ?€å¾Œä???(pos 3) ?é¢??1 ?‹æ?å®ƒå?ï¼Œå‰©ä¸?{1,2,3} ä¸­é¸ç¬?2 å°ç???2
        # ç¬¬ä???(pos 2) ?é¢??1 ?‹æ?å®ƒå?ï¼Œå‰©ä¸?{1,3} ä¸­é¸ç¬?2 å°ç???3
        # ç¬¬ä???(pos 1) ?©ä? 1
        # çµæ??‰ç‚º 1, 3, 2
        input_str = "3\n1\n1\n"
        expected_output = "1\n3\n2\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10062.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()

