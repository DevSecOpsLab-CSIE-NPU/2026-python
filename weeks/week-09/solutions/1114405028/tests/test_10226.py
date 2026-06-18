import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10226(unittest.TestCase):
    def test_no_forbidden_positions(self):
        input_data = "3\n0\n0\n0\n"
        expected = "ABC\nCB\nBAC\nCA\nCAB\nBA\n"
        self.assertEqual(run_solution("10226.py", input_data), expected)

    def test_simple_forbidden_position(self):
        input_data = "3\n1 0\n3 0\n0\n"
        expected = "BAC\nCA\nCBA\n"
        self.assertEqual(run_solution("10226.py", input_data), expected)

    def test_empty_case(self):
        input_data = "0\n"
        expected = ""
        self.assertEqual(run_solution("10226.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()