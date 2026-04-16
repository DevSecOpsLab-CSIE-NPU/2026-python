from __future__ import annotations

import pathlib
import sys
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from task2_student_ranking import Student, rank_students, solve  # noqa: E402


class TestTask2StudentRanking(unittest.TestCase):
    def test_sample_case(self) -> None:
        raw_input = (
            "6 3\n"
            "amy 88 20\n"
            "bob 88 19\n"
            "zoe 92 21\n"
            "ian 88 19\n"
            "leo 75 20\n"
            "eva 92 20\n"
        )
        expected = "eva 92 20\nzoe 92 21\nbob 88 19"
        self.assertEqual(solve(raw_input), expected)

    def test_tie_break_by_age_then_name(self) -> None:
        students = [
            Student("zoe", 90, 20),
            Student("amy", 90, 20),
            Student("bob", 90, 19),
        ]
        ranked = rank_students(students)
        self.assertEqual([s.name for s in ranked], ["bob", "amy", "zoe"])

    def test_k_greater_than_n(self) -> None:
        raw_input = "2 5\namy 80 20\nbob 70 21\n"
        expected = "amy 80 20\nbob 70 21"
        self.assertEqual(solve(raw_input), expected)


if __name__ == "__main__":
    unittest.main()