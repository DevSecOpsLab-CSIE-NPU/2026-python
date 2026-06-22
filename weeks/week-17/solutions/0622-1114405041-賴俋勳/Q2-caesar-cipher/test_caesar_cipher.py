import unittest
from caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    """
    題目：凱撒密碼 (Caesar Cipher) - 25分
    
    輸入：多行文字字串，每行包含字母和符號
    - 輸入包含多行，每行一個字串 (可能含行、長度≤1000)
    - 請獲得結束 (EOF) 為止
    
    輸出說明：
    - 對每一行輸入，輸出加密後的字串 (一行一行)
    - 對每行中的字元進行 SHIFT 替換
    
    加密規則 (SHIFT=2，依據學號1114405041)：
    - 大寫字母: A→C, B→D, ..., Y→A, Z→B (SHIFT=2)
    - 小寫字母: a→c, b→d, ..., y→a, z→b (SHIFT=2)
    - 其他字元保持不變
    """
    
    def test_basic_cipher_uppercase(self):
        """基本測試：大寫字母加密 (SHIFT=2)"""
        result = caesar_cipher("ABC", shift=2)
        self.assertEqual(result, "CDE")
    
    def test_basic_cipher_lowercase(self):
        """基本測試：小寫字母加密 (SHIFT=2)"""
        result = caesar_cipher("abc", shift=2)
        self.assertEqual(result, "cde")
    
    def test_cipher_with_wrap_around(self):
        """邊界測試：字母環繞 (SHIFT=2)"""
        result = caesar_cipher("YZA", shift=2)
        self.assertEqual(result, "ABC")
    
    def test_cipher_with_wrap_around_lowercase(self):
        """邊界測試：小寫字母環繞 (SHIFT=2)"""
        result = caesar_cipher("yza", shift=2)
        self.assertEqual(result, "abc")
    
    def test_cipher_mixed_case(self):
        """測試：混合大小寫 (SHIFT=2)"""
        result = caesar_cipher("Hello", shift=2)
        self.assertEqual(result, "Jgnnq")
    
    def test_cipher_with_punctuation(self):
        """測試：含標點符號 (SHIFT=2)"""
        result = caesar_cipher("Hello, World!", shift=2)
        self.assertEqual(result, "Jgnnq, Yqtnf!")
    
    def test_cipher_with_numbers(self):
        """測試：含數字 (SHIFT=2)"""
        result = caesar_cipher("abc123XYZ", shift=2)
        self.assertEqual(result, "cde123ZAB")
    
    def test_example_from_problem(self):
        """測試：來自題目的範例 (SHIFT=2)"""
        # 根據學號1114405041，SHIFT=2
        result = caesar_cipher("Hello, NPU!", shift=2)
        self.assertEqual(result, "Jgnnq, PRW!")
        
        result = caesar_cipher("abc XYZ", shift=2)
        self.assertEqual(result, "cde ZAB")
    
    def test_shift_zero(self):
        """邊界測試：SHIFT=0"""
        result = caesar_cipher("ABC xyz", shift=0)
        self.assertEqual(result, "ABC xyz")
    
    def test_shift_24(self):
        """邊界測試：SHIFT=24 (等於 -2 mod 26)"""
        result = caesar_cipher("ABC xyz", shift=24)
        self.assertEqual(result, "YZA vwx")


if __name__ == '__main__':
    unittest.main()
