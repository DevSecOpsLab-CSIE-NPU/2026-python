import unittest
from task2 import student_ranking

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
        expected = [
            {'name': 'eva', 'score': 92, 'age': 20},
            {'name': 'zoe', 'score': 92, 'age': 21},
            {'name': 'bob', 'score': 88, 'age': 19}
        ]
        self.assertEqual(student_ranking(students, k), expected)

    def test_empty_list(self):
        students = []
        k = 1
        expected = []
        self.assertEqual(student_ranking(students, k), expected)

    def test_all_same_score(self):
        students = [
            {'name': 'a', 'score': 90, 'age': 20},
            {'name': 'b', 'score': 90, 'age': 19},
            {'name': 'c', 'score': 90, 'age': 21}
        ]
        k = 2
        expected = [
            {'name': 'b', 'score': 90, 'age': 19},
            {'name': 'a', 'score': 90, 'age': 20}
        ]
        self.assertEqual(student_ranking(students, k), expected)

if __name__ == '__main__':
    unittest.main()
