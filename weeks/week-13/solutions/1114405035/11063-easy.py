# -*- coding: utf-8 -*-
import sys

def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    idx = 0
    while idx < len(tokens):
        n = int(tokens[idx])
        idx += 1
        
        total = n * n
        sum_y = 0.0
        
        for _ in range(total):
            r, g, b = map(int, tokens[idx : idx + 3])
            idx += 3
            
            x = 0.5149 * r + 0.3244 * g + 0.1607 * b
            y = 0.2654 * r + 0.6704 * g + 0.0642 * b
            z = 0.0248 * r + 0.1248 * g + 0.8504 * b
            
            sum_y += y
            print(f"{x:.4f} {y:.4f} {z:.4f}")
            
        print(f"The average of Y is {sum_y / total:.4f}")

if __name__ == "__main__":
    solve()
