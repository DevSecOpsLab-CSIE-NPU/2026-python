# test_10268.py
# UVA 10268 的單元測試程式
# 測試雞蛋掉落最小次數
# 繁體中文註解：測試二分搜索計算最小 trials

import unittest
from solution_10268 import min_trials

class TestUVA10268(unittest.TestCase):
    def test_k1_n1(self):
        self.assertEqual(min_trials(1, 1), 1)

    def test_k2_n1(self):
        self.assertEqual(min_trials(2, 1), 1)

    def test_k2_n2(self):
        self.assertEqual(min_trials(2, 2), 2)

if __name__ == '__main__':
    unittest.main()