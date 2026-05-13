import sys
data = sys.stdin.read().splitlines()  
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
            if all(0 <= i < M and 0 <= j < N and grid[i][j] == char 
                   for i in range(r - half, r + half + 1) 
                   for j in range(c - half, c + half + 1)):
                max_k = k
                k += 2
            else:
                break
        print(max_k)