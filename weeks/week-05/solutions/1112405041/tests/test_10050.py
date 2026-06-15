import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
import sys
import importlib

problem_10050 = importlib.import_module("10050")

class TestHartals(unittest.TestCase):
    def test_sample_input(self):
        # ÁØÑ‰?Ëº∏ÂÖ•
        # 2 ÁµÑÊ∏¨Ë≥?
        # 1: 14 Â§? 3 ?øÈª® (3, 4, 8) -> ?çÂ§± 5 Â§?
        # 2: 100 Â§? 4 ?øÈª® (12, 15, 25, 40) -> ?çÂ§± 15 Â§?
        input_str = "2\n14\n3\n3\n4\n8\n100\n4\n12\n15\n25\n40\n"
        expected_output = "5\n15\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin

        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10050.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == '__main__':
    unittest.main()

