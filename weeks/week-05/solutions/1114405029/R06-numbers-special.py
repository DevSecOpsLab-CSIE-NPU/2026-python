# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
#
# 這份範例介紹幾種平常比較少見，但實務上很重要的數值型別與工具：
# 1. 無窮大 inf 與非數值 NaN
# 2. Fraction 分數物件
# 3. random 模組的常用隨機操作

import math
import random
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
# inf 代表正無窮大，-inf 代表負無窮大，nan 代表「不是數字」。
# 這些值在科學計算、資料清理與特殊狀態表示時都可能遇到。
a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)  # inf -inf nan

# math.isinf() / math.isnan() 是判斷這類特殊值的標準做法。
print(math.isinf(a))  # True
print(math.isnan(c))  # True

# 和無窮大運算時，部分結果仍可定義。
print(a + 45, 10 / a)  # inf 0.0

# 但有些運算在數學上沒有明確結果，因此會得到 nan。
print(a / a, a + b)  # nan nan（未定義）

# NaN 最大的特性之一：它不等於任何值，連自己也不等於自己。
print(c == c)  # False（NaN 不等於自己！）

# ── 3.8 分數運算 ──────────────────────────────────────
# Fraction 能把數值表示成「分子 / 分母」的精確分數。
# 適合示範有理數運算，或避免浮點數近似誤差。
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q
print(p + q)  # 27/16

# numerator / denominator 可分別取得分子與分母。
print(r.numerator, r.denominator)  # 35 64

# 需要和其他浮點流程整合時，也可以轉成 float。
print(float(r))  # 0.546875

# limit_denominator() 會找出「接近目前值」且分母不超過指定上限的分數。
# 常用於把近似小數還原成較好理解的分數。
print(r.limit_denominator(8))  # 4/7

# float.as_integer_ratio() 可把浮點數拆成分子與分母，再交給 Fraction 建立。
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]

# choice()：從序列中隨機取出一個元素。
print(random.choice(values))  # 隨機一個

# sample()：一次取多個且不重複，適合抽樣。
print(random.sample(values, 3))  # 3 個不重複樣本

# shuffle()：原地打亂串列順序，會直接修改原本的 values。
random.shuffle(values)
print(values)  # 打亂後的序列

# randint(a, b)：包含兩端點，也就是 a 和 b 都有機會被選到。
print(random.randint(0, 10))  # 0~10 整數

# seed() 固定亂數種子後，後續產生的亂數序列可以重現。
# 這對測試、教學示範、除錯特別有幫助。
random.seed(42)
print(random.random())  # 固定種子：可重現
