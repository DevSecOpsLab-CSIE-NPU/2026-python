"""
題目 11349 - Symmetric Matrix (對稱矩陣判斷) - 簡易版本
使用更簡潔的寫法，易於在考場快速實現
"""

def check_symmetric(m):
    """
    檢查矩陣是否為對稱矩陣
    
    簡易說明：
    1. 檢查是否有負數
    2. 檢查是否中心對稱
    """
    n = len(m)
    
    # 方法一：檢查是否有負數
    # 使用 all() 和生成式，一行程式檢查所有元素
    if not all(val >= 0 for row in m for val in row):
        return False
    
    # 方法二：檢查中心對稱
    # 只需檢查矩陣的一半（避免重複檢查）
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[n-1-i][n-1-j]:
                return False
    
    return True


# 主程式
t = int(input())

for case in range(1, t + 1):
    # 讀取維度
    n = int(input().split('=')[1].strip())
    
    # 讀取矩陣
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    # 輸出結果
    result = "Symmetric." if check_symmetric(matrix) else "Non-symmetric."
    print(f"Test #{case}: {result}")
