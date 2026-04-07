import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10055.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

process_queries = solution.process_queries


class Test10055(unittest.TestCase):
    def test_toggle_and_query(self):
        queries = [[1, 2], [2, 1, 3], [1, 1], [2, 1, 3]]
        self.assertEqual(process_queries(3, queries), [1, 0])

    def test_all_increasing(self):
        queries = [[2, 1, 5], [2, 2, 4]]
        self.assertEqual(process_queries(5, queries), [0, 0])

    def test_single_toggle(self):
        queries = [[1, 3], [2, 2, 4]]
        self.assertEqual(process_queries(4, queries), [1])

    def test_repeated_toggle(self):
        queries = [[1, 1], [1, 1], [2, 1, 1]]
        self.assertEqual(process_queries(1, queries), [0])

    def test_large_range(self):
        queries = [[1, 5], [1, 2], [2, 1, 5], [2, 2, 4]]
        self.assertEqual(process_queries(5, queries), [0, 1])


if __name__ == "__main__":
    unittest.main()
