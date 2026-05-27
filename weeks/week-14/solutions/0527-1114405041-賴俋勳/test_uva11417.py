import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from uva11417 import gcd_sum, solve


class TestUVA11417(unittest.TestCase):
    def test_gcd_sum_10(self):
        self.assertEqual(gcd_sum(10), 67)

    def test_gcd_sum_100(self):
        self.assertEqual(gcd_sum(100), 13015)

    def test_sample_io(self):
        input_data = "10\n100\n500\n0\n"
        expected = "67\n13015\n442011"
        self.assertEqual(solve(input_data), expected)


if __name__ == "__main__":
    unittest.main()
