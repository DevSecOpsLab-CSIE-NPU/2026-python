"""UVA 11332 - Mirror visibility from the origin (best-effort solver)."""

from __future__ import annotations

import math
import sys


TAU = math.tau


def angle(x: int, y: int) -> float:
    return math.atan2(y, x) % TAU


def segment_interval(sx: int, sy: int, ex: int, ey: int) -> tuple[float, float]:
    a = angle(sx, sy)
    b = angle(ex, ey)
    delta = (b - a) % TAU
    if delta <= math.pi:
        return a, a + delta
    return b, b + (TAU - delta)


def normalize(theta: float) -> float:
    return theta % TAU


def contains(theta: float, left: float, right: float) -> bool:
    theta = normalize(theta)
    left = normalize(left)
    right = normalize(right)
    if right < left:
        right += TAU
        if theta < left:
            theta += TAU
    return left <= theta <= right


def ray_distance(theta: float, sx: int, sy: int, ex: int, ey: int) -> float:
    dx = ex - sx
    dy = ey - sy
    rx = math.cos(theta)
    ry = math.sin(theta)

    cross1 = sx * ry - sy * rx
    cross2 = ex * ry - ey * rx
    denom = rx * dy - ry * dx

    if abs(denom) < 1e-12:
        if abs(cross1) < 1e-12 and abs(cross2) < 1e-12:
            proj1 = sx * rx + sy * ry
            proj2 = ex * rx + ey * ry
            if proj1 < 0 and proj2 < 0:
                return float("inf")
            candidates = [value for value in (proj1, proj2) if value >= 0]
            return min(candidates) if candidates else float("inf")
        return float("inf")

    t = (sx * dy - sy * dx) / denom
    return t if t >= 0 else float("inf")


def solve_case(segments: list[tuple[int, int, int, int]]) -> list[int]:
    if not segments:
        return []

    intervals = [segment_interval(*seg) for seg in segments]
    sample_angles: list[float] = []

    endpoints = sorted({normalize(a) for pair in intervals for a in pair})
    if not endpoints:
        return [0] * len(segments)

    for i in range(len(endpoints)):
        left = endpoints[i]
        right = endpoints[(i + 1) % len(endpoints)]
        sample_angles.append(left)

        if i + 1 < len(endpoints):
            gap = (right - left) % TAU
        else:
            gap = (endpoints[0] - left) % TAU

        if gap > 1e-9:
            sample_angles.append(normalize(left + gap / 2.0))

    visible = [False] * len(segments)

    for theta in sample_angles:
        nearest_index = None
        nearest_distance = float("inf")

        for idx, (sx, sy, ex, ey) in enumerate(segments):
            left, right = intervals[idx]
            if not contains(theta, left, right):
                continue

            dist = ray_distance(theta, sx, sy, ex, ey)
            if dist < nearest_distance:
                nearest_distance = dist
                nearest_index = idx

        if nearest_index is not None:
            visible[nearest_index] = True

    return [1 if item else 0 for item in visible]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    output: list[str] = []

    while index < len(data):
        n = data[index]
        index += 1
        segments = []
        for _ in range(n):
            sx, sy, ex, ey = data[index:index + 4]
            index += 4
            segments.append((sx, sy, ex, ey))

        output.append(" ".join(map(str, solve_case(segments))))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()