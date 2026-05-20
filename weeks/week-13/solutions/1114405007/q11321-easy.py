"""11321 簡單版：每次嘗試放陷阱，若封死左右道路就拒絕。"""

import sys
from collections import deque


def has_path_left_to_right(n, m, blocked):
    """檢查空地是否還能從左邊界走到右邊界（4 方向）。"""
    q = deque()
    seen = [[False] * m for _ in range(n)]

    for x in range(n):
        if (x, 0) not in blocked:
            q.append((x, 0))
            seen[x][0] = True

    while q:
        x, y = q.popleft()
        if y == m - 1:
            return True

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not seen[nx][ny] and (nx, ny) not in blocked:
                seen[nx][ny] = True
                q.append((nx, ny))

    return False


def solve(text):
    arr = text.split()
    if not arr:
        return ""

    p = 0
    n = int(arr[p])
    m = int(arr[p + 1])
    t = int(arr[p + 2])
    p += 3

    blocked = set()
    out = []

    for _ in range(t):
        x = int(arr[p])
        y = int(arr[p + 1])
        p += 2

        # 放上去先試，如果封死就撤回
        blocked.add((x, y))
        if has_path_left_to_right(n, m, blocked):
            out.append("<(_ _)>")
        else:
            blocked.remove((x, y))
            out.append(">_<")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
