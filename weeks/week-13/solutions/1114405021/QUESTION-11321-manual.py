#!/usr/bin/env python3
import sys
from collections import deque

def check_block(N,M,blocked,x,y):
    if blocked.get((x,y), False):
        return False
    blocked[(x,y)]=True
    vis=set(); dq=deque()
    for i in range(N):
        if not blocked.get((i,0), False):
            vis.add((i,0)); dq.append((i,0))
    found=False
    while dq:
        i,j=dq.popleft()
        if j==M-1:
            found=True; break
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and (ni,nj) not in vis and not blocked.get((ni,nj), False):
                vis.add((ni,nj)); dq.append((ni,nj))
    del blocked[(x,y)]
    return not found

def main():
    a=list(map(int, sys.stdin.read().split()))
    if not a: return
    p=0
    N=a[p]; M=a[p+1]; T=a[p+2]; p+=3
    blocked={}
    res=[]
    for _ in range(T):
        x=a[p]; y=a[p+1]; p+=2
        if check_block(N,M,blocked,x,y):
            res.append(">_<")
        else:
            blocked[(x,y)] = True
            res.append("<(_ _)>")
    print('\n'.join(res))

if __name__=='__main__':
    main()
