# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# float inf/nan / fractions.Fraction / random

# math 提供檢查無窮大、NaN 等特殊浮點數的工具
import math
# random 用來產生隨機選擇、抽樣與亂數
import random
# Fraction 可用分子與分母精確表示有理數
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
# 正無窮大、負無窮大與 NaN 都屬於特殊浮點數值
a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)  # inf -inf nan
# isinf() 用來判斷是否為正無窮大或負無窮大
print(math.isinf(a))  # True
# isnan() 用來判斷是否為 NaN（Not a Number）
print(math.isnan(c))  # True
# 無窮大加上有限數仍是無窮大；有限數除以無窮大會趨近 0
print(a + 45, 10 / a)  # inf 0.0
# 無窮大與自己相除、正負無窮大相加都屬未定義，結果會是 NaN
print(a / a, a + b)  # nan nan（未定義）
# NaN 有一個特殊性質：它不會等於任何值，包含它自己
print(c == c)  # False（NaN 不等於自己！）

# ── 3.8 分數運算 ──────────────────────────────────────
# Fraction(分子, 分母) 可建立精確分數，避免浮點數誤差
p = Fraction(5, 4)
q = Fraction(7, 16)
# Fraction 之間可直接做四則運算，結果仍保持分數型態
r = p * q
print(p + q)  # 27/16
# numerator 與 denominator 可取得約分後的分子與分母
print(r.numerator, r.denominator)  # 35 64
# 需要時也可以轉成一般浮點數
print(float(r))  # 0.546875
# limit_denominator() 可找出分母不超過指定值的近似分數
print(r.limit_denominator(8))  # 4/7
# as_integer_ratio() 可把浮點數拆成整數比，再交給 Fraction 還原為分數
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]
# choice() 會從序列中隨機挑出一個元素
print(random.choice(values))  # 隨機一個
# sample() 會抽出指定數量的不重複樣本
print(random.sample(values, 3))  # 3 個不重複樣本
# shuffle() 會直接就地打亂原本串列的順序
random.shuffle(values)
print(values)  # 打亂後的序列
# randint(a, b) 會回傳包含兩端點的整數亂數
print(random.randint(0, 10))  # 0~10 整數
# 設定 seed 後，之後產生的亂數序列就能重現
random.seed(42)
print(random.random())  # 固定種子：可重現
