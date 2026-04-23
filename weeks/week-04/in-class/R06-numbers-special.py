# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# float inf/nan / fractions.Fraction / random

import math
import random
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
# inf 表示正無窮大，-inf 表示負無窮大，nan 表示非數值
# NaN 在比較時不等於自身，必須用 math.isnan() 判斷

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
# fractions.Fraction 提供精確的有理數表示法，避免浮點誤差
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q
print(p + q)  # 27/16
print(r.numerator, r.denominator)  # 35 64
print(float(r))  # 0.546875
print(r.limit_denominator(8))  # 4/7
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ── 3.11 隨機選擇 ─────────────────────────────────────
# random 模組用於隨機抽樣和隨機排序
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))  # 隨機選一個元素
print(random.sample(values, 3))  # 取出 3 個不重複元素
random.shuffle(values)
print(values)  # 原地打亂序列
print(random.randint(0, 10))  # 0~10 範圍內的整數
random.seed(42)  # 固定種子以便結果可重現
print(random.random())  # 0~1 之間的浮點值
