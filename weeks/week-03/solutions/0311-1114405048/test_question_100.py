"""
UVA 100 — 3n+1 問題（Collatz 猜想）單元測試

測試目標：
1. cycle_length(n)：計算單一數字的 Collatz 序列長度
2. max_cycle_length(i, j)：計算區間 [i, j] 內最大的 cycle-length
3. 邊界與特殊情況
"""

import unittest


# ===== 受測函式 =====

# 記憶化字典，用來快取已計算過的 cycle-length
memo = {}


def cycle_length(n):
    """
    計算 n 的 Collatz cycle-length。
    規則：若 n 為奇數，n = 3n+1；若 n 為偶數，n = n/2；直到 n = 1。
    回傳值包含起點 n 與終點 1。
    """
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 1:
        result = 1 + cycle_length(3 * n + 1)
    else:
        result = 1 + cycle_length(n // 2)
    memo[n] = result
    return result


def max_cycle_length(i, j):
    """
    計算介於 i 與 j（含）之間所有數字中，最大的 cycle-length。
    i 可能大於 j，需先取 min/max。
    """
    start = min(i, j)
    end = max(i, j)
    max_len = 0
    for n in range(start, end + 1):
        length = cycle_length(n)
        if length > max_len:
            max_len = length
    return max_len


# ===== 測試類別 =====


class TestCycleLength(unittest.TestCase):
    """測試 cycle_length 函式：單一數字的序列長度計算"""

    def test_n_is_1(self):
        """n=1 時，序列只有 [1]，長度為 1"""
        self.assertEqual(cycle_length(1), 1)

    def test_n_is_2(self):
        """n=2 → 2, 1，長度為 2"""
        self.assertEqual(cycle_length(2), 2)

    def test_n_is_22(self):
        """題目範例：n=22 的 cycle-length 為 16"""
        # 序列：22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
        self.assertEqual(cycle_length(22), 16)

    def test_n_is_odd(self):
        """測試奇數起點 n=3 → 3,10,5,16,8,4,2,1，長度為 8"""
        self.assertEqual(cycle_length(3), 8)

    def test_n_is_power_of_2(self):
        """2 的冪次只會一直除以 2：n=16 → 16,8,4,2,1，長度為 5"""
        self.assertEqual(cycle_length(16), 5)

    def test_n_is_large(self):
        """測試較大數字 n=999999，確認不會出錯且回傳正整數"""
        result = cycle_length(999999)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

    def test_memoization_consistency(self):
        """連續呼叫同一個 n，結果應一致（驗證快取正確性）"""
        first_call = cycle_length(100)
        second_call = cycle_length(100)
        self.assertEqual(first_call, second_call)


class TestMaxCycleLength(unittest.TestCase):
    """測試 max_cycle_length 函式：區間內最大序列長度"""

    def test_sample_1_10(self):
        """題目範例：區間 [1, 10] 最大 cycle-length 為 20"""
        self.assertEqual(max_cycle_length(1, 10), 20)

    def test_sample_100_200(self):
        """題目範例：區間 [100, 200] 最大 cycle-length 為 125"""
        self.assertEqual(max_cycle_length(100, 200), 125)

    def test_sample_201_210(self):
        """題目範例：區間 [201, 210] 最大 cycle-length 為 89"""
        self.assertEqual(max_cycle_length(201, 210), 89)

    def test_sample_900_1000(self):
        """題目範例：區間 [900, 1000] 最大 cycle-length 為 174"""
        self.assertEqual(max_cycle_length(900, 1000), 174)

    def test_reversed_input(self):
        """輸入 i > j 時，結果應與 i < j 相同（題目允許 i > j）"""
        self.assertEqual(max_cycle_length(10, 1), max_cycle_length(1, 10))

    def test_single_element(self):
        """區間只有一個數字 (i == j)，結果為該數的 cycle-length"""
        self.assertEqual(max_cycle_length(5, 5), cycle_length(5))

    def test_adjacent_numbers(self):
        """兩個相鄰數字的區間，取其中較大的 cycle-length"""
        expected = max(cycle_length(6), cycle_length(7))
        self.assertEqual(max_cycle_length(6, 7), expected)


class TestEdgeCases(unittest.TestCase):
    """測試邊界與特殊情況"""

    def test_n_equals_1_range(self):
        """最小有效輸入：區間 [1, 1]"""
        self.assertEqual(max_cycle_length(1, 1), 1)

    def test_small_range(self):
        """小區間 [1, 3]，手動驗算：1→1, 2→2, 3→8，最大為 8"""
        self.assertEqual(max_cycle_length(1, 3), 8)

    def test_cycle_length_positive(self):
        """任何有效 n 的 cycle-length 都應 >= 1"""
        for n in range(1, 101):
            self.assertGreaterEqual(cycle_length(n), 1)

    def test_large_range(self):
        """較大區間 [1, 1000]，結果應為正整數"""
        result = max_cycle_length(1, 1000)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)


if __name__ == "__main__":
    unittest.main()
