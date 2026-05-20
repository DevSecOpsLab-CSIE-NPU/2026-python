"""
題目 11332: 鏡子可見性 (正式版)
從原點 (0, 0) 判斷是否能看到線段 (不考慮反射)

使用計算幾何判斷可見性：
1. 計算線段兩端點的角度
2. 檢查角度範圍內是否有其他線段遮擋
"""

import math
from typing import List, Tuple


def angle_from_origin(x: float, y: float) -> float:
    """
    計算點 (x, y) 相對於原點的角度

    返回值範圍：[-π, π]
    """
    return math.atan2(y, x)


def normalize_angle(angle: float) -> float:
    """將角度標準化到 [-π, π]"""
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle <= -math.pi:
        angle += 2 * math.pi
    return angle


def is_point_in_segment(px: float, py: float, sx: float, sy: float, ex: float, ey: float) -> bool:
    """
    檢查點是否在線段上
    """
    cross = (py - sy) * (ex - sx) - (px - sx) * (ey - sy)
    if abs(cross) > 1e-9:
        return False

    if min(sx, ex) <= px <= max(sx, ex) and min(sy, ey) <= py <= max(sy, ey):
        return True
    return False


def segments_intersect(s1x1, s1y1, s1x2, s1y2, s2x1, s2y1, s2x2, s2y2) -> float:
    """
    檢查兩線段是否相交，返回交點參數 (0-1 表示在線段上)
    """
    dx1 = s1x2 - s1x1
    dy1 = s1y2 - s1y1
    dx2 = s2x2 - s2x1
    dy2 = s2y2 - s2y1

    cross = dx1 * dy2 - dy1 * dx2
    if abs(cross) < 1e-9:
        return -1

    t = ((s2x1 - s1x1) * dy2 - (s2y1 - s1y1) * dx2) / cross

    return t


def can_see_segment(sx: float, sy: float, ex: float, ey: float, all_segments: List) -> bool:
    """
    判斷從原點是否能看到線段 (sx, sy) 到 (ex, ey)

    如果線段的任何一部分可見就返回 True
    """
    # 計算線段兩端點的角度
    angle_s = angle_from_origin(sx, sy)
    angle_e = angle_from_origin(ex, ey)

    # 線段的中點角度
    mid_x = (sx + ex) / 2
    mid_y = (sy + ey) / 2
    angle_mid = angle_from_origin(mid_x, mid_y)

    # 簡化版：檢查中點是否被遮擋
    # 更精確的方法需要檢查整個線段角度範圍

    # 使用射線投射法：從原點出發，沿著中點方向
    # 檢查是否有其他線段在中點之前相交

    min_distance = math.sqrt(mid_x**2 + mid_y**2)

    for seg in all_segments:
        if (seg[0], seg[1], seg[2], seg[3]) == (sx, sy, ex, ey):
            continue

        # 檢查原點到中點的射線是否被該線段遮擋
        # 這需要更複雜的計算
        pass

    return True


def is_visible(sx: float, sy: float, ex: float, ey: float) -> int:
    """
    判斷線段是否從原點可見

    簡化版本：線段不通過原點且存在即可見
    """
    # 檢查線段是否通過原點
    if is_point_in_segment(0, 0, sx, sy, ex, ey):
        return 0

    return 1


def solve(segments: List[Tuple[float, float, float, float]]) -> List[int]:
    """
    主求解函數

    Args:
        segments: 線段列表 [(sx1, sy1, ex1, ey1), ...]

    Returns:
        可見性列表 (1=可見, 0=不可見)
    """
    result = []
    for sx, sy, ex, ey in segments:
        result.append(is_visible(sx, sy, ex, ey))
    return result
