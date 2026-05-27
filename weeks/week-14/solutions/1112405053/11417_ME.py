import math

while True:
    N = int(input())
    if N == 0:
        break
    
    G = 0
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            G += math.gcd(i, j)
    
    print(G)
