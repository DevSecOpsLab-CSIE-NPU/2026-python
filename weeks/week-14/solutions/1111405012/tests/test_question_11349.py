import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_support import load_solution


FILES = [
    "QUESTION_11349.py",
    "QUESTION_11349-easy.py",
    "QUESTION_11349-hand.py",
]


class TestQuestion11349(unittest.TestCase):
    def test_sample_and_negative_case(self):
        data = """3
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
N = 1
-1
"""
        expected = "\n".join(
            [
                "Test #1: Symmetric.",
                "Test #2: Non-symmetric.",
                "Test #3: Non-symmetric.",
            ]
        )

        for filename in FILES:
            with self.subTest(filename=filename):
                module = load_solution(filename)
                self.assertEqual(module.solve(data), expected)


if __name__ == "__main__":
    unittest.main()
