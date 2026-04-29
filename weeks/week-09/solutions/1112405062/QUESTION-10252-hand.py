import sys
import math

def solve():
    lines = [l.strip() for l in sys.stdin if l.strip()]
    if not lines:
        return
    
    T = int(lines[0])
    idx = 1
    
    for _ in range(T):
        N = int(lines[idx])
        idx += 1
        
        pts = []
        for _ in range(N):
            x, y = map(int, lines[idx].split())
            idx += 1
            pts.append((x, y))
        
        best, cnt = find_min(pts)
        print(best, cnt)

def find_min(pts):
    N = len(pts)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    
    # 搜索範圍
    sx, ex = min(xs) - 5, max(xs) + 5
    sy, ey = min(ys) - 5, max(ys) + 5
    
    def dsum(px, py):
        return sum(math.hypot(px - x, py - y) for x, y in pts)
    
    # 找最小
    best = float('inf')
    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            best = min(best, dsum(x, y))
    
    best = int(best + 0.5)
    
    # 數個數
    cnt = sum(1 for x in range(sx, ex + 1) for y in range(sy, ey + 1) 
            if int(dsum(x, y) + 0.5) == best)
    
    return best, cnt

if __name__ == "__main__":
    solve()