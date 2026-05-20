"""
題目 11150: 青蛙過獨木橋 (正式版)
計算青蛙從起點 (0) 跳到終點 (L) 最少需要踩到的石子數

使用 BFS 求解：
- 狀態：當前位置
- 轉移：每次可以跳 S 到 T 的距離
- 目標：到達 L 或超過 L
"""

from collections import deque
from typing import List, Set, Tuple


def can_jump(from_pos: int, to_pos: int, L: int, S: int, T: int, stones: Set[int]) -> Tuple[bool, int]:
    """
    檢查是否能從 from_pos 跳到 to_pos，計算踩到的石子數

    Args:
        from_pos: 當前位置
        to_pos: 目標位置
        L: 橋的終點
        S, T: 跳躍距離範圍
        stones: 石子位置集合

    Returns:
        (是否能跳, 踩到的石子數)
    """
    distance = to_pos - from_pos
    if distance < S or distance > T:
        return (False, 0)
    if to_pos in stones:
        return (True, 1)
    return (True, 0)


def min_stones_stepped(L: int, S: int, T: int, stones: List[int]) -> int:
    """
    使用 BFS 找出最少踩到的石子數

    Args:
        L: 橋的長度
        S, T: 跳躍距離範圍
        stones: 石子位置列表

    Returns:
        最少踩到的石子數
    """
    stones_set = set(stones)

    # BFS: (位置, 踩到的石子數)
    queue = deque([(0, 0)])
    visited = {0: 0}

    while queue:
        pos, steps = queue.popleft()

        # 檢查是否已到達或超過終點
        if pos >= L:
            return steps

        # 嘗試所有可能的跳躍
        for distance in range(S, T + 1):
            next_pos = pos + distance

            # 踩到的石子數
            stones_count = 1 if next_pos in stones_set else 0
            new_steps = steps + stones_count

            # 檢查終點
            if next_pos >= L:
                return new_steps

            # 檢查是否值得訪問
            if next_pos not in visited or visited[next_pos] > new_steps:
                visited[next_pos] = new_steps
                queue.append((next_pos, new_steps))

    return -1


def solve(L: int = None, S: int = None, T: int = None, stones: List[int] = None) -> int:
    """
    主求解函數
    """
    if L is None or S is None or T is None or stones is None:
        return -1

    return min_stones_stepped(L, S, T, stones)
