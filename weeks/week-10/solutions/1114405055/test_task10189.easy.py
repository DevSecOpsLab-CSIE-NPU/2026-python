import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from student_task10189 import solve


class TestTask10189(unittest.TestCase):
    cases = [
        ("4 4\n*...\n....\n.*..\n....\n3 5\n**...\n.....\n.*...\n0 0\n",
         "Field #1:\n*100\n2210\n1*10\n1110\n\nField #2:\n**100\n33200\n1*100"),
        ("1 1\n*\n0 0\n", "Field #1:\n*"),
    ]

    def test_all_cases(self):
        for inp, expected in self.cases:
            with self.subTest(input=inp):
                self.assertEqual(solve(inp), expected)


if __name__ == "__main__":
    unittest.main()
