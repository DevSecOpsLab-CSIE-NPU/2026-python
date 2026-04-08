import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10071.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

count_six_tuples = solution.count_six_tuples


class Test10071(unittest.TestCase):
    def test_no_solution(self):
        numbers = [1, 2, 3]
        self.assertEqual(count_six_tuples(numbers), 0)

    def test_some_solutions(self):
        numbers = [0, 1, 2]
        self.assertEqual(count_six_tuples(numbers), 21)


if __name__ == "__main__":
    unittest.main()
