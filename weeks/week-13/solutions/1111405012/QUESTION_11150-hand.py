"""
題目 11150: 青蛙過獨木橋 (簡化版 - SU)
"""

from collections import deque


def min_stones_stepped(L, S, T, stones):
    stones_set = set(stones)
    queue = deque([(0, 0)])
    visited = {0: 0}

    while queue:
        pos, steps = queue.popleft()
        if pos >= L:
            return steps
        for dist in range(S, T + 1):
            next_pos = pos + dist
            new_steps = steps + (1 if next_pos in stones_set else 0)
            if next_pos >= L:
                return new_steps
            if next_pos not in visited or visited[next_pos] > new_steps:
                visited[next_pos] = new_steps
                queue.append((next_pos, new_steps))
    return -1


def solve(L=None, S=None, T=None, stones=None):
    return min_stones_stepped(L, S, T, stones) if all([L, S, T, stones is not None]) else -1
