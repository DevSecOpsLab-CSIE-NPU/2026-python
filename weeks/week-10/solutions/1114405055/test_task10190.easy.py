import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from student_task10190 import solve


class TestTask10190(unittest.TestCase):
    cases = [
        ("81 3\n31 2\n64 4\n1 5\n", "81 27 9 3 1\nBoring!\n64 16 4 1\nBoring!"),
        ("72 8\n", "Boring!"),
    ]

    def test_all_cases(self):
        for inp, expected in self.cases:
            with self.subTest(input=inp):
                self.assertEqual(solve(inp), expected)


if __name__ == "__main__":
    unittest.main()
