#!/usr/bin/env python3
# 手打版本
import sys
p=sys.stdin.read().split()
if not p: sys.exit()
t=int(p[0]);idx=1
out=[]
for _ in range(t):
    M=int(p[idx]);N=int(p[idx+1]);Q=int(p[idx+2]);idx+=3
    grid=[]
    for _ in range(M):
        grid.append(list(p[idx])); idx+=1
    out.append(f"{M} {N} {Q}")
    for _ in range(Q):
        r=int(p[idx]);c=int(p[idx+1]);idx+=2
        ch=grid[r][c]
        k=0
        while True:
            if r-k<0 or r+k>=M or c-k<0 or c+k>=N:
                break
            ok=True
            for i in range(r-k,r+k+1):
                for j in range(c-k,c+k+1):
                    if grid[i][j]!=ch:
                        ok=False;break
                if not ok:break
            if not ok:break
            k+=1
        side=2*(k-1)+1 if k>0 else 1
        out.append(str(side))
print('\n'.join(out))
