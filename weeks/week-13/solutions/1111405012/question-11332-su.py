"""
題目 11332: 鏡子可見性 (簡化版 - SU)
"""

import math


def is_point_on_segment(px, py, sx, sy, ex, ey):
    cross = (py - sy) * (ex - sx) - (px - sx) * (ey - sy)
    if abs(cross) > 1e-9:
        return False
    return min(sx, ex) <= px <= max(sx, ex) and min(sy, ey) <= py <= max(sy, ey)


def is_visible(sx, sy, ex, ey):
    return 0 if is_point_on_segment(0, 0, sx, sy, ex, ey) else 1


def solve(segments=None):
    return [is_visible(sx, sy, ex, ey) for sx, sy, ex, ey in (segments or [])]
