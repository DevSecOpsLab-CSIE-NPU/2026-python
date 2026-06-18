import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test11417(unittest.TestCase):
    def test_gcd_sum(self):
        input_data = "10\n100\n500\n0\n"
        expected = "67\n13015\n442011\n"
        self.assertEqual(run_solution("11417.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
