"""UVA 11150 - 青蛙過橋 (簡化上界的 0-1 BFS 解法)

說明：把位置限制到 max_pos = min(L, max_stone + T)，使用 0-1 BFS
計算到達任一 >= L 的最小踩石子數。
"""

from __future__ import annotations

import sys
from collections import deque


def solve_case(L: int, S: int, T: int, stones: list[int]) -> int:
    stone_set = set(stones)
    max_stone = max(stones) if stones else 0
    max_pos = min(L, max_stone + T)

    # distance = minimal stones stepped to reach position
    INF = 10 ** 9
    dist = [INF] * (max_pos + 1)
    dist[0] = 0
    dq = deque([0])

    ans = INF

    while dq:
        pos = dq.popleft()
        if pos >= L:
            ans = min(ans, dist[pos])
            continue

        for jump in range(S, T + 1):
            nxt = pos + jump
            if nxt >= L:
                # landing beyond L: no stone
                ans = min(ans, dist[pos])
                continue

            if nxt > max_pos:
                # we cap positions beyond max_pos; treat as success if beyond L
                continue

            cost = 1 if nxt in stone_set else 0
            nd = dist[pos] + cost
            if nd < dist[nxt]:
                dist[nxt] = nd
                if cost == 0:
                    dq.appendleft(nxt)
                else:
                    dq.append(nxt)

    return ans if ans != INF else 0


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    idx = 0
    outputs: list[str] = []
    while idx < len(data):
        L = data[idx]
        idx += 1
        S = data[idx]; T = data[idx+1]; M = data[idx+2]
        idx += 3
        stones = data[idx: idx + M]
        idx += M
        outputs.append(str(solve_case(L, S, T, stones)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
