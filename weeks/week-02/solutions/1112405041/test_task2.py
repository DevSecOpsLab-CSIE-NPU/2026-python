# test_task2.py
import unittest
from task2 import rank_students

class TestTask2(unittest.TestCase):
    def test_tie_breaking(self):
        # score 同分時，比 age (小到大)，再比 name (小到大)
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("ian", 88, 19)
        ]
        # bob 和 ian 同分同齡，比名字 -> bob < ian
        res = rank_students(students, 3)
        self.assertEqual(res[0][0], "bob")
        self.assertEqual(res[1][0], "ian")
        self.assertEqual(res[2][0], "amy")

    def test_k_limit(self):
        students = [("a", 100, 20), ("b", 90, 20)]
        res = rank_students(students, 1)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0][0], "a")

if __name__ == "__main__":
    unittest.main()
