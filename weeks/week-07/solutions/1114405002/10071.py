#!/usr/bin/env python3
import sys
from collections import Counter

# UVA 10071 題目：計算 a + b + c + d + e = f 的六元組數量。
# 所有變數均來自同一集合 S，可重複使用。

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    values = [int(x) for x in data[1:1 + n]]

    pair_counts = Counter()
    for a in values:
        for b in values:
            pair_counts[a + b] += 1

    triple_counts = Counter()
    for a in values:
        for b in values:
            for c in values:
                triple_counts[a + b + c] += 1

    total = 0
    for f in values:
        for triple_sum, triple_count in triple_counts.items():
            total += triple_count * pair_counts.get(f - triple_sum, 0)

    print(total)


if __name__ == "__main__":
    main()
