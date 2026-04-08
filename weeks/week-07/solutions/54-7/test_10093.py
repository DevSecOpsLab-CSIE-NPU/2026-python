import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10093.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

max_artillery = solution.max_artillery


class Test10093(unittest.TestCase):
    def test_single_cell(self):
        grid = ["P"]
        self.assertEqual(max_artillery(grid), 1)

    def test_three_by_three(self):
        grid = ["PPP", "PHP", "PPP"]
        self.assertEqual(max_artillery(grid), 3)


if __name__ == "__main__":
    unittest.main()
