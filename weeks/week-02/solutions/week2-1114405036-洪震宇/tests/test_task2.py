"""
Test Suite for Task 2: Student Ranking
測試複合排序規則功能
"""

import unittest
from task2_student_ranking import (
    Student, parse_students, rank_students, process_ranking
)


class TestStudentClass(unittest.TestCase):
    """Student 類別測試"""
    
    def test_student_creation(self):
        """測試建立學生物件"""
        student = Student("amy", "88", "20")
        self.assertEqual(student.name, "amy")
        self.assertEqual(student.score, 88)
        self.assertEqual(student.age, 20)
    
    def test_student_repr(self):
        """測試學生物件的字串表示"""
        student = Student("bob", "92", "21")
        self.assertEqual(str(student), "bob 92 21")
    
    def test_student_equality(self):
        """測試學生物件的相等性"""
        s1 = Student("alice", "85", "19")
        s2 = Student("alice", "85", "19")
        s3 = Student("alice", "85", "20")
        self.assertEqual(s1, s2)
        self.assertNotEqual(s1, s3)


class TestParseStudents(unittest.TestCase):
    """解析學生資料測試"""
    
    def test_parse_valid_students(self):
        """測試解析有效的學生資料"""
        lines = ["amy 88 20", "bob 90 19"]
        students = parse_students(lines)
        
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0].name, "amy")
        self.assertEqual(students[1].score, 90)
    
    def test_parse_invalid_format(self):
        """測試無效格式的解析"""
        lines = ["amy 88"]  # 缺少 age
        with self.assertRaises(ValueError):
            parse_students(lines)
    
    def test_parse_empty_list(self):
        """測試空列表解析"""
        lines = []
        students = parse_students(lines)
        self.assertEqual(len(students), 0)


class TestRankStudents(unittest.TestCase):
    """排序規則測試"""
    
    def test_sort_by_score_primary(self):
        """測試主排列：score 由高到低"""
        students = [
            Student("alice", "75", "20"),
            Student("bob", "92", "19"),
            Student("zoe", "92", "21"),
        ]
        ranked = rank_students(students, len(students))
        
        # 最高分應該在前面
        self.assertEqual(ranked[0].score, 92)
        self.assertEqual(ranked[2].score, 75)
    
    def test_sort_tie_break_by_age(self):
        """測試次排列：同分時 age 由小到大"""
        students = [
            Student("amy", "88", "20"),
            Student("bob", "88", "19"),
            Student("ian", "88", "19"),
        ]
        ranked = rank_students(students, len(students))
        
        # 88 分中，19 歲應該在前，且同齡時按名字排序
        scores = [s.score for s in ranked]
        ages = [s.age for s in ranked]
        
        self.assertEqual(scores, [88, 88, 88])
        self.assertEqual(ages[:2], [19, 19])  # 兩個 19 歲的在前
    
    def test_sort_tie_break_by_name(self):
        """測試三級排列：同分同齡時按名字字母序"""
        students = [
            Student("ian", "88", "19"),
            Student("bob", "88", "19"),
            Student("alice", "88", "19"),
        ]
        ranked = rank_students(students, len(students))
        
        # 應按 alice, bob, ian 順序
        names = [s.name for s in ranked]
        self.assertEqual(names, ["alice", "bob", "ian"])
    
    def test_rank_top_k(self):
        """測試只返回前 k 名"""
        students = [
            Student("alice", "75", "20"),
            Student("bob", "92", "19"),
            Student("zoe", "92", "21"),
            Student("eva", "88", "20"),
            Student("leo", "80", "18"),
        ]
        ranked = rank_students(students, 3)
        
        self.assertEqual(len(ranked), 3)
        # 應該是分數最高的三名
        self.assertEqual(ranked[0].score, 92)
        self.assertEqual(ranked[1].score, 92)
        self.assertEqual(ranked[2].score, 88)


class TestProcessRanking(unittest.TestCase):
    """完整排序流程測試"""
    
    def test_process_ranking_example(self):
        """測試作業範例"""
        n, k = 6, 3
        lines = [
            "amy 88 20",
            "bob 88 19",
            "zoe 92 21",
            "ian 88 19",
            "leo 75 20",
            "eva 92 20",
        ]
        ranked = process_ranking(n, k, lines)
        
        # 驗證結果
        self.assertEqual(len(ranked), 3)
        self.assertEqual(ranked[0].name, "eva")
        self.assertEqual(ranked[0].score, 92)
        self.assertEqual(ranked[1].name, "zoe")
        self.assertEqual(ranked[2].name, "bob")
    
    def test_process_ranking_k_equals_n(self):
        """測試 k 等於 n 的情況"""
        n, k = 3, 3
        lines = [
            "alice 90 20",
            "bob 85 21",
            "charlie 95 19",
        ]
        ranked = process_ranking(n, k, lines)
        
        self.assertEqual(len(ranked), 3)
        # 應按分數排序
        self.assertEqual(ranked[0].score, 95)
    
    def test_process_ranking_k_greater_than_n(self):
        """測試 k 大於 n 的邊界情況"""
        n, k = 2, 5
        lines = [
            "alice 90 20",
            "bob 85 21",
        ]
        ranked = process_ranking(n, k, lines)
        
        # 應該只返回存在的學生
        self.assertEqual(len(ranked), 2)


if __name__ == '__main__':
    unittest.main()
