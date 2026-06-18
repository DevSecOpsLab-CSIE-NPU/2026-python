import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10252(unittest.TestCase):
    def test_three_points(self):
        input_data = "1\n3\n0 0\n1 1\n2 2\n"
        self.assertEqual(run_solution("10252.py", input_data), "4 1\n")

    def test_four_points_rectangle(self):
        input_data = "1\n4\n0 0\n0 1\n1 0\n1 1\n"
        self.assertEqual(run_solution("10252.py", input_data), "4 4\n")

    def test_multiple_solutions(self):
        input_data = "1\n2\n0 0\n2 0\n"
        self.assertEqual(run_solution("10252.py", input_data), "2 3\n")


if __name__ == "__main__":
    unittest.main()