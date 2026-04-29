"""
UVA 10252 - 費馬點問題

找一個點 P，使得它到所有給定點的距離和最小。
輸出最小距離和（四捨五入）和達到此最小值的整數點個數。
"""

import sys
import math
from typing import List, Tuple


def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """計算兩點間的歐幾里得距離"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def sum_distances(point: Tuple[int, int], targets: List[Tuple[int, int]]) -> float:
    """計算一個點到所有目標點的距離和"""
    return sum(distance(point, target) for target in targets)


def find_fermat_point(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    使用優化方法找到費馬點（最小距離和點）。
    
    對於小規模點集，使用爬山法。
    """
    if len(points) == 0:
        return (0, 0)
    if len(points) == 1:
        return points[0]
    
    # 初始點：點集的質心
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    
    current = (int(cx), int(cy))
    current_dist = sum_distances(current, points)
    
    # 梯度下降法尋找局部最優
    improved = True
    iterations = 0
    while improved and iterations < 1000:
        iterations += 1
        improved = False
        
        # 檢查鄰近 8 個點
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                
                neighbor = (current[0] + dx, current[1] + dy)
                neighbor_dist = sum_distances(neighbor, points)
                
                if neighbor_dist < current_dist:
                    current = neighbor
                    current_dist = neighbor_dist
                    improved = True
                    break
            if improved:
                break
    
    return current


def solve_fermat_problem(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    求費馬點及達到最小距離和的整數點個數。
    
    返回：(最小距離和四捨五入, 整數點個數)
    """
    if len(points) == 0:
        return (0, 0)
    
    # 找到費馬點（費馬點不一定是整數點）
    fermat_int = find_fermat_point(points)
    min_dist = sum_distances(fermat_int, points)
    
    # 在費馬點附近搜索最優的整數點
    # 搜索範圍：費馬點周圍 50×50 的區域
    search_range = 50
    x_min = fermat_int[0] - search_range
    x_max = fermat_int[0] + search_range
    y_min = fermat_int[1] - search_range
    y_max = fermat_int[1] + search_range
    
    min_dist = float('inf')
    count = 0
    
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            dist = sum_distances((x, y), points)
            
            if dist < min_dist:
                min_dist = dist
                count = 1
            elif abs(dist - min_dist) < 1e-9:  # 浮點比較
                count += 1
    
    # 四捨五入最小距離
    min_dist_rounded = int(min_dist + 0.5)
    
    return (min_dist_rounded, count)


def read_test_cases() -> List[List[Tuple[int, int]]]:
    """讀取測試案例"""
    cases = []
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            n = int(sys.stdin.readline())
            points = []
            for _ in range(n):
                x, y = map(int, sys.stdin.readline().split())
                points.append((x, y))
            cases.append(points)
    except (EOFError, ValueError):
        pass
    
    return cases


def main():
    """主程式"""
    cases = read_test_cases()
    for points in cases:
        min_dist, count = solve_fermat_problem(points)
        print(f"{min_dist} {count}")


if __name__ == '__main__':
    main()
