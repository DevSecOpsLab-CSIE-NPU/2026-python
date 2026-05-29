# -*- coding: utf-8 -*-
"""
11417 GCD —— 簡單易記版

核心邏輯：
1. 使用 Python 內建的 `math.gcd`，免去自行撰寫最大公因數函式的麻煩。
2. 利用 Python 強大的生成式（Generator Expression），以單行直接完成雙層迴圈的相加。
3. 簡化 I/O：一次性讀取所有整數，並依序處理至 0 結束。極度適合 CPE 考試時快速填寫。

時間複雜度：O(T * N^2 * log(N))，底層使用 C 語言優化的 math.gcd，速度極快。
空間複雜度：O(1)，無額外陣列儲存。
"""

import sys
import math

def solve():
    # 將輸入依空白/換行切分並轉換為整數列表
    inputs = [int(x) for x in sys.stdin.read().split()]
    
    for n in inputs:
        # 遇到 0 即停止處理
        if n == 0:
            break
            
        # 使用生成式一行完成：G = sum_{i=1..n-1} sum_{j=i+1..n} gcd(i, j)
        # 這行語法非常直覺、不易寫錯，且極好記憶！
        g_sum = sum(math.gcd(i, j) for i in range(1, n) for j in range(i + 1, n + 1))
        
        print(g_sum)

if __name__ == "__main__":
    solve()
