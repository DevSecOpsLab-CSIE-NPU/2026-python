"""UVA 11321 - 簡化版

這份解法的核心概念很單純：
1. 每次嘗試把某個位置設成障礙
2. 立刻用 BFS 檢查左邊是否還能走到右邊
3. 如果無法通行，就把這個障礙撤回

因此，整體流程其實是在模擬「每次新增一個陷阱後，地圖是否仍可通行」。
"""

import sys
from collections import deque


def can_reach_right(N, M, blocked):
    # BFS 佇列，從左側所有沒有被擋住的格子一起當作起點。
    q = deque()
    # seen 用來記錄某個格子是否已經拜訪過，避免重複搜尋。
    seen = [[False]*M for _ in range(N)]

    # 左邊第一欄若沒有被障礙擋住，就可以作為 BFS 的起點。
    for r in range(N):
        if not blocked[r][0]:
            q.append((r,0)); seen[r][0]=True

    # 四個方向：下、上、右、左。
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    # 典型 BFS：逐步擴張可走範圍。
    while q:
        x,y = q.popleft()

        # 只要碰到最右邊那一欄，就代表成功連通到右側。
        if y == M-1:
            return True

        # 嘗試往四個方向前進。
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy

            # 先檢查是否在範圍內，再確認沒有障礙且尚未拜訪。
            if 0<=nx<N and 0<=ny<M and not blocked[nx][ny] and not seen[nx][ny]:
                seen[nx][ny]=True; q.append((nx,ny))

    # BFS 結束仍沒有到達右邊，代表左到右無法通行。
    return False


def solve():
    # 一次把所有輸入讀進來，方便逐項處理。
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    # 依照題目格式，第一組是地圖大小與障礙數量。
    it = iter(data)
    N = next(it); M = next(it); T = next(it)

    # blocked[x][y] = True 代表該格已經有障礙，不能通過。
    blocked = [[False]*M for _ in range(N)]
    out = []

    # 逐一處理每次新增障礙的操作。
    for _ in range(T):
        x = next(it); y = next(it)

        # 如果同一個位置已經是障礙，再次放置就屬於重複操作。
        if blocked[x][y]:
            out.append("<_(_ _)>")
            continue

        # 先假設這個位置可以放障礙。
        blocked[x][y] = True

        # 放上去之後檢查是否還能從左走到右。
        if can_reach_right(N, M, blocked):
            # 若仍可通行，回傳成功符號。
            out.append("<(_ _)>")
        else:
            # 若造成斷路，需撤回這次放置，保持地圖仍可通行。
            out.append(">_<")
            blocked[x][y] = False

    # 一次輸出所有結果，維持題目要求的格式。
    print("\n".join(out))

if __name__ == '__main__':
    # 直接執行此檔案時，進入解題流程。
    solve()
