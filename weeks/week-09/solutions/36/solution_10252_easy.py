# solution_10252_easy.py
# UVA 10252 簡單版本解決方案
# 使用中位數計算，更容易記憶
# 繁體中文註解：這個版本直接用中位數計算距離

import sys

def solve(points):
    x_coords = sorted([p[0] for p in points])
    y_coords = sorted([p[1] for p in points])
    n = len(points)
    x_med = x_coords[n//2]
    y_med = y_coords[n//2]
    dist = 0
    for p in points:
        dist += abs(p[0] - x_med) + abs(p[1] - y_med)
    count = 1
    return dist, count

if __name__ == "__main__":
    data = sys.stdin.read().split()
    index = 0
    T = int(data[index])
    index += 1
    for _ in range(T):
        N = int(data[index])
        index += 1
        points = []
        for _ in range(N):
            x = int(data[index])
            y = int(data[index+1])
            index += 2
            points.append((x, y))
        dist, count = solve(points)
        print(dist, count)