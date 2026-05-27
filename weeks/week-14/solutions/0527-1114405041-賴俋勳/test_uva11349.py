import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from uva11349 import is_symmetric_matrix, solve


class TestUVA11349(unittest.TestCase):
    def test_is_symmetric_true(self):
        mat = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 1, 5],
        ]
        self.assertTrue(is_symmetric_matrix(mat))

    def test_is_symmetric_false_negative(self):
        mat = [[0, -1], [1, 0]]
        self.assertFalse(is_symmetric_matrix(mat))

    def test_sample_io(self):
        input_data = """2
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
        self.assertEqual(solve(input_data), expected)


if __name__ == "__main__":
    unittest.main()
