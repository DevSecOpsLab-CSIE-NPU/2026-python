import sys
from collections import deque


def has_path(grid, n, m):
    # 這個函式負責檢查：
    # 在目前陷阱配置下，是否「仍然存在」一條路，
    # 能從左邊界走到右邊界。
    #
    # grid[x][y] = True  代表該格有陷阱（不可走）
    # grid[x][y] = False 代表該格可走

    # visited 用來避免 BFS 重複走同一格。
    visited = [[False] * m for _ in range(n)]
    q = deque()

    # BFS 起點：左邊界（y=0）所有可走的格子。
    # 因為題目說起點在左邊，所以左邊整條邊都可當作出發點。
    for x in range(n):
        if not grid[x][0]:
            visited[x][0] = True
            q.append((x, 0))

    # 若左邊界全被陷阱封住，連起步都沒辦法，直接回傳 False。
    if not q:
        return False

    # 可移動方向：上、下、左、右（不能斜走）。
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()

        # 只要有任一條路可以到達右邊界（y = m-1），
        # 就表示道路沒有被封死。
        if y == m - 1:
            return True

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            # 越界就跳過。
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 踩到陷阱或已走過就跳過。
            if grid[nx][ny] or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))

    # BFS 結束仍到不了右邊界，表示已封路。
    return False


def solve(text):
    # 輸入格式：
    # 第一行 N M T
    # 接著 T 行，每行一個陷阱座標 x y
    #
    # 這裡用 split() 一次切 token，配合指標 p 順序讀取，
    # 寫法最直覺、最好記。
    arr = text.split()
    p = 0

    n = int(arr[p])
    m = int(arr[p + 1])
    t = int(arr[p + 2])
    p += 3

    # 狀態網格：True 表示該格已放陷阱（不可走）。
    grid = [[False] * m for _ in range(n)]
    out = []

    # 依輸入順序，逐一嘗試放每顆陷阱。
    for _ in range(t):
        x = int(arr[p])
        y = int(arr[p + 1])
        p += 2

        # 先「暫時」放上去，再做連通性檢查。
        grid[x][y] = True

        # 若放完後仍有路從左到右：
        # 表示這顆陷阱可放，輸出 <(_ _)>。
        #
        # 若放完後道路封死：
        # 表示這顆陷阱不可放，必須回滾（設回 False），
        # 並輸出 >_<。
        if has_path(grid, n, m):
            out.append("<(_ _)>")
        else:
            grid[x][y] = False
            out.append(">_<")

    # 每次判定一行輸出。
    return "\n".join(out)


def main():
    # 標準輸入 -> solve -> 標準輸出。
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
