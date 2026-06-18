import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test10908(unittest.TestCase):
    def test_largest_square_query(self):
        input_data = "1\n7 10 4\nabbbaaaaaa\nabbbaaaaaa\nabbbaaaaaa\naaaaaaaaaa\naaaaaaaaaa\naaccaaaaaa\naaccaaaaaa\n1 2\n2 4\n4 6\n5 2\n"
        expected = "7 10 4\n3\n1\n5\n1\n"
        self.assertEqual(run_solution("hand10908.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
