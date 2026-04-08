import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10101.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

solve_line = solution.solve_line


class Test10101(unittest.TestCase):
    def test_already_valid_expression(self):
        self.assertEqual(solve_line("1+1=2#"), "1+1=2#")

    def test_valid_move(self):
        self.assertEqual(solve_line("1+2=4#"), "1+3=4#")


if __name__ == "__main__":
    unittest.main()
