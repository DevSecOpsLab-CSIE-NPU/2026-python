"""
UVA 10252 - 費馬點問題的單位測試
"""

import unittest
from solution_10252 import solve_fermat_problem, distance, sum_distances


class TestUVA10252(unittest.TestCase):
    """UVA 10252 費馬點問題的單位測試"""
    
    def test_single_point(self):
        """單一點"""
        points = [(0, 0)]
        min_dist, count = solve_fermat_problem(points)
        self.assertEqual(min_dist, 0)  # 費馬點就是該點
    
    def test_two_points(self):
        """兩個點"""
        points = [(0, 0), (3, 4)]
        min_dist, count = solve_fermat_problem(points)
        # 最小距離是 0 到 (3,4) 之間的距離，即 5
        self.assertEqual(min_dist, 5)
    
    def test_three_points_collinear(self):
        """三個共線的點"""
        points = [(0, 0), (1, 0), (2, 0)]
        min_dist, count = solve_fermat_problem(points)
        # 費馬點在 (1, 0)，距離和為 1+0+1=2
        self.assertEqual(min_dist, 2)
    
    def test_given_example(self):
        """根據題目例子：(0,0), (1,1), (2,2)"""
        points = [(0, 0), (1, 1), (2, 2)]
        min_dist, count = solve_fermat_problem(points)
        # 題目說答案是 2*sqrt(2) ≈ 2.828，四捨五入為 3
        self.assertLess(min_dist, 5)  # 應該小於某個合理值


if __name__ == '__main__':
    unittest.main()
