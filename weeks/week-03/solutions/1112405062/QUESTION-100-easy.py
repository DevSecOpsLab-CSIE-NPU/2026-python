# -*- coding: utf-8 -*-
"""
================================================================================
UVA 100 - Collatz 猜想（簡化版）
================================================================================

【題目】
對任意兩個整數 i、j，找出區間 [i, j] 內所有數字中，最大的 Collatz cycle-length。

【Collatz 規則】
- 如果 n 是奇數：n = 3 * n + 1
- 如果 n 是偶數：n = n / 2
- 直到 n = 1 為止

================================================================================
"""


def cycle_length(n):
    """計算 n 的 Collatz 序列長度（簡化版）"""
    count = 1  # 包含起始數字 n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count


def max_cycle(i, j):
    """找出區間 [i, j] 內的最大 cycle-length"""
    start, end = min(i, j), max(i, j)
    return max(cycle_length(n) for n in range(start, end + 1))


def solve():
    """主程式：讀取輸入、處理、輸出結果"""
    import sys

    for line in sys.stdin:
        i, j = map(int, line.split())
        print(i, j, max_cycle(i, j))


# ============================================================================
# 單元測試
# ============================================================================

if __name__ == "__main__":
    import unittest

    class TestCollatzEasy(unittest.TestCase):
        """Collatz 簡化版測試"""

        def test_basic_lengths(self):
            """測試基本長度計算"""
            self.assertEqual(cycle_length(1), 1)
            self.assertEqual(cycle_length(2), 2)
            self.assertEqual(cycle_length(3), 8)
            self.assertEqual(cycle_length(22), 16)

        def test_max_cycle(self):
            """測試區間最大 cycle-length"""
            self.assertEqual(max_cycle(1, 10), 20)
            self.assertEqual(max_cycle(100, 200), 125)
            self.assertEqual(max_cycle(201, 210), 89)
            self.assertEqual(max_cycle(900, 1000), 174)

        def test_order_independent(self):
            """測試順序無關"""
            self.assertEqual(max_cycle(10, 1), 20)
            self.assertEqual(max_cycle(200, 100), 125)

    unittest.main(verbosity=2)
