import math
import random
import sys
from typing import Optional

"""
11332 Mirror visibility

演算法概念：把每條線段投影成一個極角區間，使用極角掃描（angular sweep）處理事件。
在掃描過程中以一個能比較「在當前射線方向上誰離原點最近」的資料結構 (treap) 當作 active set，
如此可在每個角度區間內決定哪條線段為可見。

此實作細節：
- `ray_t`: 計算射線與線段交點的參數 t（用來比較遠近）。
- `seg_less`: 在當前 `ray_dx/ray_dy` 下比較兩條線段誰更靠近原點。
- `solve_case`: 建立事件（段的起終點），在事件之間的中間角度計算 active set 的最小值。
"""


class Segment:
    __slots__ = ("sx", "sy", "ex", "ey", "id")

    def __init__(self, sx: int, sy: int, ex: int, ey: int, idx: int) -> None:
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.id = idx


class Node:
    __slots__ = ("seg", "prio", "left", "right")

    def __init__(self, seg: Segment) -> None:
        self.seg = seg
        self.prio = random.randint(1, 1 << 30)
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


ray_dx = 1.0
ray_dy = 0.0


def ray_t(seg: Segment) -> float:
    # 計算目前射線與線段交點在射線上的參數 t，越小代表越靠近原點。
    # 實務上若 den 接近 0 表示線段平行於射線，呼叫端應避免選擇那種角度；此實作在事件角度中
    # 取區間中點並稍微偏移，能減少分母為 0 的情形。
    vx = seg.ex - seg.sx
    vy = seg.ey - seg.sy
    den = ray_dx * vy - ray_dy * vx
    num = seg.sx * vy - seg.sy * vx
    return num / den


def seg_less(a: Segment, b: Segment) -> bool:
    ta = ray_t(a)
    tb = ray_t(b)
    if abs(ta - tb) > 1e-12:
        return ta < tb
    return a.id < b.id


def rotate_left(root: Node) -> Node:
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    return new_root


def rotate_right(root: Node) -> Node:
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    return new_root


def insert(root: Optional[Node], seg: Segment) -> Node:
    if root is None:
        return Node(seg)

    if seg_less(seg, root.seg):
        root.left = insert(root.left, seg)
        if root.left.prio < root.prio:
            root = rotate_right(root)
    else:
        root.right = insert(root.right, seg)
        if root.right.prio < root.prio:
            root = rotate_left(root)
    return root


def erase(root: Optional[Node], seg: Segment) -> Optional[Node]:
    if root is None:
        return None

    if root.seg.id == seg.id:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        if root.left.prio < root.right.prio:
            root = rotate_right(root)
            root.right = erase(root.right, seg)
        else:
            root = rotate_left(root)
            root.left = erase(root.left, seg)
        return root

    if seg_less(seg, root.seg):
        root.left = erase(root.left, seg)
    else:
        root.right = erase(root.right, seg)
    return root


def get_min(root: Optional[Node]) -> Optional[Node]:
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root


def norm_angle(x: int, y: int) -> float:
    angle = math.atan2(y, x)
    if angle < 0:
        angle += 2 * math.pi
    return angle


def interval_direction(left: float, right: float) -> tuple[float, float]:
    # 取區間中間方向，並稍微往內偏移，避免碰到端點。
    if right < left:
        right += 2 * math.pi
    mid = (left + right) / 2.0
    angle = mid + 1e-12
    if angle >= 2 * math.pi:
        angle -= 2 * math.pi
    return math.cos(angle), math.sin(angle)


def solve_case(segments: list[Segment]) -> list[int]:
    events: dict[float, list[tuple[int, int]]] = {}
    eps = 1e-12

    for seg in segments:
        a1 = norm_angle(seg.sx, seg.sy)
        a2 = norm_angle(seg.ex, seg.ey)
        left, right = sorted((a1, a2))

        if right - left <= math.pi:
            events.setdefault(left, []).append((1, seg.id))
            events.setdefault(right, []).append((-1, seg.id))
        else:
            events.setdefault(0.0, []).append((1, seg.id))
            events.setdefault(left, []).append((-1, seg.id))
            events.setdefault(right, []).append((1, seg.id))
            events.setdefault(2 * math.pi, []).append((-1, seg.id))

    angles = sorted(set(events.keys()) | {0.0, 2 * math.pi})
    index_of = {seg.id: seg for seg in segments}
    visible = [0] * (len(segments) + 1)
    root: Optional[Node] = None

    for i in range(len(angles) - 1):
        angle = angles[i]
        next_angle = angles[i + 1]
        if next_angle - angle < eps:
            continue

        ray_angle = (angle + next_angle) / 2.0
        if ray_angle >= 2 * math.pi:
            ray_angle -= 2 * math.pi

        global ray_dx, ray_dy
        ray_dx = math.cos(ray_angle)
        ray_dy = math.sin(ray_angle)

        for kind, seg_id in sorted(events.get(angle, [])):
            seg = index_of[seg_id]
            if kind == -1:
                root = erase(root, seg)
        for kind, seg_id in sorted(events.get(angle, [])):
            seg = index_of[seg_id]
            if kind == 1:
                root = insert(root, seg)

        best = get_min(root)
        if best is not None:
            visible[best.seg.id] = 1

    return visible[1:]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    outputs = []

    while index < len(data):
        n = data[index]
        index += 1
        segments: list[Segment] = []
        for seg_id in range(1, n + 1):
            sx, sy, ex, ey = data[index:index + 4]
            index += 4
            segments.append(Segment(sx, sy, ex, ey, seg_id))

        outputs.append(" ".join(map(str, solve_case(segments))))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()