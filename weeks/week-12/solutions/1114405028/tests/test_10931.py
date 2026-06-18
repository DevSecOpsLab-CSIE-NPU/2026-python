import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10931(unittest.TestCase):
    def test_parity_examples(self):
        input_data = "1\n2\n10\n21\n0\n"
        expected = (
            "The parity of 1 is 1 (mod 2).\n"
            "The parity of 10 is 1 (mod 2).\n"
            "The parity of 1010 is 2 (mod 2).\n"
            "The parity of 10101 is 3 (mod 2).\n"
        )
        self.assertEqual(run_solution("hand10931.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
