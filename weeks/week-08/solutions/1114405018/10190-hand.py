import math
import sys

def cover_len(board, width):
    
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
    dt = math.inf

    for x, length, speed, direction in board:
        if speed == 0:
            continue
        if direction > 0:
            dt = min(dt, (width - length - x) / speed)
        else:
            dt = min(dt, x / speed)

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

    date = [int(x) for x in text.split()]
    if not date:
        return " "
    
    n, width, total_time = date[:4]
    board = []
    idx =4

    for _ in range(n):
        x = float(date[idx])
        length = float(date[idx + 1])
        v=date[idx + 2]
        board.append((x, length, abs(v), 1 if v > 0 else -1))
        idx += 3

        now = 0.0
        volume = 0.0 

        while now < total_time  - 1e-12:
            dt = min(next_dt(board, width), total_time - now)
           
            before = width - cover_len(board, width)
            for item in board:
                item[0] += item[2] * item[3] * dt
                if item[3] != 0:
                    if item[0] <= 1e-12:
                        item[0] = 0.0
                        item[3] = 1
                    elif item[0] + item[1] >= width - 1e-12:
                        item[0] = width - item[1]
                        item[3] = -1
            after = width - cover_len(board, width)
            volume += (before + after) * dt * 0.5 * rain
            now += dt

    return f"{volume:.2f}
    
    
def main():
    sys.stdout.write(solve(sys.stdin.read()))
    
if __name__ == "__main__":
    main()
    