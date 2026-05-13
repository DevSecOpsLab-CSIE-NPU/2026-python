"""
UVA 10931 — Parity 單元測試套件

測試範圍：
- 基本二進位轉換與計數
- 邊界情況（小數字、大數字）
- 主程式的輸入輸出格式
"""

import unittest
import subprocess
import sys
import importlib.util


class TestParityBasics(unittest.TestCase):
    """測試 10931.py 中的 calculate_parity() 函式"""
    
    @classmethod
    def setUpClass(cls):
        """動態載入 10931 模組"""
        spec = importlib.util.spec_from_file_location(
            "module_10931",
            r"c:\Users\nina9\OneDrive\桌面\python\python2\2026-python\weeks\week-12\solutions\1114405018\0513\10931.py"
        )
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)
    
    def test_parity_1(self):
        """測試 I=1：二進位 '1' 有 1 個 1"""
        binary, parity = self.module.calculate_parity(1)
        self.assertEqual(binary, "1")
        self.assertEqual(parity, 1)
    
    def test_parity_2(self):
        """測試 I=2：二進位 '10' 有 1 個 1"""
        binary, parity = self.module.calculate_parity(2)
        self.assertEqual(binary, "10")
        self.assertEqual(parity, 1)
    
    def test_parity_10(self):
        """測試 I=10：二進位 '1010' 有 2 個 1"""
        binary, parity = self.module.calculate_parity(10)
        self.assertEqual(binary, "1010")
        self.assertEqual(parity, 2)
    
    def test_parity_21(self):
        """測試 I=21：二進位 '10101' 有 3 個 1"""
        binary, parity = self.module.calculate_parity(21)
        self.assertEqual(binary, "10101")
        self.assertEqual(parity, 3)
    
    def test_parity_7(self):
        """測試 I=7：二進位 '111' 有 3 個 1"""
        binary, parity = self.module.calculate_parity(7)
        self.assertEqual(binary, "111")
        self.assertEqual(parity, 3)
    
    def test_parity_8(self):
        """測試 I=8：二進位 '1000' 有 1 個 1"""
        binary, parity = self.module.calculate_parity(8)
        self.assertEqual(binary, "1000")
        self.assertEqual(parity, 1)
    
    def test_parity_15(self):
        """測試 I=15：二進位 '1111' 有 4 個 1"""
        binary, parity = self.module.calculate_parity(15)
        self.assertEqual(binary, "1111")
        self.assertEqual(parity, 4)
    
    def test_parity_16(self):
        """測試 I=16：二進位 '10000' 有 1 個 1"""
        binary, parity = self.module.calculate_parity(16)
        self.assertEqual(binary, "10000")
        self.assertEqual(parity, 1)
    
    def test_parity_255(self):
        """測試 I=255：二進位 '11111111' 有 8 個 1"""
        binary, parity = self.module.calculate_parity(255)
        self.assertEqual(binary, "11111111")
        self.assertEqual(parity, 8)
    
    def test_parity_1000(self):
        """測試 I=1000：二進位 '1111101000' 有 6 個 1"""
        binary, parity = self.module.calculate_parity(1000)
        self.assertEqual(binary, "1111101000")
        self.assertEqual(parity, 6)


class TestParityMainProgram(unittest.TestCase):
    """測試 10931.py 主程式的輸入輸出格式"""
    
    def test_sample_run(self):
        """設計一組輸入來驗證輸出格式（題目範例）"""
        # 題目給的測試用例
        input_data = "1\n2\n10\n21\n0\n"
        expected_output = (
            "The parity of 1 is 1 (mod 2).\n"
            "The parity of 10 is 1 (mod 2).\n"
            "The parity of 1010 is 2 (mod 2).\n"
            "The parity of 10101 is 3 (mod 2).\n"
        )
        
        result = subprocess.run(
            [sys.executable, r"c:\Users\nina9\OneDrive\桌面\python\python2\2026-python\weeks\week-12\solutions\1114405018\0513\10931.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.stdout, expected_output)


if __name__ == "__main__":
    unittest.main()
