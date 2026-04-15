# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# float inf/nan / fractions.Fraction / random

import math
import random
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)  # inf -inf nan
print(math.isinf(a))  # True
print(math.isnan(c))  # True
print(a + 45, 10 / a)  # inf 0.0
print(a / a, a + b)  # nan nan（未定義）
print(c == c)  # False（NaN 不等於自己！）

# ── 3.8 分數運算 ──────────────────────────────────────
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q
print(p + q)  # 27/16
print(r.numerator, r.denominator)  # 35 64
print(float(r))  # 0.546875
print(r.limit_denominator(8))  # 4/7
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))  # 隨機一個
print(random.sample(values, 3))  # 3 個不重複樣本
random.shuffle(values)
print(values)  # 打亂後的序列
print(random.randint(0, 10))  # 0~10 整數
random.seed(42)
print(random.random())  # 固定種子：可重現
