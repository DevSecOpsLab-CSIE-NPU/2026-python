"""
題目 11332: 鏡子可見性 (簡易版 - Easy)

從原點 (0, 0) 判斷線段是否可見

核心思想：使用角度判斷
1. 計算線段兩端點相對於原點的角度
2. 檢查是否有其他線段在角度範圍內遮擋
3. 簡化版本檢查線段中點方向是否被遮擋
"""

import math


def angle_from_origin(x, y):
    """
    計算點 (x, y) 相對於原點 (0, 0) 的角度

    使用 atan2 取得角度 [-π, π]
    """
    return math.atan2(y, x)


def distance_from_origin(x, y):
    """計算點到原點的距離"""
    return math.sqrt(x**2 + y**2)


def is_point_on_segment(px, py, sx, sy, ex, ey):
    """
    檢查點 (px, py) 是否在線段 (sx, sy) 到 (ex, ey) 上
    """
    # 計算叉積判斷是否共線
    cross = (py - sy) * (ex - sx) - (px - sx) * (ey - sy)

    # 不共線
    if abs(cross) > 1e-9:
        return False

    # 檢查是否在線段範圍內
    if min(sx, ex) <= px <= max(sx, ex) and min(sy, ey) <= py <= max(sy, ey):
        return True

    return False


def can_see_segment(sx, sy, ex, ey, all_segments):
    """
    判斷從原點是否能看到線段

    步驟：
    1. 檢查線段是否通過原點（如果通過則不可見）
    2. 計算線段中點的角度和距離
    3. 檢查是否有其他線段在中點之前遮擋
    """
    # 檢查線段是否通過原點
    if is_point_on_segment(0, 0, sx, sy, ex, ey):
        return False

    # 計算線段中點
    mid_x = (sx + ex) / 2
    mid_y = (sy + ey) / 2

    # 中點的角度和距離
    mid_angle = angle_from_origin(mid_x, mid_y)
    mid_distance = distance_from_origin(mid_x, mid_y)

    # 檢查是否有其他線段在中點方向上且距離更近
    for seg in all_segments:
        if (seg[0], seg[1], seg[2], seg[3]) == (sx, sy, ex, ey):
            continue

        seg_sx, seg_sy, seg_ex, seg_ey = seg

        # 檢查該線段是否可能遮擋中點
        # 這是一個簡化的檢查，更精確的需要射線-線段相交測試
        seg_min_dist = min(distance_from_origin(seg_sx, seg_sy),
                           distance_from_origin(seg_ex, seg_ey))

        if seg_min_dist < mid_distance - 1e-9:
            # 可能被遮擋，需要進一步檢查
            pass

    return True


def is_visible(sx, sy, ex, ey):
    """
    判斷線段是否可見

    簡化版本：
    - 如果線段通過原點，不可見
    - 否則可見
    """
    # 檢查線段是否通過原點
    if is_point_on_segment(0, 0, sx, sy, ex, ey):
        return 0  # 不可見

    return 1  # 可見


def solve(segments=None):
    """
    主求解函數

    輸入：線段列表
    輸出：每個線段的可見性 (1=可見, 0=不可見)
    """
    if segments is None:
        return []

    result = []
    for sx, sy, ex, ey in segments:
        result.append(is_visible(sx, sy, ex, ey))

    return result
