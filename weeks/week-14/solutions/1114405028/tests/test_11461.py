import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test11461(unittest.TestCase):
    def test_square_numbers(self):
        input_data = "1 4\n1 10\n1 100000\n0 0\n"
        expected = "2\n3\n316\n"
        self.assertEqual(run_solution("11461.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
