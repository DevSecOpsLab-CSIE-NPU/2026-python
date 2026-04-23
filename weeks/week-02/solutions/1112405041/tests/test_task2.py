import unittest
from task2_student_ranking import rank_students

class TestTask2(unittest.TestCase):
    def test_normal_ranking(self):
        students = [
            {'name': 'Alice', 'score': 85},
            {'name': 'Bob', 'score': 90},
            {'name': 'Charlie', 'score': 85}
        ]
        expected = [
            {'name': 'Bob', 'score': 90},
            {'name': 'Alice', 'score': 85},
            {'name': 'Charlie', 'score': 85}
        ]
        self.assertEqual(rank_students(students), expected)

    def test_same_score_different_names(self):
        students = [
            {'name': 'Zoe', 'score': 80},
            {'name': 'Adam', 'score': 80}
        ]
        expected = [
            {'name': 'Adam', 'score': 80},
            {'name': 'Zoe', 'score': 80}
        ]
        self.assertEqual(rank_students(students), expected)

    def test_empty_list(self):
        self.assertEqual(rank_students([]), [])

    def test_single_student(self):
        students = [{'name': 'Eve', 'score': 95}]
        self.assertEqual(rank_students(students), students)

if __name__ == '__main__':
    unittest.main()