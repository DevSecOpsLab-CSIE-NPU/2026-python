# -*- coding: utf-8 -*-
import sys
import math

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    while idx < len(data):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        
        if a == 0 and b == 0:
            break
            
        # 使用 math.isqrt 計算
        l = math.isqrt(a - 1) + 1
        r = math.isqrt(b)
        print(max(0, r - l + 1))

if __name__ == "__main__":
    solve()
