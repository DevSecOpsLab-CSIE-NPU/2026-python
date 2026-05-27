import math

# 持續讀取輸入直到遇到0
while True:
    N = int(input())
    if N == 0:  # 當輸入為0時結束
        break
    
    # 初始化GCD總和
    G = 0
    
    # 雙重迴圈遍歷所有的 (i, j) 對，其中 1 <= i < j <= N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            # 計算GCD(i, j)並累加到G中
            G += math.gcd(i, j)
    
    # 輸出該N對應的GCD總和
    print(G)
