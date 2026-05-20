"""
UVA 11332 - easy 版

這題要判斷每一面鏡子，從原點往外看時有沒有任何一小段區域能看到。
可以把它想成：
1. 每面鏡子在原點看出去，會對應到一段角度區間。
2. 在某個角度上，只要有多面鏡子重疊，就只能看到離原點最近的那一面。
3. 所以只要沿著角度掃描，把每個區間中最前面的鏡子標記成可見就好。

因為鏡子不會互相交叉，所以在同一個角度區間裡，鏡子的前後順序是固定的。
"""

from __future__ import annotations

import math
import random
import sys


TAU = math.tau
PI = math.pi
EPS = 1e-12


class Segment:
    __slots__ = ("sx", "sy", "ex", "ey", "left", "right", "wrap", "visible")

    def __init__(self, sx: int, sy: int, ex: int, ey: int) -> None:
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.left = 0.0
        self.right = 0.0
        self.wrap = False
        self.visible = False


class Node:
    __slots__ = ("seg_id", "priority", "left", "right")

    def __init__(self, seg_id: int) -> None:
        self.seg_id = seg_id
        self.priority = random.randrange(1 << 30)
        self.left: Node | None = None
        self.right: Node | None = None


def norm_angle(angle: float) -> float:
    return angle % TAU


def ccw_diff(a: float, b: float) -> float:
    return (b - a) % TAU


def segment_distance(segment: Segment, ray_x: float, ray_y: float) -> float:
    dx = segment.ex - segment.sx
    dy = segment.ey - segment.sy
    denom = ray_x * dy - ray_y * dx
    num = segment.sx * dy - segment.sy * dx
    return num / denom


def compare_segments(segments: list[Segment], left_id: int, right_id: int, ray_x: float, ray_y: float) -> int:
    left_distance = segment_distance(segments[left_id], ray_x, ray_y)
    right_distance = segment_distance(segments[right_id], ray_x, ray_y)
    if left_distance < right_distance:
        return -1
    if left_distance > right_distance:
        return 1
    return -1 if left_id < right_id else 1


def rotate_right(node: Node) -> Node:
    left = node.left
    assert left is not None
    node.left = left.right
    left.right = node
    return left


def rotate_left(node: Node) -> Node:
    right = node.right
    assert right is not None
    node.right = right.left
    right.left = node
    return right


def merge(left: Node | None, right: Node | None) -> Node | None:
    if left is None:
        return right
    if right is None:
        return left
    if left.priority < right.priority:
        left.right = merge(left.right, right)
        return left
    right.left = merge(left, right.left)
    return right


def insert(node: Node | None, seg_id: int, segments: list[Segment], ray_x: float, ray_y: float) -> Node:
    if node is None:
        return Node(seg_id)

    if compare_segments(segments, seg_id, node.seg_id, ray_x, ray_y) < 0:
        node.left = insert(node.left, seg_id, segments, ray_x, ray_y)
        if node.left is not None and node.left.priority < node.priority:
            node = rotate_right(node)
    else:
        node.right = insert(node.right, seg_id, segments, ray_x, ray_y)
        if node.right is not None and node.right.priority < node.priority:
            node = rotate_left(node)
    return node


def delete(node: Node | None, seg_id: int, segments: list[Segment], ray_x: float, ray_y: float) -> Node | None:
    if node is None:
        return None

    cmp = compare_segments(segments, seg_id, node.seg_id, ray_x, ray_y)
    if cmp < 0:
        node.left = delete(node.left, seg_id, segments, ray_x, ray_y)
        return node
    if cmp > 0:
        node.right = delete(node.right, seg_id, segments, ray_x, ray_y)
        return node
    return merge(node.left, node.right)


def leftmost(node: Node | None) -> int | None:
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node.seg_id


def build_events(segments: list[Segment]) -> list[tuple[float, int, int]]:
    events: list[tuple[float, int, int]] = []
    start_offset = 0.123456789

    for index, segment in enumerate(segments):
        a1 = norm_angle(math.atan2(segment.sy, segment.sx) - start_offset)
        a2 = norm_angle(math.atan2(segment.ey, segment.ex) - start_offset)

        if ccw_diff(a1, a2) <= PI:
            left, right = a1, a2
        else:
            left, right = a2, a1

        segment.left = left
        segment.right = right
        segment.wrap = left > right

        if segment.wrap:
            events.append((right, 0, index))
            events.append((left, 1, index))
        else:
            events.append((left, 1, index))
            events.append((right, 0, index))

    events.sort(key=lambda item: item[0])
    events.append((TAU, 2, -1))
    return events


def solve_case(segments: list[Segment]) -> list[int]:
    if not segments:
        return []

    events = build_events(segments)
    visible = [False] * len(segments)

    groups: list[tuple[float, list[tuple[int, int]]]] = []
    current_angle = events[0][0]
    bucket: list[tuple[int, int]] = []

    for angle, kind, seg_id in events:
        if angle - current_angle > EPS:
            groups.append((current_angle, bucket))
            current_angle = angle
            bucket = []
        bucket.append((kind, seg_id))
    groups.append((current_angle, bucket))

    first_angle = groups[0][0]
    current_ray = first_angle / 2.0 if first_angle > 0 else 0.01
    ray_x = math.cos(current_ray)
    ray_y = math.sin(current_ray)

    root: Node | None = None
    for seg_id, segment in enumerate(segments):
        if segment.wrap:
            root = insert(root, seg_id, segments, ray_x, ray_y)

    first_visible = leftmost(root)
    if first_visible is not None:
        visible[first_visible] = True

    for index, (angle, bucket_events) in enumerate(groups):
        for kind, seg_id in bucket_events:
            if kind == 0:
                root = delete(root, seg_id, segments, ray_x, ray_y)

        next_angle = groups[index + 1][0] if index + 1 < len(groups) else TAU
        current_ray = (angle + next_angle) / 2.0
        ray_x = math.cos(current_ray)
        ray_y = math.sin(current_ray)

        for kind, seg_id in bucket_events:
            if kind == 1:
                root = insert(root, seg_id, segments, ray_x, ray_y)

        top = leftmost(root)
        if top is not None:
            visible[top] = True

    return [1 if item else 0 for item in visible]


def read_cases(data: list[int]) -> list[list[Segment]]:
    cases: list[list[Segment]] = []
    index = 0
    while index < len(data):
        n = data[index]
        index += 1
        segments: list[Segment] = []
        for _ in range(n):
            sx, sy, ex, ey = data[index:index + 4]
            index += 4
            segments.append(Segment(sx, sy, ex, ey))
        cases.append(segments)
    return cases


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    outputs: list[str] = []
    for segments in read_cases(data):
        answers = solve_case(segments)
        outputs.append(" ".join(map(str, answers)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()