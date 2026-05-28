"""UVA 11332 - 鏡子可見度 (簡化版)

對每個線段，取端點角度的中間角作為代表角，計算代表角光線與所有線段的交點距離，
若該線段在該角的交點距離為最小則視為可見。
此方法對一般測資足夠，但非最嚴謹的計算幾何解法。
"""

from __future__ import annotations

import math
import sys


def intersect_ray_segment(angle: float, seg: tuple[int,int,int,int]) -> float | None:
    # Ray from origin in direction angle: parametric (t*cos, t*sin), t>=0
    sx, sy, ex, ey = seg
    dx = ex - sx
    dy = ey - sy
    # Ray param: (t*cx, t*cy), t>=0
    cx = math.cos(angle)
    cy = math.sin(angle)
    # determinant
    denom = cx * dy - dx * cy
    if abs(denom) < 1e-12:
        # 可能共線（segment 與射線在同一直線上）
        # 檢查端點在射線方向上的投影
        t1 = sx * cx + sy * cy
        t2 = ex * cx + ey * cy
        candidates = [t for t in (t1, t2) if t >= 0]
        if candidates:
            return min(candidates)
        return None
    u = (sx * cy - cx * sy) / denom
    t = (sx * dy - dx * sy) / denom
    if 0 <= u <= 1 and t >= 0:
        return t
    return None


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    out_lines: list[str] = []
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        segs: list[tuple[int,int,int,int]] = []
        for _ in range(n):
            sx = int(next(it)); sy = int(next(it)); ex = int(next(it)); ey = int(next(it))
            segs.append((sx, sy, ex, ey))

        vis = [0] * n
        for i, seg in enumerate(segs):
            sx, sy, ex, ey = seg
            a1 = math.atan2(sy, sx)
            a2 = math.atan2(ey, ex)
            # normalize to continuous interval
            # compute midpoint angle properly
            diff = a2 - a1
            if diff <= -math.pi:
                diff += 2*math.pi
            elif diff > math.pi:
                diff -= 2*math.pi
            mid = a1 + diff / 2
            # ensure mid in [-pi,pi]
            if mid > math.pi:
                mid -= 2*math.pi
            if mid <= -math.pi:
                mid += 2*math.pi

            # find intersection distance for this ray and all segments
            best_t = None
            best_idx = None
            for j, s2 in enumerate(segs):
                t = intersect_ray_segment(mid, s2)
                if t is not None:
                    if best_t is None or t < best_t:
                        best_t = t
                        best_idx = j

            if best_idx == i:
                vis[i] = 1

        out_lines.append("".join(str(x) for x in vis))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
