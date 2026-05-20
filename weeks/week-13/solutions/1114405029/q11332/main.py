import sys
import math
import random


EPS = 1e-12
TWO_PI = 2.0 * math.pi


class MirrorPiece:
    """
    鏡子的角度區間片段。

    一面鏡子原本是一條線段。
    如果它的角度區間沒有跨過 0 度，就只會產生一個 piece。
    如果它跨過 0 度，會被拆成兩個 piece。

    每個 piece 需要記錄：
    - 原本鏡子的編號 mirror_index
    - 線段端點座標
    - 角度區間 start_angle 到 end_angle
    """

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
    """
    Treap 節點。

    Treap 是一種平衡二元搜尋樹。
    本題使用 Treap 維護目前角度下，active 鏡子的遠近順序。

    key 存的是 piece_id。
    priority 是隨機優先權，用來維持樹的平衡。
    """

    __slots__ = ("key", "priority", "left", "right")

    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None


def angle_of_point(x, y):
    """
    計算點 (x, y) 相對於原點的角度。

    atan2 回傳範圍是 -π 到 π。
    為了方便掃描，若角度為負，就加上 2π，
    轉成 0 到 2π 的範圍。
    """

    angle = math.atan2(y, x)

    if angle < 0:
        angle += TWO_PI

    return angle


def cross(ax, ay, bx, by):
    """
    計算二維向量叉積。

    cross((ax, ay), (bx, by)) = ax * by - ay * bx
    """

    return ax * by - ay * bx


def distance_on_ray(piece, theta):
    """
    計算在角度 theta 的射線上，原點到該鏡子交點的距離。

    射線方向：
        d = (cos(theta), sin(theta))

    線段：
        p = (sx, sy)
        v = (ex - sx, ey - sy)

    交點滿足：
        r * d = p + u * v

    使用叉積可得：
        r = cross(p, v) / cross(d, v)

    r 越小，代表鏡子越靠近原點。
    """

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
    """
    依照目前掃描角度 theta，維護 active 鏡子片段的 Treap。

    Treap 中越靠左，代表在目前角度下越靠近原點。
    因此最左節點就是目前可見的鏡子。
    """

    def __init__(self, pieces):
        self.root = None
        self.pieces = pieces
        self.theta = 0.0

    def set_theta(self, theta):
        """
        設定目前比較距離時使用的角度。
        """

        self.theta = theta

    def less(self, a, b):
        """
        比較 piece a 是否比 piece b 更靠近原點。

        若距離非常接近，使用 piece_id 當作穩定的 tie-breaker，
        避免 Treap 比較結果不穩定。
        """

        da = distance_on_ray(self.pieces[a], self.theta)
        db = distance_on_ray(self.pieces[b], self.theta)

        if abs(da - db) > EPS:
            return da < db

        return a < b

    def rotate_right(self, node):
        """
        Treap 右旋。
        """

        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def rotate_left(self, node):
        """
        Treap 左旋。
        """

        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def insert(self, key):
        """
        將 key 插入 Treap。
        """

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
        """
        從 Treap 刪除 key。
        """

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
        """
        合併兩棵 Treap。
        """

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
        """
        取得 Treap 中最左邊的 key。

        這代表目前角度區間中，距離原點最近的鏡子片段。
        """

        node = self.root

        if node is None:
            return None

        while node.left is not None:
            node = node.left

        return node.key


def add_piece(pieces, events, mirror_index, sx, sy, ex, ey, start_angle, end_angle):
    """
    建立一個鏡子角度片段，並加入事件列表。

    start_angle 是該片段開始被射線打到的角度。
    end_angle 是該片段結束的角度。
    """

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
    """
    將所有鏡子線段轉換成角度區間片段與掃描事件。

    若鏡子的角度區間跨過 0 度，會拆成兩段：
    - start 到 2π
    - 0 到 end
    """

    pieces = []
    events = []

    for index, (sx, sy, ex, ey) in enumerate(segments):
        angle_a = angle_of_point(sx, sy)
        angle_b = angle_of_point(ex, ey)

        a = angle_a
        b = angle_b

        if a > b:
            a, b = b, a

        # 如果兩端點角度差大於 π，
        # 代表真正較短的角度區間跨過 0 度。
        if b - a > math.pi:
            add_piece(pieces, events, index, sx, sy, ex, ey, b, TWO_PI)
            add_piece(pieces, events, index, sx, sy, ex, ey, 0.0, a)
        else:
            add_piece(pieces, events, index, sx, sy, ex, ey, a, b)

    return pieces, events


def solve_case(segments):
    """
    解一組測試資料，回傳該組鏡子的可見結果。
    """

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

        # 同一個角度的事件先刪除結束片段，再加入開始片段。
        for k in range(i, j):
            _, event_type, piece_id = events[k]

            if event_type == -1:
                treap.delete(piece_id)

        for k in range(i, j):
            _, event_type, piece_id = events[k]

            if event_type == 1:
                treap.insert(piece_id)

        # 處理 current_angle 到 next_angle 之間的開放角度區間。
        # 只要某面鏡子在這段區間最近，就表示它有一小段可見。
        if next_angle is not None and next_angle - current_angle > EPS:
            nearest_piece_id = treap.first_key()

            if nearest_piece_id is not None:
                mirror_index = pieces[nearest_piece_id].mirror_index
                visible[mirror_index] = 1

        i = j

    return visible


def solve(data):
    """
    處理完整輸入。

    本題有多組測資，直到 EOF。
    每組測資格式：
        n
        sx sy ex ey
        ...
    """

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
    """
    主程式進入點。
    """

    random.seed(0)
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()