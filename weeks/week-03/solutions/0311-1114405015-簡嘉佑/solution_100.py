"""
UVA 100 - The 3n + 1 Problem（正式版）

題意摘要：
  給定多組 i, j，對每組資料找出區間 [min(i, j), max(i, j)]
  之中所有整數的 Collatz cycle-length 最大值，並輸出：i j max_cycle。

Collatz 規則：
  - 當 n = 1 時停止，cycle-length = 1
  - n 為奇數：n = 3n + 1
  - n 為偶數：n = n / 2

實作策略：
  1. 使用 `cycle_length` 計算單一整數的 cycle-length。
  2. 使用記憶化（memoization）避免重複計算。
  3. 逐一掃描區間，更新最大 cycle-length。
"""

from __future__ import annotations

import sys


def cycle_length(n: int, memo: dict[int, int]) -> int:
    """
    計算整數 n 的 cycle-length（含起點與終點 1）。

    :param n: 正整數
    :param memo: 記憶化字典，儲存 n 對應的 cycle-length
    :return: n 的 cycle-length

    遞迴說明：
      cycle_length(n) = 1 + cycle_length(next_n)
    其中 next_n 依奇偶規則決定。
    """
    if n in memo:
        return memo[n]

    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1

    memo[n] = 1 + cycle_length(next_n, memo)
    return memo[n]


def max_cycle_length(i: int, j: int) -> int:
    """
    計算區間 [min(i, j), max(i, j)] 的最大 cycle-length。

    :param i: 輸入端點 1
    :param j: 輸入端點 2
    :return: 區間最大 cycle-length
    """
    lo = min(i, j)
    hi = max(i, j)

    memo: dict[int, int] = {1: 1}
    best = 0
    for n in range(lo, hi + 1):
        best = max(best, cycle_length(n, memo))

    return best


def format_output_line(i: int, j: int) -> str:
    """
    依題目格式輸出單行：i j max_cycle。

    注意：
      - 輸出時 i, j 維持原輸入順序
      - 但計算最大值時仍以 min/max 正規化區間
    """
    return f"{i} {j} {max_cycle_length(i, j)}"


def main() -> None:
    """逐行讀入 i, j 並輸出對應結果。"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        i, j = map(int, line.split())
        print(format_output_line(i, j))


if __name__ == "__main__":
    main()
