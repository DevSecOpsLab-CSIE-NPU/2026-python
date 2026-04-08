import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10170.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

group_size_on_day = solution.group_size_on_day


class Test10170(unittest.TestCase):
    def test_first_day(self):
        self.assertEqual(group_size_on_day(4, 1), 4)

    def test_next_group(self):
        self.assertEqual(group_size_on_day(4, 5), 5)

    def test_later_group(self):
        self.assertEqual(group_size_on_day(4, 10), 6)


if __name__ == "__main__":
    unittest.main()
