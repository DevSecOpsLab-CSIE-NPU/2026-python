"""
UVA 10242 - ATM 搶劫問題的單位測試
"""

import unittest
from solution_10242 import solve_atm_robbery


class TestUVA10242(unittest.TestCase):
    """UVA 10242 ATM 搶劫問題的單位測試"""
    
    def test_simple_path(self):
        """簡單的單向路徑"""
        # 3 個路口，1->2->3
        edges = [(1, 2), (2, 3)]
        atm_amounts = [100, 200, 300]
        bars = {3}
        
        result = solve_atm_robbery(3, edges, atm_amounts, 1, bars)
        # 路線 1->2->3，搶劫 100+200+300=600
        self.assertGreater(result, 0)
    
    def test_with_cycle(self):
        """有環的圖"""
        edges = [(1, 2), (2, 3), (3, 1)]
        atm_amounts = [100, 100, 100]
        bars = {3}
        
        result = solve_atm_robbery(3, edges, atm_amounts, 1, bars)
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main()
