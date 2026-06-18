import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10922(unittest.TestCase):
    def test_9_degree_and_not_multiple(self):
        input_data = "999999999999999999999999999999\n17\n0\n"
        expected = "9-degree of 999999999999999999999999999999 is 2.\n17 is not a multiple of 9.\n"
        self.assertEqual(run_solution("hand10922.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
