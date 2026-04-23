#!/usr/bin/env python3
import sys

# UVA 10093 手打版：把每一行的可放配置列出來，再用 DP 記錄上一行、上兩行的狀態。

def valid_patterns(width):
    patterns = []
    for mask in range(1 << width):
        if mask & (mask << 1):
            continue
        if mask & (mask << 2):
            continue
        patterns.append(mask)
    return patterns


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    lines = data[2:2 + n]

    all_patterns = valid_patterns(m)
    row_patterns = []
    for line in lines:
        allowed = 0
        for idx, ch in enumerate(line):
            if ch == 'P':
                allowed |= 1 << idx
        current = [mask for mask in all_patterns if mask & ~allowed == 0]
        row_patterns.append(current)

    popcount = [bin(x).count('1') for x in range(1 << m)]
    dp = {(0, 0): 0}

    for patterns in row_patterns:
        next_dp = {}
        for (prev1, prev2), value in dp.items():
            for mask in patterns:
                if mask & prev1:
                    continue
                if mask & prev2:
                    continue
                new_score = value + popcount[mask]
                next_key = (mask, prev1)
                if new_score > next_dp.get(next_key, -1):
                    next_dp[next_key] = new_score
        dp = next_dp

    best = max(dp.values()) if dp else 0
    print(best)


if __name__ == '__main__':
    main()
