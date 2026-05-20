"""
題目 11321: 柏油路陷阱放置 (簡易版 - Easy)

核心概念：
- N*M 的網格，從左 (y=0) 到右 (y=M-1)
- 只能四方向移動 (上下左右)
- 檢查放置陷阱後是否還能從左通到右

演算法：使用 BFS 檢查通路
1. 起點：左邊任何沒有陷阱的位置
2. 終點：右邊任何位置
3. 如果 BFS 能到達右邊，表示有通路
"""

from collections import deque


def has_path_to_right(N, M, traps):
    """
    使用 BFS 檢查從左邊到右邊的通路

    參數：
    - N: 網格高度 (x軸，0 到 N-1)
    - M: 網格寬度 (y軸，0 到 M-1)
    - traps: 陷阱位置的集合

    流程：
    1. 從左邊 (y=0) 開始，所有沒有陷阱的 x 位置
    2. 使用 BFS 探索所有能到達的位置
    3. 如果能到達右邊 (y=M-1)，返回 True
    """
    # 初始化：左邊所有可以開始的位置
    queue = deque()
    visited = set()

    # 從左邊 (y=0) 的所有非陷阱位置開始
    for x in range(N):
        if (x, 0) not in traps:
            queue.append((x, 0))
            visited.add((x, 0))

    # 如果左邊全是陷阱，無法開始
    if not queue:
        return False

    # 四個方向：上、下、右、左
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # BFS 搜尋
    while queue:
        x, y = queue.popleft()

        # 檢查是否已到達右邊
        if y == M - 1:
            return True

        # 檢查四個相鄰位置
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 檢查是否在邊界內
            if 0 <= nx < N and 0 <= ny < M:
                # 檢查是否未訪問且沒有陷阱
                if (nx, ny) not in visited and (nx, ny) not in traps:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    # 如果 BFS 結束還沒到達右邊，表示無通路
    return False


def can_place_trap(N, M, x, y, existing_traps):
    """
    判斷是否可以在 (x, y) 位置放置陷阱

    規則：只要放置後仍然存在從左到右的通路就可以放

    流程：
    1. 將新陷阱加入現有陷阱集合
    2. 檢查是否仍有左到右的通路
    3. 有通路則可放 (返回 True)，無通路則不可放 (返回 False)
    """
    # 建立包含新陷阱的陷阱集合
    traps = set(existing_traps)
    traps.add((x, y))

    # 檢查加入新陷阱後是否還有通路
    return has_path_to_right(N, M, traps)


def solve(N=None, M=None, x=None, y=None, existing_traps=None):
    """主求解函數"""
    if None in [N, M, x, y, existing_traps]:
        return False
    return can_place_trap(N, M, x, y, existing_traps)
