#!/usr/bin/env python3
"""UVA 100 - The 3n + 1 problem.

讀取多組 i, j，輸出原始 i j 以及區間內最大的 cycle length。
"""

from __future__ import annotations

import sys


def cycle_length(n: int, memo: dict[int, int]) -> int:
    """計算 n 的 cycle length，並使用記憶化避免重複計算。"""
    path: list[int] = []
    current = n

    while current not in memo:
        path.append(current)
        if current % 2 == 1:
            current = 3 * current + 1
        else:
            current //= 2

    length = memo[current]
    for value in reversed(path):
        length += 1
        memo[value] = length

    return memo[n]


def max_cycle_in_range(i: int, j: int, memo: dict[int, int]) -> int:
    """回傳 [min(i, j), max(i, j)] 區間中的最大 cycle length。"""
    left, right = (i, j) if i <= j else (j, i)
    best = 0

    for value in range(left, right + 1):
        current_length = cycle_length(value, memo)
        if current_length > best:
            best = current_length

    return best


def main() -> None:
    memo: dict[int, int] = {1: 1}
    outputs: list[str] = []

    for line in sys.stdin:
        stripped = line.strip()
        if not stripped:
            continue

        i, j = map(int, stripped.split())
        best = max_cycle_in_range(i, j, memo)
        outputs.append(f"{i} {j} {best}")

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
