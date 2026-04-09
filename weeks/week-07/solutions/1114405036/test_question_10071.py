# 測試題目 10071: 計算六元組數量的單元測試

import unittest
from question_10071 import count_six_tuples

class TestSixTuples(unittest.TestCase):
    def test_case_1(self):
        S = [-1, 0, 1]
        # 可能的組合不多，手動計算
        # 例如，0+0+0+0+0+0=0, etc.
        expected = 27  # 3^6 = 729, but only when sum==f in S
        # 實際計算：所有 a,b,c,d,e,f in S, a+b+c+d+e==f
        # 由於 S 小，暴力計算
        count = 0
        for a in S:
            for b in S:
                for c in S:
                    for d in S:
                        for e in S:
                            for f in S:
                                if a + b + c + d + e == f:
                                    count += 1
        self.assertEqual(count_six_tuples(S), count)

    def test_case_2(self):
        S = [1, 2]
        count = 0
        for a in S:
            for b in S:
                for c in S:
                    for d in S:
                        for e in S:
                            for f in S:
                                if a + b + c + d + e == f:
                                    count += 1
        self.assertEqual(count_six_tuples(S), count)

if __name__ == '__main__':
    unittest.main()