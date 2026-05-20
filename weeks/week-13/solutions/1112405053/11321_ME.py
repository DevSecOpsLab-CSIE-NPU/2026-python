import sys
from collections import deque



def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(map(int, data))
    N = next(it)
    M = next(it)
    T = next(it)

    traps = [[False] * M for _ in range(N)] 

    queries = []
    for _ in range(T):
        try:
            x = next(it)
            y = next(it)
        except StopIteration:
            break
        queries.append((x, y))

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    out_lines = []

    for x, y in queries:
        if traps[x][y]:
            out_lines.append("<(_ _)>")
            continue

        traps[x][y] = True

        visited = [[False] * M for _ in range(N)]
        dq = deque()
        for rx in range(N):
            if not traps[rx][0]:
                visited[rx][0] = True
                dq.append((rx, 0))

        reachable = False
        while dq:
            cx, cy = dq.popleft()
            if cy == M - 1:
                reachable = True
                break
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and (not traps[nx][ny]) and (not visited[nx][ny]):
                    visited[nx][ny] = True
                    dq.append((nx, ny))

        if reachable:
            out_lines.append("<(_ _)>")
        else:
            traps[x][y] = False
            out_lines.append(">_<")

    sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
    main()
