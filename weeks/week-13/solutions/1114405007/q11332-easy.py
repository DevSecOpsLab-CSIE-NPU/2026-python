"""11332 簡單版：可見鏡子判斷（教學版）。

想法：
1) 鏡子的兩端點對原點會形成角度區間
2) 在角度區間中選一個中點方向
3) 該方向上，距原點最近的鏡子可見
"""

import math
import sys


EPS = 1e-12
PI2 = 2.0 * math.pi


def norm_ang(a):
    a %= PI2
    if a < 0:
        a += PI2
    return a


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def angle_intervals(seg):
    x1, y1, x2, y2 = seg
    a = norm_ang(math.atan2(y1, x1))
    b = norm_ang(math.atan2(y2, x2))

    d = (b - a) % PI2
    if d > math.pi:
        a, b = b, a
        d = (b - a) % PI2

    if d < EPS:
        b = norm_ang(a + 1e-9)

    if a <= b:
        return [(a, b)]
    return [(a, PI2), (0.0, b)]


def ray_distance(theta, seg):
    """回傳射線與線段交點距離；無交會回傳無限大。"""
    x1, y1, x2, y2 = seg
    dx, dy = math.cos(theta), math.sin(theta)
    vx, vy = x2 - x1, y2 - y1

    den = cross(dx, dy, vx, vy)
    if abs(den) < EPS:
        return math.inf

    t = cross(x1, y1, vx, vy) / den
    u = cross(x1, y1, dx, dy) / den

    if t < -EPS or u < -EPS or u > 1.0 + EPS:
        return math.inf
    return t


def visible_list(segs):
    n = len(segs)
    vis = [0] * n
    events = []

    for i, seg in enumerate(segs):
        for l, r in angle_intervals(seg):
            if r - l > EPS:
                events.append((l, 1, i))
                events.append((r, -1, i))

    if not events:
        return vis

    events.sort(key=lambda x: (x[0], x[1]))

    # 取所有事件角度，兩兩之間挑中點測試
    uniq = []
    i = 0
    while i < len(events):
        a = events[i][0]
        uniq.append(a)
        while i < len(events) and abs(events[i][0] - a) <= EPS:
            i += 1

    active = [0] * n
    p = 0

    for k, a in enumerate(uniq):
        while p < len(events) and abs(events[p][0] - a) <= EPS and events[p][1] == -1:
            active[events[p][2]] = 0
            p += 1
        while p < len(events) and abs(events[p][0] - a) <= EPS and events[p][1] == 1:
            active[events[p][2]] = 1
            p += 1

        if k + 1 >= len(uniq):
            break

        b = uniq[k + 1]
        if b - a <= EPS:
            continue

        mid = (a + b) / 2.0
        best_id = -1
        best_d = math.inf

        for j in range(n):
            if not active[j]:
                continue
            d = ray_distance(mid, segs[j])
            if d < best_d:
                best_d = d
                best_id = j

        if best_id != -1:
            vis[best_id] = 1

    return vis


def solve(text):
    arr = text.split()
    if not arr:
        return ""

    p = 0
    out = []

    while p < len(arr):
        n = int(arr[p])
        p += 1
        segs = []
        for _ in range(n):
            sx = float(arr[p])
            sy = float(arr[p + 1])
            ex = float(arr[p + 2])
            ey = float(arr[p + 3])
            p += 4
            segs.append((sx, sy, ex, ey))

        out.append(" ".join(map(str, visible_list(segs))))

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
