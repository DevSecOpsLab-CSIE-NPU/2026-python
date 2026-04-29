def solve_10252_easy():
    import sys
    import math
    lines = sys.stdin.read().split()
    if not lines: return
    
    T = int(lines[0])
    idx = 1
    
    for _ in range(T):
        n = int(lines[idx])
        idx += 1
        
        points = []
        for _ in range(n):
            x = float(lines[idx])
            y = float(lines[idx+1])
            points.append((x, y))
            idx += 2
            
        # Weiszfeld's algorithm for Geometric Median
        # 初始猜測點 (質心)
        guess_x = sum(p[0] for p in points) / n
        guess_y = sum(p[1] for p in points) / n
        
        for _ in range(100): # 固定迭代次數通常即能收斂
            num_x, num_y, den = 0.0, 0.0, 0.0
            for x, y in points:
                dist = math.hypot(x - guess_x, y - guess_y)
                if dist > 1e-8:
                    num_x += x / dist
                    num_y += y / dist
                    den += 1.0 / dist
            if den == 0: break
            guess_x, guess_y = num_x / den, num_y / den
            
        ans = sum(math.hypot(x - guess_x, y - guess_y) for x, y in points)
        print(int(round(ans)), 1)

if __name__ == '__main__':
    solve_10252_easy()