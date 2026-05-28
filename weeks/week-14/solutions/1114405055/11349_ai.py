# UVA 11349 - Symmetric Matrix (AI 版本)
import sys

def solve():
    # 讀取所有的輸入內容
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0]) # 測試資料組數
    idx = 1
    
    for case_num in range(1, t + 1):
        # 跳過 "N", "=", "n" 這些字元，找到維度 n
        while idx < len(input_data) and input_data[idx] != '=':
            idx += 1
        idx += 1
        n = int(input_data[idx])
        idx += 1
        
        # 讀取 n*n 個矩陣元素
        matrix = []
        for _ in range(n * n):
            matrix.append(int(input_data[idx]))
            idx += 1
            
        # 檢查是否所有的元素都大於等於 0，且陣列與其反轉是否相同
        # 如果是，則為對稱矩陣
        is_symmetric = True
        for val in matrix:
            if val < 0:
                is_symmetric = False
                break
                
        if is_symmetric:
            for i in range(len(matrix) // 2):
                if matrix[i] != matrix[len(matrix) - 1 - i]:
                    is_symmetric = False
                    break
                    
        # 輸出結果
        if is_symmetric:
            print(f"Test #{case_num}: Symmetric.")
        else:
            print(f"Test #{case_num}: Non-symmetric.")

if __name__ == '__main__':
    solve()
