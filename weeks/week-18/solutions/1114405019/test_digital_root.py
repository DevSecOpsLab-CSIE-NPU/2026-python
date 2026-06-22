import unittest

from digital_root import digit_sum_in_base, digital_root


class TestDigitSumInBase(unittest.TestCase):
    def test_single_round_conversion(self):
        # 8 的六進位是 12，1+2=3：驗證「轉進位＋單輪相加」本身算得對
        self.assertEqual(digit_sum_in_base(8, 6), 3)

    def test_result_can_still_be_multi_digit(self):
        # 63 的六進位是 143，1+4+3=8：8 在六進位仍是兩位數（12），
        # 這個中間值是「需要再轉一輪才會收斂」的關鍵，不能漏掉
        self.assertEqual(digit_sum_in_base(63, 6), 8)

    def test_zero_has_no_digits_to_sum(self):
        self.assertEqual(digit_sum_in_base(0, 6), 0)


class TestDigitalRoot(unittest.TestCase):
    def test_zero_is_fixed_to_zero_by_spec(self):
        # 題目明文規定 0 的數字根固定為 0，不是公式算出來的結果
        self.assertEqual(digital_root(0, 6), 0)

    def test_value_less_than_base_needs_no_iteration(self):
        # 4 < 6，在六進位下本身就是一位數，不需要任何累加迭代
        self.assertEqual(digital_root(4, 6), 4)

    def test_converges_after_one_round(self):
        # 8 -> 12(六進位) -> 1+2=3，一輪迭代即收斂
        self.assertEqual(digital_root(8, 6), 3)

    def test_converges_after_two_rounds(self):
        # 63 -> 143(六進位) -> 8 -> 12(六進位) -> 3
        # 第一輪相加後仍是兩位數，必須再轉一次進位再加一次，
        # 這是最容易漏掉的遞迴/迴圈邊界
        self.assertEqual(digital_root(63, 6), 3)

    def test_large_value_terminates_with_valid_single_digit(self):
        # x 接近 10^9 時，確認迴圈會結束且收斂到合法的一位數範圍，
        # 避免因為迴圈邊界寫錯造成死迴圈或效能爆炸
        root = digital_root(10**9, 6)
        self.assertGreaterEqual(root, 0)
        self.assertLess(root, 6)

    def test_base16_single_round(self):
        # 16 的十六進位是 "10"，1+0=1，一位數即收斂；
        # 確認邏輯沒有寫死成只服務小 base
        self.assertEqual(digital_root(16, 16), 1)

    def test_base16_digit_can_exceed_nine(self):
        # 255 的十六進位是 FF（十進位數字 15,15），15+15=30，
        # 30 的十六進位是 "1E"（1,14），1+14=15，15<16 收斂；
        # 驗證進位數字大於 9 時仍以十進位數值相加，不是只處理 0-9 字元
        self.assertEqual(digital_root(255, 16), 15)


if __name__ == "__main__":
    unittest.main()
