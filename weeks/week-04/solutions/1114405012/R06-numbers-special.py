# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# float inf/nan / fractions.Fraction / random

import math
import random
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
# 正無窮大（infinity）
a = float("inf")
# 負無窮大
b = float("-inf")
# NaN（Not a Number，非數值）
c = float("nan")
print(a, b, c)  # inf -inf nan
# 判斷是否為無窮大
print(math.isinf(a))  # True
# 判斷是否為 NaN
print(math.isnan(c))  # True
# 無窮大參與運算：inf + 45 仍是 inf；有限數除以 inf 會趨近 0
print(a + 45, 10 / a)  # inf 0.0
# 未定義運算會得到 NaN（例如 inf/inf、inf + (-inf)）
print(a / a, a + b)  # nan nan（未定義）
# NaN 的重要特性：不等於任何值，連自己都不等於
print(c == c)  # False（NaN 不等於自己！）

# ── 3.8 分數運算 ──────────────────────────────────────
# Fraction(分子, 分母) 可精確表示有理數，避免浮點誤差
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q
print(p + q)  # 27/16
# 直接取得分子與分母
print(r.numerator, r.denominator)  # 35 64
# 需要近似值時可轉成 float
print(float(r))  # 0.546875
# 將分數近似成「分母不超過 8」的最接近分數
print(r.limit_denominator(8))  # 4/7
# 把小數 3.75 轉成最精確分數：先取整數比，再解包給 Fraction
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]
# 從序列中隨機挑 1 個元素（可重複呼叫，每次獨立）
print(random.choice(values))  # 隨機一個
# 一次抽 3 個「不重複」元素（不改動原序列）
print(random.sample(values, 3))  # 3 個不重複樣本
# 就地打亂（in-place），會直接改變 values
random.shuffle(values)
print(values)  # 打亂後的序列
# 產生區間 [0, 10] 的隨機整數（含端點）
print(random.randint(0, 10))  # 0~10 整數
# 設定亂數種子：讓隨機結果可重現（利於測試與教學）
random.seed(42)
print(random.random())  # 固定種子：可重現
