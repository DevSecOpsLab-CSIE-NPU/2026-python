
import math

# 反正切分解：arctan(1/a) = arctan(1/b) + arctan(1/c)
# 利用公式 (b-a)(c-a) = a^2 + 1，找讓 b+c 最小的整數解
# 方法：對 a^2+1 做因數分解，找最接近平方根的因數對 (d1, d2)

a = int(input())

N = a * a + 1  # 要分解的數

best_d = 1
# 找 N 的所有因數，取最大的不超過 sqrt(N) 的那個
for d in range(1, math.isqrt(N) + 1):
    if N % d == 0:
        best_d = d  # 持續更新，最後得到最大合法因數

d1 = best_d
d2 = N // best_d

# b = a + d1，c = a + d2，所以 b + c = 2a + d1 + d2
print(2 * a + d1 + d2)
