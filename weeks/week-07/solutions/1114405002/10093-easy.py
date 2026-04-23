#!/usr/bin/env python3
import sys

# UVA 10093 更簡單版本：先列出每一列可放的配置，再用 DP 追蹤前兩列的狀態。

def generate_row_masks(width):
    masks = []
    for mask in range(1 << width):
        if mask & (mask << 1):
            continue
        if mask & (mask << 2):
            continue
        masks.append(mask)
    return masks


def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    m = int(tokens[1])
    grid = tokens[2:2 + n]

    all_masks = generate_row_masks(m)
    allowed_masks = []
    for row in grid:
        allowed = 0
        for j, ch in enumerate(row):
            if ch == 'P':
                allowed |= 1 << j
        allowed_masks.append([mask for mask in all_masks if mask & ~allowed == 0])

    popcount = [bin(x).count('1') for x in range(1 << m)]
    dp = {(0, 0): 0}

    for row_masks in allowed_masks:
        next_dp = {}
        for (prev_mask, prev2_mask), value in dp.items():
            for mask in row_masks:
                if mask & prev_mask:
                    continue
                if mask & prev2_mask:
                    continue
                score = value + popcount[mask]
                state = (mask, prev_mask)
                if score > next_dp.get(state, -1):
                    next_dp[state] = score
        dp = next_dp

    print(max(dp.values()) if dp else 0)


if __name__ == "__main__":
    main()
