import unittest
from solution import digit_root

class TestDigitRoot(unittest.TestCase):
    def test_sample_case_0(self):
        # 0 的數字根永遠為 0
        self.assertEqual(digit_root(0, 16), 0)

    def test_single_digit(self):
        # 小於 base 的數，數字根為其本身
        # 10 (base 16) -> 10
        self.assertEqual(digit_root(10, 16), 10)

    def test_multi_step(self):
        # 多次相加案例 (base 16)
        # 255 (10進位) = FF (16進位)
        # 15 + 15 = 30 (10進位) = 1E (16進位)
        # 1 + 14 = 15 (10進位)
        # 15 < 16, 停止。結果為 15
        self.assertEqual(digit_root(255, 16), 15)

    def test_edge_case_base(self):
        # 剛好等於 base
        # 16 (base 16) = 10 (16進位) -> 1+0 = 1
        self.assertEqual(digit_root(16, 16), 1)

if __name__ == '__main__':
    unittest.main()
