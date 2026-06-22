import unittest
from digital_root import find_digital_root


class TestDigitalRoot(unittest.TestCase):
    def test_zero(self):
        """測試 Edge Case: x = 0 應該回傳 0"""
        self.assertEqual(find_digital_root(0, 2), 0)

    def test_sample_8(self):
        """測試 x = 8, base = 2
        8 in bin is 1000 -> sum is 1. Expected: 1
        """
        self.assertEqual(find_digital_root(8, 2), 1)

    def test_sample_63(self):
        """測試 x = 63, base = 2
        63 in bin is 111111 -> sum is 6
        6 in bin is 110 -> sum is 2
        2 in bin is 10 -> sum is 1. Expected: 1
        """
        self.assertEqual(find_digital_root(63, 2), 1)

    def test_large_number(self):
        """測試大數 Edge Case: x = 10^9, base = 2"""
        self.assertEqual(find_digital_root(10**9, 2), 1)

    def test_invalid_input(self):
        """測試例外處理: 負數或無效 base 拋出 ValueError"""
        with self.assertRaises(ValueError):
            find_digital_root(-5, 2)
        with self.assertRaises(ValueError):
            find_digital_root(10, 1)


if __name__ == "__main__":
    unittest.main()
