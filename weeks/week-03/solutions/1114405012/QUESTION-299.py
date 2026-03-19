#!/usr/bin/env python3
"""UVA 299 - Train Swapping.

最少相鄰交換次數等同於排列中的 inversion 數量。
"""

from __future__ import annotations

import sys


def count_inversions(train: list[int]) -> int:
    """以 O(n^2) 計算 inversion 數量（題目範圍 L <= 50 足夠）。"""
    swaps = 0
    n = len(train)

    for i in range(n):
        for j in range(i + 1, n):
            if train[i] > train[j]:
                swaps += 1

    return swaps


def main() -> None:
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    idx = 0
    test_cases = int(tokens[idx])
    idx += 1

    outputs: list[str] = []

    for _ in range(test_cases):
        length = int(tokens[idx])
        idx += 1

        train = list(map(int, tokens[idx : idx + length]))
        idx += length

        swaps = count_inversions(train)
        outputs.append(f"Optimal train swapping takes {swaps} swaps.")

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
