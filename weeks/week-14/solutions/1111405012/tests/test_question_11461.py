import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_support import load_solution


FILES = [
    "QUESTION_11461.py",
    "QUESTION_11461-easy.py",
    "QUESTION_11461-hand.py",
]


class TestQuestion11461(unittest.TestCase):
    def test_sample(self):
        data = """1 4
1 10
1 100000
0 0
"""
        expected = "2\n3\n316"

        for filename in FILES:
            with self.subTest(filename=filename):
                module = load_solution(filename)
                self.assertEqual(module.solve(data), expected)

    def test_boundaries(self):
        data = """15 16
17 24
25 25
0 0
"""
        expected = "1\n0\n1"

        for filename in FILES:
            with self.subTest(filename=filename):
                module = load_solution(filename)
                self.assertEqual(module.solve(data), expected)


if __name__ == "__main__":
    unittest.main()
