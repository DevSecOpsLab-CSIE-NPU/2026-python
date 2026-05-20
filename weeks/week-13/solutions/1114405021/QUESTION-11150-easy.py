#!/usr/bin/env python3
# 簡易版與繁中註解
import sys
from collections import deque

def compress(stones, L, T):
    pts = [0] + sorted(stones) + [L]
    newpos = [0]
    for i in range(1, len(pts)):
        gap = pts[i] - pts[i-1]
        newpos.append(newpos[-1] + min(gap, T))
    mp = {pts[i]: newpos[i] for i in range(len(pts))}
    return mp, newpos[-1]

def main():
    vals = list(map(int, sys.stdin.read().split()))
    if not vals:
        return
    p = 0
    out = []
    while p < len(vals):
        L = vals[p]; p+=1
        S = vals[p]; T = vals[p+1]; M = vals[p+2]; p+=3
        stones = vals[p:p+M]; p+=M
        mp, NL = compress(stones, L, T)
        blocked = [0]*(NL+1)
        for s in stones:
            blocked[mp[s]] = 1
        INF = 10**9
        dist = [INF]*(NL+1)
        dist[0] = 0
        dq = deque([0])
        goal = mp[L]
        while dq:
            u = dq.popleft()
            if u == goal:
                break
            for d in range(S, T+1):
                v = u + d
                if v > NL:
                    v = goal
                c = blocked[v]
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
                    if c == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)
        out.append(str(dist[goal]))
    print("\n".join(out))

if __name__ == '__main__':
    main()
