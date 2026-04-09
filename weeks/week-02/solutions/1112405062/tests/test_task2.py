"""
================================================================================
Task 2: Student Ranking 測試程式
================================================================================

題目說明：
    給定多筆學生資料（name score age），請依規則排序：
    1. score 由高到低
    2. 同分時 age 由小到大
    3. 再同時 name 字母序由小到大
    輸出排序後前 k 名

================================================================================
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task2_student_ranking import student_ranking



class TestStudentRanking(unittest.TestCase):
    """測試學生排名功能"""

    def test_basic_case(self):
        """測試基本情況"""
        input_data = [
            "6 3",
            "amy 88 20",
            "bob 88 19",
            "zoe 92 21",
            "ian 88 19",
            "leo 75 20",
            "eva 92 20",
        ]
        result = student_ranking(input_data)
        expected = ["eva 92 20", "zoe 92 21", "bob 88 19"]
        self.assertEqual(result, expected)

    def test_empty_students(self):
        """測試無學生"""
        input_data = ["0 1"]
        result = student_ranking(input_data)
        self.assertEqual(result, [])

    def test_single_student(self):
        """測試單一學生"""
        input_data = ["1 1", "alice 100 20"]
        result = student_ranking(input_data)
        self.assertEqual(result, ["alice 100 20"])

    def test_same_score_different_age(self):
        """測試同分不同年齡"""
        input_data = ["3 3", "alice 90 20", "bob 90 19", "carol 90 21"]
        result = student_ranking(input_data)
        self.assertEqual(result[0], "bob 90 19")
        self.assertEqual(result[1], "alice 90 20")
        self.assertEqual(result[2], "carol 90 21")

    def test_k_less_than_n(self):
        """測試 k 小於 n"""
        input_data = [
            "5 2",
            "amy 88 20",
            "bob 95 19",
            "carol 92 21",
            "dave 85 20",
            "eve 90 19",
        ]
        result = student_ranking(input_data)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "bob 95 19")
        self.assertEqual(result[1], "carol 92 21")

    def test_all_same_score(self):
        """測試全部同分"""
        input_data = ["3 3", "alice 80 20", "bob 80 19", "carol 80 21"]
        result = student_ranking(input_data)
        self.assertEqual(result[0], "bob 80 19")
        self.assertEqual(result[1], "alice 80 20")
        self.assertEqual(result[2], "carol 80 21")


if __name__ == "__main__":
    unittest.main()
