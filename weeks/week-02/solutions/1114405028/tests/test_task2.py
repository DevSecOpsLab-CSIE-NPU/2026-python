import unittest
from task2_student_ranking import rank_students

class TestStudentRanking(unittest.TestCase):
    def test_normal_case(self):
        students = [
            {'name': 'amy', 'score': 88, 'age': 20},
            {'name': 'bob', 'score': 88, 'age': 19},
            {'name': 'zoe', 'score': 92, 'age': 21},
            {'name': 'ian', 'score': 88, 'age': 19},
            {'name': 'leo', 'score': 75, 'age': 20},
            {'name': 'eva', 'score': 92, 'age': 20}
        ]
        k = 3
        result = rank_students(students, k)
        expected = [
            {'name': 'eva', 'score': 92, 'age': 20},
            {'name': 'zoe', 'score': 92, 'age': 21},
            {'name': 'bob', 'score': 88, 'age': 19}
        ]
        self.assertEqual(result, expected)

    def test_k_larger_than_n(self):
        students = [
            {'name': 'a', 'score': 90, 'age': 20},
            {'name': 'b', 'score': 80, 'age': 21}
        ]
        k = 5
        result = rank_students(students, k)
        expected = [
            {'name': 'a', 'score': 90, 'age': 20},
            {'name': 'b', 'score': 80, 'age': 21}
        ]
        self.assertEqual(result, expected)

    def test_same_score_age_different_name(self):
        students = [
            {'name': 'charlie', 'score': 85, 'age': 22},
            {'name': 'alice', 'score': 85, 'age': 22},
            {'name': 'bob', 'score': 85, 'age': 22}
        ]
        k = 2
        result = rank_students(students, k)
        expected = [
            {'name': 'alice', 'score': 85, 'age': 22},
            {'name': 'bob', 'score': 85, 'age': 22}
        ]
        self.assertEqual(result, expected)

    def test_empty_list(self):
        students = []
        k = 3
        result = rank_students(students, k)
        self.assertEqual(result, [])

    def test_k_zero(self):
        students = [
            {'name': 'a', 'score': 90, 'age': 20}
        ]
        k = 0
        result = rank_students(students, k)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()