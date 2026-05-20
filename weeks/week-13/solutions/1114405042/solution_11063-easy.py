# 題目 11063: RGB 轉 XYZ (簡易版)

def solve():
    # 讀取全部輸入
    import sys
    data = sys.stdin.read().split()
    if not data: return
    
    n = int(data[0])
    total_y = 0
    
    # 每次取 3 個數字 (R, G, B)
    idx = 1
    for _ in range(n * n):
        r, g, b = float(data[idx]), float(data[idx+1]), float(data[idx+2])
        idx += 3
        
        # 代入公式
        x = 0.5149*r + 0.3244*g + 0.1607*b
        y = 0.2654*r + 0.6704*g + 0.0642*b
        z = 0.0248*r + 0.1248*g + 0.8504*b
        
        total_y += y
        
        # 輸出結果
        print(f"{x:.4f} {y:.4f} {z:.4f}")
        
    # 輸出平均值
    print(f"The average of Y is {total_y / (n * n):.4f}")

if __name__ == '__main__':
    solve()
