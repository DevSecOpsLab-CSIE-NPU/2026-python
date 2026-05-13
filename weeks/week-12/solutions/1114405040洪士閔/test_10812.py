"""
題目 10812 的單元測試

測試 q10812_solution.py 中的函數
"""

import unittest
from q10812_solution import find_scores


class TestFindScores(unittest.TestCase):
    """測試 find_scores 函數"""
    
    def test_valid_example1(self):
        """測試官方範例 1：S=40, D=20"""
        result = find_scores(40, 20)
        self.assertEqual(result, (30, 10))
    
    def test_valid_example2(self):
        """測試官方範例 2：S=20, D=40（應無解）"""
        result = find_scores(20, 40)
        self.assertIsNone(result)
    
    def test_valid_equal_scores(self):
        """測試兩隊得分相同：S=20, D=0"""
        result = find_scores(20, 0)
        self.assertEqual(result, (10, 10))
    
    def test_valid_single_point(self):
        """測試最小情況：S=2, D=0"""
        result = find_scores(2, 0)
        self.assertEqual(result, (1, 1))
    
    def test_odd_sum_plus_diff(self):
        """測試 S+D 為奇數：S=21, D=10"""
        result = find_scores(21, 10)
        self.assertIsNone(result)
    
    def test_negative_lower_score(self):
        """測試較低分為負：S=10, D=20"""
        result = find_scores(10, 20)
        self.assertIsNone(result)
    
    def test_zero_scores(self):
        """測試零分：S=0, D=0"""
        result = find_scores(0, 0)
        self.assertEqual(result, (0, 0))
    
    def test_large_scores(self):
        """測試大分數：S=1000, D=500"""
        result = find_scores(1000, 500)
        self.assertEqual(result, (750, 250))


if __name__ == '__main__':
    unittest.main(verbosity=2)
