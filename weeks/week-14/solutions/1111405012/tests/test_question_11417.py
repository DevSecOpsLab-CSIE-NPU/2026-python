import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_support import load_solution


FILES = [
    "QUESTION_11417.py",
    "QUESTION_11417-easy.py",
    "QUESTION_11417-hand.py",
]


class TestQuestion11417(unittest.TestCase):
    def test_sample(self):
        data = """10
100
500
0
"""
        expected = "67\n13015\n442011"

        for filename in FILES:
            with self.subTest(filename=filename):
                module = load_solution(filename)
                self.assertEqual(module.solve(data), expected)

    def test_small_values(self):
        data = "2\n3\n4\n0\n"
        expected = "1\n3\n7"

        for filename in FILES:
            with self.subTest(filename=filename):
                module = load_solution(filename)
                self.assertEqual(module.solve(data), expected)


if __name__ == "__main__":
    unittest.main()
