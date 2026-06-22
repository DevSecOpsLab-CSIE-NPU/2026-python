import unittest
from caesar_cipher import caesar_cipher_encrypt

class TestCaesarCipher(unittest.TestCase):
    def test_sample_case_1(self):
        # 測試範例一（位移量 SHIFT=6）
        # Hello, NPU! -> Nkrru, TVA!
        self.assertEqual(caesar_cipher_encrypt("Hello, NPU!", 6), "Nkrru, TVA!")

    def test_sample_case_2(self):
        # 測試範例二（位移量 SHIFT=6）
        # abc XYZ -> ghi DEF
        self.assertEqual(caesar_cipher_encrypt("abc XYZ", 6), "ghi DEF")

    def test_edge_case_circular(self):
        # 邊角案例：英文字母循環溢位
        self.assertEqual(caesar_cipher_encrypt("Zz", 1), "Aa")

    def test_edge_case_non_english(self):
        # 邊角案例：非英文字元與空格
        text = "123!@# 澎科大"
        self.assertEqual(caesar_cipher_encrypt(text, 5), text)

    def test_empty_line(self):
        # 空行與空字串
        self.assertEqual(caesar_cipher_encrypt("", 6), "")

if __name__ == '__main__':
    unittest.main()
