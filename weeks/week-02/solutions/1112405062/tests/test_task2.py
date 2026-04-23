import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task2_student_ranking import get_top_students


class TestTask2StudentRanking(unittest.TestCase):
    """Task 2: Student Ranking 測試類別"""

    def test_normal_case(self):
        """一般情況：正常排序取前3名"""
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("zoe", 92, 21),
            ("ian", 88, 19),
            ("leo", 75, 20),
            ("eva", 92, 20),
        ]
        result = get_top_students(students, 3)
        self.assertEqual(result[0][0], "eva")
        self.assertEqual(result[0][1], 92)
        self.assertEqual(result[1][0], "zoe")
        self.assertEqual(result[2][0], "bob")

    def test_tie_break_by_age(self):
        """同分時按 age 由小到大排序"""
        students = [
            ("alice", 100, 22),
            ("bob", 100, 19),
            ("chris", 100, 20),
        ]
        result = get_top_students(students, 3)
        self.assertEqual(result[0][0], "bob")
        self.assertEqual(result[1][0], "chris")
        self.assertEqual(result[2][0], "alice")

    def test_tie_break_by_name(self):
        """同分同 age 時按 name 字母序排序"""
        students = [
            ("zoe", 88, 20),
            ("amy", 88, 20),
            ("bob", 88, 20),
        ]
        result = get_top_students(students, 3)
        self.assertEqual(result[0][0], "amy")
        self.assertEqual(result[1][0], "bob")
        self.assertEqual(result[2][0], "zoe")

    def test_k_larger_than_n(self):
        """邊界情況：k 大於學生人數"""
        students = [("amy", 88, 20), ("bob", 75, 19)]
        result = get_top_students(students, 5)
        self.assertEqual(len(result), 2)

    def test_empty_input(self):
        """邊界情況：空列表"""
        result = get_top_students([], 3)
        self.assertEqual(result, [])

    def test_single_student(self):
        """邊界情況：只有一個學生"""
        students = [("amy", 88, 20)]
        result = get_top_students(students, 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "amy")


if __name__ == "__main__":
    unittest.main()
