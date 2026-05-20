#!/usr/bin/env python3
# 含繁體中文註解的簡易版（使用取樣角度檢查能見度，O(n^2)）
import sys, math

def ang(p):
    return math.atan2(p[1], p[0])

def ray_int(theta, s, e):
    dx = e[0]-s[0]; dy = e[1]-s[1]
    cx = math.cos(theta); cy = math.sin(theta)
    denom = dx*cy - dy*cx
    if abs(denom) < 1e-12: return None
    t = (dx*s[1] - dy*s[0]) / denom
    u = (cx*s[1] - cy*s[0]) / denom
    if t>0 and 0<=u<=1: return t
    return None

def main():
    vals = list(map(int, sys.stdin.read().split()))
    if not vals: return
    p=0
    outputs=[]
    while p < len(vals):
        n = vals[p]; p+=1
        segs=[]
        for _ in range(n):
            sx,sy,ex,ey = vals[p],vals[p+1],vals[p+2],vals[p+3]; p+=4
            segs.append(((sx,sy),(ex,ey)))
        res=[]
        for i,(s,e) in enumerate(segs):
            mid = (ang(s)+ang(e))/2.0
            ti = ray_int(mid, s, e)
            if ti is None:
                res.append(0); continue
            vis = True
            for j,(s2,e2) in enumerate(segs):
                if j==i: continue
                tj = ray_int(mid, s2, e2)
                if tj is not None and tj < ti - 1e-9:
                    vis=False; break
            res.append(1 if vis else 0)
        outputs.append(' '.join(map(str,res)))
    print('\n'.join(outputs))

if __name__=='__main__':
    main()
