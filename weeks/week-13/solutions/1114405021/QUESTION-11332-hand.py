from __future__ import annotations

import math
import sys


TAU = math.tau


def a(x: int, y: int) -> float:
    return math.atan2(y, x) % TAU


def rng(sx: int, sy: int, ex: int, ey: int) -> tuple[float, float]:
    p = a(sx, sy)
    q = a(ex, ey)
    d = (q - p) % TAU
    if d <= math.pi:
        return p, p + d
    return q, q + (TAU - d)


def norm(v: float) -> float:
    return v % TAU


def ok(theta: float, l: float, r: float) -> bool:
    theta = norm(theta)
    l = norm(l)
    r = norm(r)
    if r < l:
        r += TAU
        if theta < l:
            theta += TAU
    return l <= theta <= r


def dd(theta: float, sx: int, sy: int, ex: int, ey: int) -> float:
    dx = ex - sx
    dy = ey - sy
    c = math.cos(theta)
    s = math.sin(theta)
    c1 = sx * s - sy * c
    c2 = ex * s - ey * c
    den = c * dy - s * dx
    if abs(den) < 1e-12:
        if abs(c1) < 1e-12 and abs(c2) < 1e-12:
            p1 = sx * c + sy * s
            p2 = ex * c + ey * s
            if p1 < 0 and p2 < 0:
                return float("inf")
            vals = [v for v in (p1, p2) if v >= 0]
            return min(vals) if vals else float("inf")
        return float("inf")
    t = (sx * dy - sy * dx) / den
    return t if t >= 0 else float("inf")


def solve_one(segs: list[tuple[int, int, int, int]]) -> list[int]:
    if not segs:
        return []

    rs = [rng(*x) for x in segs]
    angs = sorted({norm(v) for pair in rs for v in pair})
    samples: list[float] = []

    for i, left in enumerate(angs):
        samples.append(left)
        right = angs[(i + 1) % len(angs)]
        gap = (right - left) % TAU
        if gap > 1e-9:
            samples.append(norm(left + gap / 2.0))

    vis = [False] * len(segs)
    for theta in samples:
        best = None
        best_d = float("inf")
        for i, (sx, sy, ex, ey) in enumerate(segs):
            l, r = rs[i]
            if not ok(theta, l, r):
                continue
            cur = dd(theta, sx, sy, ex, ey)
            if cur < best_d:
                best_d = cur
                best = i
        if best is not None:
            vis[best] = True

    return [1 if x else 0 for x in vis]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    p = 0
    out: list[str] = []
    while p < len(data):
        n = data[p]
        p += 1
        segs = []
        for _ in range(n):
            sx, sy, ex, ey = data[p:p + 4]
            p += 4
            segs.append((sx, sy, ex, ey))
        out.append(" ".join(map(str, solve_one(segs))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()