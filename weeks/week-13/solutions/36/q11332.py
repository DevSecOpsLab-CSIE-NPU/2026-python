import math
from typing import List, Tuple


def cross(ax: float, ay: float, bx: float, by: float) -> float:
    return ax * by - ay * bx


def dot(ax: float, ay: float, bx: float, by: float) -> float:
    return ax * bx + ay * by


def normalize_angle(angle: float) -> float:
    return math.atan2(math.sin(angle), math.cos(angle))


def endpoint_angles(sx: int, sy: int, ex: int, ey: int) -> List[float]:
    a1 = math.atan2(sy, sx)
    a2 = math.atan2(ey, ex)
    return [normalize_angle(a1), normalize_angle(a2)]


def foot_angle(sx: int, sy: int, ex: int, ey: int) -> float:
    dx = ex - sx
    dy = ey - sy
    denom = dx * dx + dy * dy
    if denom == 0:
        return float('nan')
    t = -(sx * dx + sy * dy) / denom
    if 0.0 <= t <= 1.0:
        fx = sx + t * dx
        fy = sy + t * dy
        return normalize_angle(math.atan2(fy, fx))
    return float('nan')


def ray_intersection_distance(sx: int, sy: int, ex: int, ey: int, angle: float) -> float:
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
        candidates = [v for v in (t1, t2) if v >= 0]
        return min(candidates) if candidates else float('inf')
    t = cross(px, py, segx, segy) / denom
    u = cross(px, py, cx, cy) / denom
    if t >= 0 and 0 <= u <= 1:
        return t
    return float('inf')


def is_segment_visible(segment: Tuple[int, int, int, int], others: List[Tuple[int, int, int, int]]) -> bool:
    sx, sy, ex, ey = segment
    angles = endpoint_angles(sx, sy, ex, ey)
    foot = foot_angle(sx, sy, ex, ey)
    if not math.isnan(foot):
        angles.append(foot)

    for angle in angles:
        dist = ray_intersection_distance(sx, sy, ex, ey, angle)
        if dist == float('inf'):
            continue
        blocked = False
        for ox, oy, ox2, oy2 in others:
            other_dist = ray_intersection_distance(ox, oy, ox2, oy2, angle)
            if other_dist < dist - 1e-9:
                blocked = True
                break
        if not blocked:
            return True
    return False


def solve(lines: List[str]) -> List[str]:
    """判斷每組測資中哪些鏡子可見。"""
    output: List[str] = []
    data = [int(token) for line in lines for token in line.split()]
    index = 0
    while index < len(data):
        n = data[index]
        index += 1
        segments: List[Tuple[int, int, int, int]] = []
        for _ in range(n):
            sx = data[index]
            sy = data[index + 1]
            ex = data[index + 2]
            ey = data[index + 3]
            index += 4
            segments.append((sx, sy, ex, ey))

        visibility = []
        for i, seg in enumerate(segments):
            others = segments[:i] + segments[i + 1:]
            visibility.append('1' if is_segment_visible(seg, others) else '0')
        output.append(' '.join(visibility))
    return output


def main() -> None:
    import sys
    lines = [line.rstrip("\n") for line in sys.stdin]
    print("\n".join(solve(lines)))


if __name__ == "__main__":
    main()
