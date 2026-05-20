#!/usr/bin/env python3
import sys
from collections import deque

def would_block(N,M,blocked, x,y):
    # temporarily block (x,y) and test connectivity from any left-col to any right-col
    if blocked.get((x,y), False):
        return False
    blocked[(x,y)] = True
    visited = set()
    dq = deque()
    for i in range(N):
        if not blocked.get((i,0), False):
            dq.append((i,0)); visited.add((i,0))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    can = False
    while dq:
        i,j = dq.popleft()
        if j == M-1:
            can = True
            break
        for di,dj in dirs:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and (ni,nj) not in visited and not blocked.get((ni,nj), False):
                visited.add((ni,nj))
                dq.append((ni,nj))
    # undo
    del blocked[(x,y)]
    return not can

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    N = next(it); M = next(it); T = next(it)
    blocked = {}
    out = []
    for _ in range(T):
        x = next(it); y = next(it)
        if would_block(N,M,blocked,x,y):
            out.append(">_<")
        else:
            blocked[(x,y)] = True
            out.append("<(_ _)>")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
