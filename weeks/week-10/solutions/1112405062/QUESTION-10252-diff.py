"""
UVA 10252 - The Closest Points Problem
=====================================

題目說明：
- 給定 N 個點 (Xi, Yi)
- 找一個整數點 P，使得 P 到所有點的 Euclidean 距離和最小
- 輸出：最小距離和（四捨五入）+ 有幾個整數點可達到最小值

解題思路：
- 幾何中位數問題，最優整數點通常在輸入點坐標範圍內
- 候選點限制為輸入點的 x/y 坐標（因為中位數性質）
- 一次遍歷同時找最小值和統計個數
"""

import sys
import math

def solve():
    lines = [l.strip() for l in sys.stdin if l.strip()]
    if not lines:
        return

    T = int(lines[0])
    idx = 1

    for _ in range(T):
        N = int(lines[idx])
        idx += 1

        points = []
        for _ in range(N):
            x, y = map(int, lines[idx].split())
            idx += 1
            points.append((x, y))

        ans = solve_one(points)
        print(f"{ans[0]} {ans[1]}")

def solve_one(points):
    N = len(points)
    if N == 0:
        return 0, 0

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    # 候選 x 和 y：輸入點的坐標值（幾何中位數性質）
    cand_x = sorted(set(xs))
    cand_y = sorted(set(ys))

    def dist_sum(px, py):
        total = 0.0
        for i in range(N):
            dx = px - xs[i]
            dy = py - ys[i]
            total += math.hypot(dx, dy)
        return total

    # 一次遍歷：找最小距離並統計達到最小值的點數
    min_dist = float('inf')
    count = 0
    best_rounded = None

    for px in cand_x:
        for py in cand_y:
            d = dist_sum(px, py)
            rounded = int(d + 0.5)
            if d < min_dist - 1e-9:
                min_dist = d
                best_rounded = rounded
                count = 1
            elif abs(d - min_dist) <= 1e-9:
                if rounded == best_rounded:
                    count += 1

    return best_rounded, count

if __name__ == "__main__":
    solve()
