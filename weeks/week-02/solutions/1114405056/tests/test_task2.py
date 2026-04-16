"""tests/test_task2.py — Task 2: Student Ranking 的單元測試"""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from task2_student_ranking import parse_students, rank_students


class TestParseStudents(unittest.TestCase):
    """測試學生資料解析。"""

    def test_basic_parse(self):
        """基本兩筆資料的解析。"""
        lines = ["amy 88 20", "bob 92 19"]
        result = parse_students(lines)
        self.assertEqual(result, [("amy", 88, 20), ("bob", 92, 19)])

    def test_single_student(self):
        """只有一位學生。"""
        result = parse_students(["zoe 75 21"])
        self.assertEqual(result, [("zoe", 75, 21)])

    def test_score_and_age_are_int(self):
        """確認 score 與 age 被解析為整數，而非字串。"""
        result = parse_students(["alice 100 18"])
        self.assertIsInstance(result[0][1], int)
        self.assertIsInstance(result[0][2], int)


class TestRankStudents(unittest.TestCase):
    """測試多條件排序邏輯。"""

    def test_normal_case(self):
        """HOMEWORK.md 提供的範例測資。"""
        students = [
            ("amy", 88, 20), ("bob", 88, 19), ("zoe", 92, 21),
            ("ian", 88, 19), ("leo", 75, 20), ("eva", 92, 20),
        ]
        result = rank_students(students, 3)
        self.assertEqual(result, [("eva", 92, 20), ("zoe", 92, 21), ("bob", 88, 19)])

    def test_tie_break_by_age(self):
        """同分時，年齡小的排前面。"""
        students = [("alice", 90, 22), ("bob", 90, 20)]
        result = rank_students(students, 2)
        self.assertEqual(result[0], ("bob", 90, 20))

    def test_tie_break_by_name(self):
        """同分同齡時，姓名字母序小的排前面。"""
        students = [("zoe", 90, 20), ("ann", 90, 20)]
        result = rank_students(students, 2)
        self.assertEqual(result[0], ("ann", 90, 20))

    def test_k_limits_output(self):
        """k 小於 n 時只輸出前 k 名。"""
        students = [("a", 100, 20), ("b", 80, 20), ("c", 60, 20)]
        result = rank_students(students, 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "a")

    def test_all_same_score_and_age(self):
        """分數與年齡全相同時，依姓名升冪排列。"""
        students = [("charlie", 80, 20), ("alice", 80, 20), ("bob", 80, 20)]
        result = rank_students(students, 3)
        self.assertEqual([s[0] for s in result], ["alice", "bob", "charlie"])


if __name__ == "__main__":
    unittest.main()
