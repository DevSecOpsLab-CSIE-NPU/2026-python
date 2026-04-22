# test_10252.py
# UVA 10252 的單元測試程式
# 測試幾何中位數
# 繁體中文註解：測試曼哈頓距離下的最小距離和

import unittest
from solution_10252 import solve

class TestUVA10252(unittest.TestCase):
    def test_example(self):
        # 範例測試
        points = [(0,0),(1,1),(2,2)]
        dist, count = solve(points)
        self.assertEqual(dist, 4)
        self.assertEqual(count, 1)

if __name__ == '__main__':
    unittest.main()