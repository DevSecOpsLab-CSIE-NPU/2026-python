"""UVA 10242 - Fourth Point!!

一般版：完整實現最小距離點
"""

import math
import sys


def distance(p1, p2):
    """計算兩點歐幾里得距離"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def min_distance_point(points):
    """
    費馬點問題：找一個點 P 使得到給定 n 個點的距離和最小
    """
    min_sum = float('inf')
    best_point = None
    count = 0
    
    # 搜尋範圍：使用所有點的邊界
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    # 網格搜尋
    step = 1
    for x in range(int(min_x) - 100, int(max_x) + 100, step):
        for y in range(int(min_y) - 100, int(max_y) + 100, step):
            dist_sum = sum(distance((x, y), p) for p in points)
            
            if dist_sum < min_sum:
                min_sum = dist_sum
                best_point = (x, y)
                count = 1
            elif dist_sum == min_sum:
                count += 1
    
    return int(min_sum), count


def main():
    lines = sys.stdin.read().strip().split('\n')
    t = int(lines[0])
    idx = 1
    
    for _ in range(t):
        n = int(lines[idx])
        idx += 1
        
        points = []
        for i in range(n):
            x, y = map(int, lines[idx].split())
            points.append((x, y))
            idx += 1
        
        dist, count = min_distance_point(points)
        print(dist, count)


if __name__ == "__main__":
    main()
