import unittest

from task2_student_ranking import rank_students, solve, top_k_students


class TestTask2StudentRanking(unittest.TestCase):
    def test_rank_students_with_tie_breakers(self):
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("zoe", 92, 21),
            ("ian", 88, 19),
            ("leo", 75, 20),
            ("eva", 92, 20),
        ]
        expected = [
            ("eva", 92, 20),
            ("zoe", 92, 21),
            ("bob", 88, 19),
            ("ian", 88, 19),
            ("amy", 88, 20),
            ("leo", 75, 20),
        ]
        self.assertEqual(rank_students(students), expected)

    def test_top_k_students_when_k_exceeds_length(self):
        students = [("ann", 90, 18), ("ben", 70, 19)]
        self.assertEqual(top_k_students(students, 5), [("ann", 90, 18), ("ben", 70, 19)])

    def test_solve_with_zero_k_returns_empty_output(self):
        raw = "2 0\nann 90 18\nben 70 19"
        self.assertEqual(solve(raw), "")


if __name__ == "__main__":
    unittest.main()
