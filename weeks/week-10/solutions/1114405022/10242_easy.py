"""UVA 10242 - Fourth Point!!

簡單版：找第四個點使得距離和最小
"""

import math


def distance(p1, p2):
    """計算兩點距離"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def find_fourth_point(points):
    """
    給定 3 點，找第四個點 P 使得到其他三點距離和最小。
    根據費馬點理論，最小距離和在費馬點（Fermat point）達到。
    """
    # 簡單版：直接計算三角形的外心
    p1, p2, p3 = points
    
    # 計算三角形外心（費馬點的近似）
    x = (p1[0] + p2[0] + p3[0]) / 3
    y = (p1[1] + p2[1] + p3[1]) / 3
    
    # 計算到三點的距離和
    min_dist = distance((x, y), p1) + distance((x, y), p2) + distance((x, y), p3)
    
    return int(min_dist), 1


def main():
    import sys
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
        
        dist, count = find_fourth_point(points)
        print(dist, count)


if __name__ == "__main__":
    main()
