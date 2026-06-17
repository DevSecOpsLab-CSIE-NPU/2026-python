import sys
import math

def min_distance_to_segment(ox, oy, sx, sy, ex, ey):
    """回傳原點到線段的最短距離"""
    dx = ex - sx
    dy = ey - sy
    if dx == 0 and dy == 0:
        return math.hypot(sx - ox, sy - oy)
    t = ((ox - sx) * dx + (oy - sy) * dy) / (dx * dx + dy * dy)
    if t < 0:
        return math.hypot(sx - ox, sy - oy)
    elif t > 1:
        return math.hypot(ex - ox, ey - oy)
    px = sx + t * dx
    py = sy + t * dy
    return math.hypot(px - ox, py - oy)

def get_angular_range(sx, sy, ex, ey):
    """
    計算從原點到線段兩端點的方位角範圍（弧度）。
    回傳 (start, end)，逆時針夾角小於 π。
    """
    a1 = math.atan2(sy, sx)
    a2 = math.atan2(ey, ex)
    if a1 < 0:
        a1 += 2 * math.pi
    if a2 < 0:
        a2 += 2 * math.pi
    # 零長度（點）鏡子：給予微小範圍
    if abs(a1 - a2) < 1e-12:
        return (a1, a1 + 1e-9)
    ccw = (a2 - a1) % (2 * math.pi)
    if ccw <= math.pi:
        return (a1, a2)
    else:
        return (a2, a1)

def subtract_one(ps, pe, bs, be):
    """從不環繞的區間 (ps,pe) 中減去不環繞的區間 (bs,be)"""
    if be <= ps or bs >= pe:
        return [(ps, pe)]
    if bs <= ps and be >= pe:
        return []
    if bs > ps and be < pe:
        return [(ps, bs), (be, pe)]
    if bs <= ps and be < pe:
        return [(be, pe)]
    if bs > ps and be >= pe:
        return [(ps, bs)]
    return [(ps, pe)]

def unwrap_range(start, end):
    """將可能環繞的區間拆成不環繞的多個區間"""
    if start > end:
        return [(start, 2 * math.pi), (0, end)]
    return [(start, end)]

def range_subtract(ranges, blockers):
    """從一個或多個區間中減去多個遮擋區間"""
    result = []
    for r_start, r_end in ranges:
        source_parts = unwrap_range(r_start, r_end)
        blocker_parts = []
        for b_start, b_end in blockers:
            blocker_parts.extend(unwrap_range(b_start, b_end))
        remaining = source_parts[:]
        for bs, be in blocker_parts:
            new_remaining = []
            for ps, pe in remaining:
                new_remaining.extend(subtract_one(ps, pe, bs, be))
            remaining = new_remaining
        result.extend(remaining)
    return result

def visible_mirrors(mirrors):
    """
    判斷每個鏡子是否可從原點看到。
    採用角度區間合併法：由近至遠處理，若該鏡子的角度
    範圍未被更近的鏡子完全遮擋，則視為可見。
    """
    n = len(mirrors)
    if n == 0:
        return []

    # 計算每個鏡子的角度範圍與距離
    infos = []
    for idx, (sx, sy, ex, ey) in enumerate(mirrors):
        r = get_angular_range(sx, sy, ex, ey)
        d = min_distance_to_segment(0, 0, sx, sy, ex, ey)
        infos.append((d, r[0], r[1], idx))

    # 由近至遠排序
    infos.sort(key=lambda x: x[0])

    covered = []       # 已被遮擋的角度區間
    result = [0] * n
    EPS = 1e-12

    for dist, a_start, a_end, idx in infos:
        remaining = range_subtract([(a_start, a_end)], covered)
        has_visible = False
        for rs, re in remaining:
            if rs > re:
                length = (2 * math.pi - rs) + re
            else:
                length = re - rs
            if length > EPS:
                has_visible = True
                break

        if has_visible:
            result[idx] = 1
            # 將此鏡子角度範圍加入已遮擋區間，並合併重疊區間
            covered.append((a_start, a_end))
            covered.sort()
            merged = []
            for cs, ce in covered:
                if not merged:
                    merged.append((cs, ce))
                else:
                    ls, le = merged[-1]
                    if cs <= le + EPS:
                        merged[-1] = (ls, max(le, ce))
                    else:
                        merged.append((cs, ce))
            covered = merged

    return result

def solve(data=None):
    """主程式：讀取多組測資，輸出各鏡子可見性"""
    if data is None:
        data = sys.stdin.read()
    lines = data.strip().splitlines()
    idx = 0
    out_lines = []
    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue
        n = int(lines[idx].strip())
        idx += 1
        mirrors = []
        for _ in range(n):
            sx, sy, ex, ey = map(int, lines[idx].split())
            mirrors.append((sx, sy, ex, ey))
            idx += 1
        res = visible_mirrors(mirrors)
        out_lines.append(" ".join(str(x) for x in res))
    return "\n".join(out_lines) + "\n"

if __name__ == "__main__":
    sys.stdout.write(solve())
