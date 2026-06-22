import unittest
from digital_root import digital_root


class TestDigitalRoot(unittest.TestCase):

    def test_basic_base16(self):
        # 測試 base=16: 31 (10進位) -> 1F (16進位) -> 1+15=16 -> 10 (16進位) -> 1+0=1
        self.assertEqual(digital_root(31, 16), 1)

    def test_base16_large(self):
        # 測試 base=16: 255 (10進位) -> FF (16進位) -> 15+15=30 -> 1E (16進位) -> 1+14=15
        self.assertEqual(digital_root(255, 16), 15)

    def test_zero_input(self):
        # 測試 x=0
        self.assertEqual(digital_root(0, 16), 0)

    def test_base_zero(self):
        # 測試 base=0 時回傳 0
        self.assertEqual(digital_root(100, 0), 0)

    def test_different_base(self):
        # 測試其他基底: x=12, base=8 -> 14 (8進位) -> 1+4=5
        self.assertEqual(digital_root(12, 8), 5)


if __name__ == "__main__":
    unittest.main()
