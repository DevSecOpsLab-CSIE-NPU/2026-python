#!/usr/bin/env python3
import sys
from collections import Counter

# UVA 10071：更簡單的版本，直接先計算兩數之和與三數之和的出現次數，再統計符合 f 的組合。

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    values = [int(x) for x in data[1:1 + n]]

    two_sums = Counter()
    for a in values:
        for b in values:
            two_sums[a + b] += 1

    three_sums = Counter()
    for a in values:
        for b in values:
            for c in values:
                three_sums[a + b + c] += 1

    total = 0
    for f in values:
        for three_sum, count in three_sums.items():
            total += count * two_sums.get(f - three_sum, 0)

    print(total)


if __name__ == "__main__":
    main()
