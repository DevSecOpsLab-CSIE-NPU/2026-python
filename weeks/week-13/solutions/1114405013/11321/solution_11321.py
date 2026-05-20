import sys
from collections import deque


def can_reach_right(blocked, n, m):
    """檢查是否存在從左邊界到右邊界的可行路徑。"""
    visited = [[False] * m for _ in range(n)]
    queue = deque()

    # 把左邊界所有未封鎖格子當成 BFS 起點。
    for x in range(n):
        if not blocked[x][0]:
            visited[x][0] = True
            queue.append((x, 0))

    # 左邊界若全被封住，直接不可達。
    if not queue:
        return False

    # 四方向移動（上、下、左、右）。
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        # 只要走到右邊界，就代表道路未封死。
        if y == m - 1:
            return True

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if blocked[nx][ny] or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))

    return False


def simulate(n, m, traps):
    """依序嘗試放陷阱，回傳每次操作的輸出字串。"""
    blocked = [[False] * m for _ in range(n)]
    answers = []

    for x, y in traps:
        # 先暫時放上陷阱，再檢查道路是否仍可通行。
        blocked[x][y] = True

        if can_reach_right(blocked, n, m):
            answers.append("<(_ _)>")
        else:
            # 若封死就回滾，不真的放上這顆陷阱。
            blocked[x][y] = False
            answers.append(">_<")

    return answers


def solve(text):
    """讀取輸入並回傳每次放陷阱後的結果。"""
    tokens = text.split()
    idx = 0

    n = int(tokens[idx])
    m = int(tokens[idx + 1])
    t = int(tokens[idx + 2])
    idx += 3

    traps = []
    for _ in range(t):
        x = int(tokens[idx])
        y = int(tokens[idx + 1])
        idx += 2
        traps.append((x, y))

    return "\n".join(simulate(n, m, traps))


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
