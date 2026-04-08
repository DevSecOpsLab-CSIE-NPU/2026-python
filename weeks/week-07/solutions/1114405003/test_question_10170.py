"""
UVA 10170 / ZeroJudge a163 單元測試

題意：
給定起始旅行團人數 S 與天數 D，求第 D 天住的是幾人團。

核心概念：
- S 人團住 S 天
- S+1 人團住 S+1 天
- ...

因此要找最小 x（x >= S）使得：
S + (S+1) + ... + x >= D

測試策略：
1. 被測函式 solve_fast：使用二分搜尋找最小 x。
2. 對照函式 solve_oracle：逐團累加的直觀模擬。
3. 以固定案例、邊界案例、隨機案例做比對。
"""

from __future__ import annotations

import random
import unittest


def days_sum(s: int, x: int) -> int:
    """計算從 s 累加到 x 的總和。"""
    return (s + x) * (x - s + 1) // 2


def solve_fast(s: int, d: int) -> int:
    """
    二分搜尋最小 x，使 days_sum(s, x) >= d。

    先用倍增擴大右界，再做標準二分。
    """
    left = s
    right = s

    while days_sum(s, right) < d:
        right *= 2

    while left < right:
        mid = (left + right) // 2
        if days_sum(s, mid) >= d:
            right = mid
        else:
            left = mid + 1

    return left


def solve_oracle(s: int, d: int) -> int:
    """
    直觀模擬：
    依序累加每個旅行團停留天數，直到覆蓋第 d 天。
    """
    group = s
    elapsed = 0

    while True:
        elapsed += group
        if elapsed >= d:
            return group
        group += 1


def solve_all_fast(pairs: list[tuple[int, int]]) -> list[int]:
    """批次版本，對應原題 EOF 多筆輸入情境。"""
    return [solve_fast(s, d) for s, d in pairs]


class TestQuestion10170(unittest.TestCase):
    """UVA 10170 測試集合。"""

    def test_small_known_case(self) -> None:
        # S=4 時：
        # day 1~4 -> 4, day 5~9 -> 5, day 10~15 -> 6
        self.assertEqual(solve_fast(4, 1), 4)
        self.assertEqual(solve_fast(4, 4), 4)
        self.assertEqual(solve_fast(4, 5), 5)
        self.assertEqual(solve_fast(4, 9), 5)
        self.assertEqual(solve_fast(4, 10), 6)

    def test_boundaries(self) -> None:
        self.assertEqual(solve_fast(1, 1), 1)

        # S=7，sum(7..9)=24
        self.assertEqual(solve_fast(7, 24), 9)
        self.assertEqual(solve_fast(7, 25), 10)

    def test_random_compare_oracle(self) -> None:
        random.seed(1017001)

        for _ in range(400):
            s = random.randint(1, 80)
            d = random.randint(1, 50000)
            self.assertEqual(solve_fast(s, d), solve_oracle(s, d))

    def test_monotonic_in_d(self) -> None:
        # 固定 S，D 變大時答案不會下降
        s = 15
        prev = solve_fast(s, 1)
        for d in range(2, 3000):
            cur = solve_fast(s, d)
            self.assertGreaterEqual(cur, prev)
            prev = cur

    def test_batch_solver(self) -> None:
        pairs = [(4, 1), (4, 5), (7, 24), (7, 25), (1, 1)]
        expected = [4, 5, 9, 10, 1]
        self.assertEqual(solve_all_fast(pairs), expected)


if __name__ == "__main__":
    unittest.main()
