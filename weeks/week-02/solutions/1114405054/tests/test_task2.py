import unittest
from task2_student_ranking import get_ranking

class TestTask2(unittest.TestCase):
    def test_sorting(self):
        data = [("amy", 88, 20), ("bob", 88, 19), ("eva", 92, 20)]
        res = get_ranking(data, 3)
        self.assertEqual(res[0][0], "eva")
        self.assertEqual(res[1][0], "bob")
    def test_k_limit(self):
        res = get_ranking([("a", 90, 20), ("b", 80, 20)], 1)
        self.assertEqual(len(res), 1)
    def test_name_order(self):
        res = get_ranking([("ian", 88, 19), ("bob", 88, 19)], 2)
        self.assertEqual(res[0][0], "bob")