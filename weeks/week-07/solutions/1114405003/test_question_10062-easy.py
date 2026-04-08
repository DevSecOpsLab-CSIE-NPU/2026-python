"""
UVA 10062 / ZeroJudge a055 單元測試（-easy 版）

這份檔案的目標：
1) 示範如何為此題撰寫 Python unit test。
2) 用「容易記憶」的方式理解題意與驗證流程。
3) 註解採繁體中文，幫助複習時快速回想。

核心想法（好記版）：
- 題目給的是 inversion-like 資訊：
  對第 i 個位置（1-based），給你前面有幾頭牛編號比它小。
- 若從「最後一個位置」往前填答案：
  每一步都知道「目前可用編號集合」中，該拿第幾小的編號。
- 快速作法用 Fenwick Tree（BIT）維護可用編號，
  並透過二分搜尋找第 k 小。
- 單元測試用一個「慢但直觀」的版本當作 oracle（標準答案），
  再把快速版與它比對，這樣最容易驗證正確性。
"""

from __future__ import annotations

import random
import sys
import unittest


# =========================
# 一、被測試邏輯（快速版）
# =========================
# 這裡直接放進測試檔，方便你單檔學習與執行。
# 若你之後把解題程式拆到別檔，也可改成 import 進來測試。


def solve_fast(n: int, smaller_counts: list[int]) -> list[int]:
    """
    快速解法：Fenwick Tree + 倒著還原排列。

    參數：
    - n: 牛的總數（編號 1..n）
    - smaller_counts: 長度 n-1，
      smaller_counts[i-2] 代表第 i 個位置前面有幾個更小編號。

    回傳：
    - 還原後的排列（長度 n，元素為 1..n）
    """

    # 將輸入補成 1-based 的 a[1..n]，其中 a[1] 固定為 0（題目不給）
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = smaller_counts[i - 2]

    # Fenwick Tree 用來記錄「某編號是否還可用」
    # 初始所有編號 1..n 都可用，因此值都設為 1。
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

    # 初始化：每個編號都可用
    for value in range(1, n + 1):
        add(value, 1)

    ans = [0] * (n + 1)

    # 倒著填位置 i：
    # 目標是拿「目前可用編號中的第 (a[i] + 1) 小」
    for i in range(n, 0, -1):
        k = a[i] + 1

        # 用二分找最小 x，使得 prefix_sum(x) >= k
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if prefix_sum(mid) >= k:
                right = mid
            else:
                left = mid + 1

        picked = left
        ans[i] = picked

        # 拿走後要從可用集合移除
        add(picked, -1)

    return ans[1:]


# =========================
# 二、測試用標準答案（慢速直觀版）
# =========================
# 這版時間複雜度較高，不適合大資料，
# 但邏輯很直覺，拿來做單元測試 oracle 很適合。


def solve_oracle_easy(n: int, smaller_counts: list[int]) -> list[int]:
    """
    慢速直觀版：
    - 維護目前可用編號清單 available（已排序）
    - 從後往前，直接取 available[a[i]]（0-based）
    - 取完後刪掉該元素
    """
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = smaller_counts[i - 2]

    available = list(range(1, n + 1))
    ans = [0] * (n + 1)

    for i in range(n, 0, -1):
        idx = a[i]  # 0-based，第 idx 個元素就是第 idx+1 小
        ans[i] = available[idx]
        del available[idx]

    return ans[1:]


# =========================
# 三、輔助工具
# =========================


def build_smaller_counts_from_perm(perm: list[int]) -> list[int]:
    """
    由真實排列反推題目輸入 smaller_counts，
    方便製造隨機測資。
    """
    n = len(perm)
    result: list[int] = []

    for i in range(1, n):
        current = perm[i]
        cnt = 0
        for j in range(i):
            if perm[j] < current:
                cnt += 1
        result.append(cnt)

    return result


# =========================
# 四、Unit Tests
# =========================


class TestQuestion10062Easy(unittest.TestCase):
    """UVA 10062 題目的 -easy 單元測試集合。"""

    def test_min_case_n2(self) -> None:
        # n=2 時，第二頭前面較小數量可能是 0 或 1
        self.assertEqual(solve_fast(2, [0]), [2, 1])
        self.assertEqual(solve_fast(2, [1]), [1, 2])

    def test_small_handcrafted_cases(self) -> None:
        # 案例 1：排列 [2, 1, 3]
        # smaller_counts = [0, 2]
        self.assertEqual(solve_fast(3, [0, 2]), [2, 1, 3])

        # 案例 2：排列 [3, 1, 4, 2]
        # smaller_counts = [0, 2, 1]
        self.assertEqual(solve_fast(4, [0, 2, 1]), [3, 1, 4, 2])

    def test_compare_with_oracle_random(self) -> None:
        # 使用固定隨機種子，確保每次測試結果可重現
        random.seed(10062)

        # 測試多組小中型隨機資料：
        # 先隨機生成排列，再反推 smaller_counts，
        # 最後比對 fast 與 oracle 是否一致。
        for n in range(2, 70):
            for _ in range(30):
                perm = list(range(1, n + 1))
                random.shuffle(perm)

                smaller_counts = build_smaller_counts_from_perm(perm)

                fast_ans = solve_fast(n, smaller_counts)
                oracle_ans = solve_oracle_easy(n, smaller_counts)

                self.assertEqual(fast_ans, oracle_ans)

    def test_output_is_valid_permutation(self) -> None:
        # 除了比對答案，也要驗證輸出確實是 1..n 的排列
        random.seed(777)
        n = 50
        for _ in range(50):
            perm = list(range(1, n + 1))
            random.shuffle(perm)
            smaller_counts = build_smaller_counts_from_perm(perm)

            ans = solve_fast(n, smaller_counts)
            self.assertEqual(sorted(ans), list(range(1, n + 1)))


def solve_from_stdin() -> None:
    """
    手打主程式（可直接拿去解題平台使用）：
    - 讀取 N 與後續 N-1 行數字
    - 輸出還原後排列，每行一個編號
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    smaller_counts = [int(x) for x in data[1:]]

    ans = solve_fast(n, smaller_counts)
    sys.stdout.write("\n".join(map(str, ans)))


if __name__ == "__main__":
    # 用法 1：執行測試
    #   python test_question_10062-easy.py
    # 用法 2：執行手打解題程式
    #   python test_question_10062-easy.py solve < input.txt
    if len(sys.argv) > 1 and sys.argv[1] == "solve":
        solve_from_stdin()
    else:
        unittest.main()
