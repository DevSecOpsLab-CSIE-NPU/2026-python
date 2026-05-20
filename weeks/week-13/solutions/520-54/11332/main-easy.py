import sys
import math
import random


EPS = 1e-12
TWO_PI = 2.0 * math.pi


def solve(data):
    tokens = data.split()

    if not tokens:
        return ""

    random.seed(0)

    pos = 0
    all_outputs = []

    while pos < len(tokens):
        n = int(tokens[pos])
        pos += 1

        segments = []

        for _ in range(n):
            sx = int(tokens[pos])
            sy = int(tokens[pos + 1])
            ex = int(tokens[pos + 2])
            ey = int(tokens[pos + 3])
            pos += 4

            segments.append((sx, sy, ex, ey))

        visible = [0] * n
        pieces = []
        events = []

        def get_angle(x, y):
            angle = math.atan2(y, x)

            if angle < 0:
                angle += TWO_PI

            return angle

        def add_piece(mirror_index, sx, sy, ex, ey, start, end):
            if end - start <= EPS:
                return

            piece_id = len(pieces)
            pieces.append((mirror_index, sx, sy, ex, ey, start, end))
            events.append((start, 1, piece_id))
            events.append((end, -1, piece_id))

        for mirror_index, (sx, sy, ex, ey) in enumerate(segments):
            angle1 = get_angle(sx, sy)
            angle2 = get_angle(ex, ey)

            a = min(angle1, angle2)
            b = max(angle1, angle2)

            if b - a > math.pi:
                add_piece(mirror_index, sx, sy, ex, ey, b, TWO_PI)
                add_piece(mirror_index, sx, sy, ex, ey, 0.0, a)
            else:
                add_piece(mirror_index, sx, sy, ex, ey, a, b)

        if not events:
            all_outputs.append(" ".join(map(str, visible)))
            continue

        events.sort(key=lambda item: item[0])

        def cross(ax, ay, bx, by):
            return ax * by - ay * bx

        current_theta = 0.0

        def distance(piece_id):
            mirror_index, sx, sy, ex, ey, start, end = pieces[piece_id]

            dx = math.cos(current_theta)
            dy = math.sin(current_theta)

            vx = ex - sx
            vy = ey - sy

            numerator = cross(sx, sy, vx, vy)
            denominator = cross(dx, dy, vx, vy)

            if abs(denominator) < EPS:
                return float("inf")

            r = numerator / denominator

            if r < 0:
                r = -r

            return r

        class Node:
            __slots__ = ("key", "priority", "left", "right")

            def __init__(self, key):
                self.key = key
                self.priority = random.random()
                self.left = None
                self.right = None

        def less(a, b):
            da = distance(a)
            db = distance(b)

            if abs(da - db) > EPS:
                return da < db

            return a < b

        def rotate_right(root):
            left = root.left
            root.left = left.right
            left.right = root
            return left

        def rotate_left(root):
            right = root.right
            root.right = right.left
            right.left = root
            return right

        def insert(root, key):
            if root is None:
                return Node(key)

            if less(key, root.key):
                root.left = insert(root.left, key)

                if root.left.priority < root.priority:
                    root = rotate_right(root)
            else:
                root.right = insert(root.right, key)

                if root.right.priority < root.priority:
                    root = rotate_left(root)

            return root

        def merge(left, right):
            if left is None:
                return right

            if right is None:
                return left

            if left.priority < right.priority:
                left.right = merge(left.right, right)
                return left

            right.left = merge(left, right.left)
            return right

        def delete(root, key):
            if root is None:
                return None

            if key == root.key:
                return merge(root.left, root.right)

            if less(key, root.key):
                root.left = delete(root.left, key)
            else:
                root.right = delete(root.right, key)

            return root

        def first_key(root):
            if root is None:
                return None

            while root.left is not None:
                root = root.left

            return root.key

        root = None
        i = 0

        while i < len(events):
            angle = events[i][0]

            j = i

            while j < len(events) and abs(events[j][0] - angle) <= EPS:
                j += 1

            if j < len(events):
                next_angle = events[j][0]
                current_theta = (angle + next_angle) / 2.0
            else:
                next_angle = None

            for k in range(i, j):
                event_angle, event_type, piece_id = events[k]

                if event_type == -1:
                    root = delete(root, piece_id)

            for k in range(i, j):
                event_angle, event_type, piece_id = events[k]

                if event_type == 1:
                    root = insert(root, piece_id)

            if next_angle is not None and next_angle - angle > EPS:
                nearest_piece = first_key(root)

                if nearest_piece is not None:
                    mirror_index = pieces[nearest_piece][0]
                    visible[mirror_index] = 1

            i = j

        all_outputs.append(" ".join(map(str, visible)))

    return "\n".join(all_outputs)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
