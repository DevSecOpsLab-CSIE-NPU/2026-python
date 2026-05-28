import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from student_task10193 import solve


class TestTask10193(unittest.TestCase):
    cases = [
        ("3\n110\n101\n1010\n1011\n100\n10000\n",
         "Pair #1: Love is not all you need!\nPair #2: Love is not all you need!\nPair #3: All you need is love!"),
        ("1\n10\n100\n", "Pair #1: All you need is love!"),
    ]

    def test_all_cases(self):
        for inp, expected in self.cases:
            with self.subTest(input=inp):
                self.assertEqual(solve(inp), expected)


if __name__ == "__main__":
    unittest.main()
