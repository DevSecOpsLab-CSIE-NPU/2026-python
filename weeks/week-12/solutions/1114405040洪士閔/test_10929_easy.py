"""
題目 10929 簡易版的單元測試
"""

import unittest


def is_div_11(num_str):
    """判斷是否為 11 的倍數"""
    odd_sum = 0
    even_sum = 0
    for idx, digit in enumerate(reversed(num_str)):
        if (idx + 1) % 2 == 1:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    return (odd_sum - even_sum) % 11 == 0


class TestDivisibleBy11(unittest.TestCase):
    """測試 11 的倍數判斷"""
    
    def test_11(self):
        """測試 11"""
        self.assertTrue(is_div_11("11"))
    
    def test_22(self):
        """測試 22"""
        self.assertTrue(is_div_11("22"))
    
    def test_12(self):
        """測試 12（非倍數）"""
        self.assertFalse(is_div_11("12"))
    
    def test_121(self):
        """測試 121（11×11）"""
        self.assertTrue(is_div_11("121"))
    
    def test_123(self):
        """測試 123（非倍數）"""
        self.assertFalse(is_div_11("123"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
