"""
UVA 10931 — Parity (Easy Version) 測試套件
"""

import unittest
import subprocess
import sys
import importlib.util


class TestParityEasy(unittest.TestCase):
    """測試 10931-easy.py 中的 get_parity_output() 函式"""
    
    @classmethod
    def setUpClass(cls):
        """動態載入 10931-easy 模組"""
        spec = importlib.util.spec_from_file_location(
            "module_10931_easy",
            r"c:\Users\nina9\OneDrive\桌面\python\python2\2026-python\weeks\week-12\solutions\1114405018\0513\10931-easy.py"
        )
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)
    
    def test_parity_1(self):
        """I=1：二進位 '1' 有 1 個 1"""
        result = self.module.get_parity_output(1)
        self.assertEqual(result, "The parity of 1 is 1 (mod 2).")
    
    def test_parity_2(self):
        """I=2：二進位 '10' 有 1 個 1"""
        result = self.module.get_parity_output(2)
        self.assertEqual(result, "The parity of 10 is 1 (mod 2).")
    
    def test_parity_10(self):
        """I=10：二進位 '1010' 有 2 個 1"""
        result = self.module.get_parity_output(10)
        self.assertEqual(result, "The parity of 1010 is 2 (mod 2).")
    
    def test_parity_21(self):
        """I=21：二進位 '10101' 有 3 個 1"""
        result = self.module.get_parity_output(21)
        self.assertEqual(result, "The parity of 10101 is 3 (mod 2).")
    
    def test_parity_7(self):
        """I=7：二進位 '111' 有 3 個 1"""
        result = self.module.get_parity_output(7)
        self.assertEqual(result, "The parity of 111 is 3 (mod 2).")
    
    def test_parity_8(self):
        """I=8：二進位 '1000' 有 1 個 1"""
        result = self.module.get_parity_output(8)
        self.assertEqual(result, "The parity of 1000 is 1 (mod 2).")
    
    def test_parity_15(self):
        """I=15：二進位 '1111' 有 4 個 1"""
        result = self.module.get_parity_output(15)
        self.assertEqual(result, "The parity of 1111 is 4 (mod 2).")
    
    def test_parity_16(self):
        """I=16：二進位 '10000' 有 1 個 1"""
        result = self.module.get_parity_output(16)
        self.assertEqual(result, "The parity of 10000 is 1 (mod 2).")
    
    def test_parity_255(self):
        """I=255：二進位 '11111111' 有 8 個 1"""
        result = self.module.get_parity_output(255)
        self.assertEqual(result, "The parity of 11111111 is 8 (mod 2).")
    
    def test_parity_1000(self):
        """I=1000：二進位 '1111101000' 有 6 個 1"""
        result = self.module.get_parity_output(1000)
        self.assertEqual(result, "The parity of 1111101000 is 6 (mod 2).")


class TestParityEasyMainProgram(unittest.TestCase):
    """測試 10931-easy.py 主程式"""
    
    def test_sample_run(self):
        """驗證整合測試（題目範例）"""
        input_data = "1\n2\n10\n21\n0\n"
        expected_output = (
            "The parity of 1 is 1 (mod 2).\n"
            "The parity of 10 is 1 (mod 2).\n"
            "The parity of 1010 is 2 (mod 2).\n"
            "The parity of 10101 is 3 (mod 2).\n"
        )
        
        result = subprocess.run(
            [sys.executable, r"c:\Users\nina9\OneDrive\桌面\python\python2\2026-python\weeks\week-12\solutions\1114405018\0513\10931-easy.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.stdout, expected_output)


if __name__ == "__main__":
    unittest.main()
