# Symmetric Matrix 簡單版本
# 題目 11349: UVA — Symmetric Matrix
# 簡單易懂的寫法

# 讀取測試用例數量
t = int(input())

# 每個測試用例都處理一次
for test_num in range(1, t + 1):
    # 讀取矩陣維度
    # 格式是 "N = n"
    line = input().strip()
    n = int(line.split('=')[1])
    
    # 讀取 n 行 n 列的矩陣
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # 判斷是否為對稱矩陣
    # 條件1：所有元素都要非負
    # 條件2：中心對稱 M[i][j] = M[n-1-i][n-1-j]
    
    is_symmetric = True
    
    # 檢查所有元素是否非負
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                is_symmetric = False
                break
        if not is_symmetric:
            break
    
    # 檢查中心對稱
    if is_symmetric:
        for i in range(n):
            for j in range(n):
                # M[i][j] 應該等於 M[n-1-i][n-1-j]
                if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                    is_symmetric = False
                    break
            if not is_symmetric:
                break
    
    # 輸出結果
    if is_symmetric:
        print(f"Test #{test_num}: Symmetric.")
    else:
        print(f"Test #{test_num}: Non-symmetric.")
