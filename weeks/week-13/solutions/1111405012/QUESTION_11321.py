"""
題目 11321: 柏油路陷阱放置 (正式版)
判斷在 N*M 網格上放置陷阱是否會斷路

使用 BFS 檢查是否存在從左 (x=0) 到右 (x=N-1) 的通路
- 可四方向移動 (上下左右)
- 起點：x=0, 任意 y
- 終點：x=N-1, 任意 y
"""

from collections import deque
from typing import List, Tuple, Set


def has_path_to_right(N: int, M: int, traps: Set[Tuple[int, int]]) -> bool:
    """
    使用 BFS 檢查是否存在從左到右的通路

    Args:
        N: 網格高度 (x軸)
        M: 網格寬度 (y軸)
        traps: 陷阱位置集合

    Returns:
        True 如果存在通路，False 否則
    """
    # 從左邊所有位置開始搜尋
    queue = deque()
    visited = set()

    # 初始化：左邊沒有陷阱的位置
    for x in range(N):
        if (x, 0) not in traps:
            queue.append((x, 0))
            visited.add((x, 0))

    # 如果左邊全是陷阱，無法開始
    if not queue:
        return False

    # BFS 搜尋
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        x, y = queue.popleft()

        # 檢查是否到達右邊
        if y == M - 1:
            return True

        # 檢查四個方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 檢查邊界
            if 0 <= nx < N and 0 <= ny < M:
                # 檢查是否未訪問且沒有陷阱
                if (nx, ny) not in visited and (nx, ny) not in traps:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return False


def can_place_trap(N: int, M: int, x: int, y: int, existing_traps: List[Tuple[int, int]]) -> bool:
    """
    判斷是否可以在 (x, y) 放置陷阱

    可以放置當且僅當放置後仍存在從左到右的通路

    Args:
        N: 網格高度
        M: 網格寬度
        x: 陷阱 x 座標
        y: 陷阱 y 座標
        existing_traps: 現有陷阱列表

    Returns:
        True 可以放置，False 不能放置
    """
    # 建立包含新陷阱的陷阱集合
    traps = set(existing_traps)
    traps.add((x, y))

    # 檢查是否仍有通路
    return has_path_to_right(N, M, traps)


def solve(N: int = None, M: int = None, x: int = None, y: int = None, existing_traps: List = None) -> bool:
    """主求解函數"""
    if None in [N, M, x, y, existing_traps]:
        return False
    return can_place_trap(N, M, x, y, existing_traps)
