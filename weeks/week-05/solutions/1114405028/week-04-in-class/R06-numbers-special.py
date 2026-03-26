# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# 主題：float("inf"/"nan") / Fraction / random

import math
import random
from fractions import Fraction

# ------------------------------------------------------------
# 3.7 無窮大（inf）與 NaN（Not a Number）
# ------------------------------------------------------------
a = float("inf")
b = float("-inf")
c = float("nan")

print(a, b, c)      # inf -inf nan
print(math.isinf(a))   # True
print(math.isnan(c))   # True

# inf 的運算特性
print(a + 45, 10 / a)  # inf 0.0

# 未定義運算通常得到 NaN
print(a / a, a + b)    # nan nan

# NaN 的一個重要特性：不等於任何值，連自己也不等於自己
print(c == c)          # False

# ------------------------------------------------------------
# 3.8 Fraction：有理數精確運算
# ------------------------------------------------------------
# Fraction(分子, 分母) 會自動約分。
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q

print(p + q)                     # 27/16
print(r.numerator, r.denominator)  # 35 64
print(float(r))                  # 0.546875

# limit_denominator(max_denominator)
# 用較小分母近似目前分數，常用於顯示或人類可讀表達。
print(r.limit_denominator(8))    # 4/7

# 從 float 轉 Fraction 的常見技巧
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ------------------------------------------------------------
# 3.11 random：隨機操作
# ------------------------------------------------------------
values = [1, 2, 3, 4, 5, 6]

# 隨機選 1 個元素（可重複呼叫）
print(random.choice(values))

# 隨機抽樣 k 個，不重複
print(random.sample(values, 3))

# 就地打亂序列
random.shuffle(values)
print(values)

# 隨機整數區間 [0, 10]
print(random.randint(0, 10))

# 設定種子：讓結果可重現（測試/教學非常重要）
random.seed(42)
print(random.random())
