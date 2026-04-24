# -*- coding: utf-8 -*-
# 這是 UVA 10193 的簡易好記版 (Easy Version)
import sys
import math

def solve(a):
    """
    簡易好記秘訣：【公式推導 + 因數分解】
    1. 題目公式可推導成 (b-a)(c-a) = a^2 + 1。
    2. 目標是讓 b+c 最小，等同於讓 (b-a) + (c-a) 最小。
    3. 兩個數相乘為定值 (a^2+1)，要讓它們相加最小，這兩個數必須最接近。
    4. 所以我們只要找 a^2+1 最接近平方根的兩個因數 x, y 即可。
    5. 答案就是 2a + x + y。
    """
    N = a * a + 1
    
    # 從 sqrt(N) 開始往下找，第一個找到的因數 x，
    # 就是離 sqrt(N) 最近的，這樣 x 和 y = N/x 的差距最小。
    for x in range(math.isqrt(N), 0, -1):
        if N % x == 0:
            y = N // x
            # b+c = (b-a) + (c-a) + 2a = x + y + 2a
            return 2 * a + x + y
            
    return -1 

if __name__ == '__main__':
    for line in sys.stdin:
        if line.strip():
            print(solve(int(line.strip())))