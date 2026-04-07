import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10050.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

hartal_lost_days = solution.hartal_lost_days


class Test10050(unittest.TestCase):
    def test_single_party(self):
        self.assertEqual(hartal_lost_days(14, [3]), 3)

    def test_multiple_parties(self):
        self.assertEqual(hartal_lost_days(14, [3, 4, 8]), 5)

    def test_exclude_weekends(self):
        self.assertEqual(hartal_lost_days(15, [7]), 0)

    def test_duplicate_parameters(self):
        self.assertEqual(hartal_lost_days(20, [3, 3]), 5)

    def test_long_simulation(self):
        self.assertEqual(hartal_lost_days(30, [2, 3, 5]), 16)


if __name__ == "__main__":
    unittest.main()
