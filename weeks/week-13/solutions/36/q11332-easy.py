import math
from typing import List, Tuple


def cross(ax: float, ay: float, bx: float, by: float) -> float:
    return ax * by - ay * bx


def dot(ax: float, ay: float, bx: float, by: float) -> float:
    return ax * bx + ay * by


def normalize_angle(angle: float) -> float:
    return math.atan2(math.sin(angle), math.cos(angle))


def get_candidate_angles(sx: int, sy: int, ex: int, ey: int) -> List[float]:
    angles = [normalize_angle(math.atan2(sy, sx)), normalize_angle(math.atan2(ey, ex))]
    dx = ex - sx
    dy = ey - sy
    denom = dx * dx + dy * dy
    if denom != 0:
        t = -(sx * dx + sy * dy) / denom
        if 0.0 <= t <= 1.0:
            fx = sx + t * dx
            fy = sy + t * dy
            angles.append(normalize_angle(math.atan2(fy, fx)))
    return angles


def ray_distance(sx: int, sy: int, ex: int, ey: int, angle: float) -> float:
    cx = math.cos(angle)
    cy = math.sin(angle)
    segx = ex - sx
    segy = ey - sy
    denom = cross(cx, cy, segx, segy)
    px = sx
    py = sy
    if abs(denom) < 1e-12:
        if abs(cross(px, py, segx, segy)) > 1e-12:
            return float('inf')
        t1 = px * cx + py * cy
        t2 = (px + segx) * cx + (py + segy) * cy
        dist = float('inf')
        if t1 >= 0:
            dist = min(dist, t1)
        if t2 >= 0:
            dist = min(dist, t2)
        return dist

    t = cross(px, py, segx, segy) / denom
    u = cross(px, py, cx, cy) / denom
    if t >= 0 and 0 <= u <= 1:
        return t
    return float('inf')


def is_visible(segment: Tuple[int, int, int, int], others: List[Tuple[int, int, int, int]]) -> bool:
    angles = get_candidate_angles(*segment)
    for angle in angles:
        dist = ray_distance(*segment, angle)
        if dist == float('inf'):
            continue
        blocked = False
        for other in others:
            if ray_distance(*other, angle) < dist - 1e-9:
                blocked = True
                break
        if not blocked:
            return True
    return False


def solve(lines: List[str]) -> List[str]:
    data = [int(token) for line in lines for token in line.split()]
    output: List[str] = []
    idx = 0
    while idx < len(data):
        n = data[idx]
        idx += 1
        segments: List[Tuple[int, int, int, int]] = []
        for _ in range(n):
            sx = data[idx]
            sy = data[idx + 1]
            ex = data[idx + 2]
            ey = data[idx + 3]
            idx += 4
            segments.append((sx, sy, ex, ey))
        answers = []
        for i, segment in enumerate(segments):
            others = segments[:i] + segments[i + 1:]
            answers.append('1' if is_visible(segment, others) else '0')
        output.append(' '.join(answers))
    return output


def main() -> None:
    import sys
    lines = [line.rstrip("\n") for line in sys.stdin]
    print("\n".join(solve(lines)))


if __name__ == "__main__":
    main()
