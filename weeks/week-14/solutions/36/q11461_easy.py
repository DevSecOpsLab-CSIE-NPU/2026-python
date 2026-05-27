# Square Numbers 簡單版本
# 題目 11461: UVA — Square Numbers
# 簡單易懂的寫法

import math

# 不斷讀取輸入直到遇到 0 0
while True:
    # 讀取兩個整數 a 和 b
    a, b = map(int, input().split())
    
    # 如果輸入是 0 0，則結束程式
    if a == 0 and b == 0:
        break
    
    # 計算最小的 i，使得 i^2 >= a
    # 例：sqrt(1) = 1.0，向上取整得 1
    # 例：sqrt(2) = 1.41...，向上取整得 2
    min_i = math.ceil(math.sqrt(a))
    
    # 計算最大的 i，使得 i^2 <= b
    # 例：sqrt(10) = 3.16...，向下取整得 3（因為3^2=9, 4^2=16）
    max_i = math.floor(math.sqrt(b))
    
    # 完全平方數個數
    # = 從 min_i 到 max_i 的整數個數
    # = max_i - min_i + 1
    # 例：[1, 10] → min_i=1, max_i=3 → 3-1+1=3 個 (1, 4, 9)
    count = max_i - min_i + 1
    
    # 如果 min_i > max_i，表示沒有完全平方數
    if min_i > max_i:
        count = 0
    
    # 輸出結果
    print(count)
