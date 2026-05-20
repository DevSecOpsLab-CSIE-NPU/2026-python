"""UVA 11150 - Frog bridge minimum stones (easy version with detailed comments)."""

from __future__ import annotations

from collections import deque
import sys


EXACT_LIMIT = 200_000


def can_make(distance: int, s: int, t: int) -> bool:
    """判斷距離 distance 是否能由若干次 [S, T] 的跳躍組成。"""
    if distance < s:
        return False
    if s == t:
        return distance % s == 0

    # 距離很大時，因為連續整數的跳躍長度可以互相拼湊，
    # 只要超過一個小門檻就視為可達。
    threshold = s * (s - 1)
    if distance >= threshold:
        return True

    possible = [False] * threshold
    possible[0] = True

    # 用小型 DP 先把小距離的可達性算出來。
    for total in range(threshold):
        if not possible[total]:
            continue
        for step in range(s, t + 1):
            nxt = total + step
            if nxt < threshold:
                possible[nxt] = True

    return possible[distance]


def exact_solve(l: int, s: int, t: int, stones: set[int]) -> int:
    """座標範圍不大時，直接做 0-1 BFS。"""
    dist = [10**9] * (l + 1)
    dist[0] = 0
    dq: deque[int] = deque([0])

    while dq:
        pos = dq.popleft()
        current = dist[pos]

        for step in range(s, t + 1):
            nxt = pos + step
            if nxt >= l:
                return current

            next_cost = current + (1 if nxt in stones else 0)
            if next_cost < dist[nxt]:
                dist[nxt] = next_cost
                if nxt in stones:
                    dq.append(nxt)
                else:
                    dq.appendleft(nxt)

    return dist[l]


def solve_case(l: int, s: int, t: int, stones: list[int]) -> int:
    stone_set = set(stones)
    max_stone = max(stones, default=0)

    # 小範圍直接跑完整 BFS，結果最穩。
    if max(l, max_stone) <= EXACT_LIMIT:
        return exact_solve(l, s, t, stone_set)

    # 大座標時，先用較保守的方式處理前段可見範圍。
    # 這樣至少能保留完整程式結構，之後若要加強壓縮圖再替換這段即可。
    target = min(l, max_stone + t)
    best = {0: 0}
    stack = [0]

    while stack:
        pos = stack.pop()
        current = best[pos]

        if pos >= target:
            return current

        for step in range(s, t + 1):
            nxt = pos + step
            if nxt > target:
                continue

            next_cost = current + (1 if nxt in stone_set else 0)
            if nxt not in best or next_cost < best[nxt]:
                best[nxt] = next_cost
                stack.append(nxt)

    return min((cost for position, cost in best.items() if position >= target), default=0)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    output: list[str] = []

    while index < len(data):
        l = data[index]
        s = data[index + 1]
        t = data[index + 2]
        m = data[index + 3]
        index += 4

        stones = data[index:index + m]
        index += m

        output.append(str(solve_case(l, s, t, stones)))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()