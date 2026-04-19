import unittest

from task2_student_ranking import Student, format_ranked_students, parse_students, rank_students, solve, top_k_students


class Task2StudentRankingTests(unittest.TestCase):
    def test_rank_students_sorts_by_score_age_name(self):
        students = [
            Student("amy", 88, 20),
            Student("bob", 88, 19),
            Student("zoe", 92, 21),
            Student("ian", 88, 19),
        ]
        ranked = rank_students(students)
        self.assertEqual([student.name for student in ranked], ["zoe", "bob", "ian", "amy"])

    def test_top_k_students_returns_prefix(self):
        students = [Student("a", 90, 20), Student("b", 80, 18)]
        self.assertEqual(top_k_students(students, 1), [Student("a", 90, 20)])

    def test_parse_students_handles_basic_input(self):
        n, k, students = parse_students("2 1\na 90 20\nb 85 19\n")
        self.assertEqual((n, k), (2, 1))
        self.assertEqual(students, [Student("a", 90, 20), Student("b", 85, 19)])

    def test_format_ranked_students_formats_lines(self):
        result = format_ranked_students([Student("a", 90, 20), Student("b", 80, 18)])
        self.assertEqual(result, "a 90 20\nb 80 18")

    def test_solve_outputs_top_k_sample(self):
        text = "6 3\namy 88 20\nbob 88 19\nzoe 92 21\nian 88 19\nleo 75 20\neva 92 20\n"
        expected = "eva 92 20\nzoe 92 21\nbob 88 19"
        self.assertEqual(solve(text), expected)


if __name__ == "__main__":
    unittest.main()