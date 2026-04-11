import unittest
from task2_student_ranking import sort_students

class TestTask2(unittest.TestCase):

    def setUp(self):
        """準備測試資料"""
        self.students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("zoe", 92, 21),
            ("ian", 88, 19),
            ("leo", 75, 20),
            ("eva", 92, 20)
        ]

    def test_basic_ranking(self):
        """測試基本排序與 K 值截斷"""
        # 取前 3 名
        result = sort_students(self.students, 3)
        expected = [
            ("eva", 92, 20),
            ("zoe", 92, 21),
            ("bob", 88, 19)
        ]
        self.assertEqual(result, expected)

    def test_tie_break_score_age(self):
        """測試同分時，年齡小的優先 (88分裡, 19歲應在20歲前)"""
        data = [("older", 80, 25), ("younger", 80, 20)]
        result = sort_students(data, 2)
        self.assertEqual(result[0][0], "younger")

    def test_tie_break_all(self):
        """測試同分同齡時，名字字母序小的優先 (ian vs bob)"""
        # bob 和 ian 都是 88分/19歲，b < i，所以 bob 應在前
        data = [("ian", 88, 19), ("bob", 88, 19)]
        result = sort_students(data, 2)
        self.assertEqual(result[0][0], "bob")

    def test_k_greater_than_n(self):
        """邊界測試：當 k 大於學生總數時，應回傳所有學生"""
        data = [("amy", 100, 18)]
        result = sort_students(data, 5)
        self.assertEqual(len(result), 1)

    def test_zero_k(self):
        """邊界測試：當 k 為 0 時，應回傳空列表"""
        result = sort_students(self.students, 0)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()