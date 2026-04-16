import math

a = int(input())

N = a * a + 1
best_d = 1
for d in range(1, math.isqrt(N) + 1):
    if N % d == 0:
        best_d = d

d1 = best_d
d2 = N // best_d
print(2 * a + d1 + d2)
