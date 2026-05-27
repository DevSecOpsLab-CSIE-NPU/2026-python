"""
題目 11349 - Symmetric Matrix (對稱矩陣判斷) - 手打版本
學生自己手動編寫的解題程式
"""

def is_symmetric(matrix):
    # 檢查是否有負數
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                return False
    
    # 檢查中心對稱
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n-1-i][n-1-j]:
                return False
    
    return True

t = int(input())
for test_num in range(1, t + 1):
    line = input().strip()
    n = int(line.split('=')[1].strip())
    
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    if is_symmetric(matrix):
        print(f"Test #{test_num}: Symmetric.")
    else:
        print(f"Test #{test_num}: Non-symmetric.")
