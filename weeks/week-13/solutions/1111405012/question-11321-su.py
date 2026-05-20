"""
題目 11321: 柏油路陷阱放置 (簡化版 - SU)
"""

from collections import deque


def has_path_to_right(N, M, traps):
    queue = deque()
    visited = set()
    for x in range(N):
        if (x, 0) not in traps:
            queue.append((x, 0))
            visited.add((x, 0))
    if not queue:
        return False
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x, y = queue.popleft()
        if y == M - 1:
            return True
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and (nx, ny) not in traps:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False


def can_place_trap(N, M, x, y, existing_traps):
    traps = set(existing_traps)
    traps.add((x, y))
    return has_path_to_right(N, M, traps)


def solve(N=None, M=None, x=None, y=None, existing_traps=None):
    return can_place_trap(N, M, x, y, existing_traps) if None not in [N, M, x, y, existing_traps] else False
