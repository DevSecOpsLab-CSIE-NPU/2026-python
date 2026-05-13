#!/usr/bin/env python3
# 手打版本（簡短、少註解）
import sys
p=sys.stdin.read().split()
if not p: sys.exit()
t=int(p[0]);k=1
out=[]
for _ in range(t):
    S=int(p[k]);D=int(p[k+1]);k+=2
    if S<D or (S+D)%2!=0:
        out.append('impossible')
    else:
        a=(S+D)//2;b=(S-D)//2
        out.append(f"{a} {b}" if b>=0 else 'impossible')
print('\n'.join(out))
