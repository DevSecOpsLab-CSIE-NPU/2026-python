"""
UVA 10252 - 費馬點問題 (簡化版本)

題目：給定 N 個點，找費馬點（距離和最小的點）。
      輸出最小距離和（四捨五入）和達到該值的整數點個數。

費馬點性質：使得到所有點距離和最小的點（一般不在格點上）。
此解使用暴力搜索：以質心為中心，檢查周邊整數點。
"""

import math
from typing import List, Tuple

# 搜索範圍常數
SEARCH_RADIUS = 100  # 質心周邊 ±100 的範圍


def calc_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """計算兩點歐幾里得距離（浮點精度）"""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)


def total_distance(pt: Tuple[int, int], targets: List[Tuple[int, int]]) -> float:
    """計算一點到所有目標的距離和"""
    return sum(calc_distance(pt, t) for t in targets)


def find_min_sum_point(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    尋找最小距離和點及達到最小值的點數。
    
    時間複雜度: O(R^2 × N)，R = 搜索範圍
    空間複雜度: O(1)
    
    參數：points - 目標點列表
    
    回傳：(最小距離和四捨五入, 達到最小值的整數點數)
    """
    if not points:
        return (0, 0)
    
    # 計算質心作為搜索起點（O(N)）
    centroid_x = sum(p[0] for p in points) / len(points)
    centroid_y = sum(p[1] for p in points) / len(points)
    cx = int(centroid_x)
    cy = int(centroid_y)
    
    # 搜索費馬點（暴力掃描周邊整數點）
    min_dist = float('inf')
    count = 0
    eps = 1e-9  # 浮點精度容許誤差
    
    for x in range(cx - SEARCH_RADIUS, cx + SEARCH_RADIUS + 1):
        for y in range(cy - SEARCH_RADIUS, cy + SEARCH_RADIUS + 1):
            dist = total_distance((x, y), points)
            
            # 找到更小的距離和
            if dist < min_dist - eps:
                min_dist = dist
                count = 1
            # 發現相同距離和（浮點比較）
            elif abs(dist - min_dist) <= eps:
                count += 1
    
    # 四捨五入距離（使用 +0.5 而非 round()，避免 banker's rounding）
    min_dist_rounded = int(min_dist + 0.5)
    
    return (min_dist_rounded, count)


def solve(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """求解函數"""
    return find_min_sum_point(points)
