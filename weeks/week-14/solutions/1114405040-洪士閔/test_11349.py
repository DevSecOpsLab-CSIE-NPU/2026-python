import io
import unittest

from solution_11349 import is_symmetric_matrix, solve


class TestSymmetricMatrix(unittest.TestCase):
    def test_sample_symmetric(self):
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 1, 5],
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_sample_non_symmetric(self):
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [0, 1, 5],
        ]
        self.assertFalse(is_symmetric_matrix(matrix))

    def test_negative_element_is_not_symmetric(self):
        matrix = [
            [1, -1],
            [-1, 1],
        ]
        self.assertFalse(is_symmetric_matrix(matrix))

    def test_single_non_negative_element(self):
        self.assertTrue(is_symmetric_matrix([[42]]))

    def test_even_size_symmetric(self):
        matrix = [
            [1, 2],
            [2, 1],
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_not_square_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        self.assertFalse(is_symmetric_matrix(matrix))

    def test_large_values(self):
        big = 2**40
        matrix = [
            [big, 0, 0],
            [0, big, 0],
            [0, 0, big],
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_solve_sample_input(self):
        sample_input = """2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
"""
        expected = "Test #1: Symmetric.\nTest #2: Non-symmetric."
        self.assertEqual(solve(io.StringIO(sample_input)), expected)


if __name__ == "__main__":
    unittest.main()
