import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_support import load_solution


FILES = [
    "QUESTION_12019.py",
    "QUESTION_12019-easy.py",
    "QUESTION_12019-hand.py",
]


class TestQuestion12019(unittest.TestCase):
    def test_2012_dates(self):
        data = """5
1 1
2 29
4 4
12 12
12 31
"""
        expected = "\n".join(
            ["Sunday", "Wednesday", "Wednesday", "Wednesday", "Monday"]
        )

        for filename in FILES:
            with self.subTest(filename=filename):
                module = load_solution(filename)
                self.assertEqual(module.solve(data), expected)


if __name__ == "__main__":
    unittest.main()
