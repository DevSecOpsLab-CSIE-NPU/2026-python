# -*- coding: utf-8 -*-
import sys
import math

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        
        segs, angles = [], []
        for i in range(n):
            x1, y1 = float(data[idx]), float(data[idx+1])
            x2, y2 = float(data[idx+2]), float(data[idx+3])
            idx += 4
            
            t1, t2 = math.atan2(y1, x1), math.atan2(y2, x2)
            if t1 > t2:
                t1, t2 = t2, t1
                x1, y1, x2, y2 = x2, y2, x1, y1
            segs.append(((x1, y1), (x2, y2), t1, t2, i))
            angles.extend([t1, t2])
            
        if n == 1:
            print("1")
            continue
            
        angles = sorted(list(set(angles)))
        visible = [0] * n
        
        # 產生極角區間中點
        mids = []
        for i in range(len(angles) - 1):
            mids.append((angles[i] + angles[i+1]) / 2)
        mids.append((angles[-1] + angles[0] + 2 * math.pi) / 2)
        
        for alpha in mids:
            cos_a, sin_a = math.cos(alpha), math.sin(alpha)
            
            # 標準化角度
            norm = alpha
            while norm > math.pi: norm -= 2 * math.pi
            while norm < -math.pi: norm += 2 * math.pi
            
            best_id, min_d = -1, float('inf')
            for (A, B, t1, t2, fid) in segs:
                in_span = (t1 <= norm <= t2) if (t2 - t1 <= math.pi) else (norm >= t2 or norm <= t1)
                if in_span:
                    ax, ay = A
                    bx, by = B
                    cr_A = cos_a * ay - sin_a * ax
                    cr_B = cos_a * by - sin_a * bx
                    denom = cr_A - cr_B
                    if abs(denom) > 1e-11:
                        u = cr_A / denom
                        ix, iy = ax + u * (bx - ax), ay + u * (by - ay)
                        d = ix * ix + iy * iy
                        if d < min_d:
                            min_d, best_id = d, fid
            if best_id != -1:
                visible[best_id] = 1
                
        print(" ".join(map(str, visible)))

if __name__ == "__main__":
    solve()
