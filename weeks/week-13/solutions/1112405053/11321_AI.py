import sys
from collections import deque


# 每次嘗試放置陷阱：若放置後會讓左側任一格無法到達右側任一格，則視為封死，該陷阱不能放。
# 輸出：能放 -> <(_ _)>；不能放（導致道路封死）-> >_<


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(map(int, data))
    N = next(it)
    M = next(it)
    T = next(it)

    traps = [[False] * M for _ in range(N)]  # 使用輸入的 x,y 座標（x=0 為底）

    # 讀取所有待放置的陷阱座標
    queries = []
    for _ in range(T):
        try:
            x = next(it)
            y = next(it)
        except StopIteration:
            break
        queries.append((x, y))

    # 四方向移動：上下左右（x 是縱軸）
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    out_lines = []

    for x, y in queries:
        # 若該點已經放過陷阱，根據題意這種情況不會發生（保證最多放一次），但我們保守處理：直接回應能放
        if traps[x][y]:
            out_lines.append("<(_ _)>")
            continue

        # 暫時放置陷阱
        traps[x][y] = True

        # BFS 從左邊所有未被陷阱阻擋的格子開始，檢查是否能到達任一右邊格子 y == M-1
        visited = [[False] * M for _ in range(N)]
        dq = deque()
        # 所有左側欄位 y == 0 的格子
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
            # 可以放，保持 traps 標記
            out_lines.append("<(_ _)>")
        else:
            # 不能放，撤銷放置
            traps[x][y] = False
            out_lines.append(">_<")

    sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
    main()
