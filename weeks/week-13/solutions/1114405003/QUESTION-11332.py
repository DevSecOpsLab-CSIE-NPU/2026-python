"""
題目：UVA 11332 - 鏡子可見性判定
判斷從原點(0,0)是否能看到各個鏡子(線段)
"""

import math

def ccw(A, B, C):
    """檢查三點的方向(反時針)"""
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def segments_intersect(A, B, C, D):
    """檢查線段AB和CD是否相交"""
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

def point_on_segment(P, A, B, eps=1e-9):
    """檢查點P是否在線段AB上"""
    # 檢查P是否在AB的邊界框內
    if not (min(A[0], B[0]) - eps <= P[0] <= max(A[0], B[0]) + eps and
            min(A[1], B[1]) - eps <= P[1] <= max(A[1], B[1]) + eps):
        return False
    
    # 檢查P是否在AB所在直線上
    cross = (P[1] - A[1]) * (B[0] - A[0]) - (P[0] - A[0]) * (B[1] - A[1])
    return abs(cross) < eps

def ray_intersects_segment(origin, direction, seg_start, seg_end, eps=1e-9):
    """
    檢查從origin沿direction方向的射線是否與線段相交
    返回: (是否相交, 相交距離)
    """
    # 參數方程: P = origin + t * direction (t >= 0)
    # 線段: Q = seg_start + s * (seg_end - seg_start) (0 <= s <= 1)
    
    dx = seg_end[0] - seg_start[0]
    dy = seg_end[1] - seg_start[1]
    
    denom = direction[0] * dy - direction[1] * dx
    
    if abs(denom) < eps:
        # 平行
        return False, float('inf')
    
    px = seg_start[0] - origin[0]
    py = seg_start[1] - origin[1]
    
    t = (px * dy - py * dx) / denom
    s = (px * direction[1] - py * direction[0]) / denom
    
    if t > eps and 0 - eps <= s <= 1 + eps:
        distance = math.sqrt(t * t * (direction[0]**2 + direction[1]**2))
        return True, distance
    
    return False, float('inf')

def is_mirror_visible(mirror_idx, mirrors, eps=1e-9):
    """檢查鏡子是否可見"""
    origin = (0, 0)
    sx, sy, ex, ey = mirrors[mirror_idx]
    mirror_start = (sx, ey)
    mirror_end = (ex, ey)
    
    # 計算到鏡子的最近點
    # 優先級: 先檢查線段的端點
    min_dist = float('inf')
    check_points = [(sx, sy), (ex, ey)]
    
    for point in check_points:
        if point[0]**2 + point[1]**2 > eps:  # 不是原點
            # 計算射線方向
            direction = (point[0], point[1])
            
            # 檢查是否被其他鏡子遮擋
            blocked = False
            for other_idx, other_mirror in enumerate(mirrors):
                if other_idx != mirror_idx:
                    osx, osy, oex, oey = other_mirror
                    intersects, dist = ray_intersects_segment(
                        origin, direction, 
                        (osx, osy), (oex, oey),
                        eps
                    )
                    if intersects:
                        point_dist = math.sqrt(point[0]**2 + point[1]**2)
                        if dist < point_dist - eps:
                            blocked = True
                            break
            
            if not blocked:
                return True
    
    return False

# 讀取輸入
while True:
    line = input().strip()
    if not line:
        break
    
    n = int(line)
    if n == 0:
        break
    
    mirrors = []
    for _ in range(n):
        sx, sy, ex, ey = map(int, input().split())
        mirrors.append((sx, sy, ex, ey))
    
    # 檢查每個鏡子
    result = []
    for i in range(n):
        if is_mirror_visible(i, mirrors):
            result.append('1')
        else:
            result.append('0')
    
    print(''.join(result))
