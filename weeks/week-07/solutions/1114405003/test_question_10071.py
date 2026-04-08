"""
UVA 10071 / ZeroJudge a064 單元測試

題意：計算有序六元組數量，滿足 a+b+c+d+e=f，且 a~f 都來自集合 S（可重複使用）。

測試策略：
1. 被測函式使用 O(N^3)（先統計 a+b+c，再枚舉 d,e,f）。
2. 對照函式使用 O(N^6) 暴力法（只用於小資料）。
3. 透過固定案例與隨機案例檢查兩者一致。
"""

from __future__ import annotations

import random
import unittest
from collections import Counter


def solve_fast(values: list[int]) -> int:
    """
    快速解法：
    count3[x] = 滿足 a+b+c=x 的有序三元組數量。
    接著枚舉 d,e,f，答案加上 count3[f-d-e]。
    """
    count3: Counter[int] = Counter()

    for a in values:
        for b in values:
            for c in values:
                count3[a + b + c] += 1

    ans = 0
    for d in values:
        for e in values:
            for f in values:
                ans += count3[f - d - e]

    return ans


def solve_oracle(values: list[int]) -> int:
    """暴力對照解：完整枚舉六元組。"""
    ans = 0

    for a in values:
        for b in values:
            for c in values:
                for d in values:
                    for e in values:
                        for f in values:
                            if a + b + c + d + e == f:
                                ans += 1

    return ans


class TestQuestion10071(unittest.TestCase):
    """UVA 10071 測試集合。"""

    def test_single_value_cases(self) -> None:
        self.assertEqual(solve_fast([0]), 1)
        self.assertEqual(solve_fast([1]), 0)
        self.assertEqual(solve_fast([-2]), 0)

    def test_small_handcrafted(self) -> None:
        s1 = [-1, 0, 1]
        s2 = [0, 2]
        s3 = [-2, 1, 4]

        self.assertEqual(solve_fast(s1), solve_oracle(s1))
        self.assertEqual(solve_fast(s2), solve_oracle(s2))
        self.assertEqual(solve_fast(s3), solve_oracle(s3))

    def test_random_compare_oracle(self) -> None:
        # 使用小 N，讓暴力對照可在合理時間內完成
        random.seed(1007101)

        for _ in range(50):
            n = random.randint(1, 5)
            pool = list(range(-7, 8))
            random.shuffle(pool)
            values = pool[:n]

            fast = solve_fast(values)
            oracle = solve_oracle(values)
            self.assertEqual(fast, oracle)

    def test_result_is_non_negative_int(self) -> None:
        test_sets = [
            [0],
            [-3, 0, 2],
            [-5, -1, 4, 7],
        ]

        for values in test_sets:
            ans = solve_fast(values)
            self.assertIsInstance(ans, int)
            self.assertGreaterEqual(ans, 0)


if __name__ == "__main__":
    unittest.main()
