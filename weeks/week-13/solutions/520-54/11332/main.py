import sys
import math
import random


EPS = 1e-12
TWO_PI = 2.0 * math.pi


class MirrorPiece:
    def __init__(self, piece_id, mirror_index, sx, sy, ex, ey, start_angle, end_angle):
        self.piece_id = piece_id
        self.mirror_index = mirror_index
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.start_angle = start_angle
        self.end_angle = end_angle


class TreapNode:
    __slots__ = ("key", "priority", "left", "right")

    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None


def angle_of_point(x, y):
    angle = math.atan2(y, x)

    if angle < 0:
        angle += TWO_PI

    return angle


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def distance_on_ray(piece, theta):
    dx = math.cos(theta)
    dy = math.sin(theta)

    vx = piece.ex - piece.sx
    vy = piece.ey - piece.sy

    numerator = cross(piece.sx, piece.sy, vx, vy)
    denominator = cross(dx, dy, vx, vy)

    if abs(denominator) < EPS:
        return float("inf")

    r = numerator / denominator

    if r < 0:
        r = -r

    return r


class Treap:
    def __init__(self, pieces):
        self.root = None
        self.pieces = pieces
        self.theta = 0.0

    def set_theta(self, theta):
        self.theta = theta

    def less(self, a, b):
        da = distance_on_ray(self.pieces[a], self.theta)
        db = distance_on_ray(self.pieces[b], self.theta)

        if abs(da - db) > EPS:
            return da < db

        return a < b

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreapNode(key)

        if self.less(key, node.key):
            node.left = self._insert(node.left, key)

            if node.left.priority < node.priority:
                node = self.rotate_right(node)
        else:
            node.right = self._insert(node.right, key)

            if node.right.priority < node.priority:
                node = self.rotate_left(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return self._merge(node.left, node.right)

        if self.less(key, node.key):
            node.left = self._delete(node.left, key)
        else:
            node.right = self._delete(node.right, key)

        return node

    def _merge(self, left, right):
        if left is None:
            return right

        if right is None:
            return left

        if left.priority < right.priority:
            left.right = self._merge(left.right, right)
            return left

        right.left = self._merge(left, right.left)
        return right

    def first_key(self):
        node = self.root

        if node is None:
            return None

        while node.left is not None:
            node = node.left

        return node.key


def add_piece(pieces, events, mirror_index, sx, sy, ex, ey, start_angle, end_angle):
    if end_angle - start_angle <= EPS:
        return

    piece_id = len(pieces)

    piece = MirrorPiece(
        piece_id,
        mirror_index,
        sx,
        sy,
        ex,
        ey,
        start_angle,
        end_angle
    )

    pieces.append(piece)
    events.append((start_angle, 1, piece_id))
    events.append((end_angle, -1, piece_id))


def build_pieces_and_events(segments):
    pieces = []
    events = []

    for index, (sx, sy, ex, ey) in enumerate(segments):
        angle_a = angle_of_point(sx, sy)
        angle_b = angle_of_point(ex, ey)

        a = angle_a
        b = angle_b

        if a > b:
            a, b = b, a

        if b - a > math.pi:
            add_piece(pieces, events, index, sx, sy, ex, ey, b, TWO_PI)
            add_piece(pieces, events, index, sx, sy, ex, ey, 0.0, a)
        else:
            add_piece(pieces, events, index, sx, sy, ex, ey, a, b)

    return pieces, events


def solve_case(segments):
    n = len(segments)
    visible = [0] * n

    pieces, events = build_pieces_and_events(segments)

    if not events:
        return visible

    events.sort(key=lambda item: item[0])

    treap = Treap(pieces)

    i = 0
    event_count = len(events)

    while i < event_count:
        current_angle = events[i][0]

        j = i

        while j < event_count and abs(events[j][0] - current_angle) <= EPS:
            j += 1

        next_angle = events[j][0] if j < event_count else None

        if next_angle is not None:
            mid_angle = (current_angle + next_angle) / 2.0
            treap.set_theta(mid_angle)

        for k in range(i, j):
            _, event_type, piece_id = events[k]

            if event_type == -1:
                treap.delete(piece_id)

        for k in range(i, j):
            _, event_type, piece_id = events[k]

            if event_type == 1:
                treap.insert(piece_id)

        if next_angle is not None and next_angle - current_angle > EPS:
            nearest_piece_id = treap.first_key()

            if nearest_piece_id is not None:
                mirror_index = pieces[nearest_piece_id].mirror_index
                visible[mirror_index] = 1

        i = j

    return visible


def solve(data):
    tokens = data.split()

    if not tokens:
        return ""

    index = 0
    outputs = []

    while index < len(tokens):
        n = int(tokens[index])
        index += 1

        segments = []

        for _ in range(n):
            sx = int(tokens[index])
            sy = int(tokens[index + 1])
            ex = int(tokens[index + 2])
            ey = int(tokens[index + 3])
            index += 4

            segments.append((sx, sy, ex, ey))

        visible = solve_case(segments)
        outputs.append(" ".join(map(str, visible)))

    return "\n".join(outputs)


def main():
    random.seed(0)
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
