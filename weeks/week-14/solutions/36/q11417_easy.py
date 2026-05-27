# GCD 簡單版本
# 題目 11417: UVA — GCD
# 簡單易懂的寫法

import math

# 不斷讀取輸入直到遇到 0
while True:
    # 讀取一個整數 N
    n = int(input())
    
    # 如果輸入是 0，則結束程式
    if n == 0:
        break
    
    # 計算所有 (i, j) 數對的 gcd 總和
    # i 從 1 到 n-1
    # j 從 i+1 到 n
    # 保證 i < j
    total = 0
    
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            # 使用 math.gcd() 計算最大公因數
            # 例：gcd(6, 9) = 3
            total += math.gcd(i, j)
    
    # 輸出結果
    print(total)
