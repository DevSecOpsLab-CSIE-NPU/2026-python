"""
UVA 10062 乳牛排序 - easy 版

這一版刻意用「更容易記憶」的寫法：
1. 維護一個已排序的可用編號清單 remaining = [1,2,...,n]
2. 從右往左填答案
3. 在第 i 個位置需要第 (counts[i-2] + 1) 小的可用編號
   -> 直接用 list.pop(index) 取出（index = counts[i-2]）

優點：
- 程式短、直覺、好記

缺點：
- pop(中間位置) 是 O(n)
- 總時間複雜度 O(n^2)，n 很大時會比 Fenwick 版慢

此檔案同樣提供：
- 單元測試
- 測試紀錄檔輸出（test_10062-easy.log）
"""

from __future__ import annotations

from pathlib import Path
from typing import List
import unittest


def solve_cow_order_easy(n: int, counts: List[int]) -> List[int]:
    """
    easy 解法：用可用編號清單 + 反向填值。

    參數：
    n: 乳牛總數
    counts: 長度為 n-1 的條件陣列

    回傳：
    還原後的排列
    """
    if n < 2:
        raise ValueError("n 必須 >= 2")
    if len(counts) != n - 1:
        raise ValueError("counts 長度必須為 n-1")

    remaining = list(range(1, n + 1))
    ans = [0] * n

    # 從右往左放值
    for i in range(n, 1, -1):
        c = counts[i - 2]
        if c < 0 or c >= i:
            raise ValueError(f"counts 在位置 {i-1} 不合法：{c}")

        ans[i - 1] = remaining.pop(c)

    # 最左邊剩下唯一一個值
    ans[0] = remaining[0]
    return ans


def build_counts_from_permutation(perm: List[int]) -> List[int]:
    """由排列反推 counts（給測試使用）。"""
    counts = []
    for i in range(1, len(perm)):
        counts.append(sum(1 for x in perm[:i] if x < perm[i]))
    return counts


class TestCowOrderEasy(unittest.TestCase):
    """easy 版測試。"""

    def test_known_case(self) -> None:
        self.assertEqual(solve_cow_order_easy(4, [0, 1, 2]), [4, 1, 2, 3])

    def test_ascending(self) -> None:
        self.assertEqual(solve_cow_order_easy(5, [1, 2, 3, 4]), [1, 2, 3, 4, 5])

    def test_round_trip(self) -> None:
        perms = [
            [2, 1],
            [3, 1, 2],
            [4, 2, 1, 3],
            [5, 3, 1, 4, 2],
        ]
        for perm in perms:
            counts = build_counts_from_permutation(perm)
            self.assertEqual(solve_cow_order_easy(len(perm), counts), perm)

    def test_invalid_length(self) -> None:
        with self.assertRaises(ValueError):
            solve_cow_order_easy(4, [0, 1])

    def test_invalid_value(self) -> None:
        with self.assertRaises(ValueError):
            solve_cow_order_easy(4, [0, 1, 4])


def run_tests() -> bool:
    """執行 easy 版測試並輸出 log。"""
    base_dir = Path(__file__).resolve().parent
    log_path = base_dir / "test_10062-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCowOrderEasy)

    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Easy test run finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
