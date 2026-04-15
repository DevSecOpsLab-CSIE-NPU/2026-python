"""
UVA 10062 乳牛排序 - 正式版（Fenwick Tree）

題意（重點）：
1. 共有 n 頭乳牛，編號為 1..n，且編號不重複。
2. 已知對每個位置 i（2 <= i <= n）：
   在它前面、編號比它小的乳牛數量為 counts[i-2]。
3. 請還原整個隊伍編號順序。

核心觀察：
若從右往左回推，在處理位置 i 時，尚未使用的編號總共有 i 個，
而該位置前面要有 c 個較小編號，代表該位置必須放「第 c+1 小」的可用編號。

這個檔案提供：
1. 高效解法（Fenwick Tree，O(n log n)）
2. 單元測試
3. 測試紀錄輸出（test_10062.log）
"""

from __future__ import annotations

from pathlib import Path
from typing import List
import unittest


class FenwickTree:
    """Fenwick Tree（Binary Indexed Tree），支援前綴和與第 k 小查詢。"""

    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        """將 idx 位置的值增加 delta（idx 為 1-based）。"""
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def prefix_sum(self, idx: int) -> int:
        """回傳 [1..idx] 的總和。"""
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def find_kth(self, k: int) -> int:
        """
        找到最小 idx，使得 prefix_sum(idx) >= k。
        這裡可用來查詢「目前可用編號中的第 k 小」。
        """
        if k <= 0 or k > self.prefix_sum(self.n):
            raise ValueError("k 超出可查詢範圍")

        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bit_mask >>= 1

        return idx + 1


def solve_cow_order(n: int, counts: List[int]) -> List[int]:
    """
    使用 Fenwick Tree 還原乳牛排列。

    參數：
    n: 乳牛總數
    counts: 長度必須為 n-1，counts[i-1] 代表第 i 個位置前方較小編號數量

    回傳：
    長度為 n 的排列（每個值介於 1..n，且不重複）
    """
    if n < 2:
        raise ValueError("n 必須 >= 2")
    if len(counts) != n - 1:
        raise ValueError("counts 長度必須為 n-1")

    # 初始化：所有編號 1..n 都是可用狀態（值為 1）。
    ft = FenwickTree(n)
    for x in range(1, n + 1):
        ft.add(x, 1)

    ans = [0] * n

    # 從右往左填值。
    for i in range(n, 1, -1):
        c = counts[i - 2]
        if c < 0 or c >= i:
            raise ValueError(f"counts 在位置 {i-1} 不合法：{c}")

        # 第 c+1 小（1-based）
        kth = c + 1
        val = ft.find_kth(kth)
        ans[i - 1] = val
        ft.add(val, -1)

    # 第一個位置就是剩下唯一編號。
    ans[0] = ft.find_kth(1)
    return ans


def build_counts_from_permutation(perm: List[int]) -> List[int]:
    """由排列反推題目給定的 counts，供測試用。"""
    n = len(perm)
    counts = []
    for i in range(1, n):
        c = sum(1 for x in perm[:i] if x < perm[i])
        counts.append(c)
    return counts


class TestCowOrder(unittest.TestCase):
    """測試 UVA 10062 還原邏輯。"""

    def test_known_case_1(self) -> None:
        # 由排列 [4,1,2,3] 反推得到 counts = [0,1,2]
        n = 4
        counts = [0, 1, 2]
        self.assertEqual(solve_cow_order(n, counts), [4, 1, 2, 3])

    def test_known_case_2(self) -> None:
        # 由排列 [2,1,3] 反推得到 counts = [0,2]
        n = 3
        counts = [0, 2]
        self.assertEqual(solve_cow_order(n, counts), [2, 1, 3])

    def test_known_case_3(self) -> None:
        # 由排列 [1,2,3,4,5] 反推得到 counts = [1,2,3,4]
        n = 5
        counts = [1, 2, 3, 4]
        self.assertEqual(solve_cow_order(n, counts), [1, 2, 3, 4, 5])

    def test_round_trip_small(self) -> None:
        # 小型回圈測試：用多組固定排列做 round-trip 驗證
        test_perms = [
            [2, 1],
            [1, 2, 3],
            [3, 1, 2],
            [4, 2, 1, 3],
            [5, 3, 1, 4, 2],
        ]
        for perm in test_perms:
            counts = build_counts_from_permutation(perm)
            self.assertEqual(solve_cow_order(len(perm), counts), perm)

    def test_invalid_counts_length(self) -> None:
        with self.assertRaises(ValueError):
            solve_cow_order(4, [0, 1])

    def test_invalid_counts_value(self) -> None:
        # 對 n=4 而言，第三個條件最多只能是 3，這裡用 4 應拋錯
        with self.assertRaises(ValueError):
            solve_cow_order(4, [0, 1, 4])


def run_tests() -> bool:
    """執行測試並保留紀錄檔。"""
    base_dir = Path(__file__).resolve().parent
    log_path = base_dir / "test_10062.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCowOrder)

    # 用文字檔保存完整測試紀錄（UTF-8）。
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Test run finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
