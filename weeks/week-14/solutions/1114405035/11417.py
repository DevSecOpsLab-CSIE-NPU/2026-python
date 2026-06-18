# -*- coding: utf-8 -*-
import sys
import math

def solve():
    """
    UVA 11417 — GCD 解題主程式
    """
    # 讀取所有的輸入 token
    tokens = sys.stdin.read().split()
    if not tokens:
        return
        
    for token in tokens:
        n = int(token)
        if n == 0:
            break
            
        g = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                g += math.gcd(i, j)
        print(g)

if __name__ == "__main__":
    solve()
