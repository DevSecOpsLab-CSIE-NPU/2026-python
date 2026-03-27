"""
R06: 特殊數值與隨機工具。

示範重點：
1. `inf` 與 `nan` 的判斷方式。
2. `Fraction` 做精確分數運算。
3. `random` 模組常見操作。
"""

import math
import random
from fractions import Fraction

# `inf` 代表正無限大，`-inf` 代表負無限大，`nan` 代表不是數字。
a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)  # inf -inf nan
print(math.isinf(a))  # True
print(math.isnan(c))  # True
print(a + 45, 10 / a)  # inf 0.0

# 不同無限大運算可能得到 `nan`，代表結果沒有明確數值意義。
print(a / a, a + b)  # nan nan

# `nan` 的一個特性是它和自己比較也不相等。
print(c == c)  # False

# `Fraction` 可以保留分子與分母，不會像浮點數那樣失真。
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q
print(p + q)  # 27/16
print(r.numerator, r.denominator)  # 35 64
print(float(r))  # 0.546875
print(r.limit_denominator(8))  # 4/7

# 浮點數可以先拆成整數比，再轉成 Fraction。
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

values = [1, 2, 3, 4, 5, 6]

# `choice()` 隨機取一個元素。
print(random.choice(values))

# `sample()` 取出不重複的多個元素。
print(random.sample(values, 3))

# `shuffle()` 直接在原串列上重新洗牌。
random.shuffle(values)
print(values)

# `randint(a, b)` 會包含兩端點。
print(random.randint(0, 10))

# 設定種子後，後續亂數序列可以重現。
random.seed(42)
print(random.random())
