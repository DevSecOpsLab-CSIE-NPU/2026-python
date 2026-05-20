from __future__ import annotations

from collections import deque
import sys


LIMIT = 200_000


def make_ok(d: int, s: int, t: int) -> bool:
    if d < s:
        return False
    if s == t:
        return d % s == 0
    if d >= s * (s - 1):
        return True

    ok = [False] * (s * (s - 1))
    ok[0] = True
    for x in range(len(ok)):
        if not ok[x]:
            continue
        for y in range(s, t + 1):
            z = x + y
            if z < len(ok):
                ok[z] = True
    return ok[d]


def exact(l: int, s: int, t: int, st: set[int]) -> int:
    dis = [10**9] * (l + 1)
    dis[0] = 0
    q: deque[int] = deque([0])

    while q:
        p = q.popleft()
        cur = dis[p]
        for step in range(s, t + 1):
            np = p + step
            if np >= l:
                return cur
            nc = cur + (1 if np in st else 0)
            if nc < dis[np]:
                dis[np] = nc
                if np in st:
                    q.append(np)
                else:
                    q.appendleft(np)

    return dis[l]


def solve_one(l: int, s: int, t: int, stones: list[int]) -> int:
    st = set(stones)
    mx = max(stones, default=0)

    if max(l, mx) <= LIMIT:
        return exact(l, s, t, st)

    top = min(l, mx + t)
    best = {0: 0}
    stack = [0]

    while stack:
        p = stack.pop()
        cur = best[p]
        if p >= top:
            return cur
        for step in range(s, t + 1):
            np = p + step
            if np > top:
                continue
            nc = cur + (1 if np in st else 0)
            if np not in best or nc < best[np]:
                best[np] = nc
                stack.append(np)

    return min((v for k, v in best.items() if k >= top), default=0)


def main() -> None:
    a = list(map(int, sys.stdin.buffer.read().split()))
    if not a:
        return

    p = 0
    out: list[str] = []

    while p < len(a):
        l, s, t, m = a[p:p + 4]
        p += 4
        stones = a[p:p + m]
        p += m
        out.append(str(solve_one(l, s, t, stones)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()