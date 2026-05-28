# UVA 11461 — Square Numbers（AI 簡單版）
# 計算閉區間 [a, b] 中完全平方數的個數
#
# 關鍵公式：
#   floor(sqrt(b))   = b 以內最大完全平方數的平方根
#   floor(sqrt(a-1)) = a 以前最大完全平方數的平方根
#   兩者相減即為 [a, b] 內完全平方數的個數
#
# 使用 math.isqrt() 做整數平方根（不會有浮點誤差）

import math

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:  # 終止條件
        break
    count = math.isqrt(b) - math.isqrt(a - 1)
    print(count)
