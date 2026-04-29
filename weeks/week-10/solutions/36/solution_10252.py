# solution_10252.py
# UVA 10252 解決方案
# 找到最小曼哈頓距離和的點
# 繁體中文註解：使用中位數計算曼哈頓距離下的最優點

import sys

def solve(points):
    x_coords = sorted([p[0] for p in points])
    y_coords = sorted([p[1] for p in points])
    n = len(points)
    if n % 2 == 1:
        x_med = x_coords[n//2]
        y_med = y_coords[n//2]
        count = 1
    else:
        # 簡單取一個
        x_med = x_coords[n//2 - 1]
        y_med = y_coords[n//2 - 1]
        count = 1
    dist = 0
    for p in points:
        dist += abs(p[0] - x_med) + abs(p[1] - y_med)
    return dist, count

# 主程式
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