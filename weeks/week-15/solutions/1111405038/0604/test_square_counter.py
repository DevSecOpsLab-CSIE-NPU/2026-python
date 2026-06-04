import unittest

from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        self.assertEqual(count_squares(1, 10), 3)

    def test_edge_single_point_square(self):
        self.assertEqual(count_squares(1, 1), 1)

    def test_range_without_square_numbers(self):
        self.assertEqual(count_squares(5, 8), 0)

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError):
            count_squares(10, 1)


if __name__ == "__main__":
    unittest.main()
