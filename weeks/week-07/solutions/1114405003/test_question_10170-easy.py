"""
UVA 10170 / ZeroJudge a163 單元測試（-easy 版）

題目一句話：
給起始人數 S 與天數 D，找第 D 天住的是幾人團。

好記版本觀念：
- S 人團住 S 天
- S+1 人團住 S+1 天
- S+2 人團住 S+2 天
- ...

所以我們要找最小的 x（x >= S），使得：
S + (S+1) + ... + x >= D

這份檔案提供：
1) solve_fast：用二分搜尋找答案（適合大 D）。
2) solve_oracle_easy：用直觀逐團累加（適合小測資）。
3) unittest：固定案例 + 隨機對照，驗證 fast 正確。
"""

from __future__ import annotations

import random
import unittest


# =========================
# 一、被測試邏輯（快速版）
# =========================


def _days_from_s_to_x(s: int, x: int) -> int:
    """計算從 s 累加到 x 的總天數。"""
    # 等差級數和：(首項+末項)*項數//2
    # 項數 = x - s + 1
    return (s + x) * (x - s + 1) // 2


def solve_fast(s: int, d: int) -> int:
    """
    二分搜尋最小 x，使 sum(s..x) >= d。

    為了讓上界好處理，先指數擴張 right，
    直到 sum(s..right) 足夠覆蓋 d。
    """
    left = s
    right = s

    while _days_from_s_to_x(s, right) < d:
        right *= 2

    while left < right:
        mid = (left + right) // 2
        if _days_from_s_to_x(s, mid) >= d:
            right = mid
        else:
            left = mid + 1

    return left


# =========================
# 二、慢速直觀解（oracle）
# =========================


def solve_oracle_easy(s: int, d: int) -> int:
    """
    逐團累加（最容易記的方式）：
    - 目前團體大小 = group
    - 該團住 group 天
    - 依序扣掉，直到覆蓋第 d 天
    """
    group = s
    elapsed = 0

    while True:
        elapsed += group
        if elapsed >= d:
            return group
        group += 1


# =========================
# 三、批次處理（對應原題 EOF 多筆）
# =========================


def solve_all_fast(pairs: list[tuple[int, int]]) -> list[int]:
    """給多組 (S, D)，回傳對應答案列表。"""
    return [solve_fast(s, d) for s, d in pairs]


# =========================
# 四、Unit Tests
# =========================


class TestQuestion10170Easy(unittest.TestCase):
    """UVA 10170 -easy 單元測試集合。"""

    def test_small_known_values(self) -> None:
        # S=4：
        # day 1~4 -> 4
        # day 5~9 -> 5
        # day 10~15 -> 6
        self.assertEqual(solve_fast(4, 1), 4)
        self.assertEqual(solve_fast(4, 4), 4)
        self.assertEqual(solve_fast(4, 5), 5)
        self.assertEqual(solve_fast(4, 9), 5)
        self.assertEqual(solve_fast(4, 10), 6)

    def test_boundary_cases(self) -> None:
        # 最小邊界
        self.assertEqual(solve_fast(1, 1), 1)

        # 剛好落在某團最後一天
        s = 7
        # sum(7..9)=24
        self.assertEqual(solve_fast(s, 24), 9)
        # 下一天就是下一團
        self.assertEqual(solve_fast(s, 25), 10)

    def test_compare_with_oracle_random_small(self) -> None:
        # 小範圍隨機：fast 必須與直觀解一致
        random.seed(10170)
        for _ in range(300):
            s = random.randint(1, 50)
            d = random.randint(1, 20000)
            self.assertEqual(solve_fast(s, d), solve_oracle_easy(s, d))

    def test_monotonicity_in_d(self) -> None:
        # 同一個 S 下，D 越大，答案不會變小
        s = 12
        prev = solve_fast(s, 1)
        for d in range(2, 2000):
            cur = solve_fast(s, d)
            self.assertGreaterEqual(cur, prev)
            prev = cur

    def test_batch_solver(self) -> None:
        pairs = [(4, 1), (4, 5), (7, 24), (7, 25)]
        expected = [4, 5, 9, 10]
        self.assertEqual(solve_all_fast(pairs), expected)


if __name__ == "__main__":
    unittest.main()
