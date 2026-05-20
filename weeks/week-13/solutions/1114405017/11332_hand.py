import sys
import math
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    while True:
        try:
            n = int(next(iterator))
        except StopIteration:
            break
        segments = []
        angles = set() 
        for i in range(n):
            sx, sy, ex, ey = [int(next(iterator)) for _ in range(4)]
            segments.append((sx, sy, ex, ey, i))
            angles.add(math.atan2(sy, sx))
            angles.add(math.atan2(ey, ex))
        sorted_angles = sorted(list(angles))
        mid_angles = []
        for i in range(len(sorted_angles) - 1):
            mid_angles.append((sorted_angles[i] + sorted_angles[i+1]) / 2)
        mid_angles.append((sorted_angles[-1] + sorted_angles[0] + 2 * math.pi) / 2)
        visible = [0] * n
        def get_distance(ang, x1, y1, x2, y2):
            rx, ry = math.cos(ang), math.sin(ang)
            dx, dy = x2 - x1, y2 - y1
            denom = rx * dy - ry * dx
            if abs(denom) < 1e-9: 
                return float('inf')
            t = (x1 * dy - y1 * dx) / denom
            u = (x1 * ry - y1 * rx) / denom
            if t > 0 and 0 <= u <= 1:
                return t
            return float('inf')
        for ang in mid_angles:
            min_dist = float('inf')
            closest_idx = -1
            for sx, sy, ex, ey, idx in segments:
                dist = get_distance(ang, sx, sy, ex, ey)
                if dist < min_dist:
                    min_dist = dist
                    closest_idx = idx
            if closest_idx != -1:
                visible[closest_idx] = 1
        print(" ".join(map(str, visible)))
if __name__ == '__main__':
    solve()