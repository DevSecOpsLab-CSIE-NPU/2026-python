# -*- coding: utf-8 -*-
import sys
import math

def solve(a):
    """
    計算滿足 arctan(1/a) = arctan(1/b) + arctan(1/c) 時，b+c 的最小值。
    
    推導過程：
    (b-a)(c-a) = a^2 + 1
    令 x = b-a, y = c-a，則 x*y = a^2 + 1
    目標是最小化 b+c = 2a + x + y。
    要使 x+y 最小，x 和 y 必須是 a^2+1 的所有因數中最接近的一對。
    """
    N = a * a + 1
    
    # 從 sqrt(N) 向下尋找，找到的第一個因數對就是差距最小的
    limit = math.isqrt(N)
    for x in range(limit, 0, -1):
        if N % x == 0:
            y = N // x
            return 2 * a + x + y
            
    return -1

if __name__ == '__main__':
    # 處理標準輸入
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a = int(line)
        print(solve(a))