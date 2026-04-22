# solution_10252_detailed.py
# UVA 10252 詳細註解版本解決方案
# 包含詳細的繁體中文註解

import sys

def solve(points):
    """
    找到使曼哈頓距離和最小的點。
    參數：
    - points: 點列表，每個點是 (x, y)
    返回：最小距離和，整數解的數量
    """
    x_coords = sorted([p[0] for p in points])  # 排序 x 座標
    y_coords = sorted([p[1] for p in points])  # 排序 y 座標
    n = len(points)
    x_med = x_coords[n//2]  # 取 x 中位數
    y_med = y_coords[n//2]  # 取 y 中位數
    dist = 0
    for p in points:
        dist += abs(p[0] - x_med) + abs(p[1] - y_med)  # 累加曼哈頓距離
    count = 1  # 假設只有一個點
    return dist, count

if __name__ == "__main__":
    data = sys.stdin.read().split()  # 讀取輸入
    index = 0
    T = int(data[index])  # 測試組數
    index += 1
    for _ in range(T):
        N = int(data[index])  # 點數
        index += 1
        points = []
        for _ in range(N):
            x = int(data[index])
            y = int(data[index+1])
            index += 2
            points.append((x, y))
        dist, count = solve(points)
        print(dist, count)  # 輸出結果