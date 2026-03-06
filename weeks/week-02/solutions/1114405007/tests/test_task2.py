import unittest

from task2_student_ranking import Student, rank_students


class TestTask2(unittest.TestCase):
    def test_rank_students_example_case(self) -> None:
        students = [
            Student("amy", 88, 20),
            Student("bob", 88, 19),
            Student("zoe", 92, 21),
            Student("ian", 88, 19),
            Student("leo", 75, 20),
            Student("eva", 92, 20),
        ]

        ranked = rank_students(students, 3)
        self.assertEqual(
            ranked,
            [
                Student("eva", 92, 20),
                Student("zoe", 92, 21),
                Student("bob", 88, 19),
            ],
        )

    def test_rank_students_tie_break_by_name(self) -> None:
        students = [Student("tom", 90, 20), Student("amy", 90, 20)]
        ranked = rank_students(students, 2)
        self.assertEqual(ranked, [Student("amy", 90, 20), Student("tom", 90, 20)])

    def test_rank_students_k_out_of_range(self) -> None:
        students = [Student("amy", 80, 19)]
        self.assertEqual(rank_students(students, 5), [Student("amy", 80, 19)])
        self.assertEqual(rank_students(students, 0), [])


if __name__ == "__main__":
    unittest.main()
