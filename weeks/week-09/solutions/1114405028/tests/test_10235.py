import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10235(unittest.TestCase):
    def test_all_empty(self):
        input_data = "1\n1 1\n0\n"
        self.assertEqual(run_solution("10235.py", input_data), "1\n")

    def test_one_obstacle(self):
        input_data = "1\n2 2\n1 0\n1 1\n"
        self.assertEqual(run_solution("10235.py", input_data), "0\n")

    def test_full_open(self):
        input_data = "1\n2 2\n1 1\n1 1\n"
        self.assertEqual(run_solution("10235.py", input_data), "1\n")


if __name__ == "__main__":
    unittest.main()