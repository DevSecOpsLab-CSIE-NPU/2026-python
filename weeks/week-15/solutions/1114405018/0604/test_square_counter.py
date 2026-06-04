"""平方數計數 — tests for count_squares."""

import unittest

from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        self.assertEqual(count_squares(1, 10), 3)

    def test_edge_case_single_point(self):
        self.assertEqual(count_squares(100, 100), 1)

    def test_range_with_no_square(self):
        self.assertEqual(count_squares(5, 8), 0)

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError):
            count_squares(5, 2)


if __name__ == "__main__":
    unittest.main()