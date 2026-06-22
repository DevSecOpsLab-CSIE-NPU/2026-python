import unittest
import sys
import io
from A02 import caesar_encrypt, main


class TestCaesarEncrypt(unittest.TestCase):

    def test_basic_case(self):
        """基本案例：Hello, NPU! with shift=2 -> Jgnnq, PRW!"""
        result = caesar_encrypt("Hello, NPU!", shift=2)
        self.assertEqual(result, "Jgnnq, PRW!")

    def test_lowercase_wrap(self):
        """小寫繞圈：xyz -> zab"""
        result = caesar_encrypt("xyz", shift=2)
        self.assertEqual(result, "zab")

    def test_uppercase_wrap(self):
        """大寫繞圈：XYZ -> ZAB"""
        result = caesar_encrypt("XYZ", shift=2)
        self.assertEqual(result, "ZAB")

    def test_non_alpha_unchanged(self):
        """非字母不動：123 !@# -> 123 !@#"""
        result = caesar_encrypt("123 !@#", shift=2)
        self.assertEqual(result, "123 !@#")

    def test_empty_string(self):
        """空字串 -> 空字串"""
        result = caesar_encrypt("", shift=2)
        self.assertEqual(result, "")

    def test_mixed_case(self):
        """混合大小寫：abc XYZ -> cde ZAB"""
        result = caesar_encrypt("abc XYZ", shift=2)
        self.assertEqual(result, "cde ZAB")

    def test_all_letters_shift_2(self):
        """全部字母位移2驗證循環"""
        result = caesar_encrypt("AZaz", shift=2)
        self.assertEqual(result, "CBcb")

    def test_main_output(self):
        """主程式多行輸出"""
        sys.stdin = io.StringIO("Hello, NPU!\nabc XYZ\n")
        sys.stdout = io.StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Jgnnq, PRW!\ncde ZAB")


if __name__ == "__main__":
    unittest.main()
