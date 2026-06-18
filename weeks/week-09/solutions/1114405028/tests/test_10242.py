import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10242(unittest.TestCase):
    def test_simple_path(self):
        input_data = "3 2\n1 2\n2 3\n1\n2\n3\n1 1\n3\n"
        self.assertEqual(run_solution("10242.py", input_data), "6\n")

    def test_cycle_and_bar(self):
        input_data = "3 3\n1 2\n2 3\n3 1\n5\n6\n7\n1 1\n1\n"
        self.assertEqual(run_solution("10242.py", input_data), "18\n")

    def test_disconnected_bar(self):
        input_data = "3 2\n1 2\n2 3\n1\n2\n3\n1 1\n3\n"
        self.assertEqual(run_solution("10242.py", input_data), "6\n")


if __name__ == "__main__":
    unittest.main()