"""
題目 10922 簡易版的單元測試
"""

import unittest


def digit_sum(s):
    return sum(int(c) for c in s)


def degree_of_nine(s):
    depth = 0
    while len(s) > 1:
        s = str(digit_sum(s))
        depth += 1
    return depth


class TestDegreeOfNine(unittest.TestCase):
    """測試 9 的深度計算"""
    
    def test_digit_sum(self):
        """測試數字和"""
        self.assertEqual(digit_sum("18"), 9)
        self.assertEqual(digit_sum("99"), 18)
    
    def test_degree_single(self):
        """測試單位數"""
        self.assertEqual(degree_of_nine("9"), 0)
    
    def test_degree_two_digits(self):
        """測試兩位數"""
        self.assertEqual(degree_of_nine("18"), 1)
        self.assertEqual(degree_of_nine("99"), 2)
    
    def test_degree_three_digits(self):
        """測試三位數"""
        self.assertEqual(degree_of_nine("999"), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
