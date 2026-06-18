import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test11349(unittest.TestCase):
    def test_symmetric_and_non_symmetric(self):
        input_data = (
            "2\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "3 1 5\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "0 1 5\n"
        )
        expected = (
            "Test #1: Symmetric.\n"
            "Test #2: Non-symmetric.\n"
        )
        self.assertEqual(run_solution("11349.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
