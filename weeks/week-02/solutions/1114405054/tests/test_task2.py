import unittest
from task2_student_ranking import get_ranking
class TestTask2(unittest.TestCase):
    def test_sort(self):
        d = [("amy", 88, 20), ("bob", 88, 19)]
        self.assertEqual(get_ranking(d, 2)[0][0], "bob")
    def test_k(self):
        self.assertEqual(len(get_ranking([("a",90,20)], 1)), 1)
    def test_name(self):
        self.assertEqual(get_ranking([("b",80,20),("a",80,20)], 2)[0][0], "a")
