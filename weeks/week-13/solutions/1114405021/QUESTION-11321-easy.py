#!/usr/bin/env python3
# 簡易版含繁中註解
import sys
from collections import deque

def can_still_reach(N,M,blocked):
    # 從左邊任一格開始，是否能到達右邊任一格
    vis=set(); dq=deque()
    for i in range(N):
        if not blocked.get((i,0), False):
            vis.add((i,0)); dq.append((i,0))
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    while dq:
        i,j=dq.popleft()
        if j==M-1: return True
        for di,dj in dirs:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and (ni,nj) not in vis and not blocked.get((ni,nj), False):
                vis.add((ni,nj)); dq.append((ni,nj))
    return False

def main():
    a=list(map(int, sys.stdin.read().split()))
    if not a: return
    p=0
    N=a[p]; M=a[p+1]; T=a[p+2]; p+=3
    blocked={}
    out=[]
    for _ in range(T):
        x=a[p]; y=a[p+1]; p+=2
        if blocked.get((x,y), False):
            out.append(">_<")
            continue
        blocked[(x,y)] = True
        if can_still_reach(N,M,blocked):
            out.append("<(_ _)>")
        else:
            del blocked[(x,y)]
            out.append(">_<")
    print('\n'.join(out))

if __name__=='__main__':
    main()
