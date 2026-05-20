import sys

def solve():
    # 1. 一口氣讀完所有輸入，不用管換行或空白
    data = sys.stdin.read().split()
    if not data: return
    
    n = int(data[0])
    total_pixels = n * n
    sum_y = 0.0
    
    # 2. 利用 iterator (迭代器)，每次呼叫 next 就能拿取下一個數字
    inputs = iter(data[1:])
    
    for _ in range(total_pixels):
        # 每次自動抓取 3 個數字，簡單又好記
        r = float(next(inputs))
        g = float(next(inputs))
        b = float(next(inputs))
        
        # 3. 公式排排站（這樣寫比原本好背、好對齊多了）
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        
        sum_y += y
        print(f"{x:.4f} {y:.4f} {z:.4f}")
        
    # 4. 算出平均並輸出
    print(f"The average of Y is {sum_y / total_pixels:.4f}")

if __name__ == "__main__":
    solve()