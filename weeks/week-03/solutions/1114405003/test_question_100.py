"""
題目 100 - Collatz 序列 (3n+1 問題) 單元測試

描述：
給定一個正整數 n，根據以下規則生成序列：
1. 如果 n = 1，停止
2. 如果 n 是奇數，則 n = 3 * n + 1
3. 如果 n 是偶數，則 n = n / 2
4. 重複上述步驟直到 n = 1

序列的長度（步數）稱為 "cycle-length"。
例：22 的序列為 [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]，
長度為 16。

題目要求：給定兩個整數 i、j，找出區間 [min(i,j), max(i,j)] 內所有數的
cycle-length 最大值。

測試文件導入實現代碼自 solution_question_100.py
"""

import unittest
# 導入實現類
from solution_question_100 import CollatzSequence


class TestCollatzSequence(unittest.TestCase):
    """Collatz 序列的單元測試類"""
    
    def setUp(self):
        """測試前準備：初始化 CollatzSequence 實例"""
        self.collatz = CollatzSequence()
    
    # =====================================================
    # 測試 1：基本數字的 cycle-length 計算
    # =====================================================
    
    def test_cycle_length_of_one(self):
        """
        測試最基礎情況：n=1 的 cycle-length 應為 1
        
        根據題目規則，n=1 時演算法停止，序列長度為 1。
        """
        self.assertEqual(self.collatz.calculate_cycle_length(1), 1)
    
    def test_cycle_length_of_two(self):
        """
        測試 n=2 的 cycle-length
        
        序列：2 -> 1，長度為 2
        """
        self.assertEqual(self.collatz.calculate_cycle_length(2), 2)
    
    def test_cycle_length_of_five(self):
        """
        測試 n=5 的 cycle-length
        
        序列：5 -> 16 -> 8 -> 4 -> 2 -> 1，長度為 6
        """
        self.assertEqual(self.collatz.calculate_cycle_length(5), 6)
    
    def test_cycle_length_of_twenty_two(self):
        """
        測試題目範例：n=22 的 cycle-length 應為 16
        
        序列：22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
        """
        self.assertEqual(self.collatz.calculate_cycle_length(22), 16)
    
    def test_cycle_length_of_large_number(self):
        """
        測試較大的數字，例如 n=999999
        
        確保演算法能正確處理大數字（在 1,000,000 以內）
        """
        result = self.collatz.calculate_cycle_length(999999)
        # cycle-length 應為正整數，且大於等於 1
        self.assertIsInstance(result, int)
        self.assertGreater(result, 1)
    
    # =====================================================
    # 測試 2：序列生成的正確性驗證
    # =====================================================
    
    def test_sequence_generation_for_one(self):
        """
        測試序列生成：n=1 的序列應為 [1]
        """
        expected = [1]
        self.assertEqual(self.collatz.get_sequence(1), expected)
    
    def test_sequence_generation_for_two(self):
        """
        測試序列生成：n=2 的序列應為 [2, 1]
        """
        expected = [2, 1]
        self.assertEqual(self.collatz.get_sequence(2), expected)
    
    def test_sequence_generation_for_five(self):
        """
        測試序列生成：n=5 的序列應為 [5, 16, 8, 4, 2, 1]
        """
        expected = [5, 16, 8, 4, 2, 1]
        self.assertEqual(self.collatz.get_sequence(5), expected)
    
    def test_sequence_generation_for_twenty_two(self):
        """
        測試序列生成：n=22 的序列應包含題目規定的所有數字
        """
        expected = [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(self.collatz.get_sequence(22), expected)
    
    def test_sequence_always_ends_with_one(self):
        """
        測試序列恆以 1 結尾（根據題目保證，0 < n < 1,000,000）
        """
        # 測試多個不同的起始數字
        for n in [1, 2, 5, 10, 22, 100, 999]:
            sequence = self.collatz.get_sequence(n)
            self.assertEqual(sequence[-1], 1, f"序列 {n} 未以 1 結尾")
    
    def test_sequence_length_matches_cycle_length(self):
        """
        測試序列長度等於 cycle-length
        
        get_sequence 返回的列表長度應等於 calculate_cycle_length 的返回值
        """
        for n in [1, 2, 5, 10, 22, 100]:
            seq = self.collatz.get_sequence(n)
            cycle_len = self.collatz.calculate_cycle_length(n)
            self.assertEqual(len(seq), cycle_len, 
                           f"n={n} 的序列長度 {len(seq)} 不等於 cycle-length {cycle_len}")
    
    # =====================================================
    # 測試 3：區間最大 cycle-length 查詢
    # =====================================================
    
    def test_max_cycle_length_single_number(self):
        """
        測試區間只有一個數字的情況：find_max_cycle_length(5, 5) 應返回 cycle-length(5)
        """
        i, j, max_len = self.collatz.find_max_cycle_length(5, 5)
        self.assertEqual(i, 5)
        self.assertEqual(j, 5)
        self.assertEqual(max_len, self.collatz.calculate_cycle_length(5))
    
    def test_max_cycle_length_range_1_to_10(self):
        """
        測試第一個範例：區間 [1, 10] 應返回最大 cycle-length 20
        
        根據題目測試用例預期輸出為 (1, 10, 20)
        """
        i, j, max_len = self.collatz.find_max_cycle_length(1, 10)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)
        self.assertEqual(max_len, 20)
    
    def test_max_cycle_length_range_100_to_200(self):
        """
        測試第二個範例：區間 [100, 200] 應返回最大 cycle-length 125
        
        根據題目測試用例預期輸出為 (100, 200, 125)
        """
        i, j, max_len = self.collatz.find_max_cycle_length(100, 200)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)
        self.assertEqual(max_len, 125)
    
    def test_max_cycle_length_range_201_to_210(self):
        """
        測試第三個範例：區間 [201, 210] 應返回最大 cycle-length 89
        
        根據題目測試用例預期輸出為 (201, 210, 89)
        """
        i, j, max_len = self.collatz.find_max_cycle_length(201, 210)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)
        self.assertEqual(max_len, 89)
    
    def test_max_cycle_length_range_900_to_1000(self):
        """
        測試第四個範例：區間 [900, 1000] 應返回最大 cycle-length 174
        
        根據題目測試用例預期輸出為 (900, 1000, 174)
        """
        i, j, max_len = self.collatz.find_max_cycle_length(900, 1000)
        self.assertEqual(i, 900)
        self.assertEqual(j, 1000)
        self.assertEqual(max_len, 174)
    
    # =====================================================
    # 測試 4：端點順序的處理（題目要求不限順序）
    # =====================================================
    
    def test_max_cycle_length_reversed_order(self):
        """
        測試當 i > j 時的軟體行為（題目允許任意順序）
        
        find_max_cycle_length(10, 1) 應返回 (10, 1, 20)
        """
        i, j, max_len = self.collatz.find_max_cycle_length(10, 1)
        # 確認返回原始的 i, j
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)
        # 最大 cycle-length 應與 (1, 10) 相同
        self.assertEqual(max_len, 20)
    
    def test_max_cycle_length_returns_original_order(self):
        """
        測試函式返回原始的 i, j 順序而非排序後的順序
        
        這對題目的輸出格式很重要
        """
        i, j, max_len = self.collatz.find_max_cycle_length(200, 100)
        self.assertEqual(i, 200)
        self.assertEqual(j, 100)
    
    # =====================================================
    # 測試 5：快取機制的正確性（優化驗證）
    # =====================================================
    
    def test_memoization_cache_works(self):
        """
        測試記憶化快取：多次計算同一數字應使用快取
        
        驗證邏輯：第一次計算會執行完整算法，第二次應直接返回快取值
        """
        # 第一次計算
        result1 = self.collatz.calculate_cycle_length(100)
        # 檢查快取是否包含該值
        self.assertIn(100, self.collatz.cache)
        # 第二次計算應返回相同結果
        result2 = self.collatz.calculate_cycle_length(100)
        self.assertEqual(result1, result2)
    
    def test_cache_accumulates_intermediate_values(self):
        """
        測試快取會積累中間計算值
        
        計算 22 的 cycle-length 過程會產生多個中間值，
        這些值應該也被快取。
        """
        # 清空快取，只保留預設的 {1: 1}
        self.collatz.cache = {1: 1}
        
        # 計算 22
        self.collatz.calculate_cycle_length(22)
        
        # 快取應包含多個中間值（22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2）
        # 檢查幾個關鍵的中間值
        self.assertIn(1, self.collatz.cache)   # 基礎情況
        self.assertIn(22, self.collatz.cache)  # 起始值
        self.assertIn(10, self.collatz.cache)  # 中間值
    
    # =====================================================
    # 測試 6：邊界條件與特殊情況
    # =====================================================
    
    def test_small_numbers_range(self):
        """
        測試小數字範圍 [1, 10]
        
        確保演算法對小數字也正確工作
        """
        for n in range(1, 11):
            cycle_len = self.collatz.calculate_cycle_length(n)
            # cycle-length 至少為 1（n=1 時）
            self.assertGreaterEqual(cycle_len, 1)
            # 序列長度應與 cycle-length 相符
            seq = self.collatz.get_sequence(n)
            self.assertEqual(len(seq), cycle_len)
    
    def test_odd_and_even_numbers(self):
        """
        測試奇偶數混合的情況
        
        驗證奇數 (3n+1) 和偶數 (n/2) 的規則都被正確應用
        """
        # 奇數例子
        odd_seq = self.collatz.get_sequence(3)  # 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
        self.assertEqual(odd_seq[1], 10)  # 3*3+1 = 10
        
        # 偶數例子
        even_seq = self.collatz.get_sequence(10)  # 10 -> 5 -> ...
        self.assertEqual(even_seq[1], 5)  # 10/2 = 5
    
    def test_power_of_two(self):
        """
        測試 2 的次方數字（最簡單的情況）
        
        2 的次方數字序列為純粹的除以 2：2^n -> 2^(n-1) -> ... -> 2 -> 1
        """
        # 2^3 = 8 -> 4 -> 2 -> 1
        expected = [8, 4, 2, 1]
        self.assertEqual(self.collatz.get_sequence(8), expected)
        # cycle-length 應為 4
        self.assertEqual(self.collatz.calculate_cycle_length(8), 4)
    
    def test_large_intermediate_values(self):
        """
        測試可能產生較大中間值的情況
        
        某些數字可能在序列中產生遠大於起始值的中間值
        """
        # 例如 n=27 會產生很大的中間值
        seq = self.collatz.get_sequence(27)
        # 檢查序列是否有比 27 大得多的值
        max_in_seq = max(seq)
        self.assertGreater(max_in_seq, 27)


# ============================================================
# 整合測試：模擬真實的題目輸入/輸出
# ============================================================

class TestIntegration(unittest.TestCase):
    """整合測試：驗證完整的題目輸入輸出"""
    
    def setUp(self):
        """測試前準備"""
        self.collatz = CollatzSequence()
    
    def test_all_provided_examples(self):
        """
        測試題目提供的全部測試用例
        
        輸入：
            1 10
            100 200
            201 210
            900 1000
        
        預期輸出：
            1 10 20
            100 200 125
            201 210 89
            900 1000 174
        """
        test_cases = [
            ((1, 10), (1, 10, 20)),
            ((100, 200), (100, 200, 125)),
            ((201, 210), (201, 210, 89)),
            ((900, 1000), (900, 1000, 174)),
        ]
        
        for (i, j), expected in test_cases:
            with self.subTest(i=i, j=j):
                result = self.collatz.find_max_cycle_length(i, j)
                self.assertEqual(result, expected,
                               f"區間 ({i}, {j}) 的結果應為 {expected}，"
                               f"但得到 {result}")


if __name__ == '__main__':
    # 以詳細模式運行所有測試
    unittest.main(verbosity=2)
