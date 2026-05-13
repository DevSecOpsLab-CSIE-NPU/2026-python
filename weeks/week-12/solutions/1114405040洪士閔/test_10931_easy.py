"""
題目 10931 簡易版的單元測試
"""

import unittest


class TestParity(unittest.TestCase):
    """測試奇偶性計算"""
    
    def test_binary_conversion(self):
        """測試二進位轉換"""
        self.assertEqual(bin(1)[2:], "1")
        self.assertEqual(bin(2)[2:], "10")
        self.assertEqual(bin(5)[2:], "101")
    
    def test_parity_count(self):
        """測試 1 的個數計算"""
        self.assertEqual(bin(1)[2:].count('1'), 1)
        self.assertEqual(bin(3)[2:].count('1'), 2)
        self.assertEqual(bin(15)[2:].count('1'), 4)
    
    def test_various_numbers(self):
        """測試各種數字"""
        test_cases = [
            (1, 1),      # 1: 1
            (2, 1),      # 10: 1
            (3, 2),      # 11: 2
            (5, 2),      # 101: 2
            (15, 4),     # 1111: 4
        ]
        for num, expected_parity in test_cases:
            parity = bin(num)[2:].count('1')
            self.assertEqual(parity, expected_parity)


if __name__ == '__main__':
    unittest.main(verbosity=2)
