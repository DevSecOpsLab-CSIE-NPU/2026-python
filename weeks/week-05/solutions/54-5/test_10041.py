import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10041.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

best_meeting_distance = solution.best_meeting_distance


class Test10041(unittest.TestCase):
    def test_single_relative_positions(self):
        houses = [1, 2, 3]
        self.assertEqual(best_meeting_distance(houses), 2)

    def test_even_number_of_relatives(self):
        houses = [10, 20, 30, 40]
        self.assertEqual(best_meeting_distance(houses), 40)

    def test_duplicate_addresses(self):
        houses = [5, 5, 5, 10]
        self.assertEqual(best_meeting_distance(houses), 5)

    def test_unsorted_input(self):
        houses = [100, 1, 50, 20, 30]
        self.assertEqual(best_meeting_distance(houses), 129)

    def test_minimal_case(self):
        houses = [7]
        self.assertEqual(best_meeting_distance(houses), 0)


if __name__ == "__main__":
    unittest.main()
