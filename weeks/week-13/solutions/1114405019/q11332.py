import sys
import math

def get_dist(angle, x1, y1, x2, y2):
    sina, cosa = math.sin(angle), math.cos(angle)
    denom = (y2 - y1) * cosa - (x2 - x1) * sina
    if abs(denom) < 1e-9: return float('inf')
    r = (y2 * x1 - x2 * y1) / denom
    return r if r > 0 else float('inf')

def solve():
    data = sys.stdin.read().split()
    if not data: return
    idx = 0
    while idx < len(data):
        try:
            n = int(data[idx])
            idx += 1
        except: break
        mirrors, angles = [], []
        for i in range(n):
            x1, y1, x2, y2 = map(float, data[idx:idx+4])
            idx += 4
            a1, a2 = math.atan2(y1, x1), math.atan2(y2, x2)
            if a1 > a2: a1, a2 = a2, a1
            if a2 - a1 > math.pi:
                mirrors.append((a2, math.pi, x1, y1, x2, y2, i))
                mirrors.append((-math.pi, a1, x1, y1, x2, y2, i))
                angles.extend([a2, math.pi, -math.pi, a1])
            else:
                mirrors.append((a1, a2, x1, y1, x2, y2, i))
                angles.extend([a1, a2])
        angles = sorted(list(set(angles)))
        visible = [0] * n
        for i in range(len(angles) - 1):
            mid = (angles[i] + angles[i+1]) / 2
            min_r, best_id = float('inf'), -1
            for a_s, a_e, x1, y1, x2, y2, m_id in mirrors:
                if a_s <= mid <= a_e:
                    r = get_dist(mid, x1, y1, x2, y2)
                    if r < min_r:
                        min_r, best_id = r, m_id
            if best_id != -1: visible[best_id] = 1
        print(" ".join(map(str, visible)))

if __name__ == "__main__":
    solve()
