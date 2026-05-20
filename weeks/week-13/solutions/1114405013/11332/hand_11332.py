import math
import sys


PI2 = 2.0 * math.pi
EPS = 1e-10


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def dot(ax, ay, bx, by):
    return ax * bx + ay * by


def norm_angle(a):
    a %= PI2
    if a < 0:
        a += PI2
    return a


def hit_distance(angle, seg):
    sx, sy, ex, ey = seg
    dx = math.cos(angle)
    dy = math.sin(angle)

    vx = ex - sx
    vy = ey - sy
    den = cross(dx, dy, vx, vy)

    if abs(den) > EPS:
        t = cross(sx, sy, vx, vy) / den
        u = cross(sx, sy, dx, dy) / den
        if t > EPS and -EPS <= u <= 1.0 + EPS:
            return t
        return None

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


def visible_mirrors(segments):
    n = len(segments)
    if n == 0:
        return []

    angles = []
    for sx, sy, ex, ey in segments:
        angles.append(norm_angle(math.atan2(sy, sx)))
        angles.append(norm_angle(math.atan2(ey, ex)))

    angles.sort()

    uniq = []
    for a in angles:
        if not uniq or abs(a - uniq[-1]) > 1e-12:
            uniq.append(a)

    cand = list(uniq)
    m = len(uniq)
    for i in range(m):
        a = uniq[i]
        b = uniq[(i + 1) % m]
        diff = (b - a) % PI2
        if diff > 1e-12:
            cand.append(norm_angle(a + diff / 2.0))

    seen = [0] * n

    for ang in cand:
        best = None
        best_ids = []

        for i, seg in enumerate(segments):
            d = hit_distance(ang, seg)
            if d is None:
                continue

            if best is None or d < best - EPS:
                best = d
                best_ids = [i]
            elif abs(d - best) <= EPS:
                best_ids.append(i)

        for i in best_ids:
            seen[i] = 1

    return seen


def solve(text):
    arr = text.split()
    p = 0
    out = []

    while p < len(arr):
        n = int(arr[p])
        p += 1

        if n == 0:
            break

        segs = []
        for _ in range(n):
            sx = int(arr[p])
            sy = int(arr[p + 1])
            ex = int(arr[p + 2])
            ey = int(arr[p + 3])
            p += 4
            segs.append((sx, sy, ex, ey))

        out.append(" ".join(map(str, visible_mirrors(segs))))

    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
