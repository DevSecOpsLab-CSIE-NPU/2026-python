#!/usr/bin/env python3
import sys

# UVA 10170 手打版：以二分搜尋算出第 D 天所在的團次，然後回傳該團人數。

def total_days_from_start(s, group_index):
    return group_index * s + group_index * (group_index - 1) // 2


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        s, d = map(int, line.split())

        lo, hi = 1, 2000000000
        while lo < hi:
            mid = (lo + hi) // 2
            if total_days_from_start(s, mid) >= d:
                hi = mid
            else:
                lo = mid + 1

        print(s + lo - 1)


if __name__ == '__main__':
    main()
