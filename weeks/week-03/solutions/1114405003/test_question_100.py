"""
題目 100：Collatz序列 (3n+1問題)

本測試程式針對UVA 100問題進行單元測試
測試內容包括：
1. 計算單一數字的cycle-length
2. 計算區間內的最大cycle-length
3. 邊界情況和各種輸入驗證
"""

import unittest


class CollatzSolver:
    """
    用於解決Collatz序列問題的求解器類別
    """
    
    def __init__(self):
        """初始化記憶化快取"""
        # 使用字典存儲已計算過的cycle-length，以加快後續查詢
        self.memo = {
            1: 1  # 基礎情況：1的cycle-length為1
        }
    
    def calculate_cycle_length(self, n):
        """
        計算單個數字n的cycle-length
        
        演算法流程：
        1. 如果n=1，返回1
        2. 如果n已在快取中，直接返回快取值
        3. 如果n是奇數，遞迴計算 (3*n+1) 的cycle-length，然後加1
        4. 如果n是偶數，遞迴計算 (n/2) 的cycle-length，然後加1
        
        Args:
            n (int): 要計算的數字
            
        Returns:
            int: n的cycle-length（序列長度）
        """
        # 檢查是否已有快取結果
        if n in self.memo:
            return self.memo[n]
        
        # 計算下一個數字
        if n % 2 == 1:  # n是奇數
            next_n = 3 * n + 1
        else:  # n是偶數
            next_n = n // 2
        
        # 遞迴計算並存儲結果
        result = 1 + self.calculate_cycle_length(next_n)
        self.memo[n] = result
        return result
    
    def find_max_cycle_length(self, i, j):
        """
        在區間[min(i,j), max(i,j)]內找到最大的cycle-length
        
        演算法流程：
        1. 確定區間的上下限（處理i > j的情況）
        2. 遍歷區間內的所有數字
        3. 計算每個數字的cycle-length
        4. 記錄並返回最大值
        
        Args:
            i (int): 區間的一個端點
            j (int): 區間的另一個端點
            
        Returns:
            int: 區間內所有數字的最大cycle-length
        """
        # 確保min_val <= max_val
        min_val = min(i, j)
        max_val = max(i, j)
        
        # 在區間內尋找最大的cycle-length
        max_length = 0
        for num in range(min_val, max_val + 1):
            length = self.calculate_cycle_length(num)
            max_length = max(max_length, length)
        
        return max_length


class TestQuestion100(unittest.TestCase):
    """
    題目100的單元測試類別
    測試Collatz序列求解的正確性
    """
    
    def setUp(self):
        """
        測試前的初始化
        為每個測試案例建立一個新的求解器實例
        """
        self.solver = CollatzSolver()
    
    # ==================== 單一數字的Cycle-Length測試 ====================
    
    def test_cycle_length_one(self):
        """測試基礎情況：n=1時，cycle-length應為1"""
        # 1本身是終止點，數列只有[1]，長度為1
        self.assertEqual(self.solver.calculate_cycle_length(1), 1)
    
    def test_cycle_length_two(self):
        """測試n=2的情況：數列[2, 1]，長度為2"""
        # 2 -> 1（偶數，2/2=1）
        # 預期cycle-length = 2
        self.assertEqual(self.solver.calculate_cycle_length(2), 2)
    
    def test_cycle_length_three(self):
        """測試n=3的情況：數列[3, 10, 5, 16, 8, 4, 2, 1]，長度為8"""
        # 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
        # 預期cycle-length = 8
        self.assertEqual(self.solver.calculate_cycle_length(3), 8)
    
    def test_cycle_length_four(self):
        """測試n=4的情況：數列[4, 2, 1]，長度為3"""
        # 4 -> 2 -> 1（都是偶數）
        # 預期cycle-length = 3
        self.assertEqual(self.solver.calculate_cycle_length(4), 3)
    
    def test_cycle_length_nine(self):
        """測試n=9的情況"""
        # 9 -> 28 -> 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
        # 預期cycle-length = 20
        self.assertEqual(self.solver.calculate_cycle_length(9), 20)
    
    def test_cycle_length_ten(self):
        """測試n=10的情況：預期cycle-length為7"""
        # 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
        # 預期cycle-length = 7
        self.assertEqual(self.solver.calculate_cycle_length(10), 7)
    
    def test_cycle_length_twenty_two(self):
        """測試n=22的情況：題目中提及的例子"""
        # 根據題目敘述，22的數列為：22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
        # 預期cycle-length = 16
        self.assertEqual(self.solver.calculate_cycle_length(22), 16)
    
    # ==================== 區間最大Cycle-Length測試 ====================
    
    def test_max_cycle_length_1_to_10(self):
        """測試區間[1, 10]：預期最大cycle-length為20"""
        # 根據題目提供的測試用例
        result = self.solver.find_max_cycle_length(1, 10)
        self.assertEqual(result, 20)
    
    def test_max_cycle_length_100_to_200(self):
        """測試區間[100, 200]：預期最大cycle-length為125"""
        # 根據題目提供的測試用例
        result = self.solver.find_max_cycle_length(100, 200)
        self.assertEqual(result, 125)
    
    def test_max_cycle_length_201_to_210(self):
        """測試區間[201, 210]：預期最大cycle-length為89"""
        # 根據題目提供的測試用例
        result = self.solver.find_max_cycle_length(201, 210)
        self.assertEqual(result, 89)
    
    def test_max_cycle_length_900_to_1000(self):
        """測試區間[900, 1000]：預期最大cycle-length為174"""
        # 根據題目提供的測試用例
        result = self.solver.find_max_cycle_length(900, 1000)
        self.assertEqual(result, 174)
    
    # ==================== 邊界情況和順序測試 ====================
    
    def test_max_cycle_length_with_reversed_order(self):
        """測試當第一個參數大於第二個參數時的情況"""
        # find_max_cycle_length應該正確處理 j > i 的情況
        result1 = self.solver.find_max_cycle_length(1, 10)
        result2 = self.solver.find_max_cycle_length(10, 1)  # 順序相反
        self.assertEqual(result1, result2)
    
    def test_max_cycle_length_single_element(self):
        """測試只有一個元素的區間"""
        # 當i = j時，區間只包含一個數字
        result = self.solver.find_max_cycle_length(5, 5)
        expected = self.solver.calculate_cycle_length(5)
        self.assertEqual(result, expected)
    
    def test_max_cycle_length_single_element_one(self):
        """測試區間為[1, 1]的特殊情況"""
        result = self.solver.find_max_cycle_length(1, 1)
        self.assertEqual(result, 1)
    
    # ==================== 記憶化快取的正確性測試 ====================
    
    def test_memoization_cache_hit(self):
        """測試記憶化快取功能"""
        # 第一次計算會經過完整遞迴
        result1 = self.solver.calculate_cycle_length(5)
        # 第二次計算應該直接從快取取得結果
        result2 = self.solver.calculate_cycle_length(5)
        self.assertEqual(result1, result2)
        # 驗證快取中確實存儲了結果
        self.assertIn(5, self.solver.memo)
    
    def test_memoization_improves_subsequent_calls(self):
        """測試記憶化對性能的改進"""
        # 計算一個較大的範圍來構建快取
        self.solver.find_max_cycle_length(1, 50)
        
        # 再次計算同一範圍應該更快（因為使用了快取）
        # 這裡測試的是功能正確性，而不是性能
        result1 = self.solver.find_max_cycle_length(1, 50)
        result2 = self.solver.find_max_cycle_length(1, 50)
        self.assertEqual(result1, result2)
    
    # ==================== 其他測試案例 ====================
    
    def test_larger_numbers(self):
        """測試較大的數字"""
        # 測試一些較大的數字，驗證演算法的穩定性
        result = self.solver.calculate_cycle_length(100)
        self.assertGreater(result, 1)  # cycle-length應該大於1
    
    def test_odd_numbers_sequence(self):
        """測試奇數序列"""
        # 測試幾個奇數的cycle-length是否合理
        for n in [1, 3, 5, 7, 9]:
            result = self.solver.calculate_cycle_length(n)
            self.assertGreaterEqual(result, 1)  # cycle-length應 >= 1
    
    def test_large_interval(self):
        """測試較大的區間"""
        # 測試區間[100, 500]
        result = self.solver.find_max_cycle_length(100, 500)
        self.assertGreater(result, 0)
        # 驗證結果是某個介於100-500的數字的cycle-length
        for n in range(100, 501):
            individual_length = self.solver.calculate_cycle_length(n)
            self.assertLessEqual(individual_length, result)


class TestQuestion100Integration(unittest.TestCase):
    """
    整合測試：測試完整的問題解答流程
    """
    
    def test_complete_solution_workflow(self):
        """測試完整的求解流程"""
        solver = CollatzSolver()
        
        # 模擬題目的測試用例
        test_cases = [
            (1, 10, 20),
            (100, 200, 125),
            (201, 210, 89),
            (900, 1000, 174)
        ]
        
        for i, j, expected_max in test_cases:
            with self.subTest(i=i, j=j):
                result = solver.find_max_cycle_length(i, j)
                self.assertEqual(result, expected_max,
                               f"區間[{i}, {j}]的最大cycle-length應為{expected_max}，但得到{result}")


if __name__ == '__main__':
    # 運行所有測試
    unittest.main(verbosity=2)
