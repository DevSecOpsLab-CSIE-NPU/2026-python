import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10812(unittest.TestCase):
    def test_valid_scores(self):
        input_data = "3\n40 20\n20 40\n4 2\n"
        expected = "30 10\nimpossible\n3 1\n"
        self.assertEqual(run_solution("hand10812.py", input_data), expected)

    def test_impossible_when_difference_too_large(self):
        input_data = "1\n5 7\n"
        expected = "impossible\n"
        self.assertEqual(run_solution("hand10812.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
