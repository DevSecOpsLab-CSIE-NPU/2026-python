import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from task2_student_ranking import rank_students, format_output


class TestStudentRanking(unittest.TestCase):

    def test_normal_case(self):
        data = "amy 88 20\nbob 88 19\nzoe 92 21\nian 88 19\nleo 75 20\neva 92 20"
        ranked = rank_students(data, 3)
        expected = [("eva", 92, 20), ("zoe", 92, 21), ("bob", 88, 19)]
        self.assertEqual(ranked, expected)

    def test_tie_break_by_age(self):
        data = "alice 85 22\nbob 85 18\ncharlie 85 20"
        ranked = rank_students(data, 3)
        self.assertEqual(ranked[0], ("bob", 85, 18))
        self.assertEqual(ranked[1], ("charlie", 85, 20))
        self.assertEqual(ranked[2], ("alice", 85, 22))

    def test_tie_break_by_name(self):
        data = "bob 90 20\namy 90 20\nzoe 90 20"
        ranked = rank_students(data, 3)
        names = [r[0] for r in ranked]
        self.assertEqual(names, ["amy", "bob", "zoe"])

    def test_k_smaller_than_n(self):
        data = "x 50 18\ny 60 19\nz 70 20"
        ranked = rank_students(data, 1)
        self.assertEqual(ranked, [("z", 70, 20)])

    def test_k_larger_than_n(self):
        data = "a 100 20"
        ranked = rank_students(data, 5)
        self.assertEqual(ranked, [("a", 100, 20)])

    def test_format_output(self):
        ranked = [("eva", 92, 20), ("zoe", 92, 21)]
        output = format_output(ranked)
        self.assertEqual(output, "eva 92 20\nzoe 92 21")


if __name__ == "__main__":
    unittest.main()
