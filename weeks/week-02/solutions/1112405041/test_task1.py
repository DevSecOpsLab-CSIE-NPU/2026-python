# test_task1.py
import unittest
from task1 import process_sequence

class TestTask1(unittest.TestCase):
    def test_basic(self):
        input_str = "5 3 5 2 9 2 8 3 1"
        d, a, ds, e = process_sequence(input_str)
        self.assertEqual(d, [5, 3, 2, 9, 8, 1])
        self.assertEqual(a, [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(e, [2, 2, 8])

    def test_empty(self):
        # 測試空輸入
        d, a, ds, e = process_sequence("")
        self.assertEqual(d, [])

if __name__ == "__main__":
    unittest.main()
