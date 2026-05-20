import math
import sys


TAU = 2.0 * math.pi
EPS = 1e-10


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def dot(ax, ay, bx, by):
    return ax * bx + ay * by


def normalize_angle(theta):
    """把角度正規化到 [0, 2pi)。"""
    theta %= TAU
    if theta < 0:
        theta += TAU
    return theta


def ray_segment_distance(angle, seg):
    """回傳射線與線段交點距離（若不相交回傳 None）。"""
    sx, sy, ex, ey = seg
    dx = math.cos(angle)
    dy = math.sin(angle)

    vx = ex - sx
    vy = ey - sy
    den = cross(dx, dy, vx, vy)

    # 一般情況：用參數方程求交點。
    if abs(den) > EPS:
        t = cross(sx, sy, vx, vy) / den
        u = cross(sx, sy, dx, dy) / den
        if t > EPS and -EPS <= u <= 1.0 + EPS:
            return t
        return None

    # 平行時，可能是共線；共線就看線段在射線方向上的最近正投影。
    if abs(cross(sx, sy, dx, dy)) > EPS or abs(cross(ex, ey, dx, dy)) > EPS:
        return None

    t1 = dot(sx, sy, dx, dy)
    t2 = dot(ex, ey, dx, dy)
    lo = min(t1, t2)
    hi = max(t1, t2)

    if hi <= EPS:
        return None
    if lo > EPS:
        return lo
    return EPS


def unique_angles(angles):
    """排序並去除非常接近的重複角度。"""
    angles = sorted(angles)
    out = []
    for a in angles:
        if not out or abs(a - out[-1]) > 1e-12:
            out.append(a)
    return out


def visible_mirrors(segments):
    """回傳每個鏡子是否可見（1 可見 / 0 不可見）。"""
    n = len(segments)
    if n == 0:
        return []

    angles = []
    for sx, sy, ex, ey in segments:
        angles.append(normalize_angle(math.atan2(sy, sx)))
        angles.append(normalize_angle(math.atan2(ey, ex)))

    events = unique_angles(angles)

    # 候選檢查角度：
    # 1) 每個端點角度（處理共線鏡子）
    # 2) 端點角度之間的中點（角區間內可見性）
    candidates = list(events)
    m = len(events)
    for i in range(m):
        a = events[i]
        b = events[(i + 1) % m]
        diff = (b - a) % TAU
        if diff > 1e-12:
            candidates.append(normalize_angle(a + diff / 2.0))

    visible = [0] * n

    # 在每個候選角度發射射線，最近的鏡子可見。
    for angle in candidates:
        best = None
        best_ids = []

        for idx, seg in enumerate(segments):
            dist = ray_segment_distance(angle, seg)
            if dist is None:
                continue

            if best is None or dist < best - EPS:
                best = dist
                best_ids = [idx]
            elif abs(dist - best) <= EPS:
                best_ids.append(idx)

        for idx in best_ids:
            visible[idx] = 1

    return visible


def solve(text):
    """支援 EOF 多組輸入，每組輸出一行 0/1。"""
    tokens = text.split()
    idx = 0
    outputs = []

    while idx < len(tokens):
        n = int(tokens[idx])
        idx += 1

        if n == 0:
            break

        segments = []
        for _ in range(n):
            sx = int(tokens[idx])
            sy = int(tokens[idx + 1])
            ex = int(tokens[idx + 2])
            ey = int(tokens[idx + 3])
            idx += 4
            segments.append((sx, sy, ex, ey))

        outputs.append(" ".join(map(str, visible_mirrors(segments))))

    return "\n".join(outputs)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
