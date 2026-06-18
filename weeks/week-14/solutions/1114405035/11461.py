# -*- coding: utf-8 -*-
import sys
import math

def solve():
    """
    UVA 11461 — Square Numbers 解題主程式
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        idx += 2
        
        if a == 0 and b == 0:
            break
            
        # 使用 integer square root (isqrt) 避免浮點數誤差
        # [a, b] 區間內的完全平方數數量等同於
        # 平方根為整數且在 [ceil(sqrt(a)), floor(sqrt(b))] 之間。
        # 在整數運算中：
        # floor(sqrt(b)) 等於 isqrt(b)
        # ceil(sqrt(a)) 等於 isqrt(a - 1) + 1
        max_root = math.isqrt(b)
        min_root = math.isqrt(a - 1) + 1
        
        if min_root <= max_root:
            print(max_root - min_root + 1)
        else:
            print(0)

if __name__ == "__main__":
    solve()
