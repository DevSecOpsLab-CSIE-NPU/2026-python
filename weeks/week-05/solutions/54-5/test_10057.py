import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10057.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

median_password = solution.median_password


class Test10057(unittest.TestCase):
    def test_odd_length_values(self):
        values = [1, 2, 3]
        self.assertEqual(median_password(values), (2, 1, 1))

    def test_even_length_values(self):
        values = [1, 2, 4, 7]
        self.assertEqual(median_password(values), (2, 1, 3))

    def test_duplicate_median_values(self):
        values = [5, 5, 5, 7]
        self.assertEqual(median_password(values), (5, 3, 1))

    def test_single_value(self):
        values = [100]
        self.assertEqual(median_password(values), (100, 1, 1))

    def test_sorted_input(self):
        values = [3, 1, 4, 1, 5, 9]
        self.assertEqual(median_password(values), (3, 1, 2))


if __name__ == "__main__":
    unittest.main()
