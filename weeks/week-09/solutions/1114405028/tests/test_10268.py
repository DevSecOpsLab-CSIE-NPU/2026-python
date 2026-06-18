import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10268(unittest.TestCase):
    def test_example_values(self):
        input_data = "2 100\n10 786599\n"
        self.assertEqual(run_solution("10268.py", input_data), "14\n21\n")

    def test_more_than_63(self):
        input_data = "1 9223372036854775807\n"
        self.assertEqual(run_solution("10268.py", input_data), "More than 63 trials needed.\n")

    def test_small_case(self):
        input_data = "1 1\n"
        self.assertEqual(run_solution("10268.py", input_data), "1\n")


if __name__ == "__main__":
    unittest.main()