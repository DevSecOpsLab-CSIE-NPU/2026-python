"""UVA 11150 - 簡化版 0-1 BFS

這份解法保留題目的核心演算法 0-1 BFS，但把程式寫得更容易閱讀：
1. 用較清楚的變數名稱表示位置、石頭與跳躍範圍
2. 先把石頭位置整理成集合，方便快速判斷是否踩到石頭
3. 用 deque 實作 0-1 BFS，讓「不踩石頭」的移動優先處理

題目本質上是在最少踩石頭次數的前提下，從起點跳到終點或超過終點。
"""

import sys
from collections import deque


def solve_case(L, S, T, stones):
    # 將石頭位置改成集合，查詢某個位置是否有石頭時可用 O(1) 判斷。
    stone_set = set(stones)
    # 只需要考慮到「最後一塊石頭 + 最大跳躍距離」的位置，超過後就可直接視為到達終點。
    max_stone = max(stones) if stones else 0
    max_pos = min(L, max_stone + T)

    # dist[pos] 表示到達 pos 時，最少需要踩到幾次石頭。
    # INF 代表目前還沒有找到到達該位置的方法。
    INF = 10**9
    dist = [INF] * (max_pos + 1)
    dist[0] = 0

    # deque 讓我們可以把「成本 0」的下一個位置放到左邊，優先處理。
    dq = deque([0])
    ans = INF

    while dq:
        pos = dq.popleft()
        # 如果目前位置已經到達或超過 L，代表已經完成跳躍。
        if pos >= L:
            ans = min(ans, dist[pos])
            continue

        # 從目前位置可跳 S 到 T 步，逐一嘗試所有可能。
        for jump in range(S, T+1):
            nxt = pos + jump

            # 一旦跳到或超過終點，就不需要再繼續往後探索，
            # 只需更新答案即可。
            if nxt >= L:
                ans = min(ans, dist[pos])
                continue

            # 超出我們預先保留的搜尋範圍就略過，避免陣列越界。
            if nxt > max_pos:
                continue

            # 若落點有石頭，代價為 1；否則代價為 0。
            cost = 1 if nxt in stone_set else 0
            nd = dist[pos] + cost

            # 只有當找到更小代價時才更新，這是最短路徑/最小代價搜尋的基本原則。
            if nd < dist[nxt]:
                dist[nxt] = nd
                if cost == 0:
                    # 成本為 0 的狀態優先處理，放到 deque 左側。
                    dq.appendleft(nxt)
                else:
                    # 成本為 1 的狀態放到右側，稍後處理。
                    dq.append(nxt)

    # 如果完全沒辦法到達終點，就依題意回傳 0。
    return ans if ans != INF else 0


def solve():
    # 一次讀入所有測資，依照題目格式逐組解析。
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    idx = 0
    out = []
    while idx < len(data):
        # 每組測資格式為：L S T M
        L = data[idx]; idx += 1
        S = data[idx]; T = data[idx+1]; M = data[idx+2]; idx += 3
        # 接著讀入 M 個石頭位置。
        stones = data[idx: idx+M]; idx += M
        # 將每組答案轉字串後收集，最後一次輸出。
        out.append(str(solve_case(L, S, T, stones)))
    print("\n".join(out))


if __name__ == '__main__':
    # 直接執行此檔案時，進入解題流程。
    solve()
