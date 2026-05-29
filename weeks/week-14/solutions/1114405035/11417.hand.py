# -*- coding: utf-8 -*-
"""
UVA 11417 - GCD (標準結構化版本)

本程式用於計算給定正整數 N 時，所有滿足 1 <= i < j <= N 的整數對的最大公因數 (GCD) 的總和 G：
G = sum_{i=1}^{N-1} sum_{j=i+1}^{N} gcd(i, j)

時間複雜度：O(T * N^2 * log(N))，其中 T 為輸入個數，N <= 500。由於 N 較小，此複雜度可在極短時間內（< 0.1 秒）計算完成。
空間複雜度：O(1)，僅需要常數個變數進行迴圈與加總。
"""

import sys

def gcd(a, b):
    """
    使用輾轉相除法（Euclidean algorithm）計算 a 與 b 的最大公因數。
    
    參數:
    a (int): 第一個整數
    b (int): 第二個整數
    
    回傳:
    int: a 與 b 的最大公因數
    """
    while b:
        a, b = b, a % b
    return a

def compute_gcd_sum(n):
    """
    計算從 1 到 N 之間所有二元對 (i, j) 滿足 i < j 的最大公因數之和。
    
    參數:
    n (int): 目標正整數 N
    
    回傳:
    int: GCD 總和 G
    """
    g_sum = 0
    # 外層迴圈 i 從 1 遍歷到 N-1
    for i in range(1, n):
        # 內層迴圈 j 從 i+1 遍歷到 N
        for j in range(i + 1, n + 1):
            g_sum += gcd(i, j)
    return g_sum

def solve():
    """
    自標準輸入讀取資料，處理多組測資，直到讀入 N = 0 時結束。
    """
    # 讀取標準輸入中的所有行，並過濾掉首尾空白
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return

    for line in input_lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue
            
        n = int(stripped_line)
        # 題目規範：當 N = 0 時，結束輸入，不需進行處理
        if n == 0:
            break
            
        # 計算總和並印出
        result = compute_gcd_sum(n)
        print(result)

if __name__ == "__main__":
    solve()
