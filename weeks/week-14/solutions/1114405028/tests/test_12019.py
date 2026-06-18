import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import run_solution


class Test12019(unittest.TestCase):
    def test_doomsday_2012(self):
        input_data = "4\n1 1\n2 21\n3 7\n12 12\n"
        expected = (
            "Sunday\n"
            "Tuesday\n"
            "Wednesday\n"
            "Wednesday\n"
        )
        self.assertEqual(run_solution("12019.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
