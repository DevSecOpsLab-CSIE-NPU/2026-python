# UVA 11461 — Square Numbers（手打版）
# 計算閉區間 [a, b] 中完全平方數的個數
# 公式：floor(sqrt(b)) - floor(sqrt(a-1))

import math

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:  # 終止條件
        break
    # isqrt() 做整數平方根，避免浮點誤差
    print(math.isqrt(b) - math.isqrt(a - 1))
