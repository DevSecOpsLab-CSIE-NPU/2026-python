import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from uva12019 import weekday_name_2012, solve


class TestUVA12019(unittest.TestCase):
    def test_weekday_known_dates(self):
        self.assertEqual(weekday_name_2012(1, 1), "Sunday")
        self.assertEqual(weekday_name_2012(2, 29), "Wednesday")

    def test_sample_style_io(self):
        input_data = "3\n1 1\n2 29\n12 25\n"
        expected = "Sunday\nWednesday\nTuesday"
        self.assertEqual(solve(input_data), expected)


if __name__ == "__main__":
    unittest.main()
