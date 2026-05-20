import sys
from collections import deque


def has_path(grid, n, m):
    visited = [[False] * m for _ in range(n)]
    q = deque()

    for x in range(n):
        if not grid[x][0]:
            visited[x][0] = True
            q.append((x, 0))

    if not q:
        return False

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()

        if y == m - 1:
            return True

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if grid[nx][ny] or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))

    return False


def solve(text):
    arr = text.split()
    p = 0

    n = int(arr[p])
    m = int(arr[p + 1])
    t = int(arr[p + 2])
    p += 3

    grid = [[False] * m for _ in range(n)]
    out = []

    for _ in range(t):
        x = int(arr[p])
        y = int(arr[p + 1])
        p += 2

        grid[x][y] = True

        if has_path(grid, n, m):
            out.append("<(_ _)>")
        else:
            grid[x][y] = False
            out.append(">_<")

    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()