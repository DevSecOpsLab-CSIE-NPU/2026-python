import sys
import math

def main():
    data = iter(sys.stdin.read().split())
    for n_str in data:
        n = int(n_str)
        mirrors, angles = [], []
        for _ in range(n):
            sx, sy, ex, ey = float(next(data)), float(next(data)), float(next(data)), float(next(data))
            mirrors.append((sx, sy, ex, ey))
            angles.extend([math.atan2(sy, sx), math.atan2(ey, ex)])
            
        angles.sort()
        test_angles = []
        for i in range(len(angles)):
            test_angles.append(angles[i])
            diff = (angles[(i + 1) % len(angles)] - angles[i]) % (2 * math.pi)
            test_angles.append(angles[i] + diff / 2.0)
            
        ans = [0] * n
        for a in test_angles:
            dx, dy = math.cos(a), math.sin(a)
            best_t, best_i = float('inf'), -1
            for i, (sx, sy, ex, ey) in enumerate(mirrors):
                den = (ex - sx) * dy - (ey - sy) * dx
                if abs(den) < 1e-9: continue
                u = (sy * dx - sx * dy) / den
                if -1e-7 <= u <= 1 + 1e-7:
                    t = (sx + u * (ex - sx)) * dx + (sy + u * (ey - sy)) * dy
                    if 1e-7 < t < best_t:
                        best_t, best_i = t, i
        if best_i != -1: ans[best_i] = 1
        print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()