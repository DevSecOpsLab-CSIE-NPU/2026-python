import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10929(unittest.TestCase):
    def test_multiple_of_11_and_not_multiple(self):
        input_data = "11\n12345678901234567890\n121\n123456789\n0\n"
        expected = (
            "11 is a multiple of 11.\n"
            "12345678901234567890 is a multiple of 11.\n"
            "121 is a multiple of 11.\n"
            "123456789 is not a multiple of 11.\n"
        )
        self.assertEqual(run_solution("hand10929.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
