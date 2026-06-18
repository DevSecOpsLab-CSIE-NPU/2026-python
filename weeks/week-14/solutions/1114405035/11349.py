# -*- coding: utf-8 -*-
import sys

def solve():
    """
    UVA 11349 — Symmetric Matrix 解題主程式
    """
    # 讀取所有的輸入 token
    tokens = sys.stdin.read().split()
    if not tokens:
        return
        
    idx = 0
    num_cases = int(tokens[idx])
    idx += 1
    
    for case_num in range(1, num_cases + 1):
        # 讀取 "N" 和 "="
        if tokens[idx] == "N":
            idx += 1
        if tokens[idx] == "=":
            idx += 1
            
        n = int(tokens[idx])
        idx += 1
        
        # 讀取 n * n 個矩陣元素
        matrix_size = n * n
        elements = []
        for _ in range(matrix_size):
            elements.append(int(tokens[idx]))
            idx += 1
            
        # 判斷是否對稱
        is_symmetric = True
        for i in range(matrix_size):
            # 條件 1：所有元素必須為非負數
            if elements[i] < 0:
                is_symmetric = False
                break
            # 條件 2：中心對稱 M[idx] == M[matrix_size - 1 - idx]
            if elements[i] != elements[matrix_size - 1 - i]:
                is_symmetric = False
                break
                
        # 輸出結果
        if is_symmetric:
            print(f"Test #{case_num}: Symmetric.")
        else:
            print(f"Test #{case_num}: Non-symmetric.")

if __name__ == "__main__":
    solve()
