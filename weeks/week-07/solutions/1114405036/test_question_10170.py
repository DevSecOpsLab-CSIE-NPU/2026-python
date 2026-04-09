# 測試題目 10170: 旅館房間的單元測試

import unittest
from question_10170 import find_group

class TestHotel(unittest.TestCase):
    def test_case_1(self):
        S = 4
        D = 9
        # 第1團 4人，住4天
        # 第2團 5人，住5天，累積9天
        # 第9天是第2團
        expected = 5
        self.assertEqual(find_group(S, D), expected)

    def test_case_2(self):
        S = 1
        D = 1
        expected = 1
        self.assertEqual(find_group(S, D), expected)

if __name__ == '__main__':
    unittest.main()