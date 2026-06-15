import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
import sys
import importlib

# ä½¿ç”¨ importlib è®€?–é??­ç‚º?¸å??„æ¨¡çµ?
problem_10041 = importlib.import_module("10041")

class TestVitosFamily(unittest.TestCase):
    def test_sample_input(self):
        # æ¨¡æ“¬è¼¸å…¥ï¼? çµ„è???
        # ç¬¬ä?çµ„ï?2 ?‹è¦ª?šï??€??2 4 -> è·é›¢ |2-3| + |4-3| = 2 (ä¸­ä??¸æ˜¯ 2 ??4 ?½å¯ä»¥ï??™è£¡??4)
        # ä¿®æ­£: 2 2 4 è¡¨ç¤º 2 çµ„æ¸¬è³‡ï?ç¬¬ä?çµ?2 ?‹è¦ª?šæ˜¯ 2 4
        # ç¬¬ä?çµ? 3 ?‹è¦ª?šï??€??2 4 6 -> è·é›¢ |2-4| + |4-4| + |6-4| = 2 + 0 + 2 = 4
        input_str = "2\n2 2 4\n3 2 4 6\n"
        expected_output = "2\n4\n"

        # ?”æˆª stdout
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        # ?”æˆª stdin
        saved_stdin = sys.stdin
        sys.stdin = StringIO(input_str)

        try:
            problem_10041.solve()
            # ?»é™¤çµå°¾ç©ºç™½?æ?è¼?
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == '__main__':
    unittest.main()

