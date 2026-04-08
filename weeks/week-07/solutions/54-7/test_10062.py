import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10062.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

reconstruct_lineup = solution.reconstruct_lineup


class Test10062(unittest.TestCase):
    def test_simple_order(self):
        counts = [0, 0]
        self.assertEqual(reconstruct_lineup(counts), [3, 2, 1])

    def test_mixed_order(self):
        counts = [0, 1, 1]
        self.assertEqual(reconstruct_lineup(counts), [4, 1, 3, 2])

    def test_reverse_order(self):
        counts = [0, 1, 2, 3]
        self.assertEqual(reconstruct_lineup(counts), [5, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
