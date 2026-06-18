# -*- coding: utf-8 -*-
import sys

def solve():
    """
    UVA 11063 - RGB 轉 XYZ 色彩轉換解題主程式
    """
    # 讀取所有的輸入 token
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    idx = 0
    while idx < len(tokens):
        # 讀取影像大小 n
        n = int(tokens[idx])
        idx += 1
        
        total_pixels = n * n
        sum_y = 0.0
        
        # 依序讀取每個像素的 RGB 值並轉換
        for _ in range(total_pixels):
            r = int(tokens[idx])
            g = int(tokens[idx+1])
            b = int(tokens[idx+2])
            idx += 3
            
            x = 0.5149 * r + 0.3244 * g + 0.1607 * b
            y = 0.2654 * r + 0.6704 * g + 0.0642 * b
            z = 0.0248 * r + 0.1248 * g + 0.8504 * b
            
            sum_y += y
            
            print(f"{x:.4f} {y:.4f} {z:.4f}")
            
        # 計算影像平均亮度 Y
        avg_y = sum_y / total_pixels
        print(f"The average of Y is {avg_y:.4f}")

if __name__ == "__main__":
    solve()
