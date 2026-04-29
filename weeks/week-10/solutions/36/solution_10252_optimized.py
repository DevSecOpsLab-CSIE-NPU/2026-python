# solution_10252_optimized.py
# UVA 10252 優化解決方案
# 找到最小曼哈頓距離和的點和最優點個數
# 優化重點：正確處理偶數個點的中位數情況；改進代碼結構

import sys

def solve_min_manhattan(points):
    """
    計算最小曼哈頓距離和及最優點個數
    - 優化：正確處理偶數情況，計算整個中位數區間的最優點數量
    """
    if not points:
        return 0, 0
    
    n = len(points)
    x_coords = sorted([p[0] for p in points])
    y_coords = sorted([p[1] for p in points])
    
    if n % 2 == 1:
        # 奇數個點：中位數唯一
        x_med = x_coords[n // 2]
        y_med = y_coords[n // 2]
        
        # 計算距離
        dist = sum(abs(p[0] - x_med) + abs(p[1] - y_med) for p in points)
        return dist, 1
    else:
        # 偶數個點：中位數範圍內的所有整數點都是最優解
        # 計算 x 方向的最優區間
        x_lower = x_coords[n // 2 - 1]
        x_upper = x_coords[n // 2]
        x_count = x_upper - x_lower + 1
        
        # 計算 y 方向的最優區間
        y_lower = y_coords[n // 2 - 1]
        y_upper = y_coords[n // 2]
        y_count = y_upper - y_lower + 1
        
        # 最優點總數為兩個區間的乘積
        optimal_count = x_count * y_count
        
        # 計算距離（任選一個最優點）
        x_med = x_lower
        y_med = y_lower
        dist = sum(abs(p[0] - x_med) + abs(p[1] - y_med) for p in points)
        
        return dist, optimal_count

def main():
    """主程式"""
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
            y = int(data[index + 1])
            index += 2
            points.append((x, y))
        
        dist, count = solve_min_manhattan(points)
        print(dist, count)

if __name__ == "__main__":
    main()
