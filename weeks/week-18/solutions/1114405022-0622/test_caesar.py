import unittest
from caesar import encrypt_caesar


class TestCaesarCipher(unittest.TestCase):

    def test_basic_encryption(self):
        # 測試一般英文字母加密（大小寫混合、包含標點）
        self.assertEqual(encrypt_caesar("Hello, NPU!", 3), "Khoor, QSX!")

    def test_wrap_around(self):
        # 測試大寫與小寫字母表末端的循環位移
        self.assertEqual(encrypt_caesar("abc XYZ", 3), "def ABC")

    def test_non_alphabet_and_empty(self):
        # 測試非英文字母與空字串保持不變
        self.assertEqual(encrypt_caesar("123 #!", 3), "123 #!")
        self.assertEqual(encrypt_caesar("", 3), "")

    def test_invalid_shift_raises_typeerror(self):
        # 測試非整數位移量拋出 TypeError
        with self.assertRaises(TypeError):
            encrypt_caesar("abc", "invalid")


if __name__ == "__main__":
    unittest.main()
