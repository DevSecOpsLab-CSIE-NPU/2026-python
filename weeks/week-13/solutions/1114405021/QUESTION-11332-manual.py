#!/usr/bin/env python3
import sys, math

def angle(p): return math.atan2(p[1], p[0])

def intersect(theta, s, e):
    dx=e[0]-s[0]; dy=e[1]-s[1]
    cx=math.cos(theta); cy=math.sin(theta)
    denom = dx*cy - dy*cx
    if abs(denom)<1e-12: return None
    t=(dx*s[1]-dy*s[0])/denom
    u=(cx*s[1]-cy*s[0])/denom
    if t>0 and 0<=u<=1: return t
    return None

def main():
    a=list(map(int, sys.stdin.read().split()))
    if not a: return
    p=0; out=[]
    while p<len(a):
        n=a[p]; p+=1
        segs=[]
        for _ in range(n):
            sx,sy,ex,ey = a[p],a[p+1],a[p+2],a[p+3]; p+=4
            segs.append(((sx,sy),(ex,ey)))
        ans=[]
        for i,(s,e) in enumerate(segs):
            th = (angle(s)+angle(e))/2.0
            ti = intersect(th, s, e)
            if ti is None:
                ans.append(0); continue
            ok=True
            for j,(s2,e2) in enumerate(segs):
                if j==i: continue
                tj = intersect(th,s2,e2)
                if tj is not None and tj<ti-1e-9:
                    ok=False; break
            ans.append(1 if ok else 0)
        out.append(' '.join(map(str,ans)))
    print('\n'.join(out))

if __name__=='__main__':
    main()
