# -*- coding: utf-8 -*-
"""
11349 對稱矩陣 (Symmetric Matrix) —— 簡單易記版

核心邏輯：
1. 本題最關鍵的陷阱為「元素必須為非負數 (>= 0)」，很多對稱矩陣題目沒有這項要求。
2. 對稱中心點的映射關係是 M[i][j] == M[n - 1 - i][n - 1 - j]。
3. 採用單一 solve() 函式，直接逐行讀取、解析維度 N 並動態判斷，適合 CPE 考試時快速寫出。

時間複雜度：O(T * N^2)，兩層迴圈完整掃描。
空間複雜度：O(N^2)，用於儲存單次測資的矩陣。
"""

import sys

def solve():
    # 讀取標準輸入的所有行
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
        
    # 第一行為測試資料組數 T
    t = int(lines[0].strip())
    idx = 1  # 指向當前要讀取的行數
    
    for case in range(1, t + 1):
        # 讀取 "N = n" 這行，利用等號切割取出矩陣維度 n
        n = int(lines[idx].split("=")[-1].strip())
        idx += 1
        
        # 讀取接下來的 n 行，轉換成二維整數陣列
        matrix = []
        for _ in range(n):
            row = [int(x) for x in lines[idx].split()]
            matrix.append(row)
            idx += 1
            
        # 預設為對稱矩陣，開始雙層迴圈檢查
        is_symmetric = True
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                opp_val = matrix[n - 1 - i][n - 1 - j]  # 中心對稱位置的值
                
                # 判定條件：若值小於零，或者不等於其中心對稱位置的值，即非對稱
                if val < 0 or val != opp_val:
                    is_symmetric = False
                    break
            if not is_symmetric:
                break
                
        # 印出符合題目規範的格式
        if is_symmetric:
            print(f"Test #{case}: Symmetric.")
        else:
            print(f"Test #{case}: Non-symmetric.")

if __name__ == "__main__":
    solve()
