import math
import sys


def cover_len(board, width):
    """計算目前路面被傘遮住的總長度。"""

    segs = []
    for x, length, _speed, _dir in board:
        left = max(0.0, x)
        right = min(float(width), x + length)
        if left < right:
            segs.append((left, right))

    segs.sort()
    if not segs:
        return 0.0

    total = 0.0
    left, right = segs[0]
    for a, b in segs[1:]:
        if a > right:
            total += right - left
            left, right = a, b
        else:
            right = max(right, b)
    return total + right - left


def next_dt(board, width):
    """找下一個事件時間：撞邊界，或兩個端點相遇。"""

    dt = math.inf

    # 先看每把傘多久會撞邊界
    for x, length, speed, direction in board:
        if speed == 0:
            continue
        if direction > 0:
            dt = min(dt, (width - length - x) / speed)
        else:
            dt = min(dt, x / speed)

    # 再看所有端點的相遇時間
    points = []
    for i, (x, length, speed, direction) in enumerate(board):
        v = speed * direction
        points.append((i, x, v))
        points.append((i, x + length, v))

    for i in range(len(points)):
        id1, p1, v1 = points[i]
        for j in range(i + 1, len(points)):
            id2, p2, v2 = points[j]
            if id1 == id2 or v1 == v2:
                continue
            t = (p2 - p1) / (v1 - v2)
            if t > 1e-12:
                dt = min(dt, t)

    return dt


def solve(text):
    """讀入整段資料後，直接模擬到 T 秒。"""

    data = [int(x) for x in text.split()]
    if not data:
        return ""

    n, width, total_time, rain = data[:4]
    board = []
    idx = 4

    for _ in range(n):
        x = float(data[idx])
        length = float(data[idx + 1])
        v = data[idx + 2]
        board.append([x, length, abs(v), 1 if v > 0 else -1 if v < 0 else 0])
        idx += 3

    now = 0.0
    volume = 0.0

    while now < total_time - 1e-12:
        dt = min(next_dt(board, width), total_time - now)

        before = width - cover_len(board, width)
        for item in board:
            item[0] += item[3] * item[2] * dt
            if item[3] != 0:
                if item[0] <= 1e-12:
                    item[0] = 0.0
                    item[3] = 1
                elif item[0] >= width - item[1] - 1e-12:
                    item[0] = float(width - item[1])
                    item[3] = -1
        after = width - cover_len(board, width)

        # 這一小段內，未遮住的長度線性變化，用梯形公式即可
        volume += (before + after) * dt / 2.0
        now += dt

    return f"{volume * rain:.2f}"


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()