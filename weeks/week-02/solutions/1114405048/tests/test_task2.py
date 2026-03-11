"""
Task 2 Unit Tests: Student Ranking
測試學生排名功能
"""

import unittest
from task2_student_ranking import (
    parse_student_data,
    rank_students,
    format_output,
    process_ranking
)


class TestParseStudentData(unittest.TestCase):
    """測試學生資料解析"""
    
    def test_parse_normal(self):
        """正常解析"""
        n, k = 2, 1
        lines = ["amy 88 20", "bob 92 19"]
        students, returned_k = parse_student_data(n, k, lines)
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0], ("amy", 88, 20))
        self.assertEqual(students[1], ("bob", 92, 19))
        self.assertEqual(returned_k, 1)
    
    def test_parse_single_student(self):
        """單個學生"""
        n, k = 1, 1
        lines = ["zoe 100 21"]
        students, returned_k = parse_student_data(n, k, lines)
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0], ("zoe", 100, 21))


class TestRankStudents(unittest.TestCase):
    """測試排名邏輯"""
    
    def test_rank_by_score(self):
        """按 score 由高到低排名"""
        students = [
            ("amy", 88, 20),
            ("bob", 92, 19),
            ("zoe", 92, 21)
        ]
        ranked = rank_students(students, 3)
        # 92 高於 88
        self.assertEqual(ranked[2][1], 88)  # 最後是 88
        self.assertTrue(ranked[0][1] == 92)  # 前面是 92
        self.assertTrue(ranked[1][1] == 92)
    
    def test_rank_tie_break_by_age(self):
        """同分時按 age 由小到大"""
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("ian", 88, 19)
        ]
        ranked = rank_students(students, 3)
        # 同分 88，按年齡小到大
        # bob 和 ian 都是 19 歲，需要按名字排
        self.assertEqual(ranked[0][2], 19)  # 第一個是 19 歲
        self.assertEqual(ranked[1][2], 19)  # 第二個也是 19 歲
        self.assertEqual(ranked[2][2], 20)  # 第三個是 20 歲
    
    def test_rank_tie_break_by_name(self):
        """同分同年齡時按 name 字母序"""
        students = [
            ("zoe", 88, 19),
            ("bob", 88, 19),
            ("amy", 88, 19)
        ]
        ranked = rank_students(students, 3)
        # 都是 88 分，19 歲，按名字排
        self.assertEqual(ranked[0][0], "amy")
        self.assertEqual(ranked[1][0], "bob")
        self.assertEqual(ranked[2][0], "zoe")
    
    def test_rank_top_k(self):
        """只返回前 k 名"""
        students = [
            ("a", 100, 20),
            ("b", 90, 20),
            ("c", 80, 20),
            ("d", 70, 20)
        ]
        ranked = rank_students(students, 2)
        self.assertEqual(len(ranked), 2)
        self.assertEqual(ranked[0][0], "a")
        self.assertEqual(ranked[1][0], "b")


class TestFormatOutput(unittest.TestCase):
    """測試輸出格式"""
    
    def test_format_single_student(self):
        """單個學生輸出"""
        students = [("amy", 88, 20)]
        output = format_output(students)
        self.assertEqual(output[0], "amy 88 20")
    
    def test_format_multiple_students(self):
        """多個學生輸出"""
        students = [("eva", 92, 20), ("bob", 88, 19)]
        output = format_output(students)
        self.assertEqual(len(output), 2)
        self.assertEqual(output[0], "eva 92 20")
        self.assertEqual(output[1], "bob 88 19")


class TestProcessRanking(unittest.TestCase):
    """測試完整排名處理"""
    
    def test_process_ranking_example(self):
        """題目範例"""
        n, k = 6, 3
        lines = [
            "amy 88 20",
            "bob 88 19",
            "zoe 92 21",
            "ian 88 19",
            "leo 75 20",
            "eva 92 20"
        ]
        output = process_ranking(n, k, lines)
        self.assertEqual(len(output), 3)
        # 第一名應該是 eva (92, 20)
        self.assertEqual(output[0], "eva 92 20")
        # 第二名應該是 zoe (92, 21)
        self.assertEqual(output[1], "zoe 92 21")
        # 第三名應該是 bob (88, 19) - 與 ian 同分同年齡，但 b < i
        self.assertEqual(output[2], "bob 88 19")
    
    def test_process_ranking_single(self):
        """單個學生"""
        n, k = 1, 1
        lines = ["alice 100 20"]
        output = process_ranking(n, k, lines)
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], "alice 100 20")
    
    def test_process_ranking_k_greater_than_n(self):
        """k 大於學生數"""
        n, k = 2, 5
        lines = ["alice 100 20", "bob 90 21"]
        output = process_ranking(n, k, lines)
        self.assertEqual(len(output), 2)  # 只返回 2 個


if __name__ == "__main__":
    unittest.main()
