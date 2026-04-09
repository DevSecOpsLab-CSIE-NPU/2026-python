# 測試題目 10062: 乳牛排序問題的單元測試
# 使用 unittest 框架來驗證 reconstruct_cow_order 函數的正確性。

import unittest
from question_10062 import reconstruct_cow_order

class TestCowOrder(unittest.TestCase):
    def test_case_1(self):
        # 範例：N=5, counts=[1,2,1,0]
        N = 5
        counts = [1, 2, 1, 0]
        expected = [2, 4, 5, 3, 1]
        self.assertEqual(reconstruct_cow_order(N, counts), expected)

    def test_case_2(self):
        N = 4
        counts = [1, 0, 2]
        # 計算
        # position4: count=2, k=3, available 1,2,3,4, 3rd:3, order[3]=3, remove3, available1,2,4
        # position3: count=0, k=1, 1st:1, order[2]=1, remove1, available2,4
        # position2: count=1, k=2, 2nd:4, order[1]=4, remove4, available2
        # position1:2
        expected = [2, 4, 1, 3]
        self.assertEqual(reconstruct_cow_order(N, counts), expected)

    def test_case_3(self):
        N = 3
        counts = [0, 1]
        # position3: count=1, k=2, available1,2,3, 2nd:2, order[2]=2, remove2, available1,3
        # position2: count=0, k=1, 1st:1, order[1]=1, remove1, available3
        # position1:3
        expected = [3, 1, 2]
        self.assertEqual(reconstruct_cow_order(N, counts), expected)

if __name__ == '__main__':
    unittest.main()