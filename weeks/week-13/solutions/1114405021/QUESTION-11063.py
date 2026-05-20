#!/usr/bin/env python3
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    pixels = []
    for _ in range(n*n):
        r = int(next(it)); g = int(next(it)); b = int(next(it))
        pixels.append((r,g,b))
    totalY = 0.0
    for (r,g,b) in pixels:
        X = 0.5149 * r + 0.3244 * g + 0.1607 * b
        Y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        Z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        totalY += Y
        print(f"{X:.4f} {Y:.4f} {Z:.4f}")
    avgY = totalY / (n*n) if n>0 else 0.0
    print(f"The average of Y is {avgY:.4f}")

if __name__ == '__main__':
    solve()
