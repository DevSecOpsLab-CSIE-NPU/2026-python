"""UVA 10170 - The Hotel with Infinite Rooms。

給定起始團人數 S 與天數 D，求第 D 天是哪個團（人數）。
利用等差級數（連續整數和）可在 O(1) 近似 + 微調得到答案。
"""

from __future__ import annotations

import math
import sys


def day_group_size(s: int, d: int) -> int:
    """回傳第 d 天入住團的人數。"""
    # 找最小 n >= s，使 sum_{k=s..n} k >= d
    # <=> T(n) - T(s-1) >= d
    # <=> T(n) >= d + T(s-1)
    target = d + (s - 1) * s // 2

    # 先用平方根公式取近似下界，避免從 s 一路線性累加。
    n = (math.isqrt(1 + 8 * target) - 1) // 2
    if n < s:
        n = s

    # 往上補到滿足條件。
    while n * (n + 1) // 2 < target:
        n += 1
    return n


def main() -> None:
    # 題目是多筆資料直到 EOF，一行處理一組 (S, D)。
    out = []
    for line in sys.stdin.buffer.read().splitlines():
        if not line.strip():
            continue
        s, d = map(int, line.split())
        out.append(str(day_group_size(s, d)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
