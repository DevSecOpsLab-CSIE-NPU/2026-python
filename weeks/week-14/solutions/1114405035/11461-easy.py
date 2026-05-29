# -*- coding: utf-8 -*-
"""
11461 完全平方數 —— 簡單易記版

核心邏輯：
1. 區間 [a, b] 內完全平方數數量，即為平方根底數的範圍。
2. 數學公式：floor(sqrt(b)) - ceil(sqrt(a)) + 1。
3. 簡化 I/O：使用 sys.stdin.read().split() 讀入所有整數，並以步長為 2 的迴圈成對處理，極其簡短且完美防呆。

時間複雜度：O(T)，數學計算為常數時間。
空間複雜度：O(T)，儲存所有輸入元素。
"""

import sys
import math

def solve():
    # 將標準輸入中所有空白切分出的資料轉為整數列表
    data = [int(x) for x in sys.stdin.read().split()]
    
    # 每兩個數字為一組 (a, b) 進行處理
    for idx in range(0, len(data), 2):
        a = data[idx]
        b = data[idx + 1]
        
        # 遇到 0 0 即結束程式
        if a == 0 and b == 0:
            break
            
        # O(1) 數學精簡算法：底數上限減下界 + 1
        ans = math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
        
        # 防止 ans 為負數（例如區間內沒有完全平方數時）
        print(max(0, ans))

if __name__ == "__main__":
    solve()
