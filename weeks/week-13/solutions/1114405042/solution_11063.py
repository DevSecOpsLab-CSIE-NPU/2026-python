import os
import math

def solve():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    idx = 1
    
    total_y = 0.0
    pixels_count = n * n
    
    for _ in range(pixels_count):
        if idx >= len(input_data): break
        r = int(input_data[idx])
        g = int(input_data[idx+1])
        b = int(input_data[idx+2])
        idx += 3
        
        # 根據公式計算 X, Y, Z
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        
        total_y += y
        
        # 輸出到小數點後第 4 位
        print(f"{x:.4f} {y:.4f} {z:.4f}")
        
    avg_y = total_y / pixels_count
    print(f"The average of Y is {avg_y:.4f}")

if __name__ == '__main__':
    solve()
