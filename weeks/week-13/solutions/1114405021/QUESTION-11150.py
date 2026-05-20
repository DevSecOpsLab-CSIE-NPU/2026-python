#!/usr/bin/env python3
import sys
from collections import deque

def compress_positions(stones, L, T):
    pts = [0] + sorted(stones) + [L]
    new = [0]
    for i in range(1, len(pts)):
        gap = pts[i] - pts[i-1]
        new.append(new[-1] + min(gap, T))
    mapping = {}
    for i, p in enumerate(pts):
        mapping[p] = new[i]
    return mapping, new[-1]

def solve_one(L, S, T, stones):
    mapping, NL = compress_positions(stones, L, T)
    blocked = [0]*(NL+1)
    for s in stones:
        blocked[mapping[s]] = 1
    # goal is any position >= mapping[L]
    from collections import deque
    INF = 10**9
    dist = [INF]*(NL+1)
    dist[0] = 0
    dq = deque([0])
    while dq:
        u = dq.popleft()
        if u == mapping[L]:
            return dist[u]
        for step in range(S, T+1):
            v = u + step
            if v > NL:
                v = mapping[L]
            cost = blocked[v]
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if cost == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return dist[mapping[L]]

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    out = []
    while True:
        try:
            L = int(next(it))
        except StopIteration:
            break
        S = int(next(it)); T = int(next(it)); M = int(next(it))
        stones = [int(next(it)) for _ in range(M)]
        res = solve_one(L, S, T, stones)
        out.append(str(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
