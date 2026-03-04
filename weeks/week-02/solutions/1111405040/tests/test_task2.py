"""
Test for Task 2: Student Ranking
"""

import unittest
from task2_student_ranking import (
    parse_student,
    sort_students,
    format_student
)


class TestParseStudent(unittest.TestCase):
    """測試學生資料解析函式。"""
    
    def test_parse_student_basic(self):
        """基本解析測試。"""
        line = "amy 88 20"
        expected = ("amy", 88, 20)
        self.assertEqual(parse_student(line), expected)
    
    def test_parse_student_different_format(self):
        """不同資料測試。"""
        line = "zoe 92 21"
        expected = ("zoe", 92, 21)
        self.assertEqual(parse_student(line), expected)
    
    def test_parse_student_numeric_conversion(self):
        """確保分數和年齡轉為整數。"""
        line = "bob 88 19"
        name, score, age = parse_student(line)
        self.assertIsInstance(score, int)
        self.assertIsInstance(age, int)


class TestSortStudentsScorePriority(unittest.TestCase):
    """測試排序中的分數優先級。"""
    
    def test_sort_students_score_descending(self):
        """測試分數由高到低排序。"""
        students = [
            ("amy", 88, 20),
            ("zoe", 92, 21),
            ("leo", 75, 20),
            ("eva", 92, 20)
        ]
        result = sort_students(students, 2)
        # 最高分應該都是 92
        self.assertEqual(result[0][1], 92)
        self.assertEqual(result[1][1], 92)
    
    def test_sort_students_same_score_age(self):
        """測試相同分數時按年齡排序（由小到大）。"""
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("ian", 88, 19),
            ("leo", 75, 20)
        ]
        result = sort_students(students, 3)
        # 分數都是 88 的應該按年齡排序
        self.assertEqual(result[0], ("bob", 88, 19))  # 或 ian，都是 19 歲
        self.assertEqual(result[2], ("amy", 88, 20))
    
    def test_sort_students_same_score_age_name(self):
        """測試分數和年齡都相同時按名字字母序排序。"""
        students = [
            ("ian", 88, 19),
            ("bob", 88, 19),
        ]
        result = sort_students(students, 2)
        # bob < ian（字母序）
        self.assertEqual(result[0][0], "bob")
        self.assertEqual(result[1][0], "ian")


class TestSortStudentsTopK(unittest.TestCase):
    """測試 K 值限制。"""
    
    def test_sort_students_return_k_results(self):
        """測試只返回前 k 名。"""
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("zoe", 92, 21),
            ("ian", 88, 19),
            ("leo", 75, 20),
            ("eva", 92, 20)
        ]
        result = sort_students(students, 3)
        self.assertEqual(len(result), 3)
    
    def test_sort_students_k_larger_than_list(self):
        """測試 k 大於列表長度。"""
        students = [
            ("alice", 90, 20),
            ("bob", 85, 21),
        ]
        result = sort_students(students, 5)
        # 應該返回全部 2 個學生
        self.assertEqual(len(result), 2)
    
    def test_sort_students_k_zero(self):
        """測試 k=0。"""
        students = [
            ("alice", 90, 20),
            ("bob", 85, 21),
        ]
        result = sort_students(students, 0)
        self.assertEqual(len(result), 0)


class TestSortStudentsComplex(unittest.TestCase):
    """複雜排序測試：使用題目範例。"""
    
    def test_sort_students_homework_example(self):
        """使用 HOMEWORK.md 範例測試。"""
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("zoe", 92, 21),
            ("ian", 88, 19),
            ("leo", 75, 20),
            ("eva", 92, 20)
        ]
        result = sort_students(students, 3)
        
        # 預期結果：
        # eva 92 20
        # zoe 92 21
        # bob 88 19（或 ian，因為都是 88 19，但 bob < ian）
        self.assertEqual(result[0], ("eva", 92, 20))
        self.assertEqual(result[1], ("zoe", 92, 21))
        self.assertEqual(result[2][0], "bob")  # bob 或 ian
        self.assertEqual(result[2][1], 88)
        self.assertEqual(result[2][2], 19)


class TestFormatStudent(unittest.TestCase):
    """測試學生資料格式化。"""
    
    def test_format_student_basic(self):
        """基本格式化測試。"""
        student = ("amy", 88, 20)
        expected = "amy 88 20"
        self.assertEqual(format_student(student), expected)
    
    def test_format_student_different_values(self):
        """不同值的格式化測試。"""
        student = ("zoe", 92, 21)
        expected = "zoe 92 21"
        self.assertEqual(format_student(student), expected)


if __name__ == '__main__':
    unittest.main()
