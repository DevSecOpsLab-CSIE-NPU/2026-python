import datetime
import io
import unittest

from solution_12019 import solve, weekday_2011


class TestWeekday2011(unittest.TestCase):
    def assert_date_weekday(self, month, day):
        expected = datetime.date(2011, month, day).strftime("%A")
        self.assertEqual(weekday_2011(month, day), expected)

    def test_known_dates(self):
        self.assertEqual(weekday_2011(1, 1), "Saturday")
        self.assertEqual(weekday_2011(2, 28), "Monday")
        self.assertEqual(weekday_2011(12, 31), "Saturday")

    def test_doomsday_anchor_dates_are_monday(self):
        for month, day in [
            (1, 10),
            (2, 21),
            (3, 7),
            (4, 4),
            (5, 9),
            (6, 6),
            (7, 11),
            (8, 8),
            (9, 5),
            (10, 10),
            (11, 7),
            (12, 12),
        ]:
            self.assertEqual(weekday_2011(month, day), "Monday")

    def test_matches_datetime_for_more_dates(self):
        for month, day in [(1, 31), (3, 1), (7, 4), (10, 31)]:
            self.assert_date_weekday(month, day)

    def test_solve_sample_input(self):
        sample_input = """5
1 6
2 28
4 5
5 26
12 31
"""
        expected = "Thursday\nMonday\nTuesday\nThursday\nSaturday"
        self.assertEqual(solve(io.StringIO(sample_input)), expected)


if __name__ == "__main__":
    unittest.main()
