#!/usr/bin/env python3
# 簡易可讀版本，含繁體中文註解
import sys

def main():
    vals = list(map(int, sys.stdin.read().split()))
    if not vals:
        return
    it = iter(vals)
    n = next(it)
    totalY = 0.0
    for _ in range(n*n):
        r = next(it); g = next(it); b = next(it)
        X = 0.5149 * r + 0.3244 * g + 0.1607 * b
        Y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        Z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        totalY += Y
        print(f"{X:.4f} {Y:.4f} {Z:.4f}")
    avgY = totalY / (n*n)
    print(f"The average of Y is {avgY:.4f}")

if __name__ == '__main__':
    main()
