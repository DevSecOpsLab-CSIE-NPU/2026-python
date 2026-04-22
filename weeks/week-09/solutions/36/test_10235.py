# test_10235.py
# UVA 10235 的單元測試程式
# 測試環覆蓋方法數
# 繁體中文註解：測試網格環覆蓋的函數

import unittest
from solution_10235 import count_snake_ways

class TestUVA10235(unittest.TestCase):
    def test_empty_grid(self):
        # 測試空網格
        grid = [[0, 0], [0, 0]]
        self.assertEqual(count_snake_ways(grid), 1)  # 沒有 1，可以不放蛇

    def test_single_one(self):
        # 單一 1，不能形成環
        grid = [[1]]
        self.assertEqual(count_snake_ways(grid), 0)  # 不能覆蓋

    def test_two_ones(self):
        # 兩個 1，不能形成環
        grid = [[1, 1]]
        self.assertEqual(count_snake_ways(grid), 0)

    def test_ring(self):
        # 環形
        grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        # 假設可以
        self.assertEqual(count_snake_ways(grid), 1)

if __name__ == '__main__':
    unittest.main()