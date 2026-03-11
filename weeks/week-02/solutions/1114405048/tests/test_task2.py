import unittest
import sys
sys.path.insert(0, '..')
from task2_student_ranking import Student, parse_students, rank_students


class TestStudentRanking(unittest.TestCase):
    """Task 2: Student Ranking - 3個測試案例 x 3個測試"""
    
    def test_parse_students_normal(self):
        """正常情況：資料正確解析"""
        data = [
            "amy 88 20",
            "bob 88 19",
            "zoe 92 21"
        ]
        students = parse_students(data)
        self.assertEqual(len(students), 3)
        self.assertEqual(students[0].name, "amy")
        self.assertEqual(students[1].score, 88)
        self.assertEqual(students[2].age, 21)
    
    def test_parse_students_edge_empty(self):
        """邊界情況：空列表"""
        students = parse_students([])
        self.assertEqual(students, [])
    
    def test_parse_students_single(self):
        """反例：只有一個學生"""
        data = ["john 95 22"]
        students = parse_students(data)
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "john")
    
    def test_rank_students_normal(self):
        """正常情況：給定範例"""
        students = [
            Student("amy", 88, 20),
            Student("bob", 88, 19),
            Student("zoe", 92, 21),
            Student("ian", 88, 19),
            Student("leo", 75, 20),
            Student("eva", 92, 20)
        ]
        ranked = rank_students(students)[:3]
        
        # 檢驗排序正確性
        self.assertEqual(ranked[0].name, "eva")
        self.assertEqual(ranked[1].name, "zoe")
        self.assertEqual(ranked[2].name, "bob")
    
    def test_rank_students_edge_tie_all(self):
        """邊界情況：全部同分、同齡"""
        students = [
            Student("zoe", 90, 20),
            Student("bob", 90, 20),
            Student("amy", 90, 20),
        ]
        ranked = rank_students(students)
        # 應按名字字母序排列
        self.assertEqual([s.name for s in ranked], ["amy", "bob", "zoe"])
    
    def test_rank_students_k_limit(self):
        """反例：只取前k名"""
        students = [
            Student("a", 90, 20),
            Student("b", 85, 20),
            Student("c", 80, 20),
            Student("d", 75, 20),
        ]
        # 假設函式支援k參數
        ranked = rank_students(students)[:2]
        self.assertEqual(len(ranked), 2)
        self.assertEqual(ranked[0].score, 90)
        self.assertEqual(ranked[1].score, 85)
    
    def test_rank_students_secondary_sort(self):
        """排序規則：同分按age小到大"""
        students = [
            Student("alice", 88, 20),
            Student("bob", 88, 19),
            Student("charlie", 88, 21),
        ]
        ranked = rank_students(students)
        # bob年紀最小（19），應該排在前面
        self.assertEqual(ranked[0].name, "bob")
        self.assertEqual(ranked[1].name, "alice")
        self.assertEqual(ranked[2].name, "charlie")
    
    def test_rank_students_tertiary_sort(self):
        """排序規則：同分同齡按名字字母序"""
        students = [
            Student("zoe", 88, 19),
            Student("bob", 88, 19),
            Student("alice", 88, 19),
        ]
        ranked = rank_students(students)
        self.assertEqual([s.name for s in ranked], ["alice", "bob", "zoe"])
    
    def test_rank_students_mixed_sorting(self):
        """綜合：複雜的混合排序情況"""
        students = [
            Student("zelda", 80, 21),
            Student("alice", 90, 21),
            Student("bob", 90, 20),
        ]
        ranked = rank_students(students)
        # 預期：bob(90,20) > alice(90,21) > zelda(80,21)
        self.assertEqual(ranked[0].name, "bob")
        self.assertEqual(ranked[1].name, "alice")
        self.assertEqual(ranked[2].name, "zelda")


if __name__ == '__main__':
    unittest.main()
