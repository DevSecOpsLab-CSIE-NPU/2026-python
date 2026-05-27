import io
import unittest

from solution_11461 import count_squares, solve


class TestCountSquares(unittest.TestCase):
    def test_samples(self):
        self.assertEqual(count_squares(1, 4), 2)
        self.assertEqual(count_squares(1, 10), 3)
        self.assertEqual(count_squares(1, 100000), 316)

    def test_single_square_range(self):
        self.assertEqual(count_squares(4, 4), 1)
        self.assertEqual(count_squares(5, 8), 0)

    def test_ranges_not_starting_at_one(self):
        self.assertEqual(count_squares(10, 25), 2)
        self.assertEqual(count_squares(26, 80), 3)

    def test_solve_sample_input(self):
        sample_input = """1 4
1 10
1 100000
0 0
"""
        expected = "2\n3\n316"
        self.assertEqual(solve(io.StringIO(sample_input)), expected)


if __name__ == "__main__":
    unittest.main()
