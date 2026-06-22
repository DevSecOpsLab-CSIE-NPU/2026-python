import unittest
from solution import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_sample_case(self):
        # 範例測試案例 (SHIFT=2)
        # Hello, NPU! -> Jgnnq, P RW!
        # H(72) -> J(74)
        # e(101) -> g(103)
        # l(108) -> n(110)
        # l(108) -> n(110)
        # o(111) -> q(113)
        self.assertEqual(caesar_cipher("Hello, NPU!", 2), "Jgnnq, PRW!")

    def test_alphabet_wrap(self):
        # 字母循環測試 (SHIFT=2)
        # yz -> ab
        # YZ -> AB
        self.assertEqual(caesar_cipher("yz YZ", 2), "ab AB")

    def test_non_alphabet(self):
        # 非英文字母保留測試
        # 123 !@# -> 123 !@#
        self.assertEqual(caesar_cipher("123 !@#", 2), "123 !@#")

    def test_edge_case_empty(self):
        # 邊界案例: 空字串
        self.assertEqual(caesar_cipher("", 2), "")

if __name__ == '__main__':
    unittest.main()
