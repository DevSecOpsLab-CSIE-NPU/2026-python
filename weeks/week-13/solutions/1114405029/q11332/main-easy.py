import sys
import math
import random


EPS = 1e-12
TWO_PI = 2.0 * math.pi


def solve(data):
    """
    直觀版本解法。

    本題是從原點觀察多條線段鏡子。

    一面鏡子是否可見，可以轉換成角度問題：
    - 每面鏡子會佔據一段角度範圍。
    - 在同一段角度範圍內，最靠近原點的鏡子可見。
    - 如果某面鏡子在任何一小段角度內是最前面的，它就是可見。

    因此做法是：
    1. 將每面鏡子轉成角度區間。
    2. 對所有角度端點做掃描。
    3. 維護目前角度中會被射線打到的鏡子。
    4. 找出目前最靠近原點的鏡子，標記為可見。
    """

    tokens = data.split()

    if not tokens:
        return ""

    # 固定 random seed，讓 Treap 測試結果穩定。
    random.seed(0)

    pos = 0
    all_outputs = []

    while pos < len(tokens):
        # 讀取這組測資的鏡子數量。
        n = int(tokens[pos])
        pos += 1

        # segments 存放所有鏡子的兩個端點。
        segments = []

        for _ in range(n):
            sx = int(tokens[pos])
            sy = int(tokens[pos + 1])
            ex = int(tokens[pos + 2])
            ey = int(tokens[pos + 3])
            pos += 4

            segments.append((sx, sy, ex, ey))

        # visible[i] 表示第 i 面鏡子是否可見。
        visible = [0] * n

        # pieces 存放鏡子角度區間片段。
        # 每個元素格式：
        # (mirror_index, sx, sy, ex, ey, start_angle, end_angle)
        pieces = []

        # events 存放掃描事件。
        # 每個事件格式：
        # (angle, type, piece_id)
        # type = 1 表示該角度開始進入 active
        # type = -1 表示該角度離開 active
        events = []

        def get_angle(x, y):
            """
            計算點 (x, y) 相對原點的角度，並轉成 0 到 2π。
            """

            angle = math.atan2(y, x)

            if angle < 0:
                angle += TWO_PI

            return angle

        def add_piece(mirror_index, sx, sy, ex, ey, start, end):
            """
            新增一個角度區間片段。

            如果區間長度太小，表示幾乎沒有可見角度範圍，
            就不加入處理。
            """

            if end - start <= EPS:
                return

            piece_id = len(pieces)
            pieces.append((mirror_index, sx, sy, ex, ey, start, end))

            events.append((start, 1, piece_id))
            events.append((end, -1, piece_id))

        # 將每面鏡子轉成角度區間。
        for mirror_index, (sx, sy, ex, ey) in enumerate(segments):
            angle1 = get_angle(sx, sy)
            angle2 = get_angle(ex, ey)

            a = min(angle1, angle2)
            b = max(angle1, angle2)

            # 若 b - a > π，代表真正較短的視角區間跨過 0 度。
            # 例如 350 度到 10 度，要拆成：
            # 350 度到 360 度，以及 0 度到 10 度。
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
            """
            二維向量叉積。
            """

            return ax * by - ay * bx

        current_theta = 0.0

        def distance(piece_id):
            """
            計算目前掃描角度 current_theta 下，
            原點射線打到 piece_id 這面鏡子片段時的距離。
            """

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
            """
            Treap 節點。
            key 是 piece_id。
            priority 是隨機優先權。
            """

            __slots__ = ("key", "priority", "left", "right")

            def __init__(self, key):
                self.key = key
                self.priority = random.random()
                self.left = None
                self.right = None

        def less(a, b):
            """
            判斷 piece a 是否比 piece b 更靠近原點。
            """

            da = distance(a)
            db = distance(b)

            if abs(da - db) > EPS:
                return da < db

            return a < b

        def rotate_right(root):
            """
            Treap 右旋。
            """

            left = root.left
            root.left = left.right
            left.right = root
            return left

        def rotate_left(root):
            """
            Treap 左旋。
            """

            right = root.right
            root.right = right.left
            right.left = root
            return right

        def insert(root, key):
            """
            將 key 插入 Treap。
            """

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
            """
            合併兩棵 Treap。
            """

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
            """
            從 Treap 中刪除 key。
            """

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
            """
            找出 Treap 最左邊的 key。

            最左邊代表目前角度下距離原點最近的鏡子片段。
            """

            if root is None:
                return None

            while root.left is not None:
                root = root.left

            return root.key

        # root 是目前 active 鏡子片段的 Treap root。
        root = None

        i = 0

        while i < len(events):
            angle = events[i][0]

            # 找出所有同角度事件。
            j = i

            while j < len(events) and abs(events[j][0] - angle) <= EPS:
                j += 1

            # 下一個角度事件之前，中間是一段開放角度區間。
            if j < len(events):
                next_angle = events[j][0]
                current_theta = (angle + next_angle) / 2.0
            else:
                next_angle = None

            # 先刪除在此角度結束的片段。
            for k in range(i, j):
                event_angle, event_type, piece_id = events[k]

                if event_type == -1:
                    root = delete(root, piece_id)

            # 再加入在此角度開始的片段。
            for k in range(i, j):
                event_angle, event_type, piece_id = events[k]

                if event_type == 1:
                    root = insert(root, piece_id)

            # 若存在下一個角度，就代表 angle 到 next_angle 之間有一段區間。
            # 此區間內最近的鏡子可見。
            if next_angle is not None and next_angle - angle > EPS:
                nearest_piece = first_key(root)

                if nearest_piece is not None:
                    mirror_index = pieces[nearest_piece][0]
                    visible[mirror_index] = 1

            i = j

        all_outputs.append(" ".join(map(str, visible)))

    return "\n".join(all_outputs)


def main():
    """
    從標準輸入讀取多組測資，輸出每組鏡子的可見狀態。
    """

    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()