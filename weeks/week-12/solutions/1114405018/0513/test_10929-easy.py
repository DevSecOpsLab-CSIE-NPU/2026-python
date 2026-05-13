"""
UVA 10929 — Counting 11s (Easy Version) 測試套件
"""

import unittest
import subprocess
import sys
import importlib.util


class TestMultipleOf11Easy(unittest.TestCase):
    """測試 10929-easy.py 中的 is_multiple_of_11() 函式"""
    
    @classmethod
    def setUpClass(cls):
        """動態載入 10929-easy 模組"""
        spec = importlib.util.spec_from_file_location(
            "module_10929_easy",
            r"c:\Users\nina9\OneDrive\桌面\python\python2\2026-python\weeks\week-12\solutions\1114405018\0513\10929-easy.py"
        )
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)
    
    def test_simple_multiple_11(self):
        """簡單的 11 的倍數"""
        self.assertTrue(self.module.is_multiple_of_11("11"))
    
    def test_simple_multiple_22(self):
        """22 也是 11 的倍數"""
        self.assertTrue(self.module.is_multiple_of_11("22"))
    
    def test_121(self):
        """121 = 11 * 11"""
        self.assertTrue(self.module.is_multiple_of_11("121"))
    
    def test_not_multiple_10(self):
        """10 不是 11 的倍數"""
        self.assertFalse(self.module.is_multiple_of_11("10"))
    
    def test_not_multiple_12(self):
        """12 不是 11 的倍數"""
        self.assertFalse(self.module.is_multiple_of_11("12"))
    
    def test_single_digit_zero(self):
        """0 是 11 的倍數（0 % 11 == 0）"""
        self.assertTrue(self.module.is_multiple_of_11("0"))
    
    def test_alternating_sum_zero(self):
        """1001 = 11 * 91，交替和 = (1+0) - (0+1) = 0"""
        self.assertTrue(self.module.is_multiple_of_11("1001"))
    
    def test_large_multiple(self):
        """測試較大的 11 的倍數：9999 = 11 * 909"""
        self.assertTrue(self.module.is_multiple_of_11("9999"))
    
    def test_alternating_sum_negative(self):
        """測試交替和為負數的情況：5 不是 11 的倍數"""
        self.assertFalse(self.module.is_multiple_of_11("5"))
    
    def test_very_large_string(self):
        """測試超長字串：999999999999 應該是 11 的倍數"""
        self.assertTrue(self.module.is_multiple_of_11("999999999999"))


class TestMainProgramEasy(unittest.TestCase):
    """測試 10929-easy.py 主程式的 I/O"""
    
    def test_sample_run(self):
        """設計一組輸入來驗證輸出格式"""
        input_data = "121\n10\n0\n"
        expected_output = "121 is a multiple of 11.\n10 is not a multiple of 11.\n"
        
        result = subprocess.run(
            [sys.executable, r"c:\Users\nina9\OneDrive\桌面\python\python2\2026-python\weeks\week-12\solutions\1114405018\0513\10929-easy.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.stdout, expected_output)


if __name__ == "__main__":
    unittest.main()
