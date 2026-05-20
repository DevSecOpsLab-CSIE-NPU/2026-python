import sys
import math
from functools import cmp_to_key


def polar_angle(sx, sy):
    """計算相對於原點 (0,0) 的極角（弧度）"""
    return math.atan2(sy, sx)


def ccw(ox, oy, ax, ay, bx, by):
    """計算外積判定叉積方向：(A-O) × (B-O)"""
    return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox)


def segment_intersect_ray(sx, sy, ex, ey, angle):
    """
    判定線段 (sx, sy)-(ex, ey) 是否與從原點出發、角度為 angle 的射線相交。
    用叉積判定：射線兩側各有一個端點則相交。
    """
    # 射線方向：(cos(angle), sin(angle))
    ray_x, ray_y = math.cos(angle), math.sin(angle)
    # 射線上一個點（足夠遠）
    ray_end_x, ray_end_y = ray_x * 100000, ray_y * 100000

    c1 = ccw(0, 0, ray_end_x, ray_end_y, sx, sy)
    c2 = ccw(0, 0, ray_end_x, ray_end_y, ex, ey)

    # 如果兩端點在射線的兩側（叉積異號），則相交
    if c1 * c2 < 0:
        return True
    # 如果其中一個端點在射線上，也認為相交
    if c1 == 0 or c2 == 0:
        return True
    return False


def point_to_line_distance(px, py, sx, sy, ex, ey):
    """計算點到線段的距離"""
    dx = ex - sx
    dy = ey - sy
    if dx == 0 and dy == 0:
        return math.sqrt((px - sx) ** 2 + (py - sy) ** 2)
    t = max(0, min(1, ((px - sx) * dx + (py - sy) * dy) / (dx * dx + dy * dy)))
    closest_x = sx + t * dx
    closest_y = sy + t * dy
    return math.sqrt((px - closest_x) ** 2 + (py - closest_y) ** 2)


def segment_visible(idx, segments):
    """檢查第 idx 個線段是否可見"""
    sx, sy, ex, ey = segments[idx]

    # 線段兩端點的極角
    angle1 = polar_angle(sx, sy)
    angle2 = polar_angle(ex, ey)

    # 取極角範圍的中點
    if abs(angle2 - angle1) < math.pi:
        mid_angle = (angle1 + angle2) / 2
    else:
        if angle1 > angle2:
            angle1, angle2 = angle2, angle1
        mid_angle = (angle1 + angle2 + 2 * math.pi) / 2
        if mid_angle > math.pi:
            mid_angle -= 2 * math.pi

    # 在中點角度上，檢查是否有其他線段遮擋了當前線段
    for i in range(len(segments)):
        if i == idx:
            continue
        osx, osy, oex, oey = segments[i]
        # 檢查這個線段是否在中點角度與原點之間
        if segment_intersect_ray(osx, osy, oex, oey, mid_angle):
            # 檢查這個線段是否更近
            dist_curr = min(math.sqrt(sx ** 2 + sy ** 2), math.sqrt(ex ** 2 + ey ** 2))
            dist_other = point_to_line_distance(0, 0, osx, osy, oex, oey)
            if dist_other < dist_curr - 1e-9:
                return False

    return True


def main():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
        except EOFError:
            break

        segments = []
        for _ in range(n):
            sx, sy, ex, ey = map(int, input().split())
            segments.append((sx, sy, ex, ey))

        result = []
        for i in range(n):
            if segment_visible(i, segments):
                result.append(1)
            else:
                result.append(0)

        print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
