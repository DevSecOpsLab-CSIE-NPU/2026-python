import math
import sys

def intersect_ray_segment(angle, seg):
    sx, sy, ex, ey = seg
    dx = ex - sx; dy = ey - sy
    cx = math.cos(angle); cy = math.sin(angle)
    denom = cx*dy - dx*cy
    if abs(denom) < 1e-12:
        t1 = sx*cx + sy*cy
        t2 = ex*cx + ey*cy
        cand = [t for t in (t1,t2) if t>=0]
        return min(cand) if cand else None
    u = (sx*cy - cx*sy) / denom
    t = (sx*dy - dx*sy) / denom
    if 0<=u<=1 and t>=0:
        return t
    return None

def solve():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    out_lines = []
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        segs = [tuple(int(next(it)) for _ in range(4)) for _ in range(n)]
        vis = [0]*n
        for i,(sx,sy,ex,ey) in enumerate(segs):
            a1 = math.atan2(sy, sx); a2 = math.atan2(ey, ex)
            diff = a2 - a1
            if diff <= -math.pi: diff += 2*math.pi
            elif diff > math.pi: diff -= 2*math.pi
            mid = a1 + diff/2
            if mid > math.pi: mid -= 2*math.pi
            if mid <= -math.pi: mid += 2*math.pi

            best_t = None; best_idx = None
            for j,s2 in enumerate(segs):
                t = intersect_ray_segment(mid, s2)
                if t is not None and (best_t is None or t < best_t):
                    best_t = t; best_idx = j
            if best_idx == i:
                vis[i] = 1
        out_lines.append(''.join(map(str,vis)))
    print('\n'.join(out_lines))

if __name__ == '__main__':
    solve()
    