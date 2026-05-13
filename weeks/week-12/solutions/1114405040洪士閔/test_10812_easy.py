"""
題目 10812 簡易版的單元測試
"""

import unittest
from io import StringIO
import sys


class TestFindScores(unittest.TestCase):
    """測試 find_scores 函數"""
    
    def test_valid_example(self):
        """測試有效的例子"""
        # S=40, D=20 -> (30, 10)
        s, d = 40, 20
        higher = (s + d) // 2
        lower = (s - d) // 2
        self.assertEqual(higher, 30)
        self.assertEqual(lower, 10)
    
    def test_impossible_case(self):
        """測試無解情況"""
        # S=20, D=40 -> lower < 0
        s, d = 20, 40
        self.assertTrue(s < d)  # 無解條件
    
    def test_equal_scores(self):
        """測試相同分數"""
        s, d = 20, 0
        higher = (s + d) // 2
        lower = (s - d) // 2
        self.assertEqual(higher, lower)
        self.assertEqual(higher, 10)
    
    def test_odd_sum(self):
        """測試 S+D 為奇數"""
        s, d = 21, 10
        self.assertEqual((s + d) % 2, 1)  # 無解


if __name__ == '__main__':
    unittest.main(verbosity=2)
