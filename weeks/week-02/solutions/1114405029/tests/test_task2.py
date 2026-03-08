import unittest
from task2_student_ranking import ranking


class TestStudentRanking(unittest.TestCase):

    def test_normal_ranking(self):
        """Test ranking by score"""
        students = [
            {"name": "amy", "score": 85, "age": 20},
            {"name": "bob", "score": 92, "age": 19},
            {"name": "charlie", "score": 78, "age": 21}
        ]

        result = ranking(students)

        self.assertEqual(result[0]["name"], "bob")
        self.assertEqual(result[1]["name"], "amy")
        self.assertEqual(result[2]["name"], "charlie")

    def test_tie_break_by_age(self):
        """Test tie-break when score is same"""
        students = [
            {"name": "amy", "score": 88, "age": 20},
            {"name": "bob", "score": 88, "age": 19},
            {"name": "zoe", "score": 92, "age": 21}
        ]

        result = ranking(students)

        self.assertEqual(result[0]["name"], "zoe")
        self.assertEqual(result[1]["name"], "bob")
        self.assertEqual(result[2]["name"], "amy")

    def test_tie_break_by_name(self):
        """Test tie-break when score and age are same"""
        students = [
            {"name": "ian", "score": 88, "age": 19},
            {"name": "bob", "score": 88, "age": 19},
            {"name": "amy", "score": 90, "age": 20}
        ]

        result = ranking(students)

        self.assertEqual(result[0]["name"], "amy")
        self.assertEqual(result[1]["name"], "bob")
        self.assertEqual(result[2]["name"], "ian")

    def test_empty_input(self):
        """Test empty student list"""
        students = []
        result = ranking(students)

        self.assertEqual(result, [])

    def test_single_student(self):
        """Test single student case"""
        students = [{"name": "alice", "score": 95, "age": 18}]

        result = ranking(students)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "alice")
        self.assertEqual(result[0]["score"], 95)
        self.assertEqual(result[0]["age"], 18)


if __name__ == "__main__":
    unittest.main()