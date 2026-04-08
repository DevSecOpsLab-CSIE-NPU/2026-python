"""
UVA 10062 / ZeroJudge a055 單元測試

題意摘要：
給定每個位置前面「比自己小的編號數量」，還原整體排列。

測試策略：
1. 被測函式使用 Fenwick Tree（BIT）+ 二分搜尋。
2. 對照函式使用直觀列表刪除法（較慢但容易驗證正確）。
3. 用固定案例與隨機案例比對兩者輸出是否一致。
"""

from __future__ import annotations

import random
import unittest


def solve_fast(n: int, smaller_counts: list[int]) -> list[int]:
    """
    快速解法：
    從後往前還原，每一步找到「目前可用編號中的第 k 小」。
    其中 k = a[i] + 1。
    """
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = smaller_counts[i - 2]

    bit = [0] * (n + 1)

    def add(idx: int, delta: int) -> None:
        while idx <= n:
            bit[idx] += delta
            idx += idx & -idx

    def prefix_sum(idx: int) -> int:
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s

    for v in range(1, n + 1):
        add(v, 1)

    ans = [0] * (n + 1)

    for i in range(n, 0, -1):
        k = a[i] + 1

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if prefix_sum(mid) >= k:
                right = mid
            else:
                left = mid + 1

        ans[i] = left
        add(left, -1)

    return ans[1:]


def solve_oracle(n: int, smaller_counts: list[int]) -> list[int]:
    """
    對照解（直觀版本）：
    維護排序中的可用編號列表，從後往前直接取第 a[i] 個元素。
    """
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = smaller_counts[i - 2]

    available = list(range(1, n + 1))
    ans = [0] * (n + 1)

    for i in range(n, 0, -1):
        idx = a[i]
        ans[i] = available[idx]
        del available[idx]

    return ans[1:]


def build_smaller_counts_from_perm(perm: list[int]) -> list[int]:
    """由排列反推題目所需的 smaller_counts，方便產生測資。"""
    n = len(perm)
    out: list[int] = []

    for i in range(1, n):
        cnt = 0
        for j in range(i):
            if perm[j] < perm[i]:
                cnt += 1
        out.append(cnt)

    return out


class TestQuestion10062(unittest.TestCase):
    """UVA 10062 測試集合。"""

    def test_n2_basic(self) -> None:
        self.assertEqual(solve_fast(2, [0]), [2, 1])
        self.assertEqual(solve_fast(2, [1]), [1, 2])

    def test_fixed_cases(self) -> None:
        self.assertEqual(solve_fast(3, [0, 2]), [2, 1, 3])
        self.assertEqual(solve_fast(4, [0, 2, 1]), [3, 1, 4, 2])

    def test_random_compare_oracle(self) -> None:
        random.seed(1006201)

        for n in range(2, 80):
            for _ in range(20):
                perm = list(range(1, n + 1))
                random.shuffle(perm)

                smaller_counts = build_smaller_counts_from_perm(perm)
                fast = solve_fast(n, smaller_counts)
                oracle = solve_oracle(n, smaller_counts)

                self.assertEqual(fast, oracle)

    def test_result_is_permutation(self) -> None:
        random.seed(777)

        for n in [2, 5, 10, 30, 60]:
            for _ in range(20):
                perm = list(range(1, n + 1))
                random.shuffle(perm)
                smaller_counts = build_smaller_counts_from_perm(perm)

                ans = solve_fast(n, smaller_counts)
                self.assertEqual(sorted(ans), list(range(1, n + 1)))


if __name__ == "__main__":
    unittest.main()
