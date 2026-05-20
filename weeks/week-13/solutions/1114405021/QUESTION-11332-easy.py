"""UVA 11332 - Mirror visibility from the origin (easy version with detailed comments)."""

from __future__ import annotations

import math
import sys


TAU = math.tau


def ang(x: int, y: int) -> float:
    return math.atan2(y, x) % TAU


def interval(sx: int, sy: int, ex: int, ey: int) -> tuple[float, float]:
    # 一面鏡子從原點看出去，會形成一段角度區間。
    a = ang(sx, sy)
    b = ang(ex, ey)
    diff = (b - a) % TAU

    # 取較短的那一段角度。
    if diff <= math.pi:
        return a, a + diff
    return b, b + (TAU - diff)


def norm(theta: float) -> float:
    return theta % TAU


def hit(theta: float, left: float, right: float) -> bool:
    # 判斷 theta 是否落在鏡子的可見角度範圍中。
    theta = norm(theta)
    left = norm(left)
    right = norm(right)

    if right < left:
        right += TAU
        if theta < left:
            theta += TAU

    return left <= theta <= right


def dist(theta: float, sx: int, sy: int, ex: int, ey: int) -> float:
    # 射線 r = t * (cos(theta), sin(theta)) 與線段所在直線的交點距離。
    dx = ex - sx
    dy = ey - sy
    cx = math.cos(theta)
    cy = math.sin(theta)
    cross1 = sx * cy - sy * cx
    cross2 = ex * cy - ey * cx
    denom = cx * dy - cy * dx

    # 如果射線與線段共線，就取較近的那個端點。
    if abs(denom) < 1e-12:
        if abs(cross1) < 1e-12 and abs(cross2) < 1e-12:
            p1 = sx * cx + sy * cy
            p2 = ex * cx + ey * cy
            if p1 < 0 and p2 < 0:
                return float("inf")
            values = [v for v in (p1, p2) if v >= 0]
            return min(values) if values else float("inf")
        return float("inf")

    t = (sx * dy - sy * dx) / denom
    return t if t >= 0 else float("inf")


def solve_case(segments: list[tuple[int, int, int, int]]) -> list[int]:
    if not segments:
        return []

    ranges = [interval(*seg) for seg in segments]
    angles = sorted({norm(v) for pair in ranges for v in pair})
    sample: list[float] = []

    # 用端點和相鄰區間中點做採樣。
    for i, left in enumerate(angles):
        sample.append(left)
        right = angles[(i + 1) % len(angles)]
        gap = (right - left) % TAU
        if gap > 1e-9:
            sample.append(norm(left + gap / 2.0))

    visible = [False] * len(segments)

    for theta in sample:
        best_idx = None
        best_dist = float("inf")

        for i, (sx, sy, ex, ey) in enumerate(segments):
            left, right = ranges[i]
            if not hit(theta, left, right):
                continue

            current = dist(theta, sx, sy, ex, ey)
            if current < best_dist:
                best_dist = current
                best_idx = i

        if best_idx is not None:
            visible[best_idx] = True

    return [1 if item else 0 for item in visible]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    pos = 0
    out: list[str] = []

    while pos < len(data):
        n = data[pos]
        pos += 1

        segs = []
        for _ in range(n):
            sx, sy, ex, ey = data[pos:pos + 4]
            pos += 4
            segs.append((sx, sy, ex, ey))

        out.append(" ".join(map(str, solve_case(segs))))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()