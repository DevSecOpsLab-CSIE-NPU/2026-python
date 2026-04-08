"""
UVA 10071 / ZeroJudge a064 單元測試（-easy 版）

目標：
1) 針對題目「a + b + c + d + e = f」撰寫 Python unit test。
2) 使用繁體中文詳細註解，讓寫法更容易記憶與複習。
3) 提供一個快版解法 + 一個慢版正確解（oracle）來交叉驗證。

好記版本的核心：
- 直接暴力是 O(N^6)（六個變數各跑一次），只適合非常小測資。
- 可改成：先算所有 a+b+c 的次數（Counter），稱為 count3。
- 再枚舉 d,e,f，去查 count3[f-d-e]。
- 這樣總複雜度變 O(N^3)，在 N<=100 時可行。
"""

from __future__ import annotations

import random
import unittest
from collections import Counter


# =========================
# 一、被測試邏輯（較快、好記）
# =========================


def solve_fast(values: list[int]) -> int:
    """
    O(N^3) 作法：
    1. 建立 count3[sum_abc] = 有多少組 (a,b,c) 使 a+b+c=sum_abc。
    2. 枚舉 (d,e,f)，答案 += count3[f-d-e]。

    注意：
    - 本題變數可重複使用，所以所有三層迴圈都直接跑整個 values。
    - 這裡計數的是「有序」六元組，(a,b,...) 的順序不同算不同組。
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


# =========================
# 二、慢速正確解（oracle）
# =========================


def solve_oracle_bruteforce(values: list[int]) -> int:
    """
    O(N^6) 直觀暴力解：
    完整枚舉 (a,b,c,d,e,f) 並檢查 a+b+c+d+e == f。

    僅建議在 very small N 測試使用。
    """
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


# =========================
# 三、單元測試
# =========================


class TestQuestion10071Easy(unittest.TestCase):
    """UVA 10071（a064）-easy 測試集合。"""

    def test_single_zero(self) -> None:
        # S={0}
        # 唯一六元組是 (0,0,0,0,0,0)，且 0+0+0+0+0=0 成立
        self.assertEqual(solve_fast([0]), 1)

    def test_single_nonzero(self) -> None:
        # S={1}
        # 左邊固定是 1+1+1+1+1=5，右邊固定是 1，不可能相等
        self.assertEqual(solve_fast([1]), 0)

    def test_small_handcrafted(self) -> None:
        # 小型手刻測資，用 oracle 幫忙算預期值，
        # 可以避免人工計算出錯。
        s1 = [-1, 0, 1]
        s2 = [0, 2]

        self.assertEqual(solve_fast(s1), solve_oracle_bruteforce(s1))
        self.assertEqual(solve_fast(s2), solve_oracle_bruteforce(s2))

    def test_random_compare_with_oracle(self) -> None:
        # 隨機小測資：
        # - 用小 N，讓 oracle 還跑得動
        # - fast 與 oracle 必須完全一致
        random.seed(10071)

        for _ in range(40):
            n = random.randint(1, 5)

            # 從小範圍挑不重複元素，符合題目 S 元素不重複
            pool = list(range(-5, 6))
            random.shuffle(pool)
            values = pool[:n]

            fast = solve_fast(values)
            oracle = solve_oracle_bruteforce(values)
            self.assertEqual(fast, oracle)

    def test_result_non_negative(self) -> None:
        # 基本性質檢查：解答一定是非負整數
        test_sets = [
            [0],
            [-2, -1, 3],
            [-3, 0, 2, 5],
        ]
        for values in test_sets:
            ans = solve_fast(values)
            self.assertIsInstance(ans, int)
            self.assertGreaterEqual(ans, 0)


if __name__ == "__main__":
    unittest.main()
