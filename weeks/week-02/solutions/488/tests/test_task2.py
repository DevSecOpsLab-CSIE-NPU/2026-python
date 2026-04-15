import pathlib
import sys
import unittest

BASE_DIR = pathlib.Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from task2_student_ranking import parse_header, parse_student, rank_students, top_k_students


class TestTask2StudentRanking(unittest.TestCase):
    def test_normal_ranking(self):
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("zoe", 92, 21),
            ("ian", 88, 19),
            ("leo", 75, 20),
            ("eva", 92, 20),
        ]
        ranked = rank_students(students)
        self.assertEqual(ranked[:3], [("eva", 92, 20), ("zoe", 92, 21), ("bob", 88, 19)])

    def test_tie_break_by_age_then_name(self):
        students = [("d", 90, 20), ("a", 90, 20), ("b", 90, 19)]
        self.assertEqual(rank_students(students), [("b", 90, 19), ("a", 90, 20), ("d", 90, 20)])

    def test_top_k_overflow(self):
        students = [("x", 60, 20), ("y", 80, 19)]
        self.assertEqual(top_k_students(students, 5), [("y", 80, 19), ("x", 60, 20)])

    def test_parse_helpers(self):
        self.assertEqual(parse_header("6 3"), (6, 3))
        self.assertEqual(parse_student("amy 88 20"), ("amy", 88, 20))


if __name__ == "__main__":
    unittest.main()
