import sys
import re

def solve(input_text):
    """
    處理 UVA 11349 Symmetric Matrix 的主邏輯（正規標準版）
    """
    # 使用正規表達式找出所有的數字（包含負號）
    # 這樣可以忽略 'N', '=', 以及各種未知的空白字元，是最穩定且容錯率高的讀取方式
    tokens = re.findall(r'-?\d+', input_text)
    if not tokens:
        return ""
    
    # 第一個數字為測試資料的總筆數 T
    T = int(tokens[0])
    idx = 1
    output = []
    
    for t in range(1, T + 1):
        if idx >= len(tokens):
            break
            
        # 接下來的數字為矩陣大小 N
        n = int(tokens[idx])
        idx += 1
        
        # 讀取 n x n 個矩陣元素，建立二維陣列 (2D Matrix)
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(int(tokens[idx]))
                idx += 1
            matrix.append(row)
            
        # 檢查是否為對稱矩陣
        is_symmetric = True
        for i in range(n):
            for j in range(n):
                # 條件 1: 元素必須是非負數 (>= 0)，若為負數則直接不成立
                if matrix[i][j] < 0:
                    is_symmetric = False
                # 條件 2: 必須以中心為對稱點 (M[i][j] == M[n-1-i][n-1-j])
                if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                    is_symmetric = False
        
        # 根據檢查結果輸出對應格式
        if is_symmetric:
            output.append(f"Test #{t}: Symmetric.")
        else:
            output.append(f"Test #{t}: Non-symmetric.")
            
    # 將結果用換行符號連接，並在最後加上換行
    return '\n'.join(output) + '\n'

if __name__ == '__main__':
    # 讀取所有標準輸入的資料，然後輸出運算結果
    print(solve(sys.stdin.read()), end='')
