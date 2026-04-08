"""UVA 10071 的正式版解法。

題目要計算 a + b + c + d + e = f 的六元組數量。
因為元素可重複使用，所以可以把前 3 個數字與後 3 個數字拆開來統計。
"""

from __future__ import annotations

import sys
from collections import defaultdict


def solve(text: str) -> str:
    numbers = list(map(int, text.split()))
    if not numbers:
        return ""

    size = numbers[0]
    values = numbers[1 : size + 1]

    # 先統計所有「三個數字」的和出現幾次。
    triple_sum_count = defaultdict(int)
    for a in values:
        for b in values:
            ab_sum = a + b
            for c in values:
                triple_sum_count[ab_sum + c] += 1

    # 再統計所有「兩個數字」的和出現幾次。
    pair_sum_count = defaultdict(int)
    for d in values:
        for e in values:
            pair_sum_count[d + e] += 1

    # a + b + c + d + e = f
    # 等價於 a + b + c = f - d - e
    total = 0
    for f in values:
        for pair_sum, count in pair_sum_count.items():
            total += count * triple_sum_count.get(f - pair_sum, 0)

    return str(total)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()