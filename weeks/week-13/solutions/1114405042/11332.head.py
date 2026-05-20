import sys
import math

def solve():
    data = sys.stdin.read().split()
    if not data: return
    idx = 0
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        segments, rays = [], []
        for _ in range(n):
            sx, sy, ex, ey = map(float, data[idx:idx+4])
            idx += 4
            segments.append((sx, sy, ex, ey))
            ang1, ang2 = math.atan2(sy, sx), math.atan2(ey, ex)
            eps = 1e-9
            rays.extend([ang1, ang1+eps, ang1-eps, ang2, ang2+eps, ang2-eps])
            
        vis = [0] * n
        for ang in rays:
            dx, dy = math.cos(ang), math.sin(ang)
            min_t, cid = float('inf'), -1
            for i, (sx, sy, ex, ey) in enumerate(segments):
                A, B, C, D = dx, -(ex - sx), dy, -(ey - sy)
                det = A * D - B * C
                if abs(det) < 1e-9: continue
                t = (sx * D - sy * B) / det
                u = (A * sy - C * sx) / det
                if t > 1e-9 and -1e-9 <= u <= 1 + 1e-9:
                    if t < min_t: min_t, cid = t, i
            if cid != -1: vis[cid] = 1
        print(*(vis))

if __name__ == '__main__':
    solve()
