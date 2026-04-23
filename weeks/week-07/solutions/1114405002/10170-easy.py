#!/usr/bin/env python3
import sys

# UVA 10170：更簡單版本，使用二分搜尋求出第幾個團在第 D 天入住。

def days_covered(s, k):
    return k * s + k * (k - 1) // 2


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        s, d = map(int, line.split())

        left, right = 1, 2000000000
        while left < right:
            mid = (left + right) // 2
            if days_covered(s, mid) >= d:
                right = mid
            else:
                left = mid + 1

        print(s + left - 1)


if __name__ == '__main__':
    main()
