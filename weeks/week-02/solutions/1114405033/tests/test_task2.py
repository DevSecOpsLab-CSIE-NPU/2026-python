import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task2_student_ranking import rank_students

class TestTask2(unittest.TestCase):
    def test_tie_break_logic(self):
        
        students = [
            ("bob", 88, 19), ("ian", 88, 19), ("amy", 88, 20)
        ]
        #
        res = rank_students(students, 3)
        self.assertEqual(res[0][0], "bob") # bob < ian (b 比 i 前面)
        self.assertEqual(res[1][0], "ian")

    def test_top_k_limit(self):
        
        students = [("eva", 90, 20)]
        res = rank_students(students, 5)
        self.assertEqual(len(res), 1)

    def test_reverse_score(self):
        
        students = [("low", 60, 20), ("high", 100, 20)]
        res = rank_students(students, 2)
        self.assertEqual(res[0][0], "high")