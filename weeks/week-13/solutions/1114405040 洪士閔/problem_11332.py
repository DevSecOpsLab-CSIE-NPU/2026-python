"""
Problem 11332 - Mirrors visibility

方法：
- 收集所有線段端點相對原點的角度，排序後在每對相鄰角度中取一個中間角度（代表該角度間的視線方向）。
- 對每個中間角度發出射線，計算與所有線段的交點，選出最近的線段，表示該方向可見到此線段的某一小段。
- 若某線段在任一方向被選為最近，即視為可見 (輸出 1)，否則不可見 (輸出 0)。

此方法正確性來自於：可見性的改變僅發生在通過線段端點的角度。

註：為了簡潔易懂採用 O(n^2) 的做法，適用於測試檔案中的小測資。
"""

import math
from typing import List, Tuple


def cross(ax: float, ay: float, bx: float, by: float) -> float:
    return ax * by - ay * bx


def segment_angles(seg: Tuple[int, int, int, int]) -> Tuple[float, float]:
    x1, y1, x2, y2 = seg
    a1 = math.atan2(y1, x1)
    a2 = math.atan2(y2, x2)
    # normalize to [0, 2pi)
    if a1 < 0:
        a1 += 2 * math.pi
    if a2 < 0:
        a2 += 2 * math.pi
    return a1, a2


def midpoint_angle(a: float, b: float) -> float:
    # assume a < b with possible wrap handled by caller
    return (a + b) / 2.0


def visible_segments(segments: List[Tuple[int, int, int, int]]) -> List[int]:
    n = len(segments)
    angles = []
    endpoints = []
    for seg in segments:
        a1, a2 = segment_angles(seg)
        angles.append(a1)
        angles.append(a2)
        endpoints.append((a1, a2))

    if not angles:
        return []

    # Normalize and sort unique
    angles = sorted(set(angles))

    # Build a set of test angles: midpoints of adjacent angles (with loop),
    # plus small eps offsets around each endpoint angle to handle degenerate cases
    eps = 1e-7
    test_angles = []
    if len(angles) == 1:
        # single unique angle: add angle +/- eps and angle+pi to cover opposite
        a = angles[0]
        test_angles.extend([a - eps, a, a + eps, a + math.pi])
    else:
        # add midpoints between consecutive angles (with wrap)
        for i in range(len(angles)):
            a = angles[i]
            b = angles[(i + 1) % len(angles)]
            # ensure b is after a in circular sense
            if b <= a:
                b += 2 * math.pi
            mid = midpoint_angle(a, b)
            test_angles.append(mid)
        # add small offsets around each endpoint angle
        for a in angles:
            test_angles.append(a - eps)
            test_angles.append(a)
            test_angles.append(a + eps)

    # normalize test angles into [0, 2pi) and deduplicate
    norm_angles = []
    for ang in test_angles:
        a = ang % (2 * math.pi)
        norm_angles.append(a)
    norm_angles = sorted(set([round(x, 12) for x in norm_angles]))

    visible = [0] * n

    # For each test angle, shoot a ray
    for mid in norm_angles:
        dx = math.cos(mid)
        dy = math.sin(mid)
        dx = math.cos(mid)
        dy = math.sin(mid)

        best_t = float('inf')
        best_idx = -1
        # Ray is origin + t*(dx,dy), t>0
        for idx, seg in enumerate(segments):
            x1, y1, x2, y2 = seg
            sx = x2 - x1
            sy = y2 - y1
            denom = cross(dx, dy, sx, sy)
            if abs(denom) < 1e-12:
                # parallel or nearly parallel: 可能共線
                # 若與射線共線（原點、段起點與方向共線），需要特別處理
                # 判斷 P 是否在射線方向上（cross(P, D) == 0)
                if abs(cross(x1, y1, dx, dy)) < 1e-12:
                    # 共線：計算端點在射線上的參數 t = dot(P, D)
                    t1 = x1 * dx + y1 * dy
                    t2 = x2 * dx + y2 * dy
                    tmin = min(t1, t2)
                    tmax = max(t1, t2)
                    # 若整段都在射線後方則無交
                    if tmax < 1e-12:
                        continue
                    # 最近的交點為 max(tmin, 0)
                    t = max(tmin, 0.0)
                    if t > 1e-12 and t < best_t:
                        best_t = t
                        best_idx = idx
                continue
            # vector from P to origin: P - O = (x1, y1)
            t = cross(x1, y1, sx, sy) / denom
            u = cross(x1, y1, dx, dy) / denom
            # t must be > 0 (in front), u in [0,1]
            if t > 1e-12 and -1e-12 <= u <= 1 + 1e-12:
                if t < best_t:
                    best_t = t
                    best_idx = idx

        if best_idx != -1:
            visible[best_idx] = 1

    return visible


def process(input_str: str) -> str:
    tokens = input_str.strip().split()
    if not tokens:
        return ""
    p = 0
    out_lines = []
    while p < len(tokens):
        n = int(tokens[p]); p += 1
        segments = []
        for _ in range(n):
            sx = int(tokens[p]); sy = int(tokens[p+1]); ex = int(tokens[p+2]); ey = int(tokens[p+3]); p += 4
            segments.append((sx, sy, ex, ey))
        vis = visible_segments(segments)
        out_lines.append(' '.join(str(v) for v in vis))
    return '\n'.join(out_lines)


if __name__ == '__main__':
    import sys
    print(process(sys.stdin.read()))
