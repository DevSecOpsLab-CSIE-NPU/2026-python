import unittest

from task2_student_ranking import rank_students


class TestTask2(unittest.TestCase):
    def test_tie_break_by_age_then_name(self):
        records = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("ian", 88, 19),
            ("zoe", 92, 21),
            ("eva", 92, 20),
            ("leo", 75, 20),
        ]
        result = rank_students(records, 3)
        self.assertEqual(result, [("eva", 92, 20), ("zoe", 92, 21), ("bob", 88, 19)])

    def test_k_larger_than_record_count(self):
        records = [("amy", 80, 20), ("bob", 79, 21)]
        self.assertEqual(rank_students(records, 10), [("amy", 80, 20), ("bob", 79, 21)])

    def test_k_zero_returns_empty(self):
        records = [("amy", 80, 20)]
        self.assertEqual(rank_students(records, 0), [])


if __name__ == "__main__":
    unittest.main()
