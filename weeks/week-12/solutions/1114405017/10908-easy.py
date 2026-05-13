# UVA 10908 — Largest Square (超簡單版本)
# 使用 all() 生成器檢查，更簡潔。

import sys  # 匯入 sys 模組

data = sys.stdin.read().splitlines()  # 讀取所有行

index = 0

T = int(data[index])
index += 1

for _ in range(T):
    M, N, Q = map(int, data[index].split())
    index += 1
    
    grid = [list(data[index + i]) for i in range(M)]
    index += M
    
    print(M, N, Q)
    
    for _ in range(Q):
        r, c = map(int, data[index].split())
        index += 1
        
        char = grid[r][c]
        max_k = 1
        k = 1
        while True:
            half = (k - 1) // 2
            # 使用 all() 和生成器檢查所有位置字元相同且在邊界內
            if all(0 <= i < M and 0 <= j < N and grid[i][j] == char 
                   for i in range(r - half, r + half + 1) 
                   for j in range(c - half, c + half + 1)):
                max_k = k
                k += 2
            else:
                break
        print(max_k)