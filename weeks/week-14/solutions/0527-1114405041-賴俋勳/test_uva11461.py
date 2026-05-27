import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from uva11461 import count_squares, solve


class TestUVA11461(unittest.TestCase):
    def test_count_squares_basic(self):
        self.assertEqual(count_squares(1, 4), 2)
        self.assertEqual(count_squares(1, 10), 3)

    def test_count_squares_large(self):
        self.assertEqual(count_squares(1, 100000), 316)

    def test_sample_io(self):
        input_data = "1 4\n1 10\n1 100000\n0 0\n"
        expected = "2\n3\n316"
        self.assertEqual(solve(input_data), expected)


if __name__ == "__main__":
    unittest.main()
