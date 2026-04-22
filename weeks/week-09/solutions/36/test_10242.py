# test_10242.py
# UVA 10242 的單元測試程式
# 測試搶劫最大金額
# 繁體中文註解：測試圖上最大搶劫金額的函數

import unittest
from solution_10242 import max_robbery

class TestUVA10242(unittest.TestCase):
    def test_example(self):
        # 範例測試
        n = 6
        edges = [(1,2),(1,3),(2,4),(3,5),(4,1),(4,6),(5,6)]
        atm = [0,10,5,15,10,10]  # 路口 1 to 6 的 ATM 金額
        s = 1
        bars = [5,6]
        self.assertEqual(max_robbery(n, edges, atm, s, bars), 47)

if __name__ == '__main__':
    unittest.main()