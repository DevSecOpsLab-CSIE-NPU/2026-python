import unittest

from square_counter import count_squares


class CountSquaresTests(unittest.TestCase):
	def test_basic_range_counts_three_squares(self):
		self.assertEqual(count_squares(1, 10), 3)

	def test_edge_case_single_value_square(self):
		self.assertEqual(count_squares(1, 1), 1)

	def test_no_squares_in_range(self):
		self.assertEqual(count_squares(5, 8), 0)

	def test_raises_value_error_when_a_greater_than_b(self):
		with self.assertRaisesRegex(ValueError, "a must be <= b"):
			count_squares(10, 1)


if __name__ == "__main__":
	unittest.main()
