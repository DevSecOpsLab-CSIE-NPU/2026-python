import unittest
import sys
import os

# 加入上層目錄以便 import 你的程式
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class TestYourFunction(unittest.TestCase):

    def test_case_1(self):
        """基本案例"""
        self.assertEqual(your_function(...), 預期結果)

    def test_case_2(self):
        """邊界案例"""
        self.assertEqual(your_function(...), 預期結果)

    def test_case_3(self):
        """例外案例"""
        with self.assertRaises(ValueError):
            your_function(...)


if __name__ == "__main__":
    unittest.main()
