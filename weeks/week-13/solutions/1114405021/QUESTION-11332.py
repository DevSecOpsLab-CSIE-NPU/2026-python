#!/usr/bin/env python3
import sys
import math

def angle(p):
    return math.atan2(p[1], p[0])

def intersect_ray_segment(theta, s, e):
    # ray: t*(cos,sin), segment: s + u*(e-s)
    dx = e[0]-s[0]; dy = e[1]-s[1]
    cx = math.cos(theta); cy = math.sin(theta)
    denom = dx*cy - dy*cx
    if abs(denom) < 1e-12:
        return None
    t = (dx*s[1] - dy*s[0]) / denom
    u = (cx*s[1] - cy*s[0]) / denom
    if t > 0 and 0<=u<=1:
        return t
    return None

def visible_segments(segments):
    n = len(segments)
    res = [0]*n
    angles = []
    for i,(s,e) in enumerate(segments):
        a1 = angle(s); a2 = angle(e)
        # ensure interval small (choose midpoint correctly)
        mid = (a1 + a2) / 2.0
        angles.append(mid)
    for i,theta in enumerate(angles):
        s,e = segments[i]
        ti = intersect_ray_segment(theta, s, e)
        if ti is None:
            res[i]=0; continue
        visible = True
        for j,(sj,ej) in enumerate(segments):
            if j==i: continue
            tj = intersect_ray_segment(theta, sj, ej)
            if tj is not None and tj < ti - 1e-9:
                visible = False; break
        res[i] = 1 if visible else 0
    return res

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    p = 0
    out_lines = []
    while p < len(data):
        n = data[p]; p+=1
        segs = []
        for _ in range(n):
            sx = data[p]; sy = data[p+1]; ex = data[p+2]; ey = data[p+3]; p+=4
            segs.append(((sx,sy),(ex,ey)))
        vis = visible_segments(segs)
        out_lines.append(' '.join(str(x) for x in vis))
    print('\n'.join(out_lines))

if __name__ == '__main__':
    solve()
