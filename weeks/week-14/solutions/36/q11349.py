# Symmetric Matrix 解答程式
# 題目 11349: UVA — Symmetric Matrix
# 判斷矩陣是否為中心對稱矩陣

def is_symmetric_matrix(matrix):
    """
    判斷矩陣是否為對稱矩陣
    
    判斷條件:
    1. 所有元素必須非負 (>= 0)
    2. 矩陣關於中心點對稱：M[i][j] = M[n-1-i][n-1-j]
    
    參數:
        matrix: n×n 的矩陣 (二維列表)
    
    返回:
        True 為對稱矩陣，False 為非對稱矩陣
    """
    n = len(matrix)
    
    # 檢查所有元素是否非負
    for row in matrix:
        for val in row:
            if val < 0:
                return False
    
    # 檢查中心對稱
    # 只需檢查上半部分與下半部分對應位置
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                return False
    
    return True

def main():
    """
    主程式：讀取輸入並輸出結果
    """
    t = int(input())
    
    for test_num in range(1, t + 1):
        # 讀取矩陣維度
        line = input().strip()
        n = int(line.split('=')[1])
        
        # 讀取矩陣
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        
        # 判斷是否為對稱矩陣
        if is_symmetric_matrix(matrix):
            print(f"Test #{test_num}: Symmetric.")
        else:
            print(f"Test #{test_num}: Non-symmetric.")

if __name__ == '__main__':
    main()
