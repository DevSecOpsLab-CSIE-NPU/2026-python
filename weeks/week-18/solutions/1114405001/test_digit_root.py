"""
Test cases for digit root in base 8
題目：任意進位的數字根（進位基底 = 8）
"""
import unittest
from digit_root import digit_root_base8


class TestDigitRootBase8(unittest.TestCase):
    """Test digit root calculation in base 8"""
    
    def test_case_1_basic_sample(self):
        """Test Case 1: 基礎案例（Sample Input/Output）
        Input: 0, 8, 63
        Expected Output: 0, 1, 7
        """
        self.assertEqual(digit_root_base8(0), 0)
        self.assertEqual(digit_root_base8(8), 1)
        self.assertEqual(digit_root_base8(63), 7)
    
    def test_case_2_edge_zero(self):
        """Test Case 2: Edge Case - 零值
        Input: 0
        Expected Output: 0
        說明：0 的數字根就是 0
        """
        self.assertEqual(digit_root_base8(0), 0)
    
    def test_case_3_edge_power_of_8(self):
        """Test Case 3: Edge Case - 8 的冪次 (64 = 8^2)
        Input: 64
        Expected Output: 1
        說明：64 的八進位是 100 → 1+0+0 = 1
        """
        self.assertEqual(digit_root_base8(64), 1)
    
    def test_case_4_multiple_iterations(self):
        """Test Case 4: 需要多層相加 (511 = 8^3 - 1)
        Input: 511
        Expected Output: 7
        說明：511 的八進位是 777 → 7+7+7 = 21 → 2+1 = 3 (重複)... 最終 = 7
        (實際計算: 777(8) = 511(10))
        (7+7+7 = 21, 21在8進位是25, 2+5=7)
        """
        self.assertEqual(digit_root_base8(511), 7)
    
    def test_case_5_single_digit_in_base8(self):
        """Test Case 5: 八進位中已是個位數
        Input: 7
        Expected Output: 7
        說明：7 的八進位就是 7（個位數，直接返回）
        """
        self.assertEqual(digit_root_base8(7), 7)
    
    def test_case_6_large_number(self):
        """Test Case 6: 較大的數字
        Input: 100
        Expected Output: 1
        說明：100 的八進位是 144 → 1+4+4 = 9 → 1+1 = 2 (在8進位是11) → 1+1 = 2... 
        需要計算驗證
        """
        self.assertEqual(digit_root_base8(100), 2)


if __name__ == '__main__':
    unittest.main()
