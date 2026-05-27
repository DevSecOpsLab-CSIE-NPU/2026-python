import math

while True:
    
    n = int (input())

    if n == 0:
        break

    total = 0

    for i in range (1, n):
        for j in range (i + 1, n + 1):
            total += math.gcd(i, j)

    print (total)