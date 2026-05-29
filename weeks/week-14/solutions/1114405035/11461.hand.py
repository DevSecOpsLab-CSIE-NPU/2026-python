# -*- coding: utf-8 -*-
"""
UVA 11461 - Square Numbers (標準結構化版本)

本程式用於計算閉區間 [a, b] 中完全平方數（Perfect Square）的個數。
題目規定：
1. 1 <= a <= b <= 100,000
2. 以 a = 0, b = 0 代表輸入結束。

時間複雜度：O(T)，其中 T 為測資行數（最多 201 行）。每次查詢利用數學公式，可在 O(1) 常數時間內直接算得結果，極度高效。
空間複雜度：O(1)，僅使用數個常數變數存儲數值。
"""

import sys
import math

def count_squares(a, b):
    """
    使用數學開根號公式，計算閉區間 [a, b] 內的完全平方數個數。
    
    完全平方數 x 的平方根為整數，即存在整數 k 滿足 a <= k^2 <= b。
    因此：
    - k 的最小值為 ceil(sqrt(a))
    - k 的最大值為 floor(sqrt(b))
    - 符合條件的 k 的數量為 floor(sqrt(b)) - ceil(sqrt(a)) + 1
    
    參數:
    a (int): 區間起點
    b (int): 區間終點
    
    回傳:
    int: 區間內完全平方數的個數，若無則回傳 0。
    """
    # 判斷是否為非法區間
    if a > b or a <= 0 or b <= 0:
        return 0
        
    # 計算平方根的上下界限
    lower_bound = math.ceil(math.sqrt(a))
    upper_bound = math.floor(math.sqrt(b))
    
    # 計算區間內底數的數量
    count = upper_bound - lower_bound + 1
    
    # 若計算結果小於 0（例如 a=17, b=24 時，lower=5, upper=4），回傳 0
    return max(0, count)

def solve():
    """
    讀取標準輸入，解析各組測資區間並計算結果，直到讀入 0 0 為止。
    """
    # 讀取標準輸入的所有行並過濾空白
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
        
    for line in input_lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # 以空白切分出 a 與 b
        parts = stripped.split()
        if len(parts) < 2:
            continue
            
        a = int(parts[0])
        b = int(parts[1])
        
        # 題目規範：當 a = 0 且 b = 0 時，結束輸入，不需處理
        if a == 0 and b == 0:
            break
            
        # 計算完全平方數個數並輸出
        ans = count_squares(a, b)
        print(ans)

if __name__ == "__main__":
    solve()
