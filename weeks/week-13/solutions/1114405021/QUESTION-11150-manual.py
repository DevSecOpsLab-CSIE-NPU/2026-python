#!/usr/bin/env python3
import sys
from collections import deque

def solve_case(L,S,T,stones):
    pts = [0] + sorted(stones) + [L]
    newp = [0]
    for i in range(1, len(pts)):
        gap = pts[i]-pts[i-1]
        newp.append(newp[-1] + min(gap, T))
    mp = {pts[i]: newp[i] for i in range(len(pts))}
    goal = mp[L]
    blocked = [0]*(goal+1)
    for s in stones:
        blocked[mp[s]] = 1
    INF=10**9
    dist=[INF]*(goal+1)
    dist[0]=0
    dq=deque([0])
    while dq:
        u=dq.popleft()
        if u==goal: break
        for step in range(S, T+1):
            v = u+step
            if v>goal: v=goal
            c = blocked[v]
            nd = dist[u]+c
            if nd<dist[v]:
                dist[v]=nd
                if c==0: dq.appendleft(v)
                else: dq.append(v)
    return dist[goal]

def main():
    a=list(map(int, sys.stdin.read().split()))
    if not a: return
    p=0
    res=[]
    while p<len(a):
        L=a[p]; S=a[p+1]; T=a[p+2]; M=a[p+3]; p+=4
        stones=a[p:p+M]; p+=M
        res.append(str(solve_case(L,S,T,stones)))
    print('\n'.join(res))

if __name__=='__main__':
    main()
