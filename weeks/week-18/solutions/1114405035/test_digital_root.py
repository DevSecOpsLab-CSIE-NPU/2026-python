import unittest
from digital_root import get_digital_root

class TestDigitalRoot(unittest.TestCase):
    def test_sample_case_base_7(self):
        # 測試在進位基底 base=7 下的結果
        self.assertEqual(get_digital_root(0, 7), 0)
        self.assertEqual(get_digital_root(8, 7), 2)  # 8 -> 11_7 -> 1+1 = 2
        self.assertEqual(get_digital_root(63, 7), 3) # 63 -> 120_7 -> 1+2+0 = 3

    def test_sample_case_base_8(self):
        # 測試試卷上 Sample (base=8) 的結果
        self.assertEqual(get_digital_root(0, 8), 0)
        self.assertEqual(get_digital_root(8, 8), 1)  # 8 -> 10_8 -> 1+0 = 1
        self.assertEqual(get_digital_root(63, 8), 7) # 63 -> 77_8 -> 7+7 = 14 -> 16_8 -> 1+6 = 7

    def test_edge_case_less_than_base(self):
        # 邊角案例：x 本身就小於 base
        self.assertEqual(get_digital_root(5, 7), 5)

    def test_edge_case_equal_to_base(self):
        # 邊角案例：x 剛好等於 base
        self.assertEqual(get_digital_root(7, 7), 1) # 7 -> 10_7 -> 1+0 = 1

    def test_exception_negative(self):
        # 例外處理：小於 0 的負數應拋出 ValueError
        with self.assertRaises(ValueError):
            get_digital_root(-5, 7)

if __name__ == '__main__':
    unittest.main()
