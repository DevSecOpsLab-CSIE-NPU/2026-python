import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
import sys
import importlib

problem_10056 = importlib.import_module("10056")

class TestWhatIsTheProbability(unittest.TestCase):
    def test_sample_input(self):
        # æ¸¬è©¦è¼¸å…¥ï¼?
        # 1 çµ„æ¸¬è³? 2 ?‹ç©å®? ?å?æ©Ÿç? 0.1666, ?¾ç¬¬ 1 ?‹ç©å®?
        # è¨ˆç?: 0.1666 / (1 - (1-0.1666)^2) = 0.1666 / (1 - 0.8334^2)
        # = 0.1666 / (1 - 0.69455556) = 0.1666 / 0.30544444 = 0.545434...
        # ?€ä»¥é??Ÿè¼¸?ºæ???0.5454 (å¦‚æ?é¡Œç›®è¦æ? 4 ä½å???
        # æª¢æŸ¥??test_10056.py è£¡ç? expected_output ??0.5455ï¼Œé€™å¯?½æ˜¯?¨æ?å¯«ç?
        input_str = "1\n2 0.1666 1\n"
        expected_output = "0.5454\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin

        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10056.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == '__main__':
    unittest.main()

