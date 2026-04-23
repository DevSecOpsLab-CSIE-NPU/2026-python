#!/usr/bin/env python3
import sys

# UVA 10170：無限旅館，求第 D 天住宿的旅行團人數。
# 每個團的人數從 S 開始，每個團住的人數等於天數，團人數逐次遞增。

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        s, d = map(int, line.split())
        low, high = 1, 2000000000
        while low < high:
            mid = (low + high) // 2
            total_days = mid * s + mid * (mid - 1) // 2
            if total_days >= d:
                high = mid
            else:
                low = mid + 1
        print(s + low - 1)


if __name__ == '__main__':
    main()
