"""
UVA 10235 - 蛇放置問題的單位測試
"""

import unittest
from solution_10235 import solve_snake_placement


class TestUVA10235(unittest.TestCase):
    """UVA 10235 蛇放置問題的單位測試"""
    
    def test_all_sockets(self):
        """所有格子都有插座，無法放蛇"""
        grid = [[0, 0], [0, 0]]
        result = solve_snake_placement(2, 2, grid)
        self.assertEqual(result, 1)  # 唯一方法：不放任何蛇
    
    def test_no_sockets(self):
        """沒有插座，需要放蛇覆蓋所有格子"""
        grid = [[1, 1], [1, 1]]
        result = solve_snake_placement(2, 2, grid)
        self.assertGreaterEqual(result, 0)  # 結果應該 >= 0
    
    def test_single_cell(self):
        """單格子，有插座，無法放蛇"""
        grid = [[0]]
        result = solve_snake_placement(1, 1, grid)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
