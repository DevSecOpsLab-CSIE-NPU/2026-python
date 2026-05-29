# -*- coding: utf-8 -*-
"""
UVA 11349 - Symmetric Matrix (標準結構化版本)

本程式用於判斷一個 n x n 的方陣是否為「對稱矩陣」。
題目對「對稱矩陣」的定義如下：
1. 矩陣中所有的元素都必須是「非負數」（即大於或等於 0）。
2. 矩陣必須關於「中心點對稱」，也就是對任意的索引 i, j，皆滿足：
   M[i][j] == M[n - 1 - i][n - 1 - j] (以 0 為基底的索引系統表示)

時間複雜度：O(T * N^2)，其中 T 為測資組數，N 為矩陣維度。每個元素最多被檢查常數次。
空間複雜度：O(N^2)，用於儲存 N x N 的矩陣元素。
"""

import sys

def is_symmetric(matrix, n):
    """
    判斷給定的 n x n 矩陣是否為對稱矩陣。
    
    參數:
    matrix (list of list of int): 二維陣列表示的方陣
    n (int): 矩陣的維度 (n x n)
    
    回傳:
    bool: 若符合對稱矩陣定義（無負數且中心點對稱）回傳 True，否則回傳 False。
    """
    # 步驟 1: 檢查是否有任何元素為負數
    # 這是本題最常見的陷阱之一（元素範圍可能包含負數）
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                return False

    # 步驟 2: 檢查中心對稱性
    # 比對 M[i][j] 與 M[n - 1 - i][n - 1 - j] 是否相等
    # 我們只需要比對前半段的元素，即可完成完整驗證
    for i in range(n):
        for j in range(n):
            # 計算對稱位置的索引
            opp_i = n - 1 - i
            opp_j = n - 1 - j
            
            # 若對稱位置的數值不相等，則非對稱矩陣
            if matrix[i][j] != matrix[opp_i][opp_j]:
                return False
                
    return True

def solve():
    """
    讀取標準輸入，解析測資並輸出結果。
    """
    # 讀取標準輸入中的所有行，並移除多餘的空白
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return

    # 讀取測試資料組數 T
    t_cases = int(input_lines[0].strip())
    
    # 用於追蹤當前讀取到哪一行
    current_line = 1

    for t in range(1, t_cases + 1):
        # 確保讀取時不會超出索引範圍
        if current_line >= len(input_lines):
            break
            
        # 讀取矩陣大小行，例如 "N = 3" 或 "N=3"
        dim_line = input_lines[current_line].strip()
        current_line += 1
        
        # 解析 N 的數值，使用 '=' 切割並拿取最後一部分
        n = int(dim_line.split("=")[-1].strip())
        
        # 讀取接下來的 n 行，建構 n x n 的矩陣
        matrix = []
        for _ in range(n):
            if current_line < len(input_lines):
                # 將整行以空白切分並轉為整數列表
                row = [int(val) for val in input_lines[current_line].split()]
                matrix.append(row)
                current_line += 1
                
        # 判斷是否為對稱矩陣並印出結果
        if is_symmetric(matrix, n):
            print(f"Test #{t}: Symmetric.")
        else:
            print(f"Test #{t}: Non-symmetric.")

if __name__ == "__main__":
    solve()
