"""
================================================================================
UVA 10931 - Parity（奇偶性） - 單元測試

測試策略：
  使用 unittest 框架，測試以下情況：
  1. 小的 2 的冪次方數（1, 2, 4, 8, 16, ...）
  2. 單一的 1（如 1）
  3. 連續的 1（如 3 = 11b, 7 = 111b, 15 = 1111b）
  4. 混合的 1 和 0（如 10, 21, 42）
  5. 邊界情況：最小值 1、最大值 2147483647
  6. 大數字

題目核心概念：
  - 「奇偶性」定義為二進位表示中 1 的個數
  - 轉換時不含前導零
  - 只需計算 1 的個數

================================================================================
"""

import unittest


def count_ones_in_binary(n):
    """
    計算一個整數的二進位表示中 1 的個數。
    
    參數：
        n (int): 正整數（1 ≤ n ≤ 2,147,483,647）
    
    返回：
        tuple: (二進位字串, 1 的個數)
               例：(n=5) → ("101", 2)
    """
    # 使用 Python 的 bin() 函數轉換為二進位字串
    # bin(5) 返回 "0b101"，所以需要去掉 "0b" 前綴
    binary_str = bin(n)[2:]
    
    # 計算 '1' 的個數
    ones_count = binary_str.count('1')
    
    return binary_str, ones_count


def format_parity_output(n):
    """
    生成符合格式的奇偶性輸出。
    
    參數：
        n (int): 正整數
    
    返回：
        str: 格式化後的輸出字串
             例：「The parity of 101 is 2 (mod 2).」
    """
    binary_str, ones_count = count_ones_in_binary(n)
    return f"The parity of {binary_str} is {ones_count} (mod 2)."


class TestParityCalculation(unittest.TestCase):
    """
    單元測試類：測試 count_ones_in_binary() 和 format_parity_output()
    """
    
    # ========================================================================
    # 測試 count_ones_in_binary() 函數
    # ========================================================================
    
    def test_binary_conversion_1(self):
        """測試：1 的二進位是 1"""
        binary_str, ones_count = count_ones_in_binary(1)
        self.assertEqual(binary_str, "1")
        self.assertEqual(ones_count, 1)
    
    def test_binary_conversion_2(self):
        """測試：2 的二進位是 10"""
        binary_str, ones_count = count_ones_in_binary(2)
        self.assertEqual(binary_str, "10")
        self.assertEqual(ones_count, 1)
    
    def test_binary_conversion_3(self):
        """測試：3 的二進位是 11"""
        binary_str, ones_count = count_ones_in_binary(3)
        self.assertEqual(binary_str, "11")
        self.assertEqual(ones_count, 2)
    
    def test_binary_conversion_4(self):
        """測試：4 的二進位是 100"""
        binary_str, ones_count = count_ones_in_binary(4)
        self.assertEqual(binary_str, "100")
        self.assertEqual(ones_count, 1)
    
    def test_binary_conversion_5(self):
        """測試：5 的二進位是 101"""
        binary_str, ones_count = count_ones_in_binary(5)
        self.assertEqual(binary_str, "101")
        self.assertEqual(ones_count, 2)
    
    def test_binary_conversion_10(self):
        """測試：10 的二進位是 1010"""
        binary_str, ones_count = count_ones_in_binary(10)
        self.assertEqual(binary_str, "1010")
        self.assertEqual(ones_count, 2)
    
    def test_binary_conversion_21(self):
        """測試：21 的二進位是 10101"""
        binary_str, ones_count = count_ones_in_binary(21)
        self.assertEqual(binary_str, "10101")
        self.assertEqual(ones_count, 3)
    
    def test_binary_conversion_7(self):
        """測試：7 的二進位是 111（全 1）"""
        binary_str, ones_count = count_ones_in_binary(7)
        self.assertEqual(binary_str, "111")
        self.assertEqual(ones_count, 3)
    
    def test_binary_conversion_15(self):
        """測試：15 的二進位是 1111（全 1）"""
        binary_str, ones_count = count_ones_in_binary(15)
        self.assertEqual(binary_str, "1111")
        self.assertEqual(ones_count, 4)
    
    def test_binary_conversion_255(self):
        """測試：255 的二進位是 11111111（8 個 1）"""
        binary_str, ones_count = count_ones_in_binary(255)
        self.assertEqual(binary_str, "11111111")
        self.assertEqual(ones_count, 8)
    
    def test_binary_conversion_256(self):
        """測試：256 的二進位是 100000000（1 個 1）"""
        binary_str, ones_count = count_ones_in_binary(256)
        self.assertEqual(binary_str, "100000000")
        self.assertEqual(ones_count, 1)
    
    def test_binary_conversion_1024(self):
        """測試：1024 的二進位是 10000000000（1 個 1）"""
        binary_str, ones_count = count_ones_in_binary(1024)
        self.assertEqual(binary_str, "10000000000")
        self.assertEqual(ones_count, 1)
    
    def test_binary_conversion_large_number(self):
        """測試：大數字 1000000 的二進位"""
        # 1000000 = 0b11110100001001000000（7 個 1）
        binary_str, ones_count = count_ones_in_binary(1000000)
        expected_binary = bin(1000000)[2:]
        self.assertEqual(binary_str, expected_binary)
        self.assertEqual(ones_count, 7)
    
    def test_binary_conversion_max_value(self):
        """測試：最大值 2147483647 的二進位"""
        # 2147483647 = 2^31 - 1 = 0b1111111111111111111111111111111（31 個 1）
        binary_str, ones_count = count_ones_in_binary(2147483647)
        self.assertEqual(ones_count, 31)
    
    # ========================================================================
    # 測試 format_parity_output() 函數
    # ========================================================================
    
    def test_output_format_1(self):
        """測試：輸出格式 - 1"""
        expected = "The parity of 1 is 1 (mod 2)."
        self.assertEqual(format_parity_output(1), expected)
    
    def test_output_format_2(self):
        """測試：輸出格式 - 2"""
        expected = "The parity of 10 is 1 (mod 2)."
        self.assertEqual(format_parity_output(2), expected)
    
    def test_output_format_10(self):
        """測試：輸出格式 - 10"""
        expected = "The parity of 1010 is 2 (mod 2)."
        self.assertEqual(format_parity_output(10), expected)
    
    def test_output_format_21(self):
        """測試：輸出格式 - 21"""
        expected = "The parity of 10101 is 3 (mod 2)."
        self.assertEqual(format_parity_output(21), expected)
    
    def test_output_format_255(self):
        """測試：輸出格式 - 255（全 1）"""
        expected = "The parity of 11111111 is 8 (mod 2)."
        self.assertEqual(format_parity_output(255), expected)
    
    # ========================================================================
    # 邊界測試
    # ========================================================================
    
    def test_boundary_minimum(self):
        """測試：最小值 1"""
        binary_str, ones_count = count_ones_in_binary(1)
        self.assertEqual(binary_str, "1")
        self.assertEqual(ones_count, 1)
    
    def test_boundary_maximum(self):
        """測試：最大值 2147483647"""
        # 2147483647 = 0x7FFFFFFF = 31 個 1
        binary_str, ones_count = count_ones_in_binary(2147483647)
        self.assertEqual(ones_count, 31)
    
    def test_power_of_two_1(self):
        """測試：2 的 1 次方 = 2"""
        binary_str, ones_count = count_ones_in_binary(2)
        self.assertEqual(ones_count, 1)
    
    def test_power_of_two_10(self):
        """測試：2 的 10 次方 = 1024"""
        binary_str, ones_count = count_ones_in_binary(1024)
        self.assertEqual(ones_count, 1)
    
    def test_power_of_two_minus_1_3(self):
        """測試：2 的 3 次方 - 1 = 7"""
        binary_str, ones_count = count_ones_in_binary(7)
        self.assertEqual(ones_count, 3)
    
    def test_power_of_two_minus_1_16(self):
        """測試：2 的 16 次方 - 1 = 65535"""
        binary_str, ones_count = count_ones_in_binary(65535)
        self.assertEqual(ones_count, 16)


# ============================================================================
# 主程式入口
# ============================================================================
if __name__ == "__main__":
    # 運行測試
    unittest.main(verbosity=2)
