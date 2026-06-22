"""
第二題 凱撒密碼 (Caesar Cipher) - 測試檔案
學號: 1114405003
SHIFT = 4 (個位 3 % 25 + 1 = 4)
"""
import unittest
from caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    """凱撒密碼測試"""

    def test_sample_1(self):
        """範例測資1: Hello, NPU! -> Lipps, RTY!"""
        result = caesar_cipher("Hello, NPU!", 4)
        self.assertEqual(result, "Lipps, RTY!")

    def test_sample_2(self):
        """範例測資2: abc XYZ -> efg BCD"""
        result = caesar_cipher("abc XYZ", 4)
        self.assertEqual(result, "efg BCD")

    def test_uppercase_wrap(self):
        """大寫循環: XYZ -> BCD"""
        result = caesar_cipher("XYZ", 4)
        self.assertEqual(result, "BCD")

    def test_lowercase_wrap(self):
        """小寫循環: xyz -> bcd"""
        result = caesar_cipher("xyz", 4)
        self.assertEqual(result, "bcd")

    def test_non_letters(self):
        """非字母保留: 123!@# -> 123!@#"""
        result = caesar_cipher("123!@#", 4)
        self.assertEqual(result, "123!@#")

    def test_empty_string(self):
        """空字串"""
        result = caesar_cipher("", 4)
        self.assertEqual(result, "")

    def test_all_non_letters(self):
        """全部非字母"""
        result = caesar_cipher("12345 !@#$%", 4)
        self.assertEqual(result, "12345 !@#$%")

    def test_mixed_case(self):
        """大小寫混合"""
        result = caesar_cipher("HeLLo", 4)
        self.assertEqual(result, "LiPPs")

    def test_shift_0(self):
        """SHIFT=0 不變"""
        result = caesar_cipher("Hello", 0)
        self.assertEqual(result, "Hello")

    def test_shift_26(self):
        """SHIFT=26 等同 SHIFT=0"""
        result = caesar_cipher("Hello", 26)
        self.assertEqual(result, "Hello")

    def test_single_char_upper(self):
        """單一大寫字元"""
        result = caesar_cipher("A", 1)
        self.assertEqual(result, "B")

    def test_single_char_lower(self):
        """單一小寫字元"""
        result = caesar_cipher("a", 1)
        self.assertEqual(result, "b")

    def test_z_to_a(self):
        """Z 循環回 A"""
        result = caesar_cipher("Z", 1)
        self.assertEqual(result, "A")

    def test_z_wrap_full(self):
        """Z 完整循環"""
        result = caesar_cipher("Z", 4)
        self.assertEqual(result, "D")

    def test_spaces_preserved(self):
        """空白保留"""
        result = caesar_cipher("A B C", 1)
        self.assertEqual(result, "B C D")

    def test_punctuation_preserved(self):
        """標點保留"""
        result = caesar_cipher("Hello, World!", 4)
        self.assertEqual(result, "Lipps, Asvph!")

    def test_long_string(self):
        """長字串"""
        input_str = "The quick brown fox jumps over the lazy dog"
        result = caesar_cipher(input_str, 4)
        self.assertEqual(result, "Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk")


if __name__ == "__main__":
    unittest.main()
