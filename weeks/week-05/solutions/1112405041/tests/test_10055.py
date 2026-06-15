import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
import sys
import importlib

problem_10055 = importlib.import_module("10055")

class TestCompositeFunction(unittest.TestCase):
    def test_sample_input(self):
        # æ¸¬è©¦è¼¸å…¥ï¼?
        # 3 ?‹å‡½?¸ï?5 æ¬¡æ?ä½?
        # ä¸€?‹å?: f1, f2, f3 = å¢? å¢? å¢?(0, 0, 0)
        # 1. ?¥è©¢ 1~3 -> 0^0^0 = 0
        # 2. ?è? f2 -> f2 è®?1 (æ¸?
        # 3. ?¥è©¢ 1~3 -> 0^1^0 = 1
        # 4. ?è? f2 -> f2 è®?0 (å¢?
        # 5. ?¥è©¢ 1~3 -> 0^0^0 = 0
        input_str = "3 5\n2 1 3\n1 2\n2 1 3\n1 2\n2 1 3\n"
        expected_output = "0\n1\n0\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin

        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10055.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == '__main__':
    unittest.main()

