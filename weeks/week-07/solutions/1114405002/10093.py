#!/usr/bin/env python3
import sys

# UVA 10093：炮兵部署。橫向距離不能在 2 以內，縱向同一列在相鄰兩列內也不能同時部署。


def all_valid_masks(width):
    masks = []
    for mask in range(1 << width):
        if mask & (mask << 1):
            continue
        if mask & (mask << 2):
            continue
        masks.append(mask)
    return masks


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0]); m = int(data[1])
    rows = data[2:2 + n]

    allowed_masks = []
    for line in rows:
        allowed = 0
        for j, ch in enumerate(line):
            if ch == 'P':
                allowed |= 1 << j
        allowed_masks.append(allowed)

    valid_by_row = []
    base_valid = all_valid_masks(m)
    for allowed in allowed_masks:
        valid_by_row.append([mask for mask in base_valid if mask & ~allowed == 0])

    popcount = [bin(i).count('1') for i in range(1 << m)]
    dp = {(0, 0): 0}

    for row_masks in valid_by_row:
        next_dp = {}
        for (prev, prev2), value in dp.items():
            for mask in row_masks:
                if mask & prev:
                    continue
                if mask & prev2:
                    continue
                new_value = value + popcount[mask]
                key = (mask, prev)
                if new_value > next_dp.get(key, -1):
                    next_dp[key] = new_value
        dp = next_dp

    result = max(dp.values()) if dp else 0
    print(result)


if __name__ == "__main__":
    main()
