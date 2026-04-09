"""
================================================================================
UVA 10170 - The Hotel with Infinite Rooms（簡單版）
================================================================================

題目說明：
    無限房間的旅館，同一時間只有一個旅行團住宿。
    每個旅行團人數比前一個多1人，起始旅行團人數為 S。
    n 人的旅行團會住 n 天。

輸入說明：
    每行包含兩個整數 S（1 ≤ S ≤ 10000）和 D（1 ≤ D < 10^15）

輸出說明：
    輸出第 D 天住宿的旅行團人數

================================================================================
解題思路（簡單易記）
================================================================================

第 n 個旅行團的人數 = S + n - 1
累積住宿天數 = S + (S+1) + ... + (S+n-1)
            = n*S + n(n-1)/2

我們要找最小的 n 使得 n*S + n(n-1)/2 >= D

化簡為一元二次不等式：
n^2 + (2S-1)n - 2D >= 0

使用求根公式直接計算：
n = (- (2S-1) + sqrt((2S-1)^2 + 8D)) / 2

================================================================================
"""

import unittest
import math


def find_group_size(S: int, D: int) -> int:
    """
    找出第 D 天住宿的旅行團人數

    數學公式：
    - 累積天數：n*S + n(n-1)/2 >= D
    - 解一元二次不等式：n^2 + (2S-1)n - 2D >= 0
    - n = (-(2S-1) + sqrt((2S-1)^2 + 8D)) / 2

    參數：
        S: 起始旅行團人數
        D: 查詢天數
    回傳：
        第 D 天住宿的旅行團人數
    """
    n = math.ceil((-(2 * S - 1) + math.sqrt((2 * S - 1) ** 2 + 8 * D)) / 2)
    return S + n - 1


class TestHotelInfiniteRooms(unittest.TestCase):
    """測試無限房間旅館問題"""

    def test_example_from_description(self):
        """測試範例：S=4"""
        self.assertEqual(find_group_size(4, 1), 4)
        self.assertEqual(find_group_size(4, 4), 4)
        self.assertEqual(find_group_size(4, 5), 5)
        self.assertEqual(find_group_size(4, 9), 5)

    def test_S_equals_D(self):
        """測試 S 等於 D"""
        self.assertEqual(find_group_size(5, 5), 5)
        self.assertEqual(find_group_size(10, 10), 10)

    def test_large_day(self):
        """測試較大的天數"""
        self.assertEqual(find_group_size(1, 10), 4)

    def test_various_S(self):
        """測試不同起始人數"""
        self.assertEqual(find_group_size(2, 1), 2)
        self.assertEqual(find_group_size(2, 3), 3)
        self.assertEqual(find_group_size(2, 6), 4)

    def test_simple_cases(self):
        """測試簡單情況"""
        self.assertEqual(find_group_size(1, 1), 1)
        self.assertEqual(find_group_size(1, 2), 2)
        self.assertEqual(find_group_size(1, 3), 2)


if __name__ == "__main__":
    unittest.main()
