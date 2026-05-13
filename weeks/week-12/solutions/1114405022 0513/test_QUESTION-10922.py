import unittest

# ============================================================================
# UVA 10922 - 2 the 9s 解題函數
# ============================================================================

def calculate_digit_sum(n):
    """
    計算一個數字的各位數字總和。
    
    將輸入數字（可以是字串或整數）的所有位數相加。
    例如：123 → 1+2+3 = 6
    例如："9999" → 9+9+9+9 = 36
    
    參數：
        n (int or str): 輸入的數字（可以是整數或字串）
    
    返回：
        int: 各位數字的總和
    """
    # 將輸入轉換為字串，以便逐位進行計算
    s = str(n)
    
    # 初始化總和為 0
    total = 0
    
    # 遍歷每一位數字
    for digit_char in s:
        # 將字符轉換為整數並累加
        total += int(digit_char)
    
    return total


def find_nine_degree(n):
    """
    找出一個數字的「9 的深度」。
    
    定義：一個能被 9 整除的數，需要重複多少次「計算各位數字總和」
    的操作才能得到數字 9。
    
    參數：
        n (int or str): 輸入的數字
    
    返回：
        int or None: 
          - 若是 9 的倍數，返回其深度（正整數）
          - 若不是 9 的倍數，返回 None
    
    演算法：
    1. 不斷計算各位數字的總和
    2. 深度計數器每次加 1
    3. 若得到 9，返回深度
    4. 若得到其他單位數，返回 None
    """
    
    # 將輸入轉換為整數（以支持大數字和字串輸入）
    n = int(n) if isinstance(n, str) else n
    
    # 初始化深度計數器
    degree = 0
    
    # 不斷計算各位數字總和，直到得到單位數 9 或其他
    while True:
        # 計算當前數字的各位數字總和
        n = calculate_digit_sum(n)
        
        # 深度加 1
        degree += 1
        
        # 檢查是否達到 9
        if n == 9:
            # 是 9 的倍數，返回深度
            return degree
        elif n < 10:
            # 已經是個位數但不是 9，不是 9 的倍數
            return None


# ============================================================================
# 單元測試類別
# ============================================================================

class TestNineDegree(unittest.TestCase):
    """
    UVA 10922 - 2 the 9s 的單元測試類別
    """
    
    def test_digit_sum_single_digit(self):
        """
        測試: 單位數的各位數字總和
        輸入: 9
        預期: 9
        說明: 單位數的各位數字總和就是它本身
        """
        result = calculate_digit_sum(9)
        self.assertEqual(result, 9)
    
    def test_digit_sum_two_digits(self):
        """
        測試: 兩位數的各位數字總和
        輸入: 18
        預期: 9 (1 + 8)
        說明: 1 + 8 = 9
        """
        result = calculate_digit_sum(18)
        self.assertEqual(result, 9)
    
    def test_digit_sum_multiple_digits(self):
        """
        測試: 多位數的各位數字總和
        輸入: 123
        預期: 6 (1 + 2 + 3)
        說明: 1 + 2 + 3 = 6
        """
        result = calculate_digit_sum(123)
        self.assertEqual(result, 6)
    
    def test_digit_sum_with_zeros(self):
        """
        測試: 包含零的多位數的各位數字總和
        輸入: 1023
        預期: 6 (1 + 0 + 2 + 3)
        說明: 0 不影響總和
        """
        result = calculate_digit_sum(1023)
        self.assertEqual(result, 6)
    
    def test_digit_sum_string_input(self):
        """
        測試: 字串輸入的各位數字總和
        輸入: "99"
        預期: 18 (9 + 9)
        說明: 函數應該能處理字串輸入
        """
        result = calculate_digit_sum("99")
        self.assertEqual(result, 18)
    
    def test_nine_degree_of_9(self):
        """
        測試: 最簡單的 9 的倍數
        輸入: 9
        預期: 1
        說明: 9 本身就是單位數 9，深度為 1
        """
        result = find_nine_degree(9)
        self.assertEqual(result, 1)
    
    def test_nine_degree_of_18(self):
        """
        測試: 18 的 9 的深度
        輸入: 18
        預期: 1
        說明: 1 + 8 = 9 → 深度 1
        """
        result = find_nine_degree(18)
        self.assertEqual(result, 1)
    
    def test_nine_degree_of_81(self):
        """
        測試: 81 的 9 的深度
        輸入: 81
        預期: 1
        說明: 8 + 1 = 9 → 深度 1
        """
        result = find_nine_degree(81)
        self.assertEqual(result, 1)
    
    def test_nine_degree_of_99(self):
        """
        測試: 99 的 9 的深度
        輸入: 99
        預期: 2
        說明: 
          第一步：9 + 9 = 18（深度 1）
          第二步：1 + 8 = 9（深度 2）
        """
        result = find_nine_degree(99)
        self.assertEqual(result, 2)
    
    def test_nine_degree_of_999(self):
        """
        測試: 999 的 9 的深度
        輸入: 999
        預期: 2
        說明:
          第一步：9 + 9 + 9 = 27（深度 1）
          第二步：2 + 7 = 9（深度 2）
        """
        result = find_nine_degree(999)
        self.assertEqual(result, 2)
    
    def test_nine_degree_of_9999(self):
        """
        測試: 9999 的 9 的深度
        輸入: 9999
        預期: 2
        說明:
          第一步：9 + 9 + 9 + 9 = 36（深度 1）
          第二步：3 + 6 = 9（深度 2）
        """
        result = find_nine_degree(9999)
        self.assertEqual(result, 2)
    
    def test_nine_degree_of_99999(self):
        """
        測試: 99999 的 9 的深度
        輸入: 99999
        預期: 3
        說明:
          第一步：9×5 = 45（深度 1）
          第二步：4 + 5 = 9（深度 2）
          等等，這應該是 2... 讓我重新計算
          
          實際上：9+9+9+9+9 = 45 → 4+5=9 → 深度 2
        """
        result = find_nine_degree(99999)
        self.assertEqual(result, 2)
    
    def test_nine_degree_of_large_number(self):
        """
        測試: 大數字的 9 的深度
        輸入: 123456789 (能被 9 整除嗎?)
        預期: 若是 9 的倍數則返回深度，否則返回 None
        說明: 
          各位數字和：1+2+3+4+5+6+7+8+9 = 45
          4 + 5 = 9
          所以是 9 的倍數，深度為 2
        """
        result = find_nine_degree(123456789)
        self.assertEqual(result, 2)
    
    def test_nine_degree_of_very_large_number(self):
        """
        測試: 非常大的數字
        輸入: 999999999999（12個9）
        預期: 該數是 9 的倍數，深度為 2
        說明:
          各位數字和：9×12 = 108（深度 1）
          1 + 0 + 8 = 9（深度 2）
        """
        result = find_nine_degree(999999999999)
        self.assertEqual(result, 2)
    
    def test_not_multiple_of_9_single(self):
        """
        測試: 不是 9 的倍數 - 單位數
        輸入: 5
        預期: None
        說明: 5 不是 9 的倍數
        """
        result = find_nine_degree(5)
        self.assertIsNone(result)
    
    def test_not_multiple_of_9_two_digits(self):
        """
        測試: 不是 9 的倍數 - 兩位數
        輸入: 19
        預期: None
        說明: 1 + 9 = 10 → 1 + 0 = 1，不是 9
        """
        result = find_nine_degree(19)
        self.assertIsNone(result)
    
    def test_not_multiple_of_9_three_digits(self):
        """
        測試: 不是 9 的倍數 - 三位數
        輸入: 100
        預期: None
        說明: 1 + 0 + 0 = 1，不是 9
        """
        result = find_nine_degree(100)
        self.assertIsNone(result)
    
    def test_nine_degree_string_input(self):
        """
        測試: 字串輸入的深度計算
        輸入: "18"
        預期: 1
        說明: 函數應該能處理字串輸入的大整數
        """
        result = find_nine_degree("18")
        self.assertEqual(result, 1)
    
    def test_nine_degree_very_long_string(self):
        """
        測試: 非常長的字串（超出整數範圍的情況）
        輸入: "999999999999999999999999999999"（30個9）
        預期: 深度為 2
        說明:
          9×30 = 270（深度 1）
          2 + 7 + 0 = 9（深度 2）
        """
        result = find_nine_degree("999999999999999999999999999999")
        self.assertEqual(result, 2)
    
    def test_nine_degree_pattern_9_18_27(self):
        """
        測試: 9 的倍數的基本規律
        預期: 9, 18, 27 都是 9 的倍數
        說明: 驗證基本規律
        """
        self.assertEqual(find_nine_degree(9), 1)
        self.assertEqual(find_nine_degree(18), 1)
        self.assertEqual(find_nine_degree(27), 1)
    
    def test_nine_degree_pattern_90_99_108(self):
        """
        測試: 其他 9 的倍數
        預期: 90, 99, 108 都是 9 的倍數
        說明: 驗證更多規律
        """
        self.assertIsNotNone(find_nine_degree(90))
        self.assertIsNotNone(find_nine_degree(99))
        self.assertIsNotNone(find_nine_degree(108))
    
    def test_not_multiple_non_9_endings(self):
        """
        測試: 不是 9 的倍數 - 各種情況
        預期: 1, 2, 3, 4, 5, 6, 7, 8 都應該返回 None
        說明: 單位數只有 9 才是 9 的倍數
        """
        for num in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.assertIsNone(find_nine_degree(num))


if __name__ == '__main__':
    # 運行所有測試
    unittest.main()
