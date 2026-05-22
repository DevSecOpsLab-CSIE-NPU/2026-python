"""
極簡易版（-easy）：UVA 11332 的直觀 O(n^2) 實作

說明（繁體中文）：
- 對於每一個線段，取該線段兩個端點角度的中點作為代表角（處理穿越 2π 的情形），
  沿該方向發射射線並檢查所有線段的交點距離，若該線段是該方向上最接近的交點，視為可見。
- 此實作刻意簡潔、直觀容易記憶，但在最壞情況下為 O(n^2)，適合教學與小型測資。

函式：
- `visible_segments_easy(segments)` -> 回傳 0/1 列表

注意：若你需要高效版本（可處理 n~3e4），建議採用掃描線或逆序 DSU 技術。
"""

from typing import List, Tuple
import math


def angle_of(x: float, y: float) -> float:
    a = math.atan2(y, x)
    if a < 0:
        a += 2 * math.pi
    return a


def cross(ax: float, ay: float, bx: float, by: float) -> float:
    return ax * by - ay * bx


def visible_segments_easy(segments: List[Tuple[int, int, int, int]]) -> List[int]:
    """簡潔直觀的可見判斷：對每一段選代表角並找出該角度的最接近交點。"""
    n = len(segments)
    res = [0] * n

    # 若沒有線段直接回空列表
    if n == 0:
        return res

    # 為每條線段計算代表角（兩端角度的中點，考慮環狀）
    reps = []
    for sx, sy, ex, ey in segments:
        a = angle_of(sx, sy)
        b = angle_of(ex, ey)
        # 計算差值並處理穿越 2pi 的情形
        diff = b - a
        if diff <= -math.pi:
            diff += 2 * math.pi
        elif diff > math.pi:
            diff -= 2 * math.pi
        mid = (a + diff / 2.0) % (2 * math.pi)
        reps.append(mid)

    # 對每一條線段，沿其代表角檢查所有線段，找最近交點
    for i, theta in enumerate(reps):
        dx = math.cos(theta)
        dy = math.sin(theta)
        best_t = float('inf')
        best_idx = -1
        for j, (sx, sy, ex, ey) in enumerate(segments):
            vx = ex - sx
            vy = ey - sy
            denom = cross(dx, dy, vx, vy)
            if abs(denom) < 1e-12:
                # 平行或共線：若共線則用投影判斷
                if abs(cross(sx, sy, dx, dy)) < 1e-9:
                    ts = sx * dx + sy * dy
                    te = ex * dx + ey * dy
                    cand = None
                    if ts > 0 and te > 0:
                        cand = min(ts, te)
                    elif ts > 0:
                        cand = ts
                    elif te > 0:
                        cand = te
                    if cand is not None and cand < best_t:
                        best_t = cand
                        best_idx = j
                continue
            t = cross(sx, sy, vx, vy) / denom
            u = cross(sx, sy, dx, dy) / denom
            if t > 0 and 0.0 <= u <= 1.0:
                if t < best_t:
                    best_t = t
                    best_idx = j
        if best_idx == i:
            res[i] = 1

    return res


def parse_and_run_stdin():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    out_lines = []
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        segs = []
        for _ in range(n):
            sx = int(next(it)); sy = int(next(it)); ex = int(next(it)); ey = int(next(it))
            segs.append((sx, sy, ex, ey))
        vis = visible_segments_easy(segs)
        out_lines.append(' '.join(str(x) for x in vis))
    sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
    parse_and_run_stdin()
