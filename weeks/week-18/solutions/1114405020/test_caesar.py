import unittest
from caesar import encrypt_caesar


class TestCaesarCipher(unittest.TestCase):
    def test_sample_1(self):
        """測試範例測資 1 (SHIFT = 1)
        Hello, NPU! -> If SHIFT=1: H->I, e->f, l->m, o->p, N->O, P->Q, U->V
        Expected: Ifmmp, OQV!
        """
        self.assertEqual(encrypt_caesar("Hello, NPU!", 1), "Ifmmp, OQV!")

    def test_sample_2(self):
        """測試範例測資 2 (SHIFT = 1)
        abc XYZ -> bcd YZA
        Expected: bcd YZA
        """
        self.assertEqual(encrypt_caesar("abc XYZ", 1), "bcd YZA")

    def test_circular_shift(self):
        """測試大小寫字母循環邊界 (Z->A, z->a)"""
        self.assertEqual(encrypt_caesar("Z", 1), "A")
        self.assertEqual(encrypt_caesar("z", 1), "a")

    def test_non_alphabet_preserved(self):
        """測試非英文字母保留原本字元"""
        self.assertEqual(encrypt_caesar("1234!@#$ 澎湖", 1), "1234!@#$ 澎湖")

    def test_empty_string(self):
        """測試空字串"""
        self.assertEqual(encrypt_caesar("", 1), "")


if __name__ == "__main__":
    unittest.main()
