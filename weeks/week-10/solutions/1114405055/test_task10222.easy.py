import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from student_task10222 import solve


class TestTask10222(unittest.TestCase):
    cases = [
        ("Jr;;p Ept;f\n", "Hello World\n"),
        ("O S, GOMR YPFSU/\n", "I Am FINE TODAY.\n"),
    ]

    def test_all_cases(self):
        for inp, expected in self.cases:
            with self.subTest(input=inp):
                self.assertEqual(solve(inp), expected)


if __name__ == "__main__":
    unittest.main()
